#!/usr/bin/env python
"""
Example script demonstrating how to use SQLAlchemyJobStore with JobManager.

This script shows how to configure and use the SQLAlchemyJobStore with both
SQLite and PostgreSQL backends. It demonstrates:
- Setting up database configurations
- Creating the SQLAlchemyJobStore
- Using it with JobManager for typical job operations
- Verifying data persistence across sessions
"""

import asyncio
import os
import time
import logging
from datetime import datetime
from pprint import pprint

from openagents_json.job.manager import JobManager
from openagents_json.job.model import JobStatus, JobPriority
from openagents_json.job.storage import SQLAlchemyJobStore


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def run_sqlite_example():
    """Demonstrate using SQLAlchemyJobStore with SQLite."""
    print("\n=== SQLite JobStore Example ===")
    
    # Create SQLAlchemyJobStore with SQLite
    sqlite_path = "example_jobs.db"
    print(f"\n[1] Creating SQLAlchemyJobStore with SQLite ({sqlite_path})...")
    
    job_store = SQLAlchemyJobStore(
        dialect="sqlite",
        path=sqlite_path
    )
    
    # Initialize JobManager with SQLite store
    print("\n[2] Initializing JobManager with SQLite store...")
    job_manager = JobManager(
        job_store=job_store,
        retention_days=30,
        max_concurrent_jobs=5
    )
    
    # Create and manipulate jobs
    await run_job_operations(job_manager)
    
    print("\n=== End of SQLite Example ===")


async def run_postgres_example():
    """Demonstrate using SQLAlchemyJobStore with PostgreSQL (if available)."""
    # Get PostgreSQL connection details from environment variables
    pg_host = os.environ.get("OPENAGENTS_PG_HOST")
    pg_port = os.environ.get("OPENAGENTS_PG_PORT", "5432")
    pg_user = os.environ.get("OPENAGENTS_PG_USER")
    pg_pass = os.environ.get("OPENAGENTS_PG_PASS")
    pg_db = os.environ.get("OPENAGENTS_PG_DB")
    
    # Skip PostgreSQL example if connection details aren't provided
    if not all([pg_host, pg_user, pg_pass, pg_db]):
        print("\n=== PostgreSQL Example Skipped (missing connection details) ===")
        print("Set the following environment variables to run the PostgreSQL example:")
        print("  OPENAGENTS_PG_HOST - PostgreSQL host")
        print("  OPENAGENTS_PG_PORT - PostgreSQL port (default: 5432)")
        print("  OPENAGENTS_PG_USER - PostgreSQL username")
        print("  OPENAGENTS_PG_PASS - PostgreSQL password")
        print("  OPENAGENTS_PG_DB   - PostgreSQL database name")
        return
    
    print("\n=== PostgreSQL JobStore Example ===")
    
    # Create SQLAlchemyJobStore with PostgreSQL
    print(f"\n[1] Creating SQLAlchemyJobStore with PostgreSQL ({pg_host}:{pg_port})...")
    
    job_store = SQLAlchemyJobStore(
        dialect="postgresql",
        host=pg_host,
        port=int(pg_port),
        username=pg_user,
        password=pg_pass,
        database=pg_db
    )
    
    # Initialize JobManager with PostgreSQL store
    print("\n[2] Initializing JobManager with PostgreSQL store...")
    job_manager = JobManager(
        job_store=job_store,
        retention_days=30,
        max_concurrent_jobs=5
    )
    
    # Create and manipulate jobs
    await run_job_operations(job_manager)
    
    print("\n=== End of PostgreSQL Example ===")


async def run_connection_string_example():
    """Demonstrate using SQLAlchemyJobStore with a direct connection string."""
    print("\n=== Connection String JobStore Example ===")
    
    # Direct SQLAlchemy connection string
    conn_string = "sqlite:///example_conn_string.db"
    print(f"\n[1] Creating SQLAlchemyJobStore with connection string: {conn_string}")
    
    job_store = SQLAlchemyJobStore(
        connection_string=conn_string
    )
    
    # Initialize JobManager with connection string store
    print("\n[2] Initializing JobManager...")
    job_manager = JobManager(
        job_store=job_store,
        retention_days=30,
        max_concurrent_jobs=5
    )
    
    # Create and manipulate jobs
    await run_job_operations(job_manager)
    
    print("\n=== End of Connection String Example ===")


