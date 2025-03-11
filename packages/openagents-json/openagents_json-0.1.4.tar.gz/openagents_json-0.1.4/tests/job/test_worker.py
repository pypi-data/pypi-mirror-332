"""
Unit tests for the worker implementation.

This module tests the Worker and WorkerManager classes in openagents_json.job.worker,
focusing on worker registration, heartbeat, job claiming, and failure detection.
"""

import asyncio
import time
import unittest
import uuid
from unittest import mock

from openagents_json.job.model import Job, JobStatus
from openagents_json.job.storage import JobStore, MemoryJobStore
from openagents_json.job.worker import Worker, WorkerManager


class TestWorker(unittest.TestCase):
    """Tests for the Worker class."""

    def setUp(self):
        """Set up test environment."""
        self.job_store = MemoryJobStore()
        self.worker_id = f"test-worker-{uuid.uuid4()}"
        self.worker = Worker(
            worker_id=self.worker_id,
            job_store=self.job_store,
            heartbeat_interval=1,
            job_claim_batch_size=3,
            max_concurrent_jobs=2,
            tags=["test"],
        )

        # Create test jobs
        self.test_jobs = []
        for i in range(5):
            job = Job(
                name=f"Test Job {i}",
                payload={"data": f"test-{i}"},
                status=JobStatus.PENDING,
                tags=["test"] if i < 3 else ["other"],
            )
            self.job_store.save(job)
            self.test_jobs.append(job)

    def tearDown(self):
        """Clean up after tests."""
        # Ensure worker is stopped
        if hasattr(self, "worker") and self.worker.running:
            asyncio.run(self.worker.stop())

    def test_init(self):
        """Test worker initialization."""
        self.assertEqual(self.worker.worker_id, self.worker_id)
        self.assertEqual(self.worker.heartbeat_interval, 1)
        self.assertEqual(self.worker.job_claim_batch_size, 3)
        self.assertEqual(self.worker.max_concurrent_jobs, 2)
        self.assertEqual(self.worker.tags, ["test"])
        self.assertFalse(self.worker.running)
        self.assertEqual(len(self.worker.running_jobs), 0)

    def test_register(self):
        """Test worker registration."""
        result = asyncio.run(self.worker.register())
        self.assertTrue(result)

        # Check that worker is registered in job store
        workers = self.job_store.get_workers()
        self.assertEqual(len(workers), 1)
        self.assertEqual(workers[0]["worker_id"], self.worker_id)

    def test_heartbeat(self):
        """Test worker heartbeat."""
        # Register first
        asyncio.run(self.worker.register())

        # Send heartbeat
        result = asyncio.run(self.worker.heartbeat())
        self.assertTrue(result)

        # Check that heartbeat time was updated
        workers = self.job_store.get_workers()
        self.assertEqual(len(workers), 1)
        worker_info = workers[0]
        self.assertGreater(worker_info["last_heartbeat"], worker_info["started_at"])

    def test_claim_jobs(self):
        """Test job claiming."""
        # Register worker
        asyncio.run(self.worker.register())

        # Claim jobs
        claimed_jobs = asyncio.run(self.worker.claim_jobs())

        # Should claim up to job_claim_batch_size jobs with matching tags
        self.assertEqual(len(claimed_jobs), 3)

        # All claimed jobs should have the "test" tag
        for job in claimed_jobs:
            self.assertIn("test", job.tags)
            self.assertEqual(job.status, JobStatus.RUNNING)
            self.assertEqual(job.worker_id, self.worker_id)

        # Check that jobs are marked in worker's running_jobs
        self.assertEqual(len(self.worker.running_jobs), 3)

    @mock.patch("openagents_json.job.worker.Worker.execute_job")
    async def async_test_worker_loop(self, mock_execute_job):
        """Test the worker's main loop."""
        # Set up mock to avoid actually executing jobs
        mock_execute_job.return_value = None

        # Start worker
        await self.worker.register()
        task = asyncio.create_task(self.worker._worker_loop())

        # Let worker run for a bit
        await asyncio.sleep(2)

        # Stop worker
        self.worker.running = False
        await task

        # Verify jobs were claimed and execute_job was called
        self.assertTrue(mock_execute_job.called)

        # Check job store to see that jobs were processed
        jobs = self.job_store.list(status=JobStatus.RUNNING)
        self.assertGreater(len(jobs), 0)
        for job in jobs:
            self.assertEqual(job.worker_id, self.worker_id)

    def test_worker_loop(self):
        """Test the worker's main loop (synchronous wrapper)."""
        asyncio.run(self.async_test_worker_loop())

    @mock.patch("openagents_json.job.worker.Worker.execute_job")
    async def async_test_start_stop(self, mock_execute_job):
        """Test starting and stopping the worker."""
        # Start worker
        await self.worker.start()
        self.assertTrue(self.worker.running)

        # Let it run briefly
        await asyncio.sleep(2)

        # Stop worker
        await self.worker.stop()
        self.assertFalse(self.worker.running)

        # Verify worker was registered
        workers = self.job_store.get_workers()
        self.assertEqual(len(workers), 1)

    def test_start_stop(self):
        """Test starting and stopping the worker (synchronous wrapper)."""
        asyncio.run(self.async_test_start_stop())

    async def async_test_execute_job(self):
        """Test job execution."""
        # Create a test job
        job = Job(name="Execute Test", payload={"value": 42}, status=JobStatus.PENDING)
        self.job_store.save(job)

        # Set up custom executor
        async def test_executor(job):
            return {"result": job.payload["value"] * 2}

        self.worker.executor = test_executor

        # Execute job
        await self.worker.execute_job(job)

        # Check job status
        updated_job = self.job_store.get(job.job_id)
        self.assertEqual(updated_job.status, JobStatus.COMPLETED)
        self.assertEqual(updated_job.result["result"], 84)

    def test_execute_job(self):
        """Test job execution (synchronous wrapper)."""
        asyncio.run(self.async_test_execute_job())

    async def async_test_execute_job_failure(self):
        """Test job execution failure."""
        # Create a test job
        job = Job(
            name="Execute Test Failure",
            payload={"value": "not_a_number"},
            status=JobStatus.PENDING,
            max_retries=0,
        )
        self.job_store.save(job)

        # Set up executor that will fail
        async def failing_executor(job):
            raise ValueError("Test error")

        self.worker.executor = failing_executor

        # Execute job
        await self.worker.execute_job(job)

        # Check job status
        updated_job = self.job_store.get(job.job_id)
        self.assertEqual(updated_job.status, JobStatus.FAILED)
        self.assertIsNotNone(updated_job.error)
        self.assertEqual(updated_job.error["type"], "ValueError")

    def test_execute_job_failure(self):
        """Test job execution failure (synchronous wrapper)."""
        asyncio.run(self.async_test_execute_job_failure())


class TestWorkerManager(unittest.TestCase):
    """Tests for the WorkerManager class."""

    def setUp(self):
        """Set up test environment."""
        self.job_store = MemoryJobStore()
        self.worker_manager = WorkerManager(
            job_store=self.job_store, heartbeat_timeout=2, check_interval=1
        )

        # Create test workers
        self.test_workers = []
        for i in range(3):
            worker_id = f"test-worker-{i}"

            # Add worker directly to job store
            worker_info = {
                "worker_id": worker_id,
                "hostname": "test-host",
                "pid": 1000 + i,
                "tags": ["test"],
                "max_concurrent_jobs": 5,
                "started_at": time.time(),
                "last_heartbeat": time.time(),
                "status": "active",
                "running_jobs": [],
            }
            self.job_store.register_worker(worker_info)
            self.test_workers.append(worker_info)

        # Create test jobs assigned to workers
        self.test_jobs = []
        for i, worker in enumerate(self.test_workers):
            for j in range(2):
                job = Job(
                    name=f"Worker {i} Job {j}",
                    payload={"data": f"test-{i}-{j}"},
                    status=JobStatus.RUNNING,
                    worker_id=worker["worker_id"],
                )
                self.job_store.save(job)

                # Update worker running_jobs
                worker_info = self.job_store.get_workers()[i]
                running_jobs = worker_info.get("running_jobs", [])
                running_jobs.append(job.job_id)
                self.job_store.update_worker_heartbeat(
                    worker_info["worker_id"],
                    str(worker_info["last_heartbeat"]),
                    running_jobs,
                )
                self.test_jobs.append(job)

    def tearDown(self):
        """Clean up after tests."""
        # Ensure worker manager is stopped
        if hasattr(self, "worker_manager") and self.worker_manager.running:
            asyncio.run(self.worker_manager.stop())

    def test_init(self):
        """Test worker manager initialization."""
        self.assertEqual(self.worker_manager.heartbeat_timeout, 2)
        self.assertEqual(self.worker_manager.check_interval, 1)
        self.assertFalse(self.worker_manager.running)

    @mock.patch("openagents_json.job.worker.WorkerManager._check_workers")
    async def async_test_health_check_loop(self, mock_check_workers):
        """Test the health check loop."""
        # Start health check loop
        task = asyncio.create_task(self.worker_manager._health_check_loop())
        self.worker_manager.running = True

        # Let it run briefly
        await asyncio.sleep(2)

        # Stop loop
        self.worker_manager.running = False
        await task

        # Verify _check_workers was called
        self.assertTrue(mock_check_workers.called)
        self.assertGreaterEqual(mock_check_workers.call_count, 1)

    def test_health_check_loop(self):
        """Test the health check loop (synchronous wrapper)."""
        asyncio.run(self.async_test_health_check_loop())

    async def async_test_check_workers(self):
        """Test worker health check."""
        # Make one worker appear dead by setting old heartbeat
        dead_worker = self.test_workers[0]
        old_time = time.time() - 5  # 5 seconds ago, beyond timeout
        self.job_store.update_worker_heartbeat(
            dead_worker["worker_id"], str(old_time), dead_worker.get("running_jobs", [])
        )

        # Run check
        await self.worker_manager._check_workers()

        # Get updated workers
        workers = self.job_store.get_workers()

        # Verify one worker is marked as dead
        dead_workers = [w for w in workers if w["status"] == "dead"]
        self.assertEqual(len(dead_workers), 1)
        self.assertEqual(dead_workers[0]["worker_id"], dead_worker["worker_id"])

        # Check that jobs from dead worker were reset
        for job in self.test_jobs:
            updated_job = self.job_store.get(job.job_id)
            if updated_job.worker_id == dead_worker["worker_id"]:
                self.assertEqual(updated_job.status, JobStatus.PENDING)
            else:
                self.assertEqual(updated_job.status, JobStatus.RUNNING)

    def test_check_workers(self):
        """Test worker health check (synchronous wrapper)."""
        asyncio.run(self.async_test_check_workers())

    @mock.patch("openagents_json.job.worker.WorkerManager._health_check_loop")
    async def async_test_start_stop(self, mock_health_check_loop):
        """Test starting and stopping the worker manager."""
        # Set up mock to avoid actual health check loop
        mock_health_check_loop.return_value = None

        # Start manager
        await self.worker_manager.start()
        self.assertTrue(self.worker_manager.running)

        # Stop manager
        await self.worker_manager.stop()
        self.assertFalse(self.worker_manager.running)

    def test_start_stop(self):
        """Test starting and stopping the worker manager (synchronous wrapper)."""
        asyncio.run(self.async_test_start_stop())


if __name__ == "__main__":
    unittest.main()
