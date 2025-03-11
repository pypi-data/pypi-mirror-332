#!/usr/bin/env python
"""
Execution Control Demo

This script demonstrates execution control features in OpenAgents JSON:
- Retry policies for handling transient failures
- Distributed execution across multiple workers
- Worker coordination and monitoring
"""

import asyncio
import logging
import random
import sys
import time
from datetime import datetime
from typing import List

from openagents_json.job.model import Job, JobStatus, JobPriority
from openagents_json.job.retry import FixedDelayRetryPolicy, ExponentialBackoffRetryPolicy
from openagents_json.job.storage import SQLiteJobStore
from openagents_json.job.worker import Worker, WorkerManager
from openagents_json.job.manager import JobManager


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


# Example job functions
async def successful_job(params):
    """A job that always succeeds."""
    logger.info(f"Executing successful job with params: {params}")
    await asyncio.sleep(1)
    return {"result": "success", "params": params}


async def failing_job_with_retry(attempt, params):
    """
    A job that fails for the first few attempts but eventually succeeds.
    This simulates a transient error that resolves after a few attempts.
    """
    logger.info(f"Executing failing job (attempt: {attempt}) with params: {params}")
    
    # Fail for the first 2 attempts
    if attempt < 2:
        await asyncio.sleep(1)
        raise Exception(f"Simulated transient error (attempt {attempt})")
    
    # Succeed on the third attempt
    await asyncio.sleep(1)
    return {"result": "success after retry", "params": params, "attempts_needed": attempt + 1}


async def random_failure_job(params):
    """A job with random failures to test retry policies."""
    logger.info(f"Executing random failure job with params: {params}")
    
    # 50% chance of failure
    if random.random() < 0.5:
        await asyncio.sleep(1)
        raise Exception("Simulated random failure")
    
    await asyncio.sleep(1)
    return {"result": "success", "params": params}


# Create jobs with different retry policies
def create_jobs_with_retry_policies() -> List[Job]:
    """Create example jobs with different retry policies."""
    jobs = []
    
    # Job with fixed delay retry policy
    fixed_delay_job = Job(
        name="Fixed Delay Retry Job",
        description="Job with a fixed delay retry policy",
        payload={"function": "random_failure", "params": {"value": 42}},
        max_retries=3,
        retry_policy=FixedDelayRetryPolicy(delay=2, jitter=0.2)
    )
    jobs.append(fixed_delay_job)
    
    # Job with exponential backoff retry policy
    exponential_backoff_job = Job(
        name="Exponential Backoff Retry Job",
        description="Job with an exponential backoff retry policy",
        payload={"function": "random_failure", "params": {"value": 84}},
        max_retries=5,
        retry_policy=ExponentialBackoffRetryPolicy(
            initial_delay=1, 
            max_delay=30, 
            multiplier=2,
            jitter=0.3
        )
    )
    jobs.append(exponential_backoff_job)
    
    # Job with legacy retry delay (for backward compatibility)
    legacy_retry_job = Job(
        name="Legacy Retry Job",
        description="Job with legacy retry_delay parameter",
        payload={"function": "random_failure", "params": {"value": 100}},
        max_retries=2,
        retry_delay=3
    )
    jobs.append(legacy_retry_job)
    
    return jobs


# Custom job executor for a worker
async def worker_job_executor(job: Job) -> dict:
    """
    Custom executor function for worker to execute a job.
    
    This interprets the job payload to determine which function to call.
    """
    function_name = job.payload.get("function")
    params = job.payload.get("params", {})
    
    logger.info(f"Worker executing {function_name} job with params {params}")
    
    if function_name == "successful":
        return await successful_job(params)
    elif function_name == "failing_with_retry":
        return await failing_job_with_retry(job.retry_count, params)
    elif function_name == "random_failure":
        return await random_failure_job(params)
    else:
        raise ValueError(f"Unknown function: {function_name}")


