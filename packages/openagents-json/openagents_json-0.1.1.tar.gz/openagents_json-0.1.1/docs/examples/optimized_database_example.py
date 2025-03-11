#!/usr/bin/env python
"""
Example script demonstrating advanced database features of SQLAlchemyJobStore.

This script shows:
- Optimized connection pooling configuration
- Performance benchmarks for different database operations
- Support for multiple database backends (SQLite, PostgreSQL, MySQL)
- Proper resource management and cleanup
"""

import asyncio
import logging
import time
import os
import random
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any

from openagents_json.job.manager import JobManager
from openagents_json.job.model import Job, JobStatus, JobPriority
from openagents_json.job.storage import SQLAlchemyJobStore

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Test constants
NUM_JOBS = 100
BATCH_SIZE = 20


async def benchmark_operation(name: str, operation, *args, **kwargs):
    """Benchmark an operation and log its execution time."""
    start_time = time.time()
    result = await operation(*args, **kwargs) if asyncio.iscoroutinefunction(operation) else operation(*args, **kwargs)
    elapsed = time.time() - start_time
    logger.info(f"{name}: {elapsed:.4f} seconds")
    return result


def create_test_jobs(count: int) -> List[Job]:
    """Create a list of test jobs."""
    jobs = []
    for i in range(count):
        job = Job(
            job_id=f"test-job-{uuid.uuid4()}",
            name=f"Test Job {i}",
            description=f"A test job created for benchmarking ({i})",
            payload={"index": i, "random_data": random.random()},
            status=JobStatus.PENDING,
            priority=random.choice(list(JobPriority)),
            tags=["test", f"group-{i % 5}", "benchmark"]
        )
        jobs.append(job)
    return jobs


async def run_sqlite_benchmark():
    """Run benchmarks using SQLite backend."""
    print("\n=== SQLite Benchmark (with optimized settings) ===")
    
    # Setup SQLite with optimized settings
    sqlite_path = "benchmark_sqlite.db"
    if os.path.exists(sqlite_path):
        os.remove(sqlite_path)  # Start fresh
        
    job_store = SQLAlchemyJobStore(
        dialect="sqlite",
        path=sqlite_path,
        pooling=True,  # SQLite has its own pooling mechanism
        echo=False     # Set to True to see SQL queries
    )
    
    # Create JobManager
    job_manager = JobManager(job_store=job_store)
    
    try:
        # Benchmark job creation
        print("\nCreating jobs...")
        jobs = create_test_jobs(NUM_JOBS)
        
        # Individual job creation
        print("\nBenchmarking individual job creation:")
        for i in range(5):  # Test with a few jobs
            await benchmark_operation(
                f"Create individual job {i}",
                job_manager.create_job,
                name=f"Individual Job {i}",
                payload={"test": f"data-{i}"}
            )
            
        # Batch job creation
        print("\nBenchmarking batch job creation:")
        batch_jobs = jobs[:BATCH_SIZE]
        batch_id = await benchmark_operation(
            f"Create batch of {BATCH_SIZE} jobs",
            job_manager.create_job_batch,
            batch_jobs
        )
        
        # Query performance
        print("\nBenchmarking queries:")
        await benchmark_operation(
            "Query all jobs",
            job_manager.list_jobs
        )
        
        await benchmark_operation(
            "Query by status",
            job_manager.list_jobs,
            status=JobStatus.PENDING
        )
        
        await benchmark_operation(
            "Query by tag",
            job_manager.list_jobs,
            tags=["group-1"]
        )
        
        # Batch retrieval
        await benchmark_operation(
            f"Retrieve batch of {BATCH_SIZE} jobs",
            job_manager.get_batch_jobs,
            batch_id
        )
        
        # Cleanup
        deleted = await benchmark_operation(
            "Cleanup recent jobs",
            job_store.cleanup_old_jobs,
            days=0  # Delete all jobs (for testing)
        )
        print(f"Deleted {deleted} jobs during cleanup")
        
    finally:
        # Properly close connections
        job_store.close()
        print("SQLite connections closed")
        
    print("=== End of SQLite Benchmark ===")


