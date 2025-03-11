"""
Tests for the JobStore implementations.

These tests verify that the different JobStore implementations
correctly handle job persistence operations.
"""

import os
import shutil
import tempfile
from datetime import datetime

import pytest

from openagents_json.job.model import Job, JobPriority, JobStatus
from openagents_json.job.storage import FileJobStore, MemoryJobStore


class TestMemoryJobStore:
    """Tests for the MemoryJobStore implementation."""

    def setup_method(self):
        """Set up a new store for each test."""
        self.store = MemoryJobStore()

    def test_save_and_get_job(self):
        """Test saving and retrieving a job."""
        job = Job(job_id="test-job", workflow_id="test-workflow", inputs={})

        # Save the job
        self.store.save(job)

        # Retrieve the job
        retrieved_job = self.store.get("test-job")

        # Verify the job was retrieved correctly
        assert retrieved_job is not None
        assert retrieved_job.job_id == "test-job"
        assert retrieved_job.workflow_id == "test-workflow"

    def test_get_nonexistent_job(self):
        """Test retrieving a job that doesn't exist."""
        job = self.store.get("nonexistent-job")
        assert job is None

    def test_delete_job(self):
        """Test deleting a job."""
        job = Job(job_id="test-job", workflow_id="test-workflow", inputs={})

        # Save the job
        self.store.save(job)

        # Verify the job exists
        assert self.store.get("test-job") is not None

        # Delete the job
        result = self.store.delete("test-job")

        # Verify the job was deleted
        assert result is True
        assert self.store.get("test-job") is None

    def test_delete_nonexistent_job(self):
        """Test deleting a job that doesn't exist."""
        result = self.store.delete("nonexistent-job")
        assert result is False

    def test_list_jobs(self):
        """Test listing jobs with filters."""
        # Create test jobs with different properties
        job1 = Job(
            job_id="job1",
            workflow_id="workflow1",
            inputs={},
            status=JobStatus.CREATED,
            user_id="user1",
            tags=["tag1"],
        )

        job2 = Job(
            job_id="job2",
            workflow_id="workflow2",
            inputs={},
            status=JobStatus.RUNNING,
            user_id="user2",
            tags=["tag2"],
        )

        job3 = Job(
            job_id="job3",
            workflow_id="workflow1",
            inputs={},
            status=JobStatus.COMPLETED,
            user_id="user1",
            tags=["tag2", "tag3"],
        )

        # Save the jobs
        self.store.save(job1)
        self.store.save(job2)
        self.store.save(job3)

        # Test listing all jobs
        all_jobs = self.store.list()
        assert len(all_jobs) == 3

        # Test filtering by status
        created_jobs = self.store.list(status=JobStatus.CREATED)
        assert len(created_jobs) == 1
        assert created_jobs[0].job_id == "job1"

        # Test filtering by workflow_id
        workflow1_jobs = self.store.list(workflow_id="workflow1")
        assert len(workflow1_jobs) == 2
        assert {job.job_id for job in workflow1_jobs} == {"job1", "job3"}

        # Test filtering by user_id
        user1_jobs = self.store.list(user_id="user1")
        assert len(user1_jobs) == 2
        assert {job.job_id for job in user1_jobs} == {"job1", "job3"}

        # Test filtering by tags
        tag2_jobs = self.store.list(tags=["tag2"])
        assert len(tag2_jobs) == 2
        assert {job.job_id for job in tag2_jobs} == {"job2", "job3"}

        # Test sorting
        sorted_jobs = self.store.list(sort_by="job_id", sort_order="asc")
        assert [job.job_id for job in sorted_jobs] == ["job1", "job2", "job3"]

        sorted_jobs_desc = self.store.list(sort_by="job_id", sort_order="desc")
        assert [job.job_id for job in sorted_jobs_desc] == ["job3", "job2", "job1"]

        # Test pagination
        paginated_jobs = self.store.list(limit=2, offset=1)
        assert len(paginated_jobs) == 2

    def test_cleanup_old_jobs(self):
        """Test cleaning up old jobs."""
        # Create test jobs
        job1 = Job(job_id="job1", workflow_id="test", inputs={})
        job2 = Job(job_id="job2", workflow_id="test", inputs={})
        job3 = Job(job_id="job3", workflow_id="test", inputs={})

        # Save the jobs
        self.store.save(job1)
        self.store.save(job2)
        self.store.save(job3)

        # Set older creation dates for job1 and job2
        # This is accessing implementation details for testing
        self.store.jobs["job1"].created_at = "2020-01-01T00:00:00"
        self.store.jobs["job2"].created_at = "2020-01-02T00:00:00"
        # job3 keeps current timestamp

        # Clean up jobs older than 30 days (should delete job1 and job2)
        deleted_count = self.store.cleanup_old_jobs(days=30)

        # Check the result
        assert deleted_count == 2
        assert self.store.get("job1") is None
        assert self.store.get("job2") is None
        assert self.store.get("job3") is not None


