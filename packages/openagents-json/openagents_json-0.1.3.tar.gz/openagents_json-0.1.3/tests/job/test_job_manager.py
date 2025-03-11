"""
Tests for the JobManager class.

These tests verify the core functionality of the JobManager class
for creating, retrieving, and controlling workflow execution jobs.
"""

import asyncio
from typing import Any, Dict, List

import pytest

from openagents_json.job.manager import JobManager
from openagents_json.job.model import Job, JobPriority, JobStatus
from openagents_json.job.storage import MemoryJobStore


def test_job_manager_initialization():
    """Test JobManager initialization with default and custom parameters."""
    # Test with default parameters
    job_manager = JobManager()
    assert isinstance(job_manager.job_store, MemoryJobStore)
    assert job_manager.retention_days == 7
    assert job_manager.max_concurrent_jobs == 10

    # Test with custom parameters
    custom_store = MemoryJobStore()
    job_manager = JobManager(
        job_store=custom_store, retention_days=14, max_concurrent_jobs=5
    )
    assert job_manager.job_store is custom_store
    assert job_manager.retention_days == 14
    assert job_manager.max_concurrent_jobs == 5


def test_job_creation():
    """Test creating a job with the JobManager."""
    job_manager = JobManager()

    # Create a job
    job = job_manager.create_job(
        workflow_id="test-workflow", inputs={"value": "test_value"}
    )

    # Check that the job was created correctly
    assert job.job_id is not None
    assert job.workflow_id == "test-workflow"
    assert job.inputs == {"value": "test_value"}
    assert job.status == JobStatus.CREATED
    assert job.priority == JobPriority.MEDIUM

    # Verify job is in the store
    stored_job = job_manager.get_job(job.job_id)
    assert stored_job is not None
    assert stored_job.job_id == job.job_id


def test_job_create_with_options():
    """Test creating a job with additional options."""
    job_manager = JobManager()

    # Create a job with various options
    job = job_manager.create_job(
        workflow_id="test-workflow",
        inputs={"value": "test_value"},
        priority=JobPriority.HIGH,
        user_id="test-user",
        tags=["test", "example"],
        metadata={"source": "test_case"},
    )

    # Check additional properties
    assert job.priority == JobPriority.HIGH
    assert job.user_id == "test-user"
    assert job.tags == ["test", "example"]
    assert job.metadata == {"source": "test_case"}


def test_get_job():
    """Test retrieving a job by ID."""
    job_manager = JobManager()

    # Create a job
    job = job_manager.create_job(
        workflow_id="test-workflow", inputs={"value": "test_value"}
    )

    # Get the job
    retrieved_job = job_manager.get_job(job.job_id)

    # Check that the job was retrieved correctly
    assert retrieved_job is not None
    assert retrieved_job.job_id == job.job_id
    assert retrieved_job.workflow_id == "test-workflow"
    assert retrieved_job.inputs == {"value": "test_value"}


def test_get_nonexistent_job():
    """Test retrieving a job that doesn't exist."""
    job_manager = JobManager()

    # Try to get a non-existent job
    job = job_manager.get_job("non_existent_job")

    # Check that None is returned
    assert job is None


def test_list_jobs():
    """Test listing jobs with filters."""
    job_manager = JobManager()

    # Create several jobs
    job1 = job_manager.create_job(
        workflow_id="workflow-1", inputs={}, user_id="user-1", tags=["tag-1"]
    )

    job2 = job_manager.create_job(
        workflow_id="workflow-2", inputs={}, user_id="user-2", tags=["tag-2"]
    )

    job3 = job_manager.create_job(
        workflow_id="workflow-1", inputs={}, user_id="user-1", tags=["tag-2"]
    )

    # List all jobs
    all_jobs = job_manager.list_jobs()
    assert len(all_jobs) == 3

    # Filter by workflow ID
    workflow_jobs = job_manager.list_jobs(workflow_id="workflow-1")
    assert len(workflow_jobs) == 2
    assert all(job.workflow_id == "workflow-1" for job in workflow_jobs)

    # Filter by user ID
    user_jobs = job_manager.list_jobs(user_id="user-2")
    assert len(user_jobs) == 1
    assert user_jobs[0].user_id == "user-2"

    # Filter by tags
    tag_jobs = job_manager.list_jobs(tags=["tag-2"])
    assert len(tag_jobs) == 2
    assert all("tag-2" in job.tags for job in tag_jobs)


def test_delete_job():
    """Test deleting a job."""
    job_manager = JobManager()

    # Create a job
    job = job_manager.create_job(workflow_id="test-workflow", inputs={})

    # Verify job exists
    assert job_manager.get_job(job.job_id) is not None

    # Delete the job
    result = job_manager.delete_job(job.job_id)

    # Verify deletion was successful
    assert result is True
    assert job_manager.get_job(job.job_id) is None


def test_delete_nonexistent_job():
    """Test deleting a job that doesn't exist."""
    job_manager = JobManager()

    # Try to delete a non-existent job
    result = job_manager.delete_job("non_existent_job")

    # Check that False is returned
    assert result is False


@pytest.mark.asyncio
async def test_job_lifecycle():
    """Test the complete lifecycle of a job."""
    job_manager = JobManager()

    # Create a job
    job = job_manager.create_job(
        workflow_id="test-workflow", inputs={"value": "test_value"}
    )

    # Start the job
    start_result = job_manager.start_job(job.job_id)
    assert start_result is True

    # Allow some execution time
    await asyncio.sleep(1)

    # Check job status
    job_status = job_manager.get_job_status(job.job_id)
    assert job_status == JobStatus.RUNNING

    # Pause the job
    pause_result = job_manager.pause_job(job.job_id)
    assert pause_result is True

    # Check job status after pausing
    job_status = job_manager.get_job_status(job.job_id)
    assert job_status == JobStatus.PAUSED

    # Resume the job
    resume_result = job_manager.resume_job(job.job_id)
    assert resume_result is True

    # Allow some execution time
    await asyncio.sleep(1)

    # Cancel the job
    cancel_result = job_manager.cancel_job(job.job_id)
    assert cancel_result is True

    # Check job status after cancellation
    job_status = job_manager.get_job_status(job.job_id)
    assert job_status == JobStatus.CANCELLED


@pytest.mark.asyncio
async def test_completed_job_results():
    """Test retrieving results from a completed job."""
    job_manager = JobManager()

    # Create a job
    job = job_manager.create_job(
        workflow_id="test-workflow", inputs={"value": "test_value"}
    )

    # Manually update job to completed status with results
    job.update_status(JobStatus.COMPLETED)
    job.set_output("result", "test_result")
    job_manager.job_store.save(job)

    # Get job results
    results = job_manager.get_job_results(job.job_id)

    # Check results
    assert results is not None
    assert results == {"result": "test_result"}


def test_uncompleted_job_results():
    """Test retrieving results from an uncompleted job."""
    job_manager = JobManager()

    # Create a job
    job = job_manager.create_job(workflow_id="test-workflow", inputs={})

    # Get job results before completion
    results = job_manager.get_job_results(job.job_id)

    # Check that None is returned
    assert results is None


def test_cleanup_old_jobs():
    """Test cleaning up old jobs."""
    job_manager = JobManager()
    job_store = job_manager.job_store

    # Create method to access protected attributes for testing
    job_store._test_set_created_time = lambda job_id, time_str: setattr(
        job_store.jobs[job_id], "created_at", time_str
    )

    # Create jobs
    job1 = job_manager.create_job(workflow_id="test1", inputs={})
    job2 = job_manager.create_job(workflow_id="test2", inputs={})
    job3 = job_manager.create_job(workflow_id="test3", inputs={})

    # Set job creation times (job1 and job2 are "old")
    job_store._test_set_created_time(job1.job_id, "2020-01-01T00:00:00")
    job_store._test_set_created_time(job2.job_id, "2020-01-02T00:00:00")
    # job3 remains with current timestamp

    # Run cleanup
    cleanup_count = job_manager.cleanup_old_jobs()

    # Verify old jobs were cleaned up
    assert cleanup_count == 2
    assert job_manager.get_job(job1.job_id) is None
    assert job_manager.get_job(job2.job_id) is None
    assert job_manager.get_job(job3.job_id) is not None