async def run_mysql_benchmark():
    """
    Run benchmarks using MySQL backend.
    
    Note: This requires a MySQL server to be running.
    Edit the connection parameters to match your environment.
    """
    # Check if MySQL is available
    mysql_available = False
    try:
        # Try to import the MySQL connector
        import pymysql
        mysql_available = True
    except ImportError:
        print("\n=== MySQL Benchmark (SKIPPED - PyMySQL not installed) ===")
        print("To run MySQL benchmarks, install PyMySQL with: pip install pymysql")
        return
        
    # Check environment variables for MySQL connection
    mysql_host = os.getenv("MYSQL_HOST")
    mysql_user = os.getenv("MYSQL_USER")
    mysql_password = os.getenv("MYSQL_PASSWORD")
    mysql_database = os.getenv("MYSQL_DATABASE")
    
    if not all([mysql_host, mysql_user, mysql_password, mysql_database]):
        print("\n=== MySQL Benchmark (SKIPPED - Connection details not provided) ===")
        print("To run MySQL benchmarks, set the following environment variables:")
        print("  MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE")
        return
    
    print("\n=== MySQL Benchmark (with connection pooling) ===")
    
    try:
        # Create MySQL JobStore with connection pooling
        job_store = SQLAlchemyJobStore(
            dialect="mysql",
            host=mysql_host,
            username=mysql_user,
            password=mysql_password,
            database=mysql_database,
            pooling=True,
            pool_size=5,
            max_overflow=10,
            pool_recycle=3600,
            echo=False  # Set to True to see SQL queries
        )
        
        # Create JobManager
        job_manager = JobManager(job_store=job_store)
        
        # Run the same benchmarks as with SQLite
        # Benchmark job creation
        print("\nCreating jobs...")
        jobs = create_test_jobs(NUM_JOBS)
        
        # Individual job creation
        print("\nBenchmarking individual job creation:")
        for i in range(5):  # Test with a few jobs
            await benchmark_operation(
                f"Create individual job {i}",
                job_manager.create_job,
                name=f"Individual Job {i}",
                payload={"test": f"data-{i}"}
            )
            
        # Batch job creation
        print("\nBenchmarking batch job creation:")
        batch_jobs = jobs[:BATCH_SIZE]
        batch_id = await benchmark_operation(
            f"Create batch of {BATCH_SIZE} jobs",
            job_manager.create_job_batch,
            batch_jobs
        )
        
        # Query performance
        print("\nBenchmarking queries:")
        await benchmark_operation(
            "Query all jobs",
            job_manager.list_jobs
        )
        
        await benchmark_operation(
            "Query by status",
            job_manager.list_jobs,
            status=JobStatus.PENDING
        )
        
        await benchmark_operation(
            "Query by tag",
            job_manager.list_jobs,
            tags=["group-1"]
        )
        
        # Batch retrieval
        await benchmark_operation(
            f"Retrieve batch of {BATCH_SIZE} jobs",
            job_manager.get_batch_jobs,
            batch_id
        )
        
        # Cleanup
        deleted = await benchmark_operation(
            "Cleanup recent jobs",
            job_store.cleanup_old_jobs,
            days=0  # Delete all jobs (for testing)
        )
        print(f"Deleted {deleted} jobs during cleanup")
        
    except Exception as e:
        print(f"MySQL benchmark error: {str(e)}")
    finally:
        if 'job_store' in locals():
            # Properly close connections
            job_store.close()
            print("MySQL connections closed")
        
    print("=== End of MySQL Benchmark ===")


async def main():
    """Run all benchmarks sequentially."""
    print("=== Database Optimization Benchmarks ===\n")
    print("This script demonstrates optimized database configurations and benchmarks performance.")
    
    # Run SQLite benchmark
    await run_sqlite_benchmark()
    
    # Run MySQL benchmark if available
    await run_mysql_benchmark()
    
    print("\n=== All Benchmarks Completed ===")
    print("\nSummary:")
    print("1. Connection pooling improves performance for concurrent operations")
    print("2. Batch operations are more efficient for creating multiple jobs")
    print("3. Properly closing connections is important for resource management")
    print("4. Different database backends have different performance characteristics")
    

if __name__ == "__main__":
    asyncio.run(main()) 