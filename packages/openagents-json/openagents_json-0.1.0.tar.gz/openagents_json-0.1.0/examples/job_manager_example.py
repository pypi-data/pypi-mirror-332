#!/usr/bin/env python
"""
Example script demonstrating how to use the JobManager.

This script shows common operations with the JobManager, including:
- Creating and starting jobs
- Retrieving job status and results
- Managing job lifecycle
- Listing and filtering jobs
- Cleanup operations
"""

import asyncio
import time
from datetime import datetime
from pprint import pprint

from openagents_json.job.manager import JobManager
from openagents_json.job.model import JobStatus, JobPriority
from openagents_json.job.storage import FileJobStore


async def main():
    """Run the JobManager demonstration."""
    print("=== JobManager Example ===")
    
    # Create a JobManager with file-based storage
    print("\n[1] Creating JobManager...")
    job_store = FileJobStore(storage_dir=".example_jobs")
    job_manager = JobManager(
        job_store=job_store,
        retention_days=30,
        max_concurrent_jobs=5
    )
    
    # Create several jobs
    print("\n[2] Creating jobs...")
    job1 = job_manager.create_job(
        workflow_id="example-workflow-1",
        inputs={"parameter1": "value1"},
        priority=JobPriority.HIGH,
        user_id="user-123",
        tags=["example", "high-priority"]
    )
    print(f"  Created job: {job1.job_id} (HIGH priority)")
    
    job2 = job_manager.create_job(
        workflow_id="example-workflow-2",
        inputs={"parameter1": "value2"},
        priority=JobPriority.MEDIUM,
        user_id="user-456",
        tags=["example", "medium-priority"]
    )
    print(f"  Created job: {job2.job_id} (MEDIUM priority)")
    
    job3 = job_manager.create_job(
        workflow_id="example-workflow-1",
        inputs={"parameter1": "value3"},
        priority=JobPriority.LOW,
        user_id="user-123",
        tags=["example", "low-priority"]
    )
    print(f"  Created job: {job3.job_id} (LOW priority)")
    
    # Start a job
    print(f"\n[3] Starting job {job1.job_id}...")
    job_manager.start_job(job1.job_id)
    
    # Wait a moment to allow the job to start execution
    await asyncio.sleep(1)
    
    # Check job status
    status = job_manager.get_job_status(job1.job_id)
    print(f"  Job status: {status}")
    
    # Pause the job
    print(f"\n[4] Pausing job {job1.job_id}...")
    job_manager.pause_job(job1.job_id)
    
    # Check job status after pausing
    status = job_manager.get_job_status(job1.job_id)
    print(f"  Job status after pausing: {status}")
    
    # Resume the job
    print(f"\n[5] Resuming job {job1.job_id}...")
    job_manager.resume_job(job1.job_id)
    
    # Wait for the job to complete
    print(f"\n[6] Waiting for job {job1.job_id} to complete...")
    max_wait = 10  # seconds
    for _ in range(max_wait * 2):
        status = job_manager.get_job_status(job1.job_id)
        print(f"  Job status: {status}", end="\r")
        if status == JobStatus.COMPLETED:
            print(f"  Job status: {status}")
            break
        await asyncio.sleep(0.5)
    else:
        print(f"\n  Job did not complete within {max_wait} seconds")
    
    # Get job results
    if status == JobStatus.COMPLETED:
        print(f"\n[7] Getting results for job {job1.job_id}...")
        results = job_manager.get_job_results(job1.job_id)
        print("  Job results:")
        pprint(results)
    
    # Start and cancel a job
    print(f"\n[8] Starting job {job2.job_id}...")
    job_manager.start_job(job2.job_id)
    
    # Wait a moment to allow the job to start execution
    await asyncio.sleep(1)
    
    # Cancel the job
    print(f"  Cancelling job {job2.job_id}...")
    job_manager.cancel_job(job2.job_id)
    
    # Check job status after cancellation
    status = job_manager.get_job_status(job2.job_id)
    print(f"  Job status after cancellation: {status}")
    
    # List jobs with various filters
    print("\n[9] Listing jobs with filters...")
    
    # All jobs
    all_jobs = job_manager.list_jobs()
    print(f"  Total jobs: {len(all_jobs)}")
    
    # Jobs by workflow ID
    workflow_jobs = job_manager.list_jobs(workflow_id="example-workflow-1")
    print(f"  Jobs for workflow 'example-workflow-1': {len(workflow_jobs)}")
    
    # Jobs by user ID
    user_jobs = job_manager.list_jobs(user_id="user-123")
    print(f"  Jobs for user 'user-123': {len(user_jobs)}")
    
    # Jobs by status
    completed_jobs = job_manager.list_jobs(status=JobStatus.COMPLETED)
    print(f"  Completed jobs: {len(completed_jobs)}")
    
    # Jobs by tag
    tagged_jobs = job_manager.list_jobs(tags=["high-priority"])
    print(f"  High priority jobs: {len(tagged_jobs)}")
    
    # Delete a job
    print(f"\n[10] Deleting job {job3.job_id}...")
    job_manager.delete_job(job3.job_id)
    
    # Verify deletion
    job = job_manager.get_job(job3.job_id)
    print(f"  Job exists after deletion: {job is not None}")
    
    # Create some old jobs to demonstrate cleanup
    print("\n[11] Creating jobs with old timestamps for cleanup demonstration...")
    
    # Create a job and modify its timestamp
    old_job = job_manager.create_job(
        workflow_id="old-workflow",
        inputs={},
        tags=["old-job"]
    )
    
    # Access internal storage to modify timestamp for demonstration
    # Note: This is not a normal operation, just for demonstration
    job_file = job_store._get_job_path(old_job.job_id)
    import json
    with open(job_file, "r") as f:
        job_data = json.load(f)
    
    # Set created_at to a date in the past
    old_date = "2020-01-01T00:00:00"
    job_data["created_at"] = old_date
    
    with open(job_file, "w") as f:
        json.dump(job_data, f, indent=2)
    
    print(f"  Created job {old_job.job_id} with timestamp {old_date}")
    
    # Run cleanup
    print("\n[12] Cleaning up old jobs...")
    cleanup_count = job_manager.cleanup_old_jobs()
    print(f"  Cleaned up {cleanup_count} old jobs")
    
    print("\n=== End of JobManager Example ===")


if __name__ == "__main__":
    asyncio.run(main()) 