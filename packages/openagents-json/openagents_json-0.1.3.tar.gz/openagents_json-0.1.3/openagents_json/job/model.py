"""
Job model definition for the OpenAgents JSON framework.

This module defines the core Job data model and related enumerations
for job status and priority levels.
"""

import enum
import time
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from openagents_json.job.retry import FixedDelayRetryPolicy, RetryPolicy


class JobStatus(str, enum.Enum):
    """Enumeration of possible job statuses."""

    CREATED = "created"
    QUEUED = "queued"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobPriority(str, enum.Enum):
    """Enumeration of job priority levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Job:
    """
    Job model representing a workflow execution job.

    A job encapsulates the execution of a workflow, tracking its status,
    inputs, outputs, and execution metadata throughout its lifecycle.
    """

    def __init__(
        self,
        job_id: Optional[str] = None,
        name: str = "",
        description: str = "",
        payload: Any = None,
        status: Union[JobStatus, str] = JobStatus.PENDING,
        priority: Union[JobPriority, str] = JobPriority.MEDIUM,
        max_retries: int = 0,
        retry_delay: int = 0,
        retry_policy: Optional[Union[RetryPolicy, Dict[str, Any]]] = None,
        timeout: Optional[int] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        started_at: Optional[datetime] = None,
        completed_at: Optional[datetime] = None,
        result: Any = None,
        error: Optional[Dict[str, Any]] = None,
        dependencies: Optional[List[str]] = None,
        batch_id: Optional[str] = None,
        worker_id: Optional[str] = None,
    ):
        """
        Initialize a new Job instance.

        Args:
            job_id: Unique identifier for the job (generated if not provided)
            name: Descriptive name for the job
            description: Detailed description of the job
            payload: Data or parameters needed for job execution
            status: Current status of the job
            priority: Priority level of the job
            max_retries: Maximum number of retry attempts on failure
            retry_delay: Delay in seconds between retry attempts (backward compatibility)
            retry_policy: Policy for handling retries (FixedDelayRetryPolicy, ExponentialBackoffRetryPolicy)
            timeout: Maximum execution time in seconds
            tags: List of tags for categorizing the job
            metadata: Additional metadata key-value pairs
            created_at: Timestamp when job was created
            updated_at: Timestamp when job was last updated
            started_at: Timestamp when job execution started
            completed_at: Timestamp when job execution completed
            result: Result data from successful job execution
            error: Error information from failed job execution
            dependencies: List of job IDs that must complete before this job can run
            batch_id: ID of a batch this job belongs to
            worker_id: ID of the worker currently processing this job
        """
        self.job_id = job_id or str(uuid.uuid4())
        self.name = name
        self.description = description
        self.payload = payload
        self.status = JobStatus(status) if isinstance(status, str) else status
        self.priority = JobPriority(priority) if isinstance(priority, str) else priority
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.timeout = timeout
        self.tags = tags or []
        self.metadata = metadata or {}
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or self.created_at
        self.started_at = started_at
        self.completed_at = completed_at
        self.result = result
        self.error = error or {}
        self.dependencies = dependencies or []
        self.batch_id = batch_id
        self.retry_count = 0
        self.worker_id = worker_id

        # Handle retry policy
        if retry_policy is None and retry_delay > 0:
            # Create a fixed delay policy from legacy retry_delay parameter
            self.retry_policy = FixedDelayRetryPolicy(delay=retry_delay)
        elif isinstance(retry_policy, dict):
            # Create from dictionary representation
            self.retry_policy = RetryPolicy.from_dict(retry_policy)
        else:
            # Use provided policy or default
            self.retry_policy = retry_policy or FixedDelayRetryPolicy()

        # Timestamps for tracking job lifecycle
        self.created_at = datetime.now().isoformat()
        self.started_at = None
        self.updated_at = self.created_at
        self.completed_at = None

        # Error tracking
        self.error = None
        self.traceback = None

        # Runtime metrics
        self.progress = 0.0  # Progress from 0 to 1
        self.execution_time = 0.0  # Total execution time in seconds

    def update_status(self, status: JobStatus) -> None:
        """
        Update the job status and related timestamps.

        Args:
            status: New status to set for the job.
        """
        previous_status = self.status
        self.status = status
        self.updated_at = datetime.now().isoformat()

        # Update related timestamps based on status transitions
        if status == JobStatus.RUNNING and previous_status != JobStatus.RUNNING:
            self.started_at = self.updated_at
        elif status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
            self.completed_at = self.updated_at
            if self.started_at:
                # Calculate total execution time
                started = datetime.fromisoformat(self.started_at)
                completed = datetime.fromisoformat(self.completed_at)
                self.execution_time = (completed - started).total_seconds()

    def set_error(self, error: Exception) -> None:
        """
        Set error information when a job fails.

        Args:
            error: The exception that caused the job to fail.
        """
        self.error = str(error)
        self.traceback = getattr(error, "__traceback__", None)
        self.update_status(JobStatus.FAILED)

    def set_output(self, key: str, value: Any) -> None:
        """
        Set a specific output value.

        Args:
            key: Output parameter name.
            value: Output parameter value.
        """
        self.outputs[key] = value
        self.updated_at = datetime.now().isoformat()

    def set_progress(self, progress: float) -> None:
        """
        Update job progress.

        Args:
            progress: Progress value between 0 and 1.
        """
        self.progress = max(0.0, min(1.0, progress))  # Clamp between 0 and 1
        self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the job to a dictionary representation.

        Returns:
            Dictionary representation of the job.
        """
        return {
            "job_id": self.job_id,
            "name": self.name,
            "description": self.description,
            "payload": self.payload,
            "status": self.status.value,
            "priority": self.priority.value,
            "max_retries": self.max_retries,
            "retry_delay": self.retry_delay,
            "retry_policy": (
                self.retry_policy.to_dict()
                if hasattr(self, "retry_policy") and self.retry_policy
                else None
            ),
            "timeout": self.timeout,
            "tags": self.tags,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": (
                self.completed_at.isoformat() if self.completed_at else None
            ),
            "result": self.result,
            "error": self.error,
            "dependencies": self.dependencies,
            "batch_id": self.batch_id,
            "retry_count": self.retry_count,
            "worker_id": self.worker_id,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Job":
        """
        Create a job from a dictionary representation.

        Args:
            data: Dictionary representation of the job.

        Returns:
            A new Job instance.
        """
        # Handle datetime fields
        for dt_field in ["created_at", "updated_at", "started_at", "completed_at"]:
            if data.get(dt_field):
                if isinstance(data[dt_field], str):
                    data[dt_field] = datetime.fromisoformat(data[dt_field])

        # Create a new job instance
        job = cls(
            job_id=data.get("job_id"),
            name=data.get("name", ""),
            description=data.get("description", ""),
            payload=data.get("payload"),
            status=data.get("status", JobStatus.PENDING),
            priority=data.get("priority", JobPriority.MEDIUM),
            max_retries=data.get("max_retries", 0),
            retry_delay=data.get("retry_delay", 0),
            retry_policy=data.get("retry_policy"),
            timeout=data.get("timeout"),
            tags=data.get("tags", []),
            metadata=data.get("metadata", {}),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            started_at=data.get("started_at"),
            completed_at=data.get("completed_at"),
            result=data.get("result"),
            error=data.get("error", {}),
            dependencies=data.get("dependencies", []),
            batch_id=data.get("batch_id"),
            worker_id=data.get("worker_id"),
        )

        job.retry_count = data.get("retry_count", 0)
        return job

    def add_dependency(self, job_id: str) -> None:
        """
        Add a dependency to this job.

        Args:
            job_id: ID of the job this job depends on
        """
        if job_id != self.job_id and job_id not in self.dependencies:
            self.dependencies.append(job_id)
            self.updated_at = datetime.now()

    def remove_dependency(self, job_id: str) -> None:
        """
        Remove a dependency from this job.

        Args:
            job_id: ID of the job to remove from dependencies
        """
        if job_id in self.dependencies:
            self.dependencies.remove(job_id)
            self.updated_at = datetime.now()

    def has_dependencies(self) -> bool:
        """
        Check if this job has dependencies.

        Returns:
            True if the job has at least one dependency, False otherwise
        """
        return len(self.dependencies) > 0

    def set_batch_id(self, batch_id: str) -> None:
        """
        Set the batch ID for this job.

        Args:
            batch_id: ID of the batch this job belongs to
        """
        self.batch_id = batch_id
        self.updated_at = datetime.now()

    def get_retry_delay(self) -> float:
        """
        Get the delay in seconds before the next retry attempt.

        Uses the retry policy if available, otherwise falls back to the retry_delay parameter.

        Returns:
            Delay in seconds before the next retry
        """
        if hasattr(self, "retry_policy") and self.retry_policy:
            return self.retry_policy.get_retry_delay(
                attempt=self.retry_count, max_retries=self.max_retries
            )
        else:
            # Backward compatibility
            return float(self.retry_delay)