async def run_distributed_execution_demo():
    """Demonstrate distributed execution with workers."""
    # Create a shared job store
    job_store = SQLiteJobStore()
    
    # Create a job manager in distributed mode
    manager = JobManager(job_store=job_store, distributed_mode=True)
    
    # Create a worker manager
    worker_manager = WorkerManager(job_store=job_store, heartbeat_timeout=10, check_interval=5)
    
    # Start the worker manager
    await worker_manager.start()
    
    # Create workers with different tag sets
    workers = []
    
    # Worker 1 - handles "task" tag
    worker1 = Worker(
        worker_id="worker-1",
        job_store=job_store,
        tags=["task"],
        max_concurrent_jobs=2,
        executor=worker_job_executor
    )
    workers.append(worker1)
    
    # Worker 2 - handles "background" tag
    worker2 = Worker(
        worker_id="worker-2",
        job_store=job_store,
        tags=["background"],
        max_concurrent_jobs=3,
        executor=worker_job_executor
    )
    workers.append(worker2)
    
    # Worker 3 - handles both tags
    worker3 = Worker(
        worker_id="worker-3",
        job_store=job_store,
        tags=["task", "background"],
        max_concurrent_jobs=1,
        executor=worker_job_executor
    )
    workers.append(worker3)
    
    # Start the workers
    for worker in workers:
        await worker.start()
    
    logger.info("Workers started, creating jobs...")
    
    # Create jobs with different tags
    # Task jobs
    task_jobs = []
    for i in range(5):
        job = Job(
            name=f"Task Job {i}",
            description="A task job",
            payload={"function": "successful", "params": {"task_id": i}},
            tags=["task"],
            priority=JobPriority.HIGH if i % 2 == 0 else JobPriority.MEDIUM
        )
        task_jobs.append(job)
        manager.job_store.save(job)
    
    # Background jobs
    background_jobs = []
    for i in range(3):
        job = Job(
            name=f"Background Job {i}",
            description="A background job",
            payload={"function": "failing_with_retry", "params": {"job_id": i}},
            tags=["background"],
            max_retries=3,
            retry_policy=ExponentialBackoffRetryPolicy(initial_delay=1, multiplier=2),
            priority=JobPriority.LOW
        )
        background_jobs.append(job)
        manager.job_store.save(job)
        
    # Jobs with chain dependencies
    previous_job = None
    chain_jobs = []
    for i in range(4):
        job = Job(
            name=f"Chain Job {i}",
            description=f"Job {i} in a dependency chain",
            payload={"function": "successful", "params": {"position": i}},
            tags=["task" if i % 2 == 0 else "background"],
            priority=JobPriority.MEDIUM
        )
        if previous_job:
            job.add_dependency(previous_job.job_id)
        chain_jobs.append(job)
        manager.job_store.save(job)
        previous_job = job
    
    # Run the system for a while to see workers processing jobs
    logger.info(f"Created {len(task_jobs)} task jobs, {len(background_jobs)} background jobs, and {len(chain_jobs)} chain jobs")
    logger.info("Monitoring job execution for 60 seconds...")
    
    # Monitor jobs
    start_time = time.time()
    update_interval = 5  # seconds
    next_update = start_time + update_interval
    
    while time.time() - start_time < 60:
        await asyncio.sleep(0.1)
        
        # Periodically print status
        if time.time() >= next_update:
            # Count jobs by status
            all_jobs = (
                manager.job_store.list(status=JobStatus.PENDING) +
                manager.job_store.list(status=JobStatus.RUNNING) +
                manager.job_store.list(status=JobStatus.COMPLETED) +
                manager.job_store.list(status=JobStatus.FAILED)
            )
            
            pending_count = sum(1 for job in all_jobs if job.status == JobStatus.PENDING)
            running_count = sum(1 for job in all_jobs if job.status == JobStatus.RUNNING)
            completed_count = sum(1 for job in all_jobs if job.status == JobStatus.COMPLETED)
            failed_count = sum(1 for job in all_jobs if job.status == JobStatus.FAILED)
            
            logger.info(
                f"Status: PENDING={pending_count}, RUNNING={running_count}, "
                f"COMPLETED={completed_count}, FAILED={failed_count}"
            )
            
            # Check if all jobs are complete or failed
            if pending_count == 0 and running_count == 0:
                logger.info("All jobs have completed or failed.")
                break
                
            next_update = time.time() + update_interval
    
    # Stop the workers
    logger.info("Stopping workers...")
    for worker in workers:
        await worker.stop()
    
    # Stop the worker manager
    await worker_manager.stop()
    
    # Dump final job statuses
    logger.info("Final job statuses:")
    for job in manager.job_store.list():
        logger.info(f"Job {job.job_id} ({job.name}): {job.status.value}")
        if job.result:
            logger.info(f"  Result: {job.result}")
        if job.error:
            logger.info(f"  Error: {job.error}")
        if job.retry_count > 0:
            logger.info(f"  Retry count: {job.retry_count}")