async def run_job_operations(job_manager):
    """Run standard job operations with the given JobManager."""
    # Create several jobs
    print("\n[3] Creating jobs...")
    job1 = job_manager.create_job(
        workflow_id="db-workflow-1",
        inputs={"parameter1": "value1"},
        priority=JobPriority.HIGH,
        user_id="user-123",
        tags=["database", "high-priority"]
    )
    print(f"  Created job: {job1.job_id} (HIGH priority)")
    
    job2 = job_manager.create_job(
        workflow_id="db-workflow-2",
        inputs={"parameter1": "value2"},
        priority=JobPriority.MEDIUM,
        user_id="user-456",
        tags=["database", "medium-priority"]
    )
    print(f"  Created job: {job2.job_id} (MEDIUM priority)")
    
    # Start job1
    print(f"\n[4] Starting job {job1.job_id}...")
    job_manager.start_job(job1.job_id)
    
    # Wait for the job to complete
    print(f"\n[5] Waiting for job {job1.job_id} to complete...")
    max_wait = 10  # seconds
    for _ in range(max_wait * 2):
        status = job_manager.get_job_status(job1.job_id)
        print(f"  Job status: {status}", end="\r")
        if status == JobStatus.COMPLETED:
            print(f"  Job status: {status}")
            break
        await asyncio.sleep(0.5)
    
    # Get job results
    if status == JobStatus.COMPLETED:
        print(f"\n[6] Getting results for job {job1.job_id}...")
        results = job_manager.get_job_results(job1.job_id)
        print("  Job results:")
        pprint(results)
    
    # List jobs with various filters
    print("\n[7] Listing jobs with filters...")
    
    # All jobs
    all_jobs = job_manager.list_jobs()
    print(f"  Total jobs: {len(all_jobs)}")
    
    # Jobs by workflow ID
    workflow_jobs = job_manager.list_jobs(workflow_id="db-workflow-1")
    print(f"  Jobs for workflow 'db-workflow-1': {len(workflow_jobs)}")
    
    # Jobs by tag
    tagged_jobs = job_manager.list_jobs(tags=["high-priority"])
    print(f"  High priority jobs: {len(tagged_jobs)}")
    
    # Delete a job
    print(f"\n[8] Deleting job {job2.job_id}...")
    job_manager.delete_job(job2.job_id)
    
    # Verify deletion
    job = job_manager.get_job(job2.job_id)
    print(f"  Job exists after deletion: {job is not None}")


async def run_persistence_test():
    """Test that jobs persist between JobManager instances."""
    print("\n=== Persistence Test ===")
    
    # SQLite file for persistence test
    db_path = "persistence_test.db"
    
    # Create first JobManager
    print("\n[1] Creating first JobManager...")
    job_store1 = SQLAlchemyJobStore(dialect="sqlite", path=db_path)
    manager1 = JobManager(job_store=job_store1)
    
    # Create a job
    job = manager1.create_job(
        workflow_id="persistence-test",
        inputs={"test": "value"},
        tags=["persistence"]
    )
    job_id = job.job_id
    print(f"  Created job: {job_id}")
    
    # Start and wait for completion
    manager1.start_job(job_id)
    print("  Started job")
    
    # Wait for job to complete
    max_wait = 10
    for _ in range(max_wait * 2):
        if manager1.get_job_status(job_id) == JobStatus.COMPLETED:
            break
        await asyncio.sleep(0.5)
    
    print("  Job completed")
    
    # Create second JobManager instance
    print("\n[2] Creating second JobManager (should load existing job)...")
    job_store2 = SQLAlchemyJobStore(dialect="sqlite", path=db_path)
    manager2 = JobManager(job_store=job_store2)
    
    # Try to retrieve the job with the second manager
    retrieved_job = manager2.get_job(job_id)
    
    if retrieved_job:
        print(f"  Successfully retrieved job {job_id} from database")
        print(f"  Job status: {retrieved_job.status}")
        print(f"  Job workflow: {retrieved_job.workflow_id}")
        print(f"  Job tags: {retrieved_job.tags}")
    else:
        print(f"  Failed to retrieve job {job_id} (persistence issue)")
    
    print("\n=== End of Persistence Test ===")


async def main():
    """Run all examples."""
    print("=== SQLAlchemyJobStore Examples ===")
    
    try:
        # Run SQLite example
        await run_sqlite_example()
        
        # Run PostgreSQL example (if configured)
        await run_postgres_example()
        
        # Run connection string example
        await run_connection_string_example()
        
        # Test persistence between JobManager instances
        await run_persistence_test()
        
    except Exception as e:
        logger.exception("Error running examples")
        print(f"\nError: {str(e)}")
    
    print("\n=== End of SQLAlchemyJobStore Examples ===")


if __name__ == "__main__":
    asyncio.run(main()) 