# Execution Control

The OpenAgents JSON framework provides advanced execution control features, enabling reliable job processing with automatic retries and distributed execution across multiple workers. This document explains the retry policy system and distributed execution capabilities in detail.

## Retry Policies

Retry policies define how failed jobs are retried, allowing for sophisticated error handling strategies with configurable delays.

### Overview

The framework includes a flexible retry policy system with:

- Abstract base class (`RetryPolicy`) for creating custom policies
- Standard implementations for common retry strategies
- Support for delay calculation with optional jitter to avoid thundering herd problems
- Serialization and deserialization for persistent storage

### Available Retry Policies

#### Fixed Delay

The `FixedDelayRetryPolicy` applies a consistent wait time between retry attempts:

```python
from openagents_json.job import Job, FixedDelayRetryPolicy

job = Job(
    name="Process Image Batch",
    payload={"batch_id": "12345"},
    max_retries=3,
    retry_policy=FixedDelayRetryPolicy(
        delay=10,    # 10 seconds between retries
        jitter=0.2   # Add ±20% randomness to avoid thundering herd
    )
)
```

Parameters:
- `delay`: Number of seconds to wait between retries (default: 30 seconds)
- `jitter`: Random factor to apply to delay (0-1, default: 0)

#### Exponential Backoff

The `ExponentialBackoffRetryPolicy` increases the delay exponentially with each attempt, ideal for external service calls:

```python
from openagents_json.job import Job, ExponentialBackoffRetryPolicy

job = Job(
    name="External API Request",
    payload={"request_data": {...}},
    max_retries=5,
    retry_policy=ExponentialBackoffRetryPolicy(
        initial_delay=1,   # Start with 1 second
        max_delay=300,     # Cap at 5 minutes
        multiplier=2,      # Double the delay each time
        jitter=0.3         # Add ±30% randomness
    )
)
```

Parameters:
- `initial_delay`: Starting delay in seconds (default: 5 seconds)
- `max_delay`: Maximum delay between retries (default: 300 seconds)
- `multiplier`: Factor to increase delay by each attempt (default: 2)
- `jitter`: Random factor to apply to delay (0-1, default: 0)

### Custom Retry Policies

You can create custom retry policies by extending the `RetryPolicy` abstract base class:

```python
from openagents_json.job.retry import RetryPolicy

class CustomRetryPolicy(RetryPolicy):
    def __init__(self, custom_param=30):
        self.custom_param = custom_param
        
    def get_retry_delay(self, attempt, max_retries):
        # Custom logic to calculate delay
        return min(self.custom_param * (attempt * 0.5), 60)
        
    def to_dict(self):
        return {
            "type": "custom",
            "custom_param": self.custom_param
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(custom_param=data.get("custom_param", 30))
```

## Distributed Execution

The distributed execution system allows jobs to be processed by multiple worker processes, potentially running on different machines, for improved throughput and reliability.

### Architecture

The distributed execution system consists of:

1. **Workers**: Processes that claim and execute jobs
2. **Worker Manager**: Coordinates workers and handles failure detection
3. **Job Store**: Shared storage for jobs and worker state
4. **Job Manager**: Orchestrates the overall job lifecycle

### Worker Model

Workers operate independently and communicate through the shared job store:

```python
from openagents_json.job import Worker

worker = Worker(
    job_store=job_store,
    heartbeat_interval=60,        # Seconds between heartbeats
    job_claim_batch_size=5,       # Number of jobs to claim at once
    max_concurrent_jobs=10,       # Maximum jobs to run in parallel
    tags=["image-processing"],    # Job tags this worker handles
    executor=custom_executor      # Optional custom execution function
)

await worker.start()  # Start the worker in the background
```

Each worker:
1. Registers itself in the job store
2. Sends periodic heartbeats to indicate it's alive
3. Claims available jobs matching its tags
4. Executes jobs concurrently up to its capacity
5. Reports job completion or failure

### Worker Manager

The `WorkerManager` monitors worker health and handles failures:

```python
from openagents_json.job import WorkerManager

worker_manager = WorkerManager(
    job_store=job_store,
    heartbeat_timeout=120,    # Seconds before a worker is considered dead
    check_interval=60         # Seconds between health checks
)

await worker_manager.start()  # Start the manager in the background
```

The manager:
1. Periodically checks worker heartbeats
2. Detects dead workers (those that haven't sent a heartbeat)
3. Resets jobs from dead workers back to pending status
4. Logs worker failure information for troubleshooting

### Job Tagging and Routing

Tags provide a flexible mechanism for routing jobs to appropriate workers:

```python
# Create jobs with specific tags
job = Job(
    name="Process Image",
    payload={"image_url": "https://example.com/image.jpg"},
    tags=["image-processing", "high-memory"]
)

# Create workers for specific job types
image_worker = Worker(
    job_store=job_store,
    tags=["image-processing", "high-memory"],
    max_concurrent_jobs=2  # Limit concurrent jobs for resource-intensive work
)

general_worker = Worker(
    job_store=job_store,
    tags=["default"],  # Handle general-purpose jobs
    max_concurrent_jobs=20
)
```

Jobs will be routed to workers that match ALL of their tags. If a job has no tags, any worker can claim it.

### Custom Job Execution

Workers can use a custom executor function to handle job execution:

```python
async def custom_executor(job: Job) -> Any:
    """Custom job execution logic based on job payload."""
    if job.payload.get("type") == "image":
        return await process_image(job.payload["url"])
    elif job.payload.get("type") == "text":
        return await analyze_text(job.payload["content"])
    else:
        raise ValueError(f"Unknown job type: {job.payload.get('type')}")

worker = Worker(
    job_store=job_store,
    executor=custom_executor
)
```

This allows for flexible job dispatching based on payload content or other factors.

### Scaling Considerations

For optimal performance when scaling distributed execution:

1. **Database Connection Pooling**: Configure appropriate connection pool sizes
2. **Worker Tags**: Use tags to distribute workload by job type or resource requirements
3. **Heartbeat Intervals**: Adjust based on job duration and system responsiveness
4. **Concurrent Jobs**: Set based on available CPU cores and memory
5. **Job Claim Batch Size**: Larger batches reduce database load but may cause uneven distribution

For very large deployments, consider:
- Sharding the job store by job type or other criteria
- Implementing a dedicated worker orchestration service
- Using a message queue for job distribution

## Complete Example

Here's a complete example demonstrating both retry policies and distributed execution:

```python
import asyncio
from openagents_json.job import (
    Job, JobManager, SQLAlchemyJobStore,
    Worker, WorkerManager,
    ExponentialBackoffRetryPolicy
)

async def main():
    # Create a shared SQLite job store
    job_store = SQLAlchemyJobStore(
        dialect="sqlite",
        path="jobs.db"
    )
    
    # Create a job manager in distributed mode
    manager = JobManager(
        job_store=job_store,
        distributed_mode=True
    )
    
    # Start worker manager
    worker_manager = WorkerManager(job_store=job_store)
    await worker_manager.start()
    
    # Define a custom executor function
    async def execute_job(job: Job):
        job_type = job.payload.get("type")
        print(f"Executing job {job.job_id} of type {job_type}")
        
        # Simulate processing
        if job_type == "api_call" and job.retry_count < 2:
            # Simulate a transient failure that will be retried
            raise ConnectionError("API temporarily unavailable")
        
        await asyncio.sleep(1)  # Simulate work
        return {"success": True, "processed_at": job.started_at}
    
    # Start workers with different capabilities
    workers = []
    for i in range(3):
        worker = Worker(
            job_store=job_store,
            worker_id=f"worker-{i}",
            tags=["api"] if i == 0 else ["default"],
            max_concurrent_jobs=5,
            executor=execute_job
        )
        workers.append(worker)
        await worker.start()
    
    # Create jobs with retry policies
    jobs = []
    for i in range(10):
        is_api_job = i % 3 == 0
        job = Job(
            name=f"Job {i}",
            payload={
                "type": "api_call" if is_api_job else "processing",
                "data": f"data-{i}"
            },
            max_retries=3 if is_api_job else 0,
            retry_policy=ExponentialBackoffRetryPolicy(
                initial_delay=0.5,
                max_delay=5,
                jitter=0.2
            ) if is_api_job else None,
            tags=["api"] if is_api_job else []
        )
        job_store.save(job)
        jobs.append(job)
    
    # Monitor job progress
    pending_jobs = len(jobs)
    while pending_jobs > 0:
        pending_jobs = 0
        for job in jobs:
            updated_job = job_store.get(job.job_id)
            if updated_job.status not in ("completed", "failed", "cancelled"):
                pending_jobs += 1
        
        print(f"Pending jobs: {pending_jobs}")
        await asyncio.sleep(1)
    
    # Cleanup
    for worker in workers:
        await worker.stop()
    await worker_manager.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

## Best Practices

### Retry Policies

1. **Match retry policy to failure type**: Use fixed delay for consistent operations, exponential backoff for external services
2. **Add jitter to prevent thundering herd**: Always use some jitter (0.1-0.3) for retried operations
3. **Set reasonable max_retries**: Too many retries waste resources, too few reduce reliability
4. **Cap max_delay reasonably**: Typically 5-15 minutes is sufficient for most operations

### Distributed Execution

1. **Worker specialization**: Use tags to route jobs to specialized workers
2. **Resource allocation**: Set max_concurrent_jobs based on available resources
3. **Heartbeat monitoring**: Set heartbeat_interval to approximately 1/3 of heartbeat_timeout
4. **Connection management**: Close database connections when workers shut down
5. **Error handling**: Implement comprehensive error handling in custom executors

## Troubleshooting

### Retry Issues

- **Jobs not retrying**: Check max_retries > 0 and retry_policy is properly configured
- **Retry delays too long/short**: Adjust policy parameters (delay, initial_delay, max_delay)
- **Erratic retry timing**: Reduce jitter factor or check for clock synchronization issues

### Worker Issues

- **Workers not claiming jobs**: Check tags match between jobs and workers
- **Dead worker detection**: Verify heartbeat_timeout and check_interval in WorkerManager
- **Database contention**: Reduce frequency of job claiming or increase batch size
- **Executor failures**: Add more detailed error handling and logging in custom executors

## Integration with External Systems

The execution control system can be integrated with external systems:

- **Monitoring tools**: Implement custom metrics collection in workers
- **Distributed tracing**: Add trace context to job payload for end-to-end tracing
- **Load balancers**: Use worker tags to implement service-specific worker pools
- **Cloud autoscaling**: Adjust worker count based on job queue depth 