async def run_retry_policies_demo():
    """Demonstrate different retry policies."""
    # Create a job store and manager
    job_store = SQLiteJobStore()
    manager = JobManager(job_store=job_store)
    
    # Create jobs with retry policies
    jobs = create_jobs_with_retry_policies()
    
    # Save jobs to store
    for job in jobs:
        job_store.save(job)
        
    # Override the _execute_job method temporarily for this demo to make jobs fail predictably
    original_execute = manager._execute_job
    
    async def demo_execute_job(job_id: str):
        job = job_store.get(job_id)
        if not job:
            return
            
        logger.info(f"Starting job {job.name} (attempt: {job.retry_count + 1})")
        
        # Update job status
        job.status = JobStatus.RUNNING
        job.started_at = datetime.now()
        job.updated_at = job.started_at
        job_store.save(job)
        
        # For demo purposes, make all jobs fail on the first two attempts
        if job.retry_count < 2:
            # Wait a bit to simulate work
            await asyncio.sleep(1)
            
            # Fail the job
            logger.info(f"Job {job.name} failing (attempt: {job.retry_count + 1})")
            job.status = JobStatus.FAILED
            job.updated_at = datetime.now()
            job.error = {
                "message": f"Simulated failure on attempt {job.retry_count + 1}",
                "type": "SimulatedError"
            }
            
            # Retry logic
            if job.retry_count < job.max_retries:
                retry_delay = job.get_retry_delay()
                
                logger.info(
                    f"Job {job.name} will retry after {retry_delay:.2f}s "
                    f"(attempt {job.retry_count + 1}/{job.max_retries})"
                )
                
                job.status = JobStatus.PENDING
                job.retry_count += 1
                job_store.save(job)
                
                # Schedule retry
                asyncio.create_task(manager._retry_job_after_delay(job_id, retry_delay))
            else:
                logger.info(f"Job {job.name} has exhausted all retries")
                job_store.save(job)
        else:
            # Succeed on third attempt
            await asyncio.sleep(1)
            logger.info(f"Job {job.name} succeeding on attempt {job.retry_count + 1}")
            job.status = JobStatus.COMPLETED
            job.result = {"success": True, "attempt": job.retry_count + 1}
            job.completed_at = datetime.now()
            job.updated_at = job.completed_at
            job_store.save(job)
    
    # Replace the method for our demo
    manager._execute_job = demo_execute_job
    
    # Start all jobs
    for job in jobs:
        manager.start_job(job.job_id)
    
    # Wait for all jobs to complete
    logger.info("Waiting for all jobs to complete...")
    all_completed = False
    while not all_completed:
        await asyncio.sleep(1)
        
        # Check job statuses
        all_jobs = job_store.list()
        all_completed = all(job.status == JobStatus.COMPLETED for job in all_jobs)
        
        # Print status
        pending = sum(1 for job in all_jobs if job.status == JobStatus.PENDING)
        running = sum(1 for job in all_jobs if job.status == JobStatus.RUNNING)
        completed = sum(1 for job in all_jobs if job.status == JobStatus.COMPLETED)
        failed = sum(1 for job in all_jobs if job.status == JobStatus.FAILED)
        
        logger.info(f"Status: PENDING={pending}, RUNNING={running}, COMPLETED={completed}, FAILED={failed}")
    
    # Print results
    logger.info("All jobs completed!")
    for job in job_store.list():
        logger.info(f"Job {job.name}: completed after {job.retry_count + 1} attempts")
        logger.info(f"  Result: {job.result}")
    
    # Restore original method
    manager._execute_job = original_execute


async def main():
    """Run the demo."""
    logger.info("=== Retry Policies Demo ===")
    await run_retry_policies_demo()
    
    logger.info("\n=== Distributed Execution Demo ===")
    await run_distributed_execution_demo()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Demo interrupted by user")
        sys.exit(0) 