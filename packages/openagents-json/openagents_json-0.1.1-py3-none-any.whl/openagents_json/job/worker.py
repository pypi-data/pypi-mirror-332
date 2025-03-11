"""
Worker implementation for distributed job execution in the OpenAgents JSON framework.

This module provides the Worker class and related functionality for distributed
job execution across multiple processes or machines. The worker system includes:
- Worker registration and heartbeat monitoring
- Job claiming and locking mechanisms
- Failure detection and recovery
- Worker-specific configuration
"""

import asyncio
import logging
import os
import platform
import socket
import time
import uuid
from datetime import datetime, timedelta
from typing import Any, Awaitable, Callable, Dict, List, Optional, Union

from openagents_json.job.events import Event, EventType, event_emitter
from openagents_json.job.model import Job, JobStatus
from openagents_json.job.storage import JobStore

logger = logging.getLogger(__name__)


class Worker:
    """
    Worker for distributed job execution.

    A worker is responsible for claiming and executing jobs from a shared
    job store. Multiple workers can operate concurrently, with job locking
    mechanisms to prevent duplicate execution.
    """

    def __init__(
        self,
        worker_id: Optional[str] = None,
        job_store: Optional[JobStore] = None,
        heartbeat_interval: int = 60,
        job_claim_batch_size: int = 5,
        max_concurrent_jobs: int = 5,
        tags: Optional[List[str]] = None,
        executor: Optional[Callable[[Job], Awaitable[Any]]] = None,
    ):
        """
        Initialize a worker.

        Args:
            worker_id: Unique identifier for this worker (auto-generated if None)
            job_store: Storage backend for jobs
            heartbeat_interval: Seconds between worker heartbeats
            job_claim_batch_size: Number of jobs to claim in a single operation
            max_concurrent_jobs: Maximum number of jobs to execute concurrently
            tags: Tags determining which jobs this worker can claim
            executor: Function to execute jobs
        """
        self.worker_id = worker_id or f"worker-{uuid.uuid4()}"
        self.job_store = job_store
        self.heartbeat_interval = heartbeat_interval
        self.job_claim_batch_size = job_claim_batch_size
        self.max_concurrent_jobs = max_concurrent_jobs
        self.tags = tags or []
        self.executor = executor

        # Worker metadata
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)
        self.os = platform.system()
        self.process_id = os.getpid()

        # Runtime state
        self.running = False
        self.running_jobs: Dict[str, asyncio.Task] = {}
        self.heartbeat_task: Optional[asyncio.Task] = None
        self.claim_task: Optional[asyncio.Task] = None

        logger.info(f"Worker {self.worker_id} initialized on {self.host} ({self.ip})")

    async def register(self) -> bool:
        """
        Register this worker with the job store.

        Returns:
            True if registration succeeded, False otherwise
        """
        # Create worker registration data
        registration_data = {
            "worker_id": self.worker_id,
            "host": self.host,
            "ip": self.ip,
            "os": self.os,
            "process_id": self.process_id,
            "tags": self.tags,
            "max_concurrent_jobs": self.max_concurrent_jobs,
            "heartbeat_interval": self.heartbeat_interval,
            "registered_at": datetime.now().isoformat(),
            "last_heartbeat": datetime.now().isoformat(),
            "status": "online",
        }

        # Register with job store
        try:
            if not hasattr(self.job_store, "register_worker"):
                logger.error(
                    f"Job store {self.job_store.__class__.__name__} does not support worker registration"
                )
                return False

            success = await self.job_store.register_worker(registration_data)

            if success:
                logger.info(f"Worker {self.worker_id} registered successfully")

                # Emit worker registered event
                event_emitter.emit(
                    Event(
                        event_type=EventType.WORKER_REGISTERED,
                        worker_id=self.worker_id,
                        data=registration_data,
                    )
                )

                return True
            else:
                logger.error(f"Failed to register worker {self.worker_id}")
                return False

        except Exception as e:
            logger.error(f"Error registering worker {self.worker_id}: {str(e)}")
            return False

    async def heartbeat(self) -> bool:
        """
        Send a heartbeat to the job store.

        Returns:
            True if heartbeat succeeded, False otherwise
        """
        # Create heartbeat data
        heartbeat_data = {
            "worker_id": self.worker_id,
            "timestamp": datetime.now().isoformat(),
            "running_jobs": len(self.running_jobs),
            "running_job_ids": list(self.running_jobs.keys()),
            "status": "online",
        }

        # Send heartbeat to job store
        try:
            if not hasattr(self.job_store, "update_worker_heartbeat"):
                logger.error(
                    f"Job store {self.job_store.__class__.__name__} does not support worker heartbeats"
                )
                return False

            success = await self.job_store.update_worker_heartbeat(
                self.worker_id, heartbeat_data
            )

            if success:
                logger.debug(f"Worker {self.worker_id} heartbeat sent")

                # Emit worker heartbeat event
                event_emitter.emit(
                    Event(
                        event_type=EventType.WORKER_HEARTBEAT,
                        worker_id=self.worker_id,
                        data=heartbeat_data,
                    )
                )

                return True
            else:
                logger.warning(f"Failed to send heartbeat for worker {self.worker_id}")
                return False

        except Exception as e:
            logger.error(
                f"Error sending heartbeat for worker {self.worker_id}: {str(e)}"
            )
            return False

    async def claim_jobs(self) -> List[Job]:
        """
        Claim available jobs from the job store.

        Returns:
            List of claimed jobs
        """
        # Skip claiming if we're at capacity
        if len(self.running_jobs) >= self.max_concurrent_jobs:
            return []

        # Calculate how many jobs we can claim
        available_slots = self.max_concurrent_jobs - len(self.running_jobs)
        claim_count = min(available_slots, self.job_claim_batch_size)

        # Claim jobs from store
        try:
            if not hasattr(self.job_store, "claim_jobs"):
                logger.error(
                    f"Job store {self.job_store.__class__.__name__} does not support claiming jobs"
                )
                return []

            claimed_jobs = await self.job_store.claim_jobs(
                worker_id=self.worker_id, count=claim_count, tags=self.tags
            )

            if claimed_jobs:
                logger.info(f"Worker {self.worker_id} claimed {len(claimed_jobs)} jobs")

                # Emit events for claimed jobs
                for job in claimed_jobs:
                    event_emitter.emit(
                        Event(
                            event_type=EventType.WORKER_CLAIMED_JOB,
                            worker_id=self.worker_id,
                            job_id=job.job_id,
                            data={
                                "job": job.to_dict(),
                                "claimed_at": datetime.now().isoformat(),
                            },
                        )
                    )

                    # Start executing each claimed job
                    self.running_jobs[job.job_id] = asyncio.create_task(
                        self.execute_job(job)
                    )

            return claimed_jobs

        except Exception as e:
            logger.error(f"Error claiming jobs for worker {self.worker_id}: {str(e)}")
            return []

    async def execute_job(self, job: Job) -> None:
        """
        Execute a claimed job.

        This handles the complete execution lifecycle including status updates,
        result tracking, error handling, and cleanup.

        Args:
            job: The job to execute
        """
        if not self.running:
            logger.warning(
                f"Worker {self.worker_id} not running, cannot execute job {job.job_id}"
            )
            return

        logger.info(f"Worker {self.worker_id} executing job {job.job_id}")

        # Update job status and metadata
        original_status = job.status
        job.status = JobStatus.RUNNING
        job.worker_id = self.worker_id
        job.started_at = datetime.now()
        job.updated_at = job.started_at

        # Save initial status to store
        try:
            await self.job_store.update_job(job)

            # Emit job started event
            event_emitter.emit(
                Event.from_job(event_type=EventType.JOB_STARTED, job=job)
            )

        except Exception as e:
            logger.error(f"Failed to update job {job.job_id} status: {str(e)}")
            if job.job_id in self.running_jobs:
                del self.running_jobs[job.job_id]
            return

        # Track job execution progress
        result = None
        error = None

        try:
            # Execute job using custom executor if provided
            if self.executor:
                # Custom executor
                result = await self.executor(job)
            else:
                # Default execution
                # Placeholder for actual job execution
                for i in range(10):
                    # Check if worker is still running
                    if not self.running:
                        logger.warning(
                            f"Worker {self.worker_id} stopped during job {job.job_id} execution"
                        )
                        raise asyncio.CancelledError("Worker stopped")

                    # Update progress
                    progress = (i + 1) / 10.0
                    job.set_progress(progress)
                    await self.job_store.update_job(job)

                    # Emit progress event
                    event_emitter.emit(
                        Event.from_job(
                            event_type=EventType.JOB_PROGRESS_UPDATED,
                            job=job,
                            progress=progress * 100,
                        )
                    )

                    await asyncio.sleep(0.2)  # Simulate work

                # Set success result
                result = {"status": "success", "message": "Job completed successfully"}

        except asyncio.CancelledError:
            # Job was cancelled
            logger.info(f"Job {job.job_id} cancelled")
            job.status = JobStatus.CANCELLED
            job.updated_at = datetime.now()

            # Emit job cancelled event
            event_emitter.emit(
                Event.from_job(event_type=EventType.JOB_CANCELLED, job=job)
            )

        except Exception as e:
            # Job failed
            logger.error(f"Error executing job {job.job_id}: {str(e)}")
            job.status = JobStatus.FAILED
            job.updated_at = datetime.now()

            # Capture error details
            error = {
                "message": str(e),
                "type": e.__class__.__name__,
                "timestamp": datetime.now().isoformat(),
            }
            job.error = error

            # Emit job failed event
            event_emitter.emit(
                Event.from_job(event_type=EventType.JOB_FAILED, job=job, error=error)
            )

        else:
            # Job completed successfully
            job.status = JobStatus.COMPLETED
            job.result = result
            job.completed_at = datetime.now()
            job.updated_at = job.completed_at

            # Emit job completed event
            event_emitter.emit(
                Event.from_job(
                    event_type=EventType.JOB_COMPLETED, job=job, result=result
                )
            )

        finally:
            # Save final status to store
            try:
                await self.job_store.update_job(job)
            except Exception as e:
                logger.error(
                    f"Failed to update job {job.job_id} final status: {str(e)}"
                )

            # Clean up
            if job.job_id in self.running_jobs:
                del self.running_jobs[job.job_id]

    async def start(self) -> None:
        """Start the worker to process jobs."""
        if self.running:
            logger.warning(f"Worker {self.worker_id} is already running")
            return

        logger.info(f"Starting worker {self.worker_id}")
        self.running = True

        # Register with job store
        registration_success = await self.register()
        if not registration_success:
            logger.error(f"Failed to register worker {self.worker_id}, stopping")
            self.running = False
            return

        # Start heartbeat task
        self.heartbeat_task = asyncio.create_task(self._heartbeat_loop())

        # Start job claiming loop
        self.claim_task = asyncio.create_task(self._worker_loop())

        logger.info(f"Worker {self.worker_id} started successfully")

    async def _worker_loop(self) -> None:
        """Main worker loop for claiming and executing jobs."""
        while self.running:
            try:
                # Claim available jobs
                if len(self.running_jobs) < self.max_concurrent_jobs:
                    await self.claim_jobs()

                # Wait before next claim attempt
                await asyncio.sleep(1)

            except asyncio.CancelledError:
                logger.info(f"Worker {self.worker_id} loop cancelled")
                break

            except Exception as e:
                logger.error(f"Error in worker {self.worker_id} loop: {str(e)}")
                await asyncio.sleep(5)  # Wait before retry

    async def _heartbeat_loop(self) -> None:
        """Loop for sending periodic heartbeats."""
        while self.running:
            try:
                await self.heartbeat()
                await asyncio.sleep(self.heartbeat_interval)

            except asyncio.CancelledError:
                logger.info(f"Worker {self.worker_id} heartbeat loop cancelled")
                break

            except Exception as e:
                logger.error(f"Error in worker {self.worker_id} heartbeat: {str(e)}")
                await asyncio.sleep(5)  # Wait before retry

    async def stop(self) -> None:
        """Stop the worker gracefully."""
        if not self.running:
            logger.warning(f"Worker {self.worker_id} is not running")
            return

        logger.info(f"Stopping worker {self.worker_id}")
        self.running = False

        # Cancel heartbeat task
        if self.heartbeat_task:
            self.heartbeat_task.cancel()

        # Cancel claim task
        if self.claim_task:
            self.claim_task.cancel()

        # Cancel all running jobs
        for job_id, task in list(self.running_jobs.items()):
            logger.info(f"Cancelling job {job_id}")
            task.cancel()

        # Wait for all tasks to complete
        await asyncio.sleep(0.5)

        # Update worker status to offline
        try:
            if hasattr(self.job_store, "update_worker_status"):
                await self.job_store.update_worker_status(
                    self.worker_id,
                    {"status": "offline", "stopped_at": datetime.now().isoformat()},
                )

                # Emit worker offline event
                event_emitter.emit(
                    Event(
                        event_type=EventType.WORKER_OFFLINE,
                        worker_id=self.worker_id,
                        data={"stopped_at": datetime.now().isoformat()},
                    )
                )

        except Exception as e:
            logger.error(
                f"Error updating worker {self.worker_id} status to offline: {str(e)}"
            )

        logger.info(f"Worker {self.worker_id} stopped")


