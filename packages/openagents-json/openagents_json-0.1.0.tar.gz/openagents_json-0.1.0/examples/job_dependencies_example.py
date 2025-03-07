#!/usr/bin/env python3
"""
Job Dependencies Example

This example demonstrates how to create jobs with dependencies and use batch operations
in OpenAgents JSON. It shows how to:

1. Create jobs with dependencies
2. Create a batch of related jobs
3. Handle parallel and sequential job dependencies
4. Visualize a job dependency graph
"""

import time
import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

from openagents_json.job.manager import JobManager
from openagents_json.job.model import Job, JobStatus, JobPriority
from openagents_json.job.storage import SQLAlchemyJobStore


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def monitor_jobs(job_manager: JobManager, job_ids: List[str], interval: int = 1) -> None:
    """Monitor the status of multiple jobs until they complete or fail."""
    pending_jobs = job_ids.copy()
    
    print(f"\nMonitoring {len(job_ids)} jobs:")
    
    while pending_jobs:
        statuses = {}
        for job_id in job_ids:
            job = job_manager.get_job(job_id)
            if job:
                status = job.status.value
                if job_id in pending_jobs and job.status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
                    pending_jobs.remove(job_id)
                statuses[job_id] = status
        
        # Print status table
        print("\033[H\033[J")  # Clear screen
        print(f"Job Status at {datetime.now().strftime('%H:%M:%S')}:")
        print("-" * 50)
        print(f"{'Job ID':<36} | {'Status':<10} ")
        print("-" * 50)
        
        for job_id, status in statuses.items():
            print(f"{job_id:<36} | {status:<10}")
        
        print("-" * 50)
        print(f"Remaining: {len(pending_jobs)} jobs")
        
        if not pending_jobs:
            break
            
        await asyncio.sleep(interval)
    
    print("\nAll jobs completed or failed!")


def create_sequential_jobs(job_manager: JobManager, n: int = 3) -> List[str]:
    """Create a sequence of jobs where each depends on the previous one."""
    job_ids = []
    
    print("\nCreating sequential job chain:")
    
    # Create first job
    first_job = job_manager.create_job(
        name="Sequential Job 1",
        description="First job in a sequential chain",
        payload={"step": 1, "data": "Initial data"},
        tags=["sequential", "example"],
        auto_start=True
    )
    job_ids.append(first_job.job_id)
    print(f"  Created job {first_job.job_id} (no dependencies)")
    
    # Create subsequent jobs with dependencies
    prev_job_id = first_job.job_id
    for i in range(2, n+1):
        next_job = job_manager.create_job(
            name=f"Sequential Job {i}",
            description=f"Job {i} in a sequential chain",
            payload={"step": i, "data": f"Data from step {i}"},
            tags=["sequential", "example"],
            dependencies=[prev_job_id],
            auto_start=True
        )
        job_ids.append(next_job.job_id)
        print(f"  Created job {next_job.job_id} (depends on {prev_job_id})")
        prev_job_id = next_job.job_id
    
    return job_ids


def create_parallel_with_join(job_manager: JobManager, n_parallel: int = 3) -> List[str]:
    """Create parallel jobs that a final job depends on."""
    job_ids = []
    
    print("\nCreating parallel jobs with join pattern:")
    
    # Create parallel jobs
    parallel_job_ids = []
    for i in range(1, n_parallel+1):
        job = job_manager.create_job(
            name=f"Parallel Job {i}",
            description=f"Parallel job {i} of {n_parallel}",
            payload={"worker": i, "data": f"Parallel data {i}"},
            tags=["parallel", "example"],
            auto_start=True
        )
        parallel_job_ids.append(job.job_id)
        job_ids.append(job.job_id)
        print(f"  Created parallel job {job.job_id}")
    
    # Create the join job that depends on all parallel jobs
    join_job = job_manager.create_job(
        name="Join Job",
        description="Job that depends on all parallel jobs",
        payload={"operation": "join", "data": "Final processing"},
        tags=["join", "example"],
        dependencies=parallel_job_ids,
        auto_start=True
    )
    job_ids.append(join_job.job_id)
    
    print(f"  Created join job {join_job.job_id} (depends on {len(parallel_job_ids)} jobs)")
    
    return job_ids


def create_complex_dag(job_manager: JobManager) -> List[str]:
    """Create a more complex directed acyclic graph (DAG) of jobs."""
    
    print("\nCreating a complex job DAG:")
    
    # Create a batch of jobs with a complex dependency structure
    job_specs = [
        {
            "name": "Initialize Data",
            "description": "Set up initial dataset",
            "payload": {"action": "initialize"},
            "tags": ["dag", "initialize"],
            "dependencies": []
        },
        {
            "name": "Process A",
            "description": "Process data through method A",
            "payload": {"action": "process", "method": "A"},
            "tags": ["dag", "process"],
            "dependencies": [0]  # Depends on Initialize Data
        },
        {
            "name": "Process B",
            "description": "Process data through method B",
            "payload": {"action": "process", "method": "B"},
            "tags": ["dag", "process"],
            "dependencies": [0]  # Depends on Initialize Data
        },
        {
            "name": "Process C",
            "description": "Process data through method C",
            "payload": {"action": "process", "method": "C"},
            "tags": ["dag", "process"],
            "dependencies": [0]  # Depends on Initialize Data
        },
        {
            "name": "Combine A+B",
            "description": "Combine results from methods A and B",
            "payload": {"action": "combine", "methods": ["A", "B"]},
            "tags": ["dag", "combine"],
            "dependencies": [1, 2]  # Depends on Process A and Process B
        },
        {
            "name": "Extend C",
            "description": "Extend results from method C",
            "payload": {"action": "extend", "method": "C"},
            "tags": ["dag", "extend"],
            "dependencies": [3]  # Depends on Process C
        },
        {
            "name": "Finalize",
            "description": "Combine all processed data and finalize results",
            "payload": {"action": "finalize"},
            "tags": ["dag", "finalize"],
            "dependencies": [4, 5]  # Depends on Combine A+B and Extend C
        }
    ]
    
    # First pass: Create all jobs without dependencies
    jobs = []
    for spec in job_specs:
        job = job_manager.create_job(
            name=spec["name"],
            description=spec["description"],
            payload=spec["payload"],
            tags=spec["tags"]
        )
        jobs.append(job)
        print(f"  Created job {job.job_id}: {job.name}")
    
    # Second pass: Add dependencies using job IDs
    for i, spec in enumerate(job_specs):
        job = jobs[i]
        for dep_index in spec["dependencies"]:
            dep_job = jobs[dep_index]
            job_manager.add_job_dependency(job.job_id, dep_job.job_id)
            print(f"  Added dependency: {job.name} -> {dep_job.name}")
    
    # Start the initial job
    job_manager.start_job(jobs[0].job_id)
    print(f"  Started initial job: {jobs[0].name}")
    
    return [job.job_id for job in jobs]


