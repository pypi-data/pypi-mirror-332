"""
Tests for the Job model class.

These tests verify the core functionality of the Job class,
including status updates, serialization, and error handling.
"""

from datetime import datetime

import pytest

from openagents_json.job.model import Job, JobPriority, JobStatus


def test_job_initialization():
    """Test initializing a Job with various parameters."""
    # Test with minimal parameters
    job = Job(workflow_id="test-workflow", inputs={"key": "value"})
    assert job.job_id is not None
    assert job.workflow_id == "test-workflow"
    assert job.inputs == {"key": "value"}
    assert job.status == JobStatus.CREATED
    assert job.priority == JobPriority.MEDIUM
    assert job.outputs == {}
    assert job.created_at is not None
    assert job.started_at is None
    assert job.completed_at is None

    # Test with all parameters
    job = Job(
        job_id="custom-id",
        workflow_id="test-workflow",
        inputs={"key": "value"},
        status=JobStatus.QUEUED,
        priority=JobPriority.HIGH,
        user_id="user-123",
        tags=["tag1", "tag2"],
        metadata={"meta": "data"},
    )
    assert job.job_id == "custom-id"
    assert job.workflow_id == "test-workflow"
    assert job.inputs == {"key": "value"}
    assert job.status == JobStatus.QUEUED
    assert job.priority == JobPriority.HIGH
    assert job.user_id == "user-123"
    assert job.tags == ["tag1", "tag2"]
    assert job.metadata == {"meta": "data"}


def test_job_status_update():
    """Test updating job status and related timestamps."""
    job = Job(workflow_id="test-workflow", inputs={})
    initial_updated_at = job.updated_at

    # Allow a small delay to ensure timestamps are different
    job.update_status(JobStatus.RUNNING)

    assert job.status == JobStatus.RUNNING
    assert job.updated_at != initial_updated_at
    assert job.started_at == job.updated_at
    assert job.completed_at is None

    # Update to completed status
    job.update_status(JobStatus.COMPLETED)

    assert job.status == JobStatus.COMPLETED
    assert job.completed_at == job.updated_at
    assert job.execution_time > 0.0


def test_job_error_handling():
    """Test setting job error information."""
    job = Job(workflow_id="test-workflow", inputs={})

    # Create a test exception
    test_error = ValueError("Test error message")

    # Set the error
    job.set_error(test_error)

    assert job.status == JobStatus.FAILED
    assert job.error == "Test error message"
    assert job.traceback is not None


def test_job_output_setting():
    """Test setting job outputs."""
    job = Job(workflow_id="test-workflow", inputs={})
    initial_updated_at = job.updated_at

    # Set an output value
    job.set_output("result", "test_result")

    assert job.outputs == {"result": "test_result"}
    assert job.updated_at != initial_updated_at

    # Set another output value
    job.set_output("another", {"nested": "value"})

    assert job.outputs == {"result": "test_result", "another": {"nested": "value"}}


def test_job_progress_tracking():
    """Test job progress tracking."""
    job = Job(workflow_id="test-workflow", inputs={})

    # Set progress to 0.5 (50%)
    job.set_progress(0.5)
    assert job.progress == 0.5

    # Test clamping to 0-1 range
    job.set_progress(-0.1)
    assert job.progress == 0.0

    job.set_progress(1.5)
    assert job.progress == 1.0


def test_job_serialization():
    """Test job serialization to and from dictionary."""
    original_job = Job(
        job_id="test-id",
        workflow_id="test-workflow",
        inputs={"key": "value"},
        status=JobStatus.RUNNING,
        priority=JobPriority.HIGH,
        user_id="user-123",
        tags=["tag1", "tag2"],
        metadata={"meta": "data"},
    )

    # Add some outputs and progress
    original_job.set_output("result", "test_result")
    original_job.set_progress(0.75)

    # Convert to dictionary
    job_dict = original_job.to_dict()

    # Verify dictionary values
    assert job_dict["job_id"] == "test-id"
    assert job_dict["workflow_id"] == "test-workflow"
    assert job_dict["inputs"] == {"key": "value"}
    assert job_dict["outputs"] == {"result": "test_result"}
    assert job_dict["status"] == "running"
    assert job_dict["priority"] == "high"
    assert job_dict["user_id"] == "user-123"
    assert job_dict["tags"] == ["tag1", "tag2"]
    assert job_dict["metadata"] == {"meta": "data"}
    assert job_dict["progress"] == 0.75

    # Convert back to Job
    recreated_job = Job.from_dict(job_dict)

    # Verify recreated job
    assert recreated_job.job_id == original_job.job_id
    assert recreated_job.workflow_id == original_job.workflow_id
    assert recreated_job.inputs == original_job.inputs
    assert recreated_job.outputs == original_job.outputs
    assert recreated_job.status == original_job.status
    assert recreated_job.priority == original_job.priority
    assert recreated_job.user_id == original_job.user_id
    assert recreated_job.tags == original_job.tags
    assert recreated_job.metadata == original_job.metadata
    assert recreated_job.progress == original_job.progress