class WorkerManager:
    """
    Manager for coordinating multiple workers.

    Handles worker health checking, dead worker detection, and
    job reassignment.
    """

    def __init__(
        self,
        job_store: JobStore,
        heartbeat_timeout: int = 120,
        check_interval: int = 60,
    ):
        """
        Initialize a worker manager.

        Args:
            job_store: Storage backend for jobs and worker state
            heartbeat_timeout: Seconds before a worker is considered dead
            check_interval: Seconds between worker health checks
        """
        self.job_store = job_store
        self.heartbeat_timeout = heartbeat_timeout
        self.check_interval = check_interval
        self.running = False
        self.health_check_task: Optional[asyncio.Task] = None

        logger.info(
            f"WorkerManager initialized with heartbeat timeout {heartbeat_timeout}s"
        )

    async def start(self) -> None:
        """Start the worker manager."""
        if self.running:
            logger.warning("WorkerManager is already running")
            return

        logger.info("Starting WorkerManager")
        self.running = True

        # Start health check loop
        self.health_check_task = asyncio.create_task(self._health_check_loop())

        logger.info("WorkerManager started")

    async def stop(self) -> None:
        """Stop the worker manager."""
        if not self.running:
            logger.warning("WorkerManager is not running")
            return

        logger.info("Stopping WorkerManager")
        self.running = False

        # Cancel health check task
        if self.health_check_task:
            self.health_check_task.cancel()

        logger.info("WorkerManager stopped")

    async def _health_check_loop(self) -> None:
        """Loop for periodic worker health checking."""
        while self.running:
            try:
                await self._check_workers()
                await asyncio.sleep(self.check_interval)

            except asyncio.CancelledError:
                logger.info("WorkerManager health check loop cancelled")
                break

            except Exception as e:
                logger.error(f"Error in WorkerManager health check: {str(e)}")
                await asyncio.sleep(5)  # Wait before retry

    async def _check_workers(self) -> None:
        """Check for dead workers and handle their jobs."""
        if not hasattr(self.job_store, "get_workers"):
            logger.error(
                f"Job store {self.job_store.__class__.__name__} does not support worker management"
            )
            return

        # Get all registered workers
        workers = await self.job_store.get_workers()

        # Check each worker's heartbeat
        now = datetime.now()
        for worker in workers:
            worker_id = worker.get("worker_id")
            last_heartbeat_str = worker.get("last_heartbeat")
            status = worker.get("status", "unknown")

            # Skip workers already marked as offline
            if status == "offline":
                continue

            # Parse last heartbeat
            try:
                last_heartbeat = datetime.fromisoformat(last_heartbeat_str)
                time_since_heartbeat = (now - last_heartbeat).total_seconds()

                # Check if worker is dead
                if time_since_heartbeat > self.heartbeat_timeout:
                    logger.warning(
                        f"Worker {worker_id} appears to be dead (no heartbeat for {time_since_heartbeat:.1f}s)"
                    )
                    await self._handle_dead_worker(worker)
            except Exception as e:
                logger.error(f"Error checking worker {worker_id} health: {str(e)}")

    async def _handle_dead_worker(self, worker: Dict[str, Any]) -> None:
        """
        Handle a dead worker by releasing its jobs and updating its status.

        Args:
            worker: Worker data dictionary
        """
        worker_id = worker.get("worker_id")

        # Update worker status to offline
        try:
            await self.job_store.update_worker_status(
                worker_id,
                {
                    "status": "offline",
                    "marked_dead_at": datetime.now().isoformat(),
                    "reason": "heartbeat_timeout",
                },
            )

            # Emit worker offline event
            event_emitter.emit(
                Event(
                    event_type=EventType.WORKER_OFFLINE,
                    worker_id=worker_id,
                    data={
                        "marked_dead_at": datetime.now().isoformat(),
                        "reason": "heartbeat_timeout",
                    },
                )
            )

        except Exception as e:
            logger.error(f"Error updating dead worker {worker_id} status: {str(e)}")

        # Release assigned jobs
        try:
            if hasattr(self.job_store, "release_worker_jobs"):
                released_count = await self.job_store.release_worker_jobs(worker_id)
                logger.info(
                    f"Released {released_count} jobs from dead worker {worker_id}"
                )
        except Exception as e:
            logger.error(f"Error releasing jobs from dead worker {worker_id}: {str(e)}")
