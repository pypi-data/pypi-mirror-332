# Monitoring and Observability

OpenAgents JSON provides comprehensive monitoring and observability features through an event system and metrics collection. These features help you track job execution, worker performance, and overall system health.

## Event System

The event system enables components to publish and subscribe to job lifecycle events, creating a flexible foundation for building observability features and custom integrations.

### Key Components

- **`Event`**: Data structure representing a system event with type, timestamp, and associated data
- **`EventType`**: Enumeration of possible event types
- **`event_emitter`**: Global event emitter instance for publishing and subscribing to events

### Event Types

The system defines the following event types:

**Job Lifecycle Events:**
- `JOB_CREATED`: Job has been created
- `JOB_QUEUED`: Job has been queued for execution 
- `JOB_STARTED`: Job execution has started
- `JOB_PAUSED`: Job has been paused
- `JOB_RESUMED`: Job has been resumed
- `JOB_COMPLETED`: Job has completed successfully
- `JOB_FAILED`: Job has failed
- `JOB_CANCELLED`: Job has been cancelled
- `JOB_RETRYING`: Job failed and is being retried
- `JOB_PROGRESS_UPDATED`: Job progress has been updated

**Worker Events:**
- `WORKER_REGISTERED`: Worker has registered with the system
- `WORKER_HEARTBEAT`: Worker has sent a heartbeat
- `WORKER_CLAIMED_JOB`: Worker has claimed a job
- `WORKER_OFFLINE`: Worker has gone offline

**System Events:**
- `SYSTEM_STARTUP`: System has started
- `SYSTEM_SHUTDOWN`: System is shutting down
- `SYSTEM_ERROR`: System error has occurred

### Usage Examples

**Subscribing to Events:**

```python
from openagents_json.job import event_emitter, EventType, Event

# Subscribe to specific event type
def on_job_completed(event: Event):
    print(f"Job {event.job_id} completed with result: {event.data.get('result')}")

event_emitter.on(EventType.JOB_COMPLETED, on_job_completed)

# Subscribe to all events
def log_all_events(event: Event):
    print(f"Event: {event.event_type.value}, Job ID: {event.job_id}")

event_emitter.on_any(log_all_events)
```

**Publishing Events:**

```python
from openagents_json.job import event_emitter, EventType, Event

# Create and emit an event
event = Event(
    event_type=EventType.SYSTEM_ERROR,
    data={"message": "Database connection failed"}
)
event_emitter.emit(event)

# Create an event from a job
job = job_manager.get_job("job-123")
event = Event.from_job(
    event_type=EventType.JOB_PROGRESS_UPDATED,
    job=job,
    progress=75
)
event_emitter.emit(event)
```

**Asynchronous Event Handlers:**

```python
import asyncio
from openagents_json.job import event_emitter, EventType

async def async_handler(event):
    await asyncio.sleep(1)  # Simulate async work
    print(f"Processed event: {event.event_type}")

# Register async handler
await event_emitter.on_async(EventType.JOB_COMPLETED, async_handler)

# Emit event to async handlers
await event_emitter.emit_async(event)
```

## Monitoring System

The monitoring system collects and provides access to metrics about job execution, worker performance, and system health.

### Key Components

- **`JobMetrics`**: Collects metrics for job execution (success rates, execution times, etc.)
- **`WorkerMetrics`**: Collects metrics for worker performance (claim rates, heartbeats, etc.)
- **`SystemMetrics`**: Collects system-wide metrics (queue depth, event counts, etc.)
- **`Monitor`**: Central monitoring system integrating all metrics collectors
- **`monitor`**: Global monitor instance

### Usage Examples

**Accessing Metrics:**

```python
from openagents_json.job import monitor

# Get complete system status
status = monitor.get_complete_status()

# Get job metrics summary
job_summary = monitor.job_metrics.get_summary()
print(f"Success rate: {job_summary['success_rate']}%")
print(f"Average execution time: {job_summary['avg_execution_time']}s")

# Get worker status
worker = monitor.worker_metrics.get_worker_status("worker-123")
print(f"Worker status: {worker['status']}")
print(f"Jobs claimed: {worker['jobs_claimed']}")

# Get recent job executions
recent_jobs = monitor.job_metrics.get_recent_jobs(limit=5)
for job in recent_jobs:
    print(f"Job {job['job_id']}: {job['status']} in {job['execution_time']}s")

# Get event counts
event_counts = monitor.system_metrics.get_event_counts()
print(f"Failed jobs: {event_counts['job.failed']}")
```

**Updating Metrics:**

```python
# Update queue depth in monitoring
queue_size = len(job_manager.job_store.get_jobs(status=JobStatus.QUEUED))
monitor.update_queue_depth(queue_size)
```

**Resetting Metrics:**

```python
# Reset all metrics
monitor.reset()

# Reset specific metrics collector
monitor.job_metrics.reset()
```

## REST API for Monitoring

A FastAPI-based REST API provides easy access to monitoring data for integration with dashboards, monitoring tools, or custom UIs.

### Setup

```python
from openagents_json.job.monitoring_api import monitoring_app
import uvicorn

# Run the monitoring API
uvicorn.run(monitoring_app, host="0.0.0.0", port=8000)
```

### Available Endpoints

- **`GET /`**: Root endpoint with API information
- **`GET /status`**: Complete system status with all metrics
- **`GET /jobs/summary`**: Summary of job metrics
- **`GET /jobs/recent`**: Recent job executions
- **`GET /jobs/tags`**: Metrics grouped by job tags
- **`GET /jobs/priorities`**: Metrics grouped by job priority
- **`GET /workers`**: Status information for all workers
- **`GET /workers/{worker_id}`**: Status information for a specific worker
- **`GET /system`**: System-wide metrics
- **`GET /system/events`**: Counts of all events by type
- **`POST /system/reset`**: Reset all metrics collectors
- **`POST /system/enable`**: Enable metrics collection
- **`POST /system/disable`**: Disable metrics collection

### Example Usage with cURL

```bash
# Get complete system status
curl http://localhost:8000/status

# Get recent jobs
curl http://localhost:8000/jobs/recent?limit=5

# Get metrics for a specific worker
curl http://localhost:8000/workers/worker-123

# Reset all metrics
curl -X POST http://localhost:8000/system/reset
```

## Complete Example

See the `examples/job_monitoring.py` file for a complete demonstration of the event system and monitoring capabilities. This example creates jobs with various characteristics (successful, failing, retrying) and shows how to set up event handlers and run the monitoring API. 