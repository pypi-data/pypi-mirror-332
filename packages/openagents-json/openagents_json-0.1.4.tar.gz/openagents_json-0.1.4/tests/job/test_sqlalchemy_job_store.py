"""
Tests for the SQLAlchemyJobStore implementation.

These tests verify that the SQLAlchemyJobStore correctly handles
job persistence operations using SQLite in-memory database.
"""

import os
from datetime import datetime, timedelta

import pytest

from openagents_json.job.model import Job, JobPriority, JobStatus
from openagents_json.job.storage import SQLAlchemyJobStore


class TestSQLAlchemyJobStore:
    """Tests for the SQLAlchemyJobStore implementation."""

    @pytest.fixture
    def store(self):
        """Create a SQLAlchemyJobStore with an in-memory SQLite database."""
        # Use in-memory SQLite for testing
        store = SQLAlchemyJobStore(connection_string="sqlite:///:memory:")
        yield store
        # Clean up
        store.session_factory.close_all()

    def test_save_and_get_job(self, store):
        """Test saving and retrieving a job."""
        job = Job(
            job_id="test-job", workflow_id="test-workflow", inputs={"param": "value"}
        )

        # Save the job
        store.save(job)

        # Retrieve the job
        retrieved_job = store.get("test-job")

        # Verify the job was retrieved correctly
        assert retrieved_job is not None
        assert retrieved_job.job_id == "test-job"
        assert retrieved_job.workflow_id == "test-workflow"
        assert retrieved_job.inputs == {"param": "value"}

    def test_get_nonexistent_job(self, store):
        """Test retrieving a job that doesn't exist."""
        job = store.get("nonexistent-job")
        assert job is None

    def test_delete_job(self, store):
        """Test deleting a job."""
        job = Job(job_id="test-job", workflow_id="test-workflow", inputs={})

        # Save the job
        store.save(job)

        # Verify the job exists
        assert store.get("test-job") is not None

        # Delete the job
        result = store.delete("test-job")

        # Verify the job was deleted
        assert result is True
        assert store.get("test-job") is None

    def test_delete_nonexistent_job(self, store):
        """Test deleting a job that doesn't exist."""
        result = store.delete("nonexistent-job")
        assert result is False

    def test_update_job(self, store):
        """Test updating an existing job."""
        job = Job(
            job_id="test-job", workflow_id="test-workflow", inputs={"param": "value"}
        )

        # Save the job
        store.save(job)

        # Update the job
        job.inputs = {"param": "new-value"}
        job.status = JobStatus.RUNNING
        store.save(job)

        # Retrieve the updated job
        updated_job = store.get("test-job")

        # Verify the job was updated
        assert updated_job is not None
        assert updated_job.inputs == {"param": "new-value"}
        assert updated_job.status == JobStatus.RUNNING

    def test_list_jobs(self, store):
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
        store.save(job1)
        store.save(job2)
        store.save(job3)

        # Test listing all jobs
        all_jobs = store.list()
        assert len(all_jobs) == 3

        # Test filtering by status
        created_jobs = store.list(status=JobStatus.CREATED)
        assert len(created_jobs) == 1
        assert created_jobs[0].job_id == "job1"

        # Test filtering by workflow_id
        workflow1_jobs = store.list(workflow_id="workflow1")
        assert len(workflow1_jobs) == 2
        assert {job.job_id for job in workflow1_jobs} == {"job1", "job3"}

        # Test filtering by user_id
        user1_jobs = store.list(user_id="user1")
        assert len(user1_jobs) == 2
        assert {job.job_id for job in user1_jobs} == {"job1", "job3"}

        # Test filtering by tags
        tag2_jobs = store.list(tags=["tag2"])
        assert len(tag2_jobs) == 2
        assert {job.job_id for job in tag2_jobs} == {"job2", "job3"}

        # Test sorting
        sorted_jobs = store.list(sort_by="job_id", sort_order="asc")
        assert [job.job_id for job in sorted_jobs] == ["job1", "job2", "job3"]

        sorted_jobs_desc = store.list(sort_by="job_id", sort_order="desc")
        assert [job.job_id for job in sorted_jobs_desc] == ["job3", "job2", "job1"]

        # Test pagination
        paginated_jobs = store.list(limit=2, offset=1)
        assert len(paginated_jobs) == 2

    def test_list_jobs_with_multiple_statuses(self, store):
        """Test listing jobs with multiple status filters."""
        # Create test jobs with different statuses
        job1 = Job(
            job_id="job1", workflow_id="test", inputs={}, status=JobStatus.CREATED
        )
        job2 = Job(
            job_id="job2", workflow_id="test", inputs={}, status=JobStatus.RUNNING
        )
        job3 = Job(
            job_id="job3", workflow_id="test", inputs={}, status=JobStatus.COMPLETED
        )
        job4 = Job(
            job_id="job4", workflow_id="test", inputs={}, status=JobStatus.FAILED
        )

        # Save the jobs
        store.save(job1)
        store.save(job2)
        store.save(job3)
        store.save(job4)

        # Test filtering by multiple statuses
        active_jobs = store.list(status=[JobStatus.CREATED, JobStatus.RUNNING])
        assert len(active_jobs) == 2
        assert {job.job_id for job in active_jobs} == {"job1", "job2"}

        # Test filtering by different multiple statuses
        finished_jobs = store.list(status=[JobStatus.COMPLETED, JobStatus.FAILED])
        assert len(finished_jobs) == 2
        assert {job.job_id for job in finished_jobs} == {"job3", "job4"}

    def test_list_jobs_with_date_filters(self, store):
        """Test listing jobs with date filters."""
        # Create test jobs
        job1 = Job(job_id="job1", workflow_id="test", inputs={})
        job2 = Job(job_id="job2", workflow_id="test", inputs={})

        # Save the jobs
        store.save(job1)
        store.save(job2)

        # Get current time for reference
        now = datetime.utcnow()

        # Test filtering by created_after
        after_date = (now - timedelta(minutes=5)).isoformat()
        recent_jobs = store.list(created_after=after_date)
        assert len(recent_jobs) == 2

        # Test filtering by created_before
        before_date = (now + timedelta(minutes=5)).isoformat()
        old_jobs = store.list(created_before=before_date)
        assert len(old_jobs) == 2

        # Test filtering with both created_after and created_before
        jobs_in_range = store.list(created_after=after_date, created_before=before_date)
        assert len(jobs_in_range) == 2

    def test_cleanup_old_jobs(self, store):
        """Test cleaning up old jobs."""
        # Create test jobs
        job1 = Job(job_id="job1", workflow_id="test", inputs={})
        job2 = Job(job_id="job2", workflow_id="test", inputs={})
        job3 = Job(job_id="job3", workflow_id="test", inputs={})

        # Save the jobs
        store.save(job1)
        store.save(job2)
        store.save(job3)

        # Manually update created_at for job1 and job2 to be old
        # This requires direct database access
        with store.session_factory() as session:
            # Get the job models
            job1_model = session.query(store.JobModel).filter_by(job_id="job1").first()
            job2_model = session.query(store.JobModel).filter_by(job_id="job2").first()

            # Set older creation dates
            old_date = datetime.utcnow() - timedelta(days=60)
            job1_model.created_at = old_date
            job2_model.created_at = old_date

            # Commit the changes
            session.commit()

        # Clean up jobs older than 30 days
        deleted_count = store.cleanup_old_jobs(days=30)

        # Check the result
        assert deleted_count == 2
        assert store.get("job1") is None
        assert store.get("job2") is None
        assert store.get("job3") is not None

    def test_job_with_complex_data(self, store):
        """Test saving and retrieving a job with complex nested data."""
        # Create a job with complex nested data structures
        complex_inputs = {
            "simple_value": "string",
            "number": 42,
            "boolean": True,
            "nested_dict": {
                "key1": "value1",
                "key2": [1, 2, 3],
                "key3": {"subkey": "subvalue"},
            },
            "list_with_dicts": [
                {"name": "item1", "value": 1},
                {"name": "item2", "value": 2},
            ],
        }

        complex_metadata = {
            "version": "1.0",
            "settings": {
                "timeout": 30,
                "retry": True,
                "options": ["option1", "option2"],
            },
        }

        job = Job(
            job_id="complex-job",
            workflow_id="test-workflow",
            inputs=complex_inputs,
            metadata=complex_metadata,
            tags=["complex", "test"],
        )

        # Save the job
        store.save(job)

        # Retrieve the job
        retrieved_job = store.get("complex-job")

        # Verify the complex data was preserved
        assert retrieved_job is not None
        assert retrieved_job.inputs == complex_inputs
        assert retrieved_job.metadata == complex_metadata
        assert retrieved_job.tags == ["complex", "test"]

        # Verify nested structures
        assert retrieved_job.inputs["nested_dict"]["key2"] == [1, 2, 3]
        assert retrieved_job.inputs["list_with_dicts"][1]["name"] == "item2"
        assert retrieved_job.metadata["settings"]["options"] == ["option1", "option2"]