async def batch_job_workflow(job_manager: JobManager) -> List[str]:
    """Demonstrate creating and monitoring a batch of jobs with dependencies."""
    
    # Create a batch of jobs
    print("\nCreating a batch of jobs with dependencies:")
    
    batch_data = [
        {
            "name": "Batch Data Collection",
            "description": "First step: collect data",
            "payload": {"source": "api", "target": "raw_data"},
            "tags": ["batch", "data"],
            "dependencies": []
        },
        {
            "name": "Batch Data Validation",
            "description": "Second step: validate data",
            "payload": {"input": "raw_data", "validators": ["schema", "range"]},
            "tags": ["batch", "validation"],
            "dependencies": [0]  # Will be replaced with actual job ID
        },
        {
            "name": "Batch Data Transform A",
            "description": "Third step A: transform data",
            "payload": {"input": "raw_data", "transform": "normalize"},
            "tags": ["batch", "transform"],
            "dependencies": [1]  # Will be replaced with actual job ID
        },
        {
            "name": "Batch Data Transform B",
            "description": "Third step B: transform data",
            "payload": {"input": "raw_data", "transform": "aggregate"},
            "tags": ["batch", "transform"],
            "dependencies": [1]  # Will be replaced with actual job ID
        },
        {
            "name": "Batch Data Export",
            "description": "Final step: export results",
            "payload": {"inputs": ["transform_a", "transform_b"], "output": "final_data"},
            "tags": ["batch", "export"],
            "dependencies": [2, 3]  # Will be replaced with actual job ID
        }
    ]
    
    # Process dependencies
    jobs_data = []
    for i, job_data in enumerate(batch_data):
        # Create a copy of job data
        processed_job = job_data.copy()
        
        # Replace dependency indices with real job IDs if we have them
        if i > 0:
            real_deps = []
            for dep_idx in processed_job["dependencies"]:
                # Even though we haven't created the jobs yet, we know what the IDs will be
                # in the batch operation
                if dep_idx < i:
                    real_deps.append(batch_data[dep_idx]["name"])
            
            processed_job["dependencies"] = real_deps
        
        jobs_data.append(processed_job)
    
    # Create the batch
    batch_id, batch_jobs = job_manager.create_job_batch(
        jobs_data,
        auto_start=False  # We'll start them manually
    )
    
    # Replace names with IDs in dependencies
    name_to_id = {job.name: job.job_id for job in batch_jobs}
    
    for job in batch_jobs:
        if job.dependencies:
            new_deps = []
            for dep_name in job.dependencies:
                if dep_name in name_to_id:
                    new_deps.append(name_to_id[dep_name])
            
            # Update dependencies with actual job IDs
            if new_deps:
                job.dependencies = new_deps
                job_manager.job_store.save(job)
    
    print(f"  Created batch with ID: {batch_id}")
    for job in batch_jobs:
        deps = [f"{dep_id[:8]}..." for dep_id in job.dependencies]
        print(f"  Job: {job.job_id[:8]}... | {job.name} | Dependencies: {deps}")
    
    # Start only the first job
    job_manager.start_job(batch_jobs[0].job_id)
    print(f"  Started first job in batch: {batch_jobs[0].name}")
    
    return [job.job_id for job in batch_jobs]


async def main() -> None:
    """Run the job dependencies example."""
    # Create a job manager with SQLAlchemy job store
    job_store = SQLAlchemyJobStore(dialect="sqlite", path=":memory:")
    job_manager = JobManager(job_store=job_store, max_concurrent_jobs=5)
    
    # Examples of different job dependency patterns
    job_ids = []
    
    # Example 1: Sequential jobs
    sequential_job_ids = create_sequential_jobs(job_manager, n=4)
    job_ids.extend(sequential_job_ids)
    
    # Example 2: Parallel jobs with join
    parallel_job_ids = create_parallel_with_join(job_manager, n_parallel=3)
    job_ids.extend(parallel_job_ids)
    
    # Example 3: Complex DAG
    dag_job_ids = create_complex_dag(job_manager)
    job_ids.extend(dag_job_ids)
    
    # Example 4: Batch job workflow
    batch_job_ids = await batch_job_workflow(job_manager)
    job_ids.extend(batch_job_ids)
    
    # Monitor all jobs
    await monitor_jobs(job_manager, job_ids)
    
    # Show results after completion
    print("\nResults after completion:")
    for job_id in job_ids:
        job = job_manager.get_job(job_id)
        if job:
            print(f"Job {job.name} ({job.job_id[:8]}...): {job.status.value}")


if __name__ == "__main__":
    asyncio.run(main()) 