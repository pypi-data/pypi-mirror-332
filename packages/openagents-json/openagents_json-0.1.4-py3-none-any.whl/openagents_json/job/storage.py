"""
Job storage implementations for the OpenAgents JSON framework.

This module provides storage backends for persisting and retrieving jobs,
with implementations for in-memory, file-based, and database storage.
"""

import abc
import json
import logging
import os
import threading
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from sqlalchemy import and_, asc, desc, or_
from sqlalchemy.exc import SQLAlchemyError

from openagents_json.job.database import (
    Base,
    JobModel,
    TagModel,
    build_connection_string,
    get_engine,
    get_session_factory,
    init_db,
)
from openagents_json.job.model import Job, JobStatus


class BaseJobStore(abc.ABC):
    """
    Abstract base class for job storage.

    Provides interface for storing and retrieving jobs with various
    filtering and sorting capabilities.
    """

    @abc.abstractmethod
    def save(self, job: Job) -> None:
        """
        Save a job to the store.

        Args:
            job: The job to save.
        """
        pass

    @abc.abstractmethod
    def get(self, job_id: str) -> Optional[Job]:
        """
        Retrieve a job by its ID.

        Args:
            job_id: The ID of the job to retrieve.

        Returns:
            The job if found, None otherwise.
        """
        pass

    @abc.abstractmethod
    def delete(self, job_id: str) -> bool:
        """
        Delete a job from the store.

        Args:
            job_id: The ID of the job to delete.

        Returns:
            True if the job was deleted, False otherwise.
        """
        pass

    @abc.abstractmethod
    def list(
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
            status: Filter by job status(es).
            workflow_id: Filter by workflow ID.
            user_id: Filter by user ID.
            tags: Filter by tags (jobs must have all specified tags).
            created_after: Filter by creation date (include jobs created after this ISO datetime).
            created_before: Filter by creation date (include jobs created before this ISO datetime).
            limit: Maximum number of jobs to return.
            offset: Number of jobs to skip.
            sort_by: Field to sort by.
            sort_order: Sort order ("asc" or "desc").

        Returns:
            List of jobs matching the criteria.
        """
        pass

    @abc.abstractmethod
    def cleanup_old_jobs(self, days: int) -> int:
        """
        Clean up jobs older than a specified number of days.

        Args:
            days: Number of days to keep jobs for.

        Returns:
            Number of jobs cleaned up.
        """
        pass

    # Worker support methods - these are optional for storage backends

    def register_worker(self, worker_info: Dict[str, Any]) -> bool:
        """
        Register a worker in the system.

        This is an optional method for storage backends that support
        worker registration for distributed execution.

        Args:
            worker_info: Dictionary with worker information

        Returns:
            True if registration was successful, False otherwise
        """
        # Default implementation for storage backends that don't support workers
        return False

    def update_worker_heartbeat(
        self, worker_id: str, last_heartbeat: str, running_jobs: List[str]
    ) -> bool:
        """
        Update a worker's heartbeat timestamp.

        This is an optional method for storage backends that support
        worker heartbeats for distributed execution.

        Args:
            worker_id: Worker identifier
            last_heartbeat: ISO format timestamp of the heartbeat
            running_jobs: List of job IDs currently running on this worker

        Returns:
            True if update was successful, False otherwise
        """
        # Default implementation for storage backends that don't support workers
        return False

    def get_workers(self) -> List[Dict[str, Any]]:
        """
        Get a list of all registered workers.

        This is an optional method for storage backends that support
        worker registration for distributed execution.

        Returns:
            List of dictionaries with worker information
        """
        # Default implementation for storage backends that don't support workers
        return []

    def get_jobs_by_worker(self, worker_id: str) -> List[Job]:
        """
        Get all jobs assigned to a specific worker.

        This is an optional method for storage backends that support
        worker job assignment for distributed execution.

        Args:
            worker_id: Worker identifier

        Returns:
            List of jobs assigned to the worker
        """
        # Default implementation for storage backends that don't support workers
        return []

    def reset_worker_jobs(self, worker_id: str) -> bool:
        """
        Reset all jobs assigned to a worker back to PENDING status.

        This is used when a worker is detected as dead to reassign its jobs.
        This is an optional method for storage backends that support
        worker job assignment for distributed execution.

        Args:
            worker_id: Worker identifier

        Returns:
            True if reset was successful, False otherwise
        """
        # Default implementation for storage backends that don't support workers
        return False

    def claim_jobs_for_worker(
        self, worker_id: str, batch_size: int, tags: Optional[List[str]] = None
    ) -> List[Job]:
        """
        Claim jobs for a worker to execute.

        This is an optional method for storage backends that support
        worker job claiming for distributed execution.

        Args:
            worker_id: Worker identifier
            batch_size: Maximum number of jobs to claim
            tags: Optional list of tags to filter jobs by

        Returns:
            List of jobs claimed by the worker
        """
        # Default implementation for storage backends that don't support workers
        return []

    def recover_interrupted_jobs(self) -> List[Job]:
        """
        Recover jobs that were interrupted by system failure.

        This method finds jobs in RUNNING state that might have been
        interrupted by a system crash or shutdown, and resets them
        to PENDING state so they can be retried.

        Returns:
            List of recovered jobs
        """
        # Default implementation does nothing
        return []


class MemoryJobStore(BaseJobStore):
    """
    In-memory implementation of JobStore.

    Stores jobs in memory with thread-safe access. Suitable for
    development and testing, but not for production use as jobs
    are lost when the application restarts.
    """

    def __init__(self):
        """Initialize in-memory job store."""
        self.jobs: Dict[str, Job] = {}
        self.lock = threading.RLock()

    def save(self, job: Job) -> None:
        """
        Save a job to the in-memory store.

        Args:
            job: The job to save.
        """
        with self.lock:
            self.jobs[job.job_id] = job

    def get(self, job_id: str) -> Optional[Job]:
        """
        Retrieve a job by its ID from the in-memory store.

        Args:
            job_id: The ID of the job to retrieve.

        Returns:
            The job if found, None otherwise.
        """
        with self.lock:
            return self.jobs.get(job_id)

    def delete(self, job_id: str) -> bool:
        """
        Delete a job from the in-memory store.

        Args:
            job_id: The ID of the job to delete.

        Returns:
            True if the job was deleted, False otherwise.
        """
        with self.lock:
            if job_id in self.jobs:
                del self.jobs[job_id]
                return True
            return False

    def list(
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
        List jobs with optional filtering and sorting from the in-memory store.

        Args:
            status: Filter by job status(es).
            workflow_id: Filter by workflow ID.
            user_id: Filter by user ID.
            tags: Filter by tags (jobs must have all specified tags).
            created_after: Filter by creation date (include jobs created after this ISO datetime).
            created_before: Filter by creation date (include jobs created before this ISO datetime).
            limit: Maximum number of jobs to return.
            offset: Number of jobs to skip.
            sort_by: Field to sort by.
            sort_order: Sort order ("asc" or "desc").

        Returns:
            List of jobs matching the criteria.
        """
        with self.lock:
            # Start with all jobs
            filtered_jobs = list(self.jobs.values())

            # Apply filters
            if status is not None:
                statuses = [status] if isinstance(status, JobStatus) else status
                filtered_jobs = [job for job in filtered_jobs if job.status in statuses]

            if workflow_id is not None:
                filtered_jobs = [
                    job for job in filtered_jobs if job.workflow_id == workflow_id
                ]

            if user_id is not None:
                filtered_jobs = [job for job in filtered_jobs if job.user_id == user_id]

            if tags is not None and tags:
                filtered_jobs = [
                    job for job in filtered_jobs if all(tag in job.tags for tag in tags)
                ]

            if created_after is not None:
                filtered_jobs = [
                    job for job in filtered_jobs if job.created_at >= created_after
                ]

            if created_before is not None:
                filtered_jobs = [
                    job for job in filtered_jobs if job.created_at <= created_before
                ]

            # Sort jobs
            reverse = sort_order.lower() == "desc"
            filtered_jobs.sort(
                key=lambda job: getattr(job, sort_by, job.created_at), reverse=reverse
            )

            # Apply pagination
            start = offset
            end = None if limit is None else offset + limit
            return filtered_jobs[start:end]

    def cleanup_old_jobs(self, days: int) -> int:
        """
        Clean up jobs older than a specified number of days from the in-memory store.

        Args:
            days: Number of days to keep jobs for.

        Returns:
            Number of jobs cleaned up.
        """
        with self.lock:
            cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
            job_ids_to_delete = [
                job_id
                for job_id, job in self.jobs.items()
                if job.created_at < cutoff_date
            ]

            for job_id in job_ids_to_delete:
                del self.jobs[job_id]

            return len(job_ids_to_delete)


class FileJobStore(BaseJobStore):
    """
    File-based implementation of JobStore.

    Stores jobs as JSON files in the provided directory. Provides
    persistent storage suitable for simple deployments or development.
    """

    def __init__(self, storage_dir: Union[str, Path] = ".jobs"):
        """
        Initialize file-based job store.

        Args:
            storage_dir: Directory to store job files in.
        """
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.lock = threading.RLock()

    def _get_job_path(self, job_id: str) -> Path:
        """
        Get the file path for a job.

        Args:
            job_id: Job ID.

        Returns:
            Path to the job file.
        """
        return self.storage_dir / f"{job_id}.json"

    def save(self, job: Job) -> None:
        """
        Save a job to a file.

        Args:
            job: The job to save.
        """
        with self.lock:
            job_path = self._get_job_path(job.job_id)
            with open(job_path, "w") as f:
                json.dump(job.to_dict(), f, indent=2)

    def get(self, job_id: str) -> Optional[Job]:
        """
        Retrieve a job by its ID from a file.

        Args:
            job_id: The ID of the job to retrieve.

        Returns:
            The job if found, None otherwise.
        """
        with self.lock:
            job_path = self._get_job_path(job_id)
            if not job_path.exists():
                return None

            try:
                with open(job_path, "r") as f:
                    job_data = json.load(f)
                return Job.from_dict(job_data)
            except (json.JSONDecodeError, IOError):
                return None

    def delete(self, job_id: str) -> bool:
        """
        Delete a job file.

        Args:
            job_id: The ID of the job to delete.

        Returns:
            True if the job was deleted, False otherwise.
        """
        with self.lock:
            job_path = self._get_job_path(job_id)
            if job_path.exists():
                job_path.unlink()
                return True
            return False

    def list(
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
        List jobs with optional filtering and sorting from files.

        Args:
            status: Filter by job status(es).
            workflow_id: Filter by workflow ID.
            user_id: Filter by user ID.
            tags: Filter by tags (jobs must have all specified tags).
            created_after: Filter by creation date (include jobs created after this ISO datetime).
            created_before: Filter by creation date (include jobs created before this ISO datetime).
            limit: Maximum number of jobs to return.
            offset: Number of jobs to skip.
            sort_by: Field to sort by.
            sort_order: Sort order ("asc" or "desc").

        Returns:
            List of jobs matching the criteria.
        """
        with self.lock:
            # Load all jobs from files
            jobs = []
            for job_file in self.storage_dir.glob("*.json"):
                try:
                    with open(job_file, "r") as f:
                        job_data = json.load(f)
                    jobs.append(Job.from_dict(job_data))
                except (json.JSONDecodeError, IOError):
                    continue

            # Apply filters
            if status is not None:
                statuses = [status] if isinstance(status, JobStatus) else status
                jobs = [job for job in jobs if job.status in statuses]

            if workflow_id is not None:
                jobs = [job for job in jobs if job.workflow_id == workflow_id]

            if user_id is not None:
                jobs = [job for job in jobs if job.user_id == user_id]

            if tags is not None and tags:
                jobs = [job for job in jobs if all(tag in job.tags for tag in tags)]

            if created_after is not None:
                jobs = [job for job in jobs if job.created_at >= created_after]

            if created_before is not None:
                jobs = [job for job in jobs if job.created_at <= created_before]

            # Sort jobs
            reverse = sort_order.lower() == "desc"
            jobs.sort(
                key=lambda job: getattr(job, sort_by, job.created_at), reverse=reverse
            )

            # Apply pagination
            start = offset
            end = None if limit is None else offset + limit
            return jobs[start:end]

    def cleanup_old_jobs(self, days: int) -> int:
        """
        Clean up jobs older than a specified number of days from files.

        Args:
            days: Number of days to keep jobs for.

        Returns:
            Number of jobs cleaned up.
        """
        with self.lock:
            cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
            deleted_count = 0

            for job_file in self.storage_dir.glob("*.json"):
                try:
                    with open(job_file, "r") as f:
                        job_data = json.load(f)

                    if job_data.get("created_at", "") < cutoff_date:
                        job_file.unlink()
                        deleted_count += 1
                except (json.JSONDecodeError, IOError):
                    continue

            return deleted_count


class DatabaseJobStore(BaseJobStore):
    """
    Database implementation of JobStore using SQLAlchemy ORM.

    Stores jobs in a SQL database with support for SQLite, PostgreSQL,
    and MySQL backends. This is the primary production storage option,
    providing durability and performance.
    """

    def __init__(
        self,
        connection_string: Optional[str] = None,
        dialect: str = "sqlite",
        host: Optional[str] = None,
        port: Optional[int] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        database: Optional[str] = None,
        path: Optional[str] = None,
        pooling: bool = True,
        pool_size: int = 5,
        max_overflow: int = 10,
        pool_timeout: int = 30,
        pool_recycle: int = 3600,
        echo: bool = False,
    ):
        """
        Initialize database job store.

        Args:
            connection_string: Direct SQLAlchemy connection string (overrides other parameters).
            dialect: Database dialect (sqlite, postgresql, mysql).
            host: Database host (for postgresql, mysql).
            port: Database port (for postgresql, mysql).
            username: Database username (for postgresql, mysql).
            password: Database password (for postgresql, mysql).
            database: Database name (for postgresql, mysql).
            path: Database file path (for sqlite).
            pooling: Whether to enable connection pooling.
            pool_size: The size of the connection pool.
            max_overflow: The maximum overflow size of the pool.
            pool_timeout: The number of seconds to wait before giving up on getting a connection from the pool.
            pool_recycle: The number of seconds after which a connection is automatically recycled.
            echo: Whether to echo SQL queries (useful for debugging).
        """
        try:
            # Build connection string if not provided directly
            self.connection_string = connection_string or build_connection_string(
                dialect=dialect,
                host=host,
                port=port,
                username=username,
                password=password,
                database=database,
                path=path,
            )

            # Create engine and session factory with connection pooling
            self.engine = get_engine(
                self.connection_string,
                pooling=pooling,
                pool_size=pool_size,
                max_overflow=max_overflow,
                pool_timeout=pool_timeout,
                pool_recycle=pool_recycle,
                echo=echo,
            )
            self.Session = get_session_factory(self.engine)

            # Initialize database schema
            init_db(self.engine)

            logging.info(f"Initialized DatabaseJobStore with {dialect} backend")
        except Exception as e:
            logging.error(f"Failed to initialize DatabaseJobStore: {str(e)}")
            raise

    def close(self):
        """
        Close the database connection and release resources.
        Should be called when the job store is no longer needed.
        """
        if hasattr(self, "Session"):
            self.Session.remove()
        if hasattr(self, "engine"):
            self.engine.dispose()
            logging.info("JobStore closed and resources released")

    def save(self, job: Job) -> None:
        """
        Save a job to the database.

        Args:
            job: The job to save.
        """
        session = self.Session()
        try:
            # Check if job already exists
            existing_job = session.query(JobModel).filter_by(job_id=job.job_id).first()

            if existing_job:
                # Update existing job
                job_model = JobModel.from_job(job)
                for attr, value in vars(job_model).items():
                    if (
                        attr != "_sa_instance_state"
                        and attr != "tags"
                        and attr != "dependencies"
                    ):
                        setattr(existing_job, attr, value)

                # Clear and update tags
                existing_job.tags = []
                for tag_name in job.tags:
                    tag = session.query(TagModel).filter_by(name=tag_name).first()
                    if not tag:
                        tag = TagModel(name=tag_name)
                        session.add(tag)
                    existing_job.tags.append(tag)

                # Update dependencies
                existing_job.dependencies = []
                for dep_id in job.dependencies:
                    dep_job = session.query(JobModel).filter_by(job_id=dep_id).first()
                    if dep_job:
                        existing_job.dependencies.append(dep_job)
            else:
                # Create new job
                job_model = JobModel.from_job(job)
                session.add(job_model)

                # Add tags
                for tag_name in job.tags:
                    tag = session.query(TagModel).filter_by(name=tag_name).first()
                    if not tag:
                        tag = TagModel(name=tag_name)
                        session.add(tag)
                    job_model.tags.append(tag)

                # Add dependencies
                for dep_id in job.dependencies:
                    dep_job = session.query(JobModel).filter_by(job_id=dep_id).first()
                    if dep_job:
                        job_model.dependencies.append(dep_job)

            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error saving job {job.job_id}: {str(e)}")
            raise
        finally:
            session.close()

    def get(self, job_id: str) -> Optional[Job]:
        """
        Retrieve a job by its ID from the database.

        Args:
            job_id: The ID of the job to retrieve.

        Returns:
            The job if found, None otherwise.
        """
        session = self.Session()
        try:
            job_model = session.query(JobModel).filter_by(job_id=job_id).first()
            if job_model:
                return job_model.to_job()
            return None
        except SQLAlchemyError as e:
            logging.error(f"Error retrieving job {job_id}: {str(e)}")
            return None
        finally:
            session.close()

    def delete(self, job_id: str) -> bool:
        """
        Delete a job from the database.

        Args:
            job_id: The ID of the job to delete.

        Returns:
            True if the job was deleted, False otherwise.
        """
        session = self.Session()
        try:
            job_model = session.query(JobModel).filter_by(job_id=job_id).first()
            if job_model:
                session.delete(job_model)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error deleting job {job_id}: {str(e)}")
            return False
        finally:
            session.close()

    def _build_query_filters(
        self,
        status: Optional[Union[JobStatus, List[JobStatus]]] = None,
        workflow_id: Optional[str] = None,
        user_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
    ) -> List:
        """
        Build SQLAlchemy query filters based on parameters.

        Args:
            status: Filter by job status(es).
            workflow_id: Filter by workflow ID.
            user_id: Filter by user ID.
            tags: Filter by tags.
            created_after: Filter by creation date (after).
            created_before: Filter by creation date (before).

        Returns:
            List of SQLAlchemy filter conditions.
        """
        filters = []

        # Status filter
        if status is not None:
            if isinstance(status, JobStatus):
                filters.append(JobModel.status == status.value)
            else:
                filters.append(JobModel.status.in_([s.value for s in status]))

        # Workflow ID filter
        if workflow_id is not None:
            filters.append(JobModel.workflow_id == workflow_id)

        # User ID filter
        if user_id is not None:
            filters.append(JobModel.user_id == user_id)

        # Creation date filters
        if created_after is not None:
            filters.append(JobModel.created_at >= created_after)

        if created_before is not None:
            filters.append(JobModel.created_at <= created_before)

        return filters

    def list(
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
        List jobs with optional filtering and sorting from the database.

        Args:
            status: Filter by job status(es).
            workflow_id: Filter by workflow ID.
            user_id: Filter by user ID.
            tags: Filter by tags (jobs must have all specified tags).
            created_after: Filter by creation date (include jobs created after this ISO datetime).
            created_before: Filter by creation date (include jobs created before this ISO datetime).
            limit: Maximum number of jobs to return.
            offset: Number of jobs to skip.
            sort_by: Field to sort by.
            sort_order: Sort order ("asc" or "desc").

        Returns:
            List of jobs matching the criteria.
        """
        session = self.Session()
        try:
            # Build basic query with filters
            query = session.query(JobModel)

            # Apply basic filters
            filters = self._build_query_filters(
                status=status,
                workflow_id=workflow_id,
                user_id=user_id,
                created_after=created_after,
                created_before=created_before,
            )

            for filter_condition in filters:
                query = query.filter(filter_condition)

            # Handle tag filtering separately (it's more complex due to the many-to-many relationship)
            if tags and len(tags) > 0:
                for tag in tags:
                    query = query.filter(JobModel.tags.any(TagModel.tag == tag))

            # Apply sorting
            sort_column = getattr(JobModel, sort_by, JobModel.created_at)
            if sort_order.lower() == "desc":
                query = query.order_by(desc(sort_column))
            else:
                query = query.order_by(asc(sort_column))

            # Apply pagination
            if limit is not None:
                query = query.limit(limit)

            if offset > 0:
                query = query.offset(offset)

            # Execute query and convert results to Job objects
            job_models = query.all()
            return [job_model.to_job() for job_model in job_models]

        except SQLAlchemyError as e:
            logging.error(f"Error listing jobs: {str(e)}")
            return []
        finally:
            session.close()

    def cleanup_old_jobs(self, days: int) -> int:
        """
        Clean up jobs older than a specified number of days from the database.

        Args:
            days: Number of days to keep jobs for.

        Returns:
            Number of jobs cleaned up.
        """
        session = self.Session()
        try:
            # Calculate cutoff date
            cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()

            # Find jobs to delete
            jobs_to_delete = (
                session.query(JobModel).filter(JobModel.created_at < cutoff_date).all()
            )
            count = len(jobs_to_delete)

            # Delete jobs
            for job in jobs_to_delete:
                session.delete(job)

            session.commit()
            return count

        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error cleaning up old jobs: {str(e)}")
            return 0
        finally:
            session.close()

    def get_batch_jobs(self, batch_id: str) -> List[Job]:
        """
        Retrieve all jobs in a batch.

        Args:
            batch_id: The batch ID to retrieve jobs for.

        Returns:
            List of jobs in the batch.
        """
        session = self.Session()
        try:
            job_models = session.query(JobModel).filter_by(batch_id=batch_id).all()
            return [job_model.to_job() for job_model in job_models]
        except SQLAlchemyError as e:
            logging.error(f"Error retrieving jobs for batch {batch_id}: {str(e)}")
            return []
        finally:
            session.close()

    def get_dependent_jobs(self, job_id: str) -> List[Job]:
        """
        Retrieve all jobs that depend on the specified job.

        Args:
            job_id: ID of the job to find dependents for.

        Returns:
            List of jobs that depend on the specified job.
        """
        session = self.Session()
        try:
            job_model = session.query(JobModel).filter_by(job_id=job_id).first()
            if not job_model:
                return []

            dependent_jobs = [dep.to_job() for dep in job_model.dependent_jobs]
            return dependent_jobs
        except SQLAlchemyError as e:
            logging.error(f"Error retrieving dependent jobs for {job_id}: {str(e)}")
            return []
        finally:
            session.close()

    def get_dependencies(self, job_id: str) -> List[Job]:
        """
        Retrieve all jobs that the specified job depends on.

        Args:
            job_id: ID of the job to find dependencies for.

        Returns:
            List of jobs that the specified job depends on.
        """
        session = self.Session()
        try:
            job_model = session.query(JobModel).filter_by(job_id=job_id).first()
            if not job_model:
                return []

            dependencies = [dep.to_job() for dep in job_model.dependencies]
            return dependencies
        except SQLAlchemyError as e:
            logging.error(f"Error retrieving dependencies for {job_id}: {str(e)}")
            return []
        finally:
            session.close()

    def add_job_dependency(self, job_id: str, depends_on_id: str) -> bool:
        """
        Add a dependency relationship between jobs.

        Args:
            job_id: ID of the job that depends on another.
            depends_on_id: ID of the job that must complete first.

        Returns:
            True if dependency was added, False otherwise.
        """
        if job_id == depends_on_id:
            return False  # Can't depend on itself

        session = self.Session()
        try:
            job = session.query(JobModel).filter_by(job_id=job_id).first()
            depends_on = session.query(JobModel).filter_by(job_id=depends_on_id).first()

            if not job or not depends_on:
                return False

            # Check if dependency already exists
            if depends_on in job.dependencies:
                return True

            job.dependencies.append(depends_on)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(
                f"Error adding dependency {job_id} -> {depends_on_id}: {str(e)}"
            )
            return False
        finally:
            session.close()

    def remove_job_dependency(self, job_id: str, depends_on_id: str) -> bool:
        """
        Remove a dependency relationship between jobs.

        Args:
            job_id: ID of the job that depends on another.
            depends_on_id: ID of the job that must complete first.

        Returns:
            True if dependency was removed, False otherwise.
        """
        session = self.Session()
        try:
            job = session.query(JobModel).filter_by(job_id=job_id).first()
            depends_on = session.query(JobModel).filter_by(job_id=depends_on_id).first()

            if not job or not depends_on:
                return False

            if depends_on in job.dependencies:
                job.dependencies.remove(depends_on)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(
                f"Error removing dependency {job_id} -> {depends_on_id}: {str(e)}"
            )
            return False
        finally:
            session.close()

    def create_job_batch(self, jobs: List[Job], batch_id: Optional[str] = None) -> str:
        """
        Create a batch of jobs with a shared batch ID.

        Args:
            jobs: List of jobs to include in the batch.
            batch_id: Optional batch ID (generated if not provided).

        Returns:
            The batch ID.
        """
        if not jobs:
            return ""

        batch_id = batch_id or str(uuid.uuid4())
        session = self.Session()
        try:
            # Set batch ID on all jobs
            for job in jobs:
                job.set_batch_id(batch_id)
                job_model = JobModel.from_job(job)

                existing_job = (
                    session.query(JobModel).filter_by(job_id=job.job_id).first()
                )
                if existing_job:
                    existing_job.batch_id = batch_id
                else:
                    session.add(job_model)

                    # Add tags
                    for tag_name in job.tags:
                        tag = session.query(TagModel).filter_by(name=tag_name).first()
                        if not tag:
                            tag = TagModel(name=tag_name)
                            session.add(tag)
                        job_model.tags.append(tag)

                    # Add dependencies
                    for dep_id in job.dependencies:
                        dep_job = (
                            session.query(JobModel).filter_by(job_id=dep_id).first()
                        )
                        if dep_job:
                            job_model.dependencies.append(dep_job)

            session.commit()
            return batch_id
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error creating job batch: {str(e)}")
            raise
        finally:
            session.close()

    def register_worker(self, worker_info: Dict[str, Any]) -> bool:
        """
        Register a worker in the database.

        Args:
            worker_info: Dictionary with worker information

        Returns:
            True if registration was successful, False otherwise
        """
        from openagents_json.job.database import WorkerModel

        session = self.Session()
        try:
            # Check if worker already exists
            worker_id = worker_info.get("worker_id")
            if not worker_id:
                return False

            existing_worker = (
                session.query(WorkerModel).filter_by(worker_id=worker_id).first()
            )

            if existing_worker:
                # Update existing worker
                for key, value in worker_info.items():
                    if hasattr(existing_worker, key):
                        setattr(existing_worker, key, value)
                worker_model = existing_worker
            else:
                # Create new worker
                worker_model = WorkerModel.from_dict(worker_info)
                session.add(worker_model)

            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            logging.error(
                f"Error registering worker {worker_info.get('worker_id')}: {str(e)}"
            )
            return False
        finally:
            session.close()

    def update_worker_heartbeat(
        self, worker_id: str, last_heartbeat: str, running_jobs: List[str]
    ) -> bool:
        """
        Update a worker's heartbeat timestamp.

        Args:
            worker_id: Worker identifier
            last_heartbeat: ISO format timestamp of the heartbeat
            running_jobs: List of job IDs currently running on this worker

        Returns:
            True if update was successful, False otherwise
        """
        from openagents_json.job.database import WorkerModel

        session = self.Session()
        try:
            worker = session.query(WorkerModel).filter_by(worker_id=worker_id).first()

            if not worker:
                return False

            # Update heartbeat timestamp
            if isinstance(last_heartbeat, str):
                try:
                    timestamp = datetime.fromisoformat(last_heartbeat).timestamp()
                except ValueError:
                    timestamp = datetime.now().timestamp()
            else:
                timestamp = datetime.now().timestamp()

            worker.last_heartbeat = timestamp
            worker.running_jobs = running_jobs

            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error updating worker heartbeat {worker_id}: {str(e)}")
            return False
        finally:
            session.close()

    def get_workers(self) -> List[Dict[str, Any]]:
        """
        Get a list of all registered workers.

        Returns:
            List of dictionaries with worker information
        """
        from openagents_json.job.database import WorkerModel

        session = self.Session()
        try:
            workers = session.query(WorkerModel).all()
            return [worker.to_dict() for worker in workers]

        except SQLAlchemyError as e:
            logging.error(f"Error retrieving workers: {str(e)}")
            return []
        finally:
            session.close()

    def get_jobs_by_worker(self, worker_id: str) -> List[Job]:
        """
        Get all jobs assigned to a specific worker.

        Args:
            worker_id: Worker identifier

        Returns:
            List of jobs assigned to the worker
        """
        session = self.Session()
        try:
            # Find jobs where worker_id matches or metadata contains worker_id
            job_models = (
                session.query(JobModel)
                .filter(
                    or_(
                        JobModel.worker_id == worker_id,
                        JobModel.metadata.contains({"worker_id": worker_id}),
                    )
                )
                .all()
            )

            return [job_model.to_job() for job_model in job_models]

        except SQLAlchemyError as e:
            logging.error(f"Error retrieving jobs for worker {worker_id}: {str(e)}")
            return []
        finally:
            session.close()

    def reset_worker_jobs(self, worker_id: str) -> bool:
        """
        Reset all jobs assigned to a worker back to PENDING status.

        Args:
            worker_id: Worker identifier

        Returns:
            True if reset was successful, False otherwise
        """
        session = self.Session()
        try:
            # Find running jobs assigned to this worker
            job_models = (
                session.query(JobModel)
                .filter(
                    and_(
                        or_(
                            JobModel.worker_id == worker_id,
                            JobModel.metadata.contains({"worker_id": worker_id}),
                        ),
                        JobModel.status == JobStatus.RUNNING,
                    )
                )
                .all()
            )

            # Reset jobs to PENDING status
            for job_model in job_models:
                job_model.status = JobStatus.PENDING
                job_model.worker_id = None

                # Remove worker info from metadata if present
                if job_model.metadata and "worker_id" in job_model.metadata:
                    job_model.metadata.pop("worker_id")
                if job_model.metadata and "claimed_at" in job_model.metadata:
                    job_model.metadata.pop("claimed_at")

                job_model.updated_at = datetime.now().timestamp()

            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error resetting jobs for worker {worker_id}: {str(e)}")
            return False
        finally:
            session.close()

    def claim_jobs_for_worker(
        self, worker_id: str, batch_size: int, tags: Optional[List[str]] = None
    ) -> List[Job]:
        """
        Claim jobs for a worker to execute.

        Args:
            worker_id: Worker identifier
            batch_size: Maximum number of jobs to claim
            tags: Optional list of tags to filter jobs by

        Returns:
            List of jobs claimed by the worker
        """
        session = self.Session()
        try:
            # Start with a query for PENDING jobs
            query = session.query(JobModel).filter(JobModel.status == JobStatus.PENDING)

            # Apply tag filtering if provided
            if tags and len(tags) > 0:
                from openagents_json.job.database import TagModel, job_tags

                tag_subquery = (
                    session.query(TagModel.id)
                    .filter(TagModel.name.in_(tags))
                    .subquery()
                )

                query = query.join(job_tags).filter(job_tags.c.tag_id.in_(tag_subquery))

            # Order by priority and creation time
            query = query.order_by(desc(JobModel.priority), asc(JobModel.created_at))

            # Limit to batch size
            query = query.limit(batch_size)

            # Execute query to get candidate jobs
            candidate_jobs = query.all()

            # Check for dependencies and claim jobs
            claimed_jobs = []
            for job_model in candidate_jobs:
                # Skip jobs with unmet dependencies
                if job_model.dependencies:
                    dependencies = job_model.dependencies
                    dependencies_satisfied = all(
                        dep.status == JobStatus.COMPLETED for dep in dependencies
                    )

                    if not dependencies_satisfied:
                        continue

                # Claim the job
                job_model.status = JobStatus.RUNNING
                job_model.worker_id = worker_id
                job_model.updated_at = datetime.now().timestamp()

                # Update metadata
                if job_model.metadata is None:
                    job_model.metadata = {}

                job_model.metadata["worker_id"] = worker_id
                job_model.metadata["claimed_at"] = datetime.now().isoformat()

                claimed_jobs.append(job_model)

            # Save changes if any jobs were claimed
            if claimed_jobs:
                session.commit()

            # Convert to Job objects
            return [job_model.to_job() for job_model in claimed_jobs]

        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error claiming jobs for worker {worker_id}: {str(e)}")
            return []
        finally:
            session.close()

    def recover_interrupted_jobs(self, recovery_timeout_minutes: int = 5) -> List[Job]:
        """
        Recover jobs that were interrupted by system failure.

        This method finds jobs in RUNNING state that might have been
        interrupted by a system crash or shutdown, and resets them
        to PENDING state so they can be retried.

        Args:
            recovery_timeout_minutes: Number of minutes after which a running job
                                      with no updates is considered interrupted

        Returns:
            List of recovered jobs
        """
        recovered_jobs = []
        try:
            session = self.Session()
            try:
                # Find all running jobs with no heartbeat update within the configured timeout
                cutoff_time = datetime.now() - timedelta(
                    minutes=recovery_timeout_minutes
                )

                # Query for running jobs that haven't been updated recently
                job_models = (
                    session.query(JobModel)
                    .filter(
                        and_(
                            JobModel.status == JobStatus.RUNNING.value,
                            JobModel.updated_at < cutoff_time,
                        )
                    )
                    .all()
                )

                for job_model in job_models:
                    # Reset to pending status
                    job_model.status = JobStatus.PENDING.value
                    job_model.worker_id = None
                    job_model.updated_at = datetime.now()

                    # Add note about recovery in metadata
                    metadata = json.loads(job_model.metadata or "{}")
                    recovery_history = metadata.get("recovery_history", [])
                    recovery_history.append(
                        {
                            "recovered_at": datetime.now().isoformat(),
                            "previous_status": JobStatus.RUNNING.value,
                            "previous_worker": job_model.worker_id,
                            "recovery_timeout_minutes": recovery_timeout_minutes,
                        }
                    )
                    metadata["recovery_history"] = recovery_history
                    job_model.metadata = json.dumps(metadata)

                    # Create Job object for return
                    job = self._job_model_to_job(job_model)
                    recovered_jobs.append(job)

                # Commit the changes
                session.commit()

                logging.info(
                    f"Recovered {len(recovered_jobs)} interrupted jobs using {recovery_timeout_minutes}-minute timeout"
                )

            except SQLAlchemyError as e:
                session.rollback()
                logging.error(f"Error recovering interrupted jobs: {str(e)}")
            finally:
                session.close()
        except Exception as e:
            logging.error(f"Failed to recover jobs: {str(e)}")

        return recovered_jobs