class TestFileJobStore:
    """Tests for the FileJobStore implementation."""

    def setup_method(self):
        """Set up a new store with a temporary directory for each test."""
        self.temp_dir = tempfile.mkdtemp()
        self.store = FileJobStore(storage_dir=self.temp_dir)

    def teardown_method(self):
        """Clean up temporary directory after each test."""
        shutil.rmtree(self.temp_dir)

    def test_save_and_get_job(self):
        """Test saving and retrieving a job."""
        job = Job(job_id="test-job", workflow_id="test-workflow", inputs={})

        # Save the job
        self.store.save(job)

        # Verify the file was created
        assert os.path.exists(os.path.join(self.temp_dir, "test-job.json"))

        # Retrieve the job
        retrieved_job = self.store.get("test-job")

        # Verify the job was retrieved correctly
        assert retrieved_job is not None
        assert retrieved_job.job_id == "test-job"
        assert retrieved_job.workflow_id == "test-workflow"

    def test_get_nonexistent_job(self):
        """Test retrieving a job that doesn't exist."""
        job = self.store.get("nonexistent-job")
        assert job is None

    def test_delete_job(self):
        """Test deleting a job."""
        job = Job(job_id="test-job", workflow_id="test-workflow", inputs={})

        # Save the job
        self.store.save(job)

        # Verify the job exists
        assert os.path.exists(os.path.join(self.temp_dir, "test-job.json"))

        # Delete the job
        result = self.store.delete("test-job")

        # Verify the job was deleted
        assert result is True
        assert not os.path.exists(os.path.join(self.temp_dir, "test-job.json"))

    def test_delete_nonexistent_job(self):
        """Test deleting a job that doesn't exist."""
        result = self.store.delete("nonexistent-job")
        assert result is False

    def test_list_jobs(self):
        """Test listing jobs with filters."""
        # Create test jobs with different properties
        job1 = Job(
            job_id="job1",
            workflow_id="workflow1",
            inputs={},
            status=JobStatus.CREATED,
            user_id="user1",
            tags=["tag1"],
        )

        job2 = Job(
            job_id="job2",
            workflow_id="workflow2",
            inputs={},
            status=JobStatus.RUNNING,
            user_id="user2",
            tags=["tag2"],
        )

        job3 = Job(
            job_id="job3",
            workflow_id="workflow1",
            inputs={},
            status=JobStatus.COMPLETED,
            user_id="user1",
            tags=["tag2", "tag3"],
        )

        # Save the jobs
        self.store.save(job1)
        self.store.save(job2)
        self.store.save(job3)

        # Test listing all jobs
        all_jobs = self.store.list()
        assert len(all_jobs) == 3

        # Test filtering by status
        created_jobs = self.store.list(status=JobStatus.CREATED)
        assert len(created_jobs) == 1
        assert created_jobs[0].job_id == "job1"

        # Test filtering by workflow_id
        workflow1_jobs = self.store.list(workflow_id="workflow1")
        assert len(workflow1_jobs) == 2
        job_ids = {job.job_id for job in workflow1_jobs}
        assert job_ids == {"job1", "job3"}

        # Test filtering by user_id
        user1_jobs = self.store.list(user_id="user1")
        assert len(user1_jobs) == 2
        job_ids = {job.job_id for job in user1_jobs}
        assert job_ids == {"job1", "job3"}

    def test_cleanup_old_jobs(self):
        """Test cleaning up old jobs."""

        # Create a custom method to create job files with specific dates
        def create_job_file_with_date(job_id, created_at):
            job = Job(job_id=job_id, workflow_id="test", inputs={})
            job_dict = job.to_dict()
            job_dict["created_at"] = created_at
            with open(os.path.join(self.temp_dir, f"{job_id}.json"), "w") as f:
                import json

                json.dump(job_dict, f)

        # Create test job files
        create_job_file_with_date("job1", "2020-01-01T00:00:00")
        create_job_file_with_date("job2", "2020-01-02T00:00:00")
        create_job_file_with_date("job3", datetime.now().isoformat())

        # Clean up jobs older than 30 days (should delete job1 and job2)
        deleted_count = self.store.cleanup_old_jobs(days=30)

        # Check the result
        assert deleted_count == 2
        assert not os.path.exists(os.path.join(self.temp_dir, "job1.json"))
        assert not os.path.exists(os.path.join(self.temp_dir, "job2.json"))
        assert os.path.exists(os.path.join(self.temp_dir, "job3.json"))
