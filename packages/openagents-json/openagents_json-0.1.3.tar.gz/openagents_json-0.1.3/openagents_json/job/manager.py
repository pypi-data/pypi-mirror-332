"""
JobManager implementation for the OpenAgents JSON framework.

This module provides the main JobManager class responsible for creating,
managing, and executing workflow jobs.
"""

import asyncio
import logging
import time
import uuid
from datetime import datetime, timedelta
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

from openagents_json.job.events import Event, EventType, event_emitter
from openagents_json.job.model import Job, JobPriority, JobStatus
from openagents_json.job.monitoring import monitor
from openagents_json.job.storage import (
    BaseJobStore,
    DatabaseJobStore,
    FileJobStore,
    MemoryJobStore,
)
from openagents_json.settings import settings

logger = logging.getLogger(__name__)


class JobManager:
    """
    Manager for job scheduling, execution, and lifecycle management.

    The JobManager handles:
    - Job creation and scheduling
    - Dependency tracking and resolution
    - Job execution and monitoring
    - Batch operations
    - Retry handling
    - Worker coordination
    """

    def __init__(
        self,
        job_store: Optional[BaseJobStore] = None,
        retention_days: int = None,
        max_concurrent_jobs: int = None,
        distributed_mode: bool = False,
        enable_monitoring: bool = True,
    ):
        """
        Initialize a JobManager.

        Args:
            job_store: Storage backend for jobs
            retention_days: Number of days to retain job history
            max_concurrent_jobs: Maximum number of jobs to run concurrently
            distributed_mode: Whether to operate in distributed mode with workers
            enable_monitoring: Whether to enable monitoring and metrics collection
        """
        if job_store is None:
            # Create job store based on configuration
            store_type = settings.job.store_type.lower()

            if store_type == "memory":
                job_store = MemoryJobStore()
            elif store_type == "file":
                job_store = FileJobStore(storage_dir=settings.job.store_path)
            elif store_type == "database" or store_type == "sqlalchemy":
                job_store = DatabaseJobStore(
                    dialect=settings.storage.database.dialect,
                    host=settings.storage.database.host,
                    port=settings.storage.database.port,
                    username=settings.storage.database.username,
                    password=(
                        settings.storage.database.password.get_secret_value()
                        if settings.storage.database.password
                        else None
                    ),
                    database=settings.storage.database.name,
                    path=settings.storage.database.path,
                    # Add connection pool settings
                    pooling=True,
                    pool_size=settings.storage.database.connection_pool_size,
                    max_overflow=settings.storage.database.connection_max_overflow,
                    pool_timeout=settings.storage.database.connection_timeout,
                    pool_recycle=settings.storage.database.connection_recycle,
                )
            else:
                logger.warning(
                    f"Unknown job store type: {store_type}, defaulting to memory"
                )
                job_store = MemoryJobStore()

        self.job_store = job_store
        self.retention_days = (
            retention_days
            if retention_days is not None
            else settings.job.job_retention_days
        )
        self.max_concurrent_jobs = (
            max_concurrent_jobs
            if max_concurrent_jobs is not None
            else settings.job.max_concurrent_jobs
        )
        self.distributed_mode = distributed_mode
        self.running_jobs: Dict[str, asyncio.Task] = {}
        self.job_queue: List[str] = []
        self.worker_manager = None

        # Internal counters and state
        self._jobs_completed = 0
        self._jobs_failed = 0

        # If monitoring is disabled, disable the global monitor
        if not enable_monitoring:
            monitor.disable()

        # Recover interrupted jobs
        if not distributed_mode:
            recovery_timeout = getattr(settings.job, "job_recovery_timeout_minutes", 5)
            recovered_jobs = self.job_store.recover_interrupted_jobs(
                recovery_timeout_minutes=recovery_timeout
            )
            if recovered_jobs:
                logger.info(
                    f"Recovered {len(recovered_jobs)} interrupted jobs with {recovery_timeout}-minute timeout"
                )
                for job in recovered_jobs:
                    logger.info(f"  - Job {job.job_id}: {job.name}")

        # Emit system startup event
        event_emitter.emit(
            Event(
                event_type=EventType.SYSTEM_STARTUP,
                data={
                    "max_concurrent_jobs": self.max_concurrent_jobs,
                    "distributed_mode": distributed_mode,
                    "retention_days": self.retention_days,
                    "job_store_type": job_store.__class__.__name__,
                    "monitoring_enabled": enable_monitoring,
                    "jobs_recovered": (
                        len(recovered_jobs) if "recovered_jobs" in locals() else 0
                    ),
                    "recovery_timeout_minutes": getattr(
                        settings.job, "job_recovery_timeout_minutes", 5
                    ),
                },
            )
        )

        logger.info(f"JobManager initialized with {job_store.__class__.__name__}")

    def create_job(
        self,
        name: str = "",
        description: str = "",
        payload: Any = None,
        priority: Union[JobPriority, str] = JobPriority.MEDIUM,
        max_retries: int = 0,
        retry_delay: int = 0,
        timeout: Optional[int] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        dependencies: Optional[List[str]] = None,
        auto_start: bool = False,
    ) -> Job:
        """
        Create a new job.

        Args:
            name: Human-readable name for the job
            description: Detailed description of the job
            payload: Data payload for the job
            priority: Job priority level
            max_retries: Maximum number of retry attempts
            retry_delay: Delay between retry attempts in seconds
            timeout: Maximum execution time in seconds
            tags: List of tags for categorizing the job
            metadata: Additional metadata for the job
            dependencies: List of job IDs this job depends on
            auto_start: Whether to automatically start the job if dependencies are satisfied

        Returns:
            The created Job instance
        """
        # Create the job
        job = Job(
            name=name,
            description=description,
            payload=payload,
            status=JobStatus.CREATED,
            priority=priority,
            max_retries=max_retries,
            retry_delay=retry_delay,
            timeout=timeout,
            tags=tags,
            metadata=metadata,
            dependencies=dependencies,
        )

        # Save the job to the store
        success = self.job_store.add_job(job)

        if not success:
            logger.error(f"Failed to create job: {job.job_id}")

            # Emit system error event
            event_emitter.emit(
                Event(
                    event_type=EventType.SYSTEM_ERROR,
                    data={
                        "message": f"Failed to create job: {job.job_id}",
                        "operation": "create_job",
                    },
                )
            )

            return job

        # Emit job created event
        event_emitter.emit(Event.from_job(event_type=EventType.JOB_CREATED, job=job))

        logger.info(f"Created job: {job.job_id}")

        # Start the job if auto_start is True and it has no dependencies
        if auto_start and (not dependencies or len(dependencies) == 0):
            self.start_job(job.job_id)

        return job

    def get_job(self, job_id: str) -> Optional[Job]:
        """
        Get a job by ID.

        Args:
            job_id: ID of the job to retrieve

        Returns:
            The Job instance if found, None otherwise
        """
        return self.job_store.get(job_id)

    def list_jobs(
        self,
        status: Optional[Union[JobStatus, List[JobStatus]]] = None,
        workflow_id: Optional[str] = None,
        user_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        limit: Optional[int] = None,
        offset: int = 0,
        sort_by: str = "created_at",
        sort_order: str = "desc",
    ) -> List[Job]:
        """
        List jobs with optional filtering and sorting.

        Args:
            status: Filter by job status(es)
            workflow_id: Filter by workflow ID
            user_id: Filter by user ID
            tags: Filter by tags
            created_after: Filter by creation date (after)
            created_before: Filter by creation date (before)
            limit: Maximum number of jobs to return
            offset: Number of jobs to skip
            sort_by: Field to sort by
            sort_order: Sort order ("asc" or "desc")

        Returns:
            List of jobs matching the criteria
        """
        return self.job_store.list(
            status=status,
            workflow_id=workflow_id,
            user_id=user_id,
            tags=tags,
            created_after=created_after,
            created_before=created_before,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
        )

    def delete_job(self, job_id: str) -> bool:
        """
        Delete a job.

        If the job is running, it will be cancelled first.

        Args:
            job_id: ID of the job to delete

        Returns:
            True if the job was deleted, False otherwise
        """
        if job_id in self.running_jobs:
            self.cancel_job(job_id)

        return self.job_store.delete(job_id)

    def start_job(self, job_id: str) -> bool:
        """
        Start execution of a job.

        Args:
            job_id: ID of the job to start

        Returns:
            True if the job was started, False otherwise
        """
        # Get the job from the store
        job = self.job_store.get_job(job_id)

        if not job:
            logger.error(f"Cannot start job: Job {job_id} not found")
            return False

        # Check if the job is already running
        if job.status == JobStatus.RUNNING:
            logger.warning(f"Job {job_id} is already running")
            return True

        # Check if the job is complete or failed
        if job.status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
            logger.warning(f"Cannot start job {job_id}: Job is {job.status}")
            return False

        # Check for unsatisfied dependencies
        if job.has_dependencies():
            dependencies = self.get_dependencies(job_id)
            for dep_job in dependencies:
                if dep_job.status != JobStatus.COMPLETED:
                    logger.info(
                        f"Cannot start job {job_id}: Dependency {dep_job.job_id} is not completed"
                    )
                    return False

        # Check if we can run more jobs
        can_run = True
        if not self.distributed_mode:
            if len(self.running_jobs) >= self.max_concurrent_jobs:
                logger.info(
                    f"Cannot start job {job_id}: Maximum concurrent jobs reached"
                )

                # Update the job status to queued
                job.update_status(JobStatus.QUEUED)
                self.job_store.update_job(job)

                # Emit job queued event
                event_emitter.emit(
                    Event.from_job(event_type=EventType.JOB_QUEUED, job=job)
                )

                # Update queue depth in monitoring
                if self._enable_monitoring:
                    monitor.update_queue_depth(
                        len(self.job_store.get_jobs(status=JobStatus.QUEUED))
                    )

                return False

        # Update job status
        job.update_status(JobStatus.RUNNING)
        job.started_at = datetime.now()
        self.job_store.update_job(job)

        # Emit job started event
        event_emitter.emit(Event.from_job(event_type=EventType.JOB_STARTED, job=job))

        # Add to running jobs set if not in distributed mode
        if not self.distributed_mode:
            self.running_jobs[job_id] = asyncio.create_task(self._execute_job(job_id))

        logger.info(f"Started job: {job_id}")
        return True

    def pause_job(self, job_id: str) -> bool:
        """
        Pause a running job.

        Args:
            job_id: ID of the job to pause

        Returns:
            True if the job was paused, False otherwise
        """
        # Get the job from the store
        job = self.job_store.get_job(job_id)

        if not job:
            logger.error(f"Cannot pause job: Job {job_id} not found")
            return False

        # Check if the job is already complete or failed
        if job.status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
            logger.warning(f"Cannot pause job {job_id}: Job is {job.status}")
            return False

        # Update job status
        job.update_status(JobStatus.PAUSED)
        self.job_store.update_job(job)

        # Emit job paused event
        event_emitter.emit(Event.from_job(event_type=EventType.JOB_PAUSED, job=job))

        # Remove from running jobs set if not in distributed mode
        if not self.distributed_mode and job_id in self.running_jobs:
            task = self.running_jobs.pop(job_id)
            task.cancel()

        logger.info(f"Paused job: {job_id}")
        return True

    def resume_job(self, job_id: str) -> bool:
        """
        Resume a paused job.

        Args:
            job_id: ID of the job to resume

        Returns:
            True if the job was resumed, False otherwise
        """
        # Get the job from the store
        job = self.job_store.get_job(job_id)

        if not job:
            logger.error(f"Cannot resume job: Job {job_id} not found")
            return False

        # Check if the job is paused
        if job.status != JobStatus.PAUSED:
            logger.warning(
                f"Cannot resume job {job_id}: Job is not paused (status: {job.status})"
            )
            return False

        # Emit job resumed event
        event_emitter.emit(Event.from_job(event_type=EventType.JOB_RESUMED, job=job))

        # Start the job
        return self.start_job(job_id)

    def cancel_job(self, job_id: str) -> bool:
        """
        Cancel a job.

        Args:
            job_id: ID of the job to cancel

        Returns:
            True if the job was cancelled, False otherwise
        """
        # Get the job from the store
        job = self.job_store.get_job(job_id)

        if not job:
            logger.error(f"Cannot cancel job: Job {job_id} not found")
            return False

        # Check if the job is already complete or failed
        if job.status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
            logger.warning(f"Cannot cancel job {job_id}: Job is {job.status}")
            return False

        # Update job status
        job.update_status(JobStatus.CANCELLED)
        self.job_store.update_job(job)

        # Emit job cancelled event
        event_emitter.emit(Event.from_job(event_type=EventType.JOB_CANCELLED, job=job))

        # Remove from running jobs set if not in distributed mode
        if not self.distributed_mode and job_id in self.running_jobs:
            task = self.running_jobs.pop(job_id)
            task.cancel()

        logger.info(f"Cancelled job: {job_id}")
        return True

    def get_job_status(self, job_id: str) -> Optional[JobStatus]:
        """
        Get the current status of a job.

        Args:
            job_id: ID of the job

        Returns:
            Current job status or None if job not found
        """
        job = self.job_store.get(job_id)
        return job.status if job else None

    def get_job_results(self, job_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the results of a completed job.

        Args:
            job_id: ID of the job

        Returns:
            Job outputs or None if job not found or not completed
        """
        job = self.job_store.get(job_id)
        if not job:
            return None

        if job.status != JobStatus.COMPLETED:
            return None

        return job.outputs

    def cleanup_old_jobs(self) -> int:
        """
        Clean up jobs older than the retention period.

        Returns:
            Number of jobs cleaned up
        """
        return self.job_store.cleanup_old_jobs(self.retention_days)

    async def _execute_job(self, job_id: str) -> None:
        """
        Execute a job asynchronously.

        Args:
            job_id: ID of the job to execute
        """
        # Get the job from the store
        job = self.job_store.get_job(job_id)

        if not job:
            logger.error(f"Cannot execute job: Job {job_id} not found")
            return

        # Set up result tracking
        result = None
        error = None

        # Track job start time for timeout
        start_time = time.time()
        timed_out = False

        try:
            # Check for timeout
            if job.timeout and job.timeout > 0:
                # Execute with timeout
                try:
                    # Placeholder for actual job execution
                    # In a real implementation, this would call the
                    # appropriate workflow executor or function
                    await asyncio.sleep(0.1)  # Simulate work

                    # Update progress every 10%
                    for progress in range(10, 101, 10):
                        # Check if the job was cancelled or paused
                        refreshed_job = self.job_store.get_job(job_id)
                        if refreshed_job.status != JobStatus.RUNNING:
                            break

                        # Update progress
                        job.set_progress(progress / 100.0)
                        self.job_store.update_job(job)

                        # Emit progress event
                        event_emitter.emit(
                            Event.from_job(
                                event_type=EventType.JOB_PROGRESS_UPDATED,
                                job=job,
                                progress=progress,
                            )
                        )

                        await asyncio.sleep(0.1)  # Simulate work

                    # Check for timeout
                    elapsed_time = time.time() - start_time
                    if job.timeout and elapsed_time > job.timeout:
                        timed_out = True
                        raise TimeoutError(
                            f"Job {job_id} timed out after {elapsed_time} seconds"
                        )

                    # Set job result
                    result = {"status": "success"}

                except asyncio.TimeoutError:
                    timed_out = True
                    raise TimeoutError(
                        f"Job {job_id} timed out after {job.timeout} seconds"
                    )
            else:
                # Execute without timeout
                # Placeholder for actual job execution
                await asyncio.sleep(0.1)  # Simulate work

                # Update progress every 10%
                for progress in range(10, 101, 10):
                    # Check if the job was cancelled or paused
                    refreshed_job = self.job_store.get_job(job_id)
                    if refreshed_job.status != JobStatus.RUNNING:
                        break

                    # Update progress
                    job.set_progress(progress / 100.0)
                    self.job_store.update_job(job)

                    # Emit progress event
                    event_emitter.emit(
                        Event.from_job(
                            event_type=EventType.JOB_PROGRESS_UPDATED,
                            job=job,
                            progress=progress,
                        )
                    )

                    await asyncio.sleep(0.1)  # Simulate work

                # Set job result
                result = {"status": "success"}

        except Exception as e:
            # Handle error
            logger.error(f"Error executing job {job_id}: {str(e)}")
            error = {
                "message": str(e),
                "type": e.__class__.__name__,
                "timed_out": timed_out,
            }

        # Get the job again to ensure we have the latest state
        job = self.job_store.get_job(job_id)

        # Only update status if the job is still running
        if job.status == JobStatus.RUNNING:
            if error:
                # Set error and update status
                job.set_error(error)
                job.update_status(JobStatus.FAILED)

                # Check if retry is needed
                if job.max_retries > 0 and job.retry_count < job.max_retries:
                    logger.info(
                        f"Job {job_id} failed, retrying ({job.retry_count + 1}/{job.max_retries})"
                    )
                    job.retry_count += 1
                    self.job_store.update_job(job)

                    # Calculate retry delay
                    delay = job.get_retry_delay()

                    # Emit job retry event
                    event_emitter.emit(
                        Event.from_job(
                            event_type=EventType.JOB_RETRYING,
                            job=job,
                            retry_count=job.retry_count,
                            max_retries=job.max_retries,
                            retry_delay=delay,
                        )
                    )

                    # Schedule retry
                    await self._retry_job_after_delay(job_id, delay)
                    return

                # Emit job failed event
                event_emitter.emit(
                    Event.from_job(
                        event_type=EventType.JOB_FAILED, job=job, error=error
                    )
                )
            else:
                # Set result and update status
                if result:
                    job.result = result
                job.update_status(JobStatus.COMPLETED)
                job.completed_at = datetime.now()

                # Emit job completed event
                event_emitter.emit(
                    Event.from_job(
                        event_type=EventType.JOB_COMPLETED, job=job, result=result
                    )
                )

                # Process dependent jobs
                self.process_completed_job(job_id)

        # Update the job in the store
        self.job_store.update_job(job)

        # Remove from running jobs set if not already removed
        if job_id in self.running_jobs:
            del self.running_jobs[job_id]

            # Start the next job if one is queued
            self._start_next_queued_job()

    async def _retry_job_after_delay(self, job_id: str, delay_seconds: float) -> None:
        """
        Schedule a job to be retried after a delay.

        Args:
            job_id: The ID of the job to retry.
            delay_seconds: Number of seconds to wait before retrying.
        """
        logger.debug(
            f"Scheduling retry for job {job_id} after {delay_seconds:.2f} seconds"
        )
        await asyncio.sleep(delay_seconds)
        self.start_job(job_id)

    def _start_next_queued_job(self) -> None:
        """Start the next queued job if capacity is available."""
        if len(self.running_jobs) >= self.max_concurrent_jobs:
            return

        # Get all queued jobs ordered by priority and creation time
        queued_jobs = self.job_store.get_jobs(
            status=JobStatus.QUEUED, sort_by="priority", sort_order="desc"
        )

        for job in queued_jobs:
            # Skip jobs with unsatisfied dependencies
            if job.has_dependencies():
                dependencies = self.get_dependencies(job.job_id)
                if any(dep.status != JobStatus.COMPLETED for dep in dependencies):
                    continue

            # Try to start the job
            if self.start_job(job.job_id):
                # Update queue depth in monitoring
                if self._enable_monitoring:
                    monitor.update_queue_depth(len(queued_jobs) - 1)
                return

    def create_job_batch(
        self,
        jobs_data: List[Dict[str, Any]],
        batch_id: Optional[str] = None,
        auto_start: bool = False,
    ) -> Tuple[str, List[Job]]:
        """
        Create a batch of related jobs.

        Args:
            jobs_data: List of job creation data dictionaries
            batch_id: Optional batch ID (generated if not provided)
            auto_start: Whether to automatically start jobs with no dependencies

        Returns:
            Tuple of (batch_id, list of created jobs)
        """
        batch_id = batch_id or str(uuid.uuid4())
        created_jobs = []

        # Create all jobs first
        for job_data in jobs_data:
            job_data.setdefault("batch_id", batch_id)

            job = Job(
                name=job_data.get("name", ""),
                description=job_data.get("description", ""),
                payload=job_data.get("payload"),
                status=JobStatus.PENDING,
                priority=job_data.get("priority", JobPriority.MEDIUM),
                max_retries=job_data.get("max_retries", 0),
                retry_delay=job_data.get("retry_delay", 0),
                timeout=job_data.get("timeout"),
                tags=job_data.get("tags", []),
                metadata=job_data.get("metadata", {}),
                dependencies=job_data.get("dependencies", []),
                batch_id=batch_id,
            )
            created_jobs.append(job)

        # Use batch creation if available in the job store
        if hasattr(self.job_store, "create_job_batch"):
            try:
                self.job_store.create_job_batch(created_jobs, batch_id)
            except Exception as e:
                logger.error(f"Error creating job batch: {str(e)}")
                # Fall back to individual saves
                for job in created_jobs:
                    self.job_store.save(job)
        else:
            # Individual saves if batch not supported
            for job in created_jobs:
                self.job_store.save(job)

        # Start jobs that have no dependencies if auto_start is True
        if auto_start:
            for job in created_jobs:
                if not job.has_dependencies():
                    self.start_job(job.job_id)

        return batch_id, created_jobs

    def get_batch_jobs(self, batch_id: str) -> List[Job]:
        """
        Get all jobs in a batch.

        Args:
            batch_id: ID of the batch.

        Returns:
            List of jobs in the batch.
        """
        if hasattr(self.job_store, "get_batch_jobs"):
            return self.job_store.get_batch_jobs(batch_id)

        # Fallback for job stores that don't support batch operations
        jobs = self.list_jobs()
        return [job for job in jobs if getattr(job, "batch_id", None) == batch_id]

    def add_job_dependency(self, job_id: str, depends_on_id: str) -> bool:
        """
        Add a dependency relationship between jobs.

        Args:
            job_id: ID of the job that depends on another.
            depends_on_id: ID of the job that must complete first.

        Returns:
            True if the dependency was added, False otherwise.
        """
        # Get both jobs to ensure they exist
        job = self.job_store.get(job_id)
        depends_on = self.job_store.get(depends_on_id)

        if not job or not depends_on:
            return False

        # Don't allow circular dependencies or self-dependencies
        if job_id == depends_on_id:
            return False

        # Use store-specific method if available
        if hasattr(self.job_store, "add_job_dependency"):
            return self.job_store.add_job_dependency(job_id, depends_on_id)

        # Fallback implementation
        job.add_dependency(depends_on_id)
        self.job_store.save(job)
        return True

    def remove_job_dependency(self, job_id: str, depends_on_id: str) -> bool:
        """
        Remove a dependency relationship between jobs.

        Args:
            job_id: ID of the job that depends on another.
            depends_on_id: ID of the job that should no longer be a dependency.

        Returns:
            True if the dependency was removed, False otherwise.
        """
        # Get the job
        job = self.job_store.get(job_id)
        if not job:
            return False

        # Use store-specific method if available
        if hasattr(self.job_store, "remove_job_dependency"):
            return self.job_store.remove_job_dependency(job_id, depends_on_id)

        # Fallback implementation
        job.remove_dependency(depends_on_id)
        self.job_store.save(job)
        return True

    def get_dependencies(self, job_id: str) -> List[Job]:
        """
        Get all jobs that a job depends on.

        Args:
            job_id: ID of the job to find dependencies for.

        Returns:
            List of jobs that the specified job depends on.
        """
        job = self.job_store.get(job_id)
        if not job:
            return []

        # Use store-specific method if available
        if hasattr(self.job_store, "get_dependencies"):
            return self.job_store.get_dependencies(job_id)

        # Fallback implementation
        return [
            self.job_store.get(dep_id)
            for dep_id in job.dependencies
            if self.job_store.get(dep_id)
        ]

    def get_dependent_jobs(self, job_id: str) -> List[Job]:
        """
        Get all jobs that depend on a job.

        Args:
            job_id: ID of the job to find dependents for.

        Returns:
            List of jobs that depend on the specified job.
        """
        # Use store-specific method if available
        if hasattr(self.job_store, "get_dependent_jobs"):
            return self.job_store.get_dependent_jobs(job_id)

        # Fallback implementation - this is inefficient but works with any store
        all_jobs = self.list_jobs()
        return [job for job in all_jobs if job_id in job.dependencies]

    def process_completed_job(self, job_id: str) -> None:
        """
        Process a job that has completed and start dependent jobs if ready.

        Args:
            job_id: ID of the completed job.
        """
        # Get dependent jobs
        dependent_jobs = self.get_dependent_jobs(job_id)

        for dependent in dependent_jobs:
            # Check if all dependencies are complete
            all_dependencies_complete = True
            for dep_id in dependent.dependencies:
                dep_job = self.job_store.get(dep_id)
                if not dep_job or dep_job.status != JobStatus.COMPLETED:
                    all_dependencies_complete = False
                    break

            # If all dependencies are complete, start the job
            if all_dependencies_complete and dependent.status == JobStatus.PENDING:
                self.start_job(dependent.job_id)

    def start_distributed_mode(self, worker_manager=None) -> None:
        """
        Start the job manager in distributed mode.

        Args:
            worker_manager: Optional WorkerManager instance
        """
        if self.distributed_mode:
            logger.warning("Job manager is already in distributed mode")
            return

        self.distributed_mode = True

        # Import WorkerManager if needed
        if worker_manager is None:
            from openagents_json.job.worker import WorkerManager

            worker_manager = WorkerManager(self.job_store)

        self.worker_manager = worker_manager

        # Start the worker manager
        asyncio.create_task(self.worker_manager.start())

        logger.info("Started job manager in distributed mode")

        # Emit system event
        event_emitter.emit(
            Event(
                event_type=EventType.SYSTEM_STARTUP,
                data={"mode": "distributed", "worker_manager": True},
            )
        )

    def stop_distributed_mode(self) -> None:
        """Stop the job manager's distributed mode."""
        if not self.distributed_mode:
            logger.warning("Job manager is not in distributed mode")
            return

        self.distributed_mode = False

        # Stop the worker manager if it exists
        if self.worker_manager:
            asyncio.create_task(self.worker_manager.stop())
            self.worker_manager = None

        logger.info("Stopped job manager's distributed mode")

        # Emit system event
        event_emitter.emit(
            Event(
                event_type=EventType.SYSTEM_SHUTDOWN,
                data={"mode": "distributed", "worker_manager": False},
            )
        )
