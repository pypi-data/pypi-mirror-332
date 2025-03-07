# Job Management

The `job` module provides a robust system for managing workflow execution jobs in the OpenAgents JSON framework. It includes classes for job model representation, storage backends, and a central manager for controlling job lifecycles.

## Overview

The job management system consists of the following key components:

1. **Job Model**: Represents a workflow execution job with metadata, payload, dependencies, and status tracking
2. **JobStore**: Storage interfaces for persisting jobs across application restarts
3. **JobManager**: Central class for creating, retrieving, and controlling jobs

## Usage Examples

### Basic Usage

```python
from openagents_json.job.manager import JobManager
from openagents_json.job.model import JobPriority

# Create a job manager with default settings (in-memory storage)
job_manager = JobManager()

# Create a job
job = job_manager.create_job(
    name="Process data",
    description="Data processing job",
    payload={"source": "database", "target": "report"},
    priority=JobPriority.HIGH,
    tags=["processing", "daily"]
)

# Start the job
job_manager.start_job(job.job_id)

# Later, check the job status
status = job_manager.get_job_status(job.job_id)
print(f"Job status: {status}")

# Get job results when completed
if status == "completed":
    results = job_manager.get_job_results(job.job_id)
    print(f"Job results: {results}")
```

### Using File-based Storage

```python
from openagents_json.job.manager import JobManager
from openagents_json.job.storage import FileJobStore

# Create a file-based job store
store = FileJobStore(storage_dir="jobs_data")

# Create a job manager with the file store
job_manager = JobManager(job_store=store, retention_days=30)

# Now jobs will be persisted to disk
job = job_manager.create_job(name="Data Export", payload={})
```

### Using Database Storage with SQLAlchemy

```python
from openagents_json.job.manager import JobManager
from openagents_json.job.storage import SQLAlchemyJobStore

# Create a SQLAlchemy job store with SQLite
store = SQLAlchemyJobStore(dialect="sqlite", path="jobs.db")

# Or with PostgreSQL
store = SQLAlchemyJobStore(
    dialect="postgresql",
    host="localhost",
    port=5432,
    username="user",
    password="pass",
    database="jobsdb"
)

# Create a job manager with the database store
job_manager = JobManager(job_store=store)

# Now jobs will be persisted in the database
job = job_manager.create_job(name="Export Data", payload={"format": "csv"})
```

### Job Filtering and Listing

```python
from openagents_json.job.model import JobStatus

# List all jobs
all_jobs = job_manager.list_jobs()

# Filter jobs by status
running_jobs = job_manager.list_jobs(status=JobStatus.RUNNING)

# Filter by tags
tagged_jobs = job_manager.list_jobs(tags=["production", "batch"])

# Filter by creation date
recent_jobs = job_manager.list_jobs(
    created_after="2023-01-01T00:00:00",
    created_before="2023-01-31T23:59:59"
)

# Sorting and pagination
sorted_jobs = job_manager.list_jobs(
    sort_by="priority",
    sort_order="desc",
    limit=10,
    offset=0
)
```

### Job Control Operations

```python
# Start a job
job_manager.start_job(job_id)

# Pause a running job
job_manager.pause_job(job_id)

# Resume a paused job
job_manager.resume_job(job_id)

# Cancel a job
job_manager.cancel_job(job_id)

# Delete a job
job_manager.delete_job(job_id)
```

### Job Dependencies

```python
# Create jobs with dependencies
first_job = job_manager.create_job(
    name="Extract Data",
    description="Extract data from source system",
    payload={"source": "api"}
)

# This job depends on the first job
second_job = job_manager.create_job(
    name="Transform Data",
    description="Transform extracted data",
    payload={"transformation": "normalize"},
    dependencies=[first_job.job_id],
    auto_start=True  # Will automatically start when dependencies complete
)

# This job depends on the second job
third_job = job_manager.create_job(
    name="Load Data",
    description="Load processed data to target",
    payload={"target": "database"},
    dependencies=[second_job.job_id],
    auto_start=True
)

# Start the first job - others will start automatically when their dependencies complete
job_manager.start_job(first_job.job_id)

# Add a dependency between existing jobs
job_manager.add_job_dependency(job_id=third_job.job_id, depends_on_id=first_job.job_id)

# Remove a dependency
job_manager.remove_job_dependency(job_id=third_job.job_id, depends_on_id=first_job.job_id)

# Get all dependencies for a job
dependencies = job_manager.get_dependencies(third_job.job_id)

# Get all jobs that depend on a specific job
dependent_jobs = job_manager.get_dependent_jobs(first_job.job_id)
```

### Batch Job Operations

```python
# Create a batch of related jobs
batch_id, jobs = job_manager.create_job_batch([
    {
        "name": "Process Region 1",
        "payload": {"region": "europe"},
        "tags": ["batch", "region"]
    },
    {
        "name": "Process Region 2", 
        "payload": {"region": "asia"},
        "tags": ["batch", "region"]
    },
    {
        "name": "Process Region 3",
        "payload": {"region": "americas"},
        "tags": ["batch", "region"]
    },
    {
        "name": "Combine Results",
        "payload": {"operation": "combine"},
        "dependencies": [0, 1, 2],  # Depends on the first three jobs in the batch
        "tags": ["batch", "aggregate"]
    }
], auto_start=True)

# Get all jobs in a batch
batch_jobs = job_manager.get_batch_jobs(batch_id)
```

### Cleanup Old Jobs

```python
# Clean up jobs older than the retention period
deleted_count = job_manager.cleanup_old_jobs()
print(f"Cleaned up {deleted_count} old jobs")
```

## Job States

Jobs can exist in the following states:

- **PENDING**: Job has been created and is waiting to run
- **RUNNING**: Job is currently executing
- **PAUSED**: Job execution has been paused
- **COMPLETED**: Job has completed successfully
- **FAILED**: Job has failed during execution
- **CANCELLED**: Job has been cancelled

## Job Priorities

Jobs can be assigned one of the following priorities:

- **LOW**: Lower priority than normal jobs
- **MEDIUM**: Default priority level
- **HIGH**: Higher priority than normal jobs
- **CRITICAL**: Highest priority, executed immediately when possible

## Retry Mechanism

Jobs can be configured with retry settings:

```python
job = job_manager.create_job(
    name="API Data Fetch",
    payload={"url": "https://api.example.com/data"},
    max_retries=3,        # Number of retry attempts
    retry_delay=60,       # Seconds between retries
    timeout=300           # Maximum execution time in seconds
)
```

## Customization

The job management system is designed to be extensible. You can:

1. Create custom storage backends by implementing the `JobStore` interface
2. Extend the `JobManager` class to customize job execution behavior
3. Add additional fields to job metadata as needed

## Integration with OpenAgentsApp

The JobManager is integrated with the main `OpenAgentsApp` class:

```python
from openagents_json import OpenAgentsApp

app = OpenAgentsApp()

# Create and manage jobs through the app interface
job = await app.create_job(
    name="Process data", 
    payload={"source": "s3://bucket/file.csv"}
)
status = await app.get_job_status(job["job_id"])
results = await app.get_job_results(job["job_id"])
``` 