#!/usr/bin/env python3
"""
Example demonstrating the event system and monitoring features of the job system.

This example shows how to:
- Create custom event handlers for job events
- Run the monitoring API
- View real-time job execution metrics
"""

import asyncio
import json
import logging
import time
from datetime import datetime
from typing import Dict, Any

from openagents_json.job import (
    JobManager, 
    Job, 
    JobStatus, 
    JobPriority,
    Event, 
    EventType, 
    event_emitter, 
    monitor
)
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from openagents_json.job.monitoring_api import monitoring_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global variables for statistics
event_counts: Dict[str, int] = {}
start_time = datetime.now()


def setup_event_handlers():
    """Set up custom event handlers for demonstrations."""
    
    # Handler for all events that counts event occurrences
    def count_event(event: Event):
        event_type = event.event_type.value
        if event_type not in event_counts:
            event_counts[event_type] = 0
        event_counts[event_type] += 1
        
        logger.debug(f"Event received: {event_type}")
    
    # Register the event counter for all events
    event_emitter.on_any(count_event)
    
    # Handler for specific job completion events
    def on_job_completed(event: Event):
        job_id = event.job_id
        execution_time = event.data.get('completed_at', '') 
        created_at = event.data.get('created_at', '')
        
        logger.info(f"🎉 Job {job_id} completed successfully!")
        logger.info(f"  - Created: {created_at}")
        logger.info(f"  - Completed: {execution_time}")
        logger.info(f"  - Result: {json.dumps(event.data.get('result', {}), indent=2)}")
    
    # Register the completion handler for job completion events
    event_emitter.on(EventType.JOB_COMPLETED, on_job_completed)
    
    # Handler for job failure events
    def on_job_failed(event: Event):
        job_id = event.job_id
        error = event.data.get('error', {})
        
        logger.error(f"❌ Job {job_id} failed!")
        logger.error(f"  - Error: {error.get('message', 'Unknown error')}")
        logger.error(f"  - Type: {error.get('type', 'Unknown')}")
    
    # Register the failure handler for job failure events
    event_emitter.on(EventType.JOB_FAILED, on_job_failed)


async def simulate_jobs(job_manager: JobManager):
    """
    Simulate various job scenarios to demonstrate events and monitoring.
    
    Args:
        job_manager: JobManager instance
    """
    # Create and run successful jobs
    logger.info("Creating successful jobs...")
    for i in range(5):
        job = job_manager.create_job(
            name=f"Successful Job {i+1}",
            description="A job that completes successfully",
            priority=JobPriority.MEDIUM,
            tags=["demo", "success"],
            auto_start=True
        )
        logger.info(f"Created job: {job.job_id}")
        await asyncio.sleep(0.5)  # Space out job creation
    
    # Create some jobs with different priorities
    logger.info("Creating jobs with different priorities...")
    priorities = [
        (JobPriority.LOW, "Low"),
        (JobPriority.MEDIUM, "Medium"),
        (JobPriority.HIGH, "High"),
        (JobPriority.CRITICAL, "Critical")
    ]
    
    for priority, name in priorities:
        job = job_manager.create_job(
            name=f"{name} Priority Job",
            description=f"A job with {name.lower()} priority",
            priority=priority,
            tags=["demo", "priority", name.lower()],
            auto_start=True
        )
        logger.info(f"Created {name} priority job: {job.job_id}")
        await asyncio.sleep(0.5)
    
    # Create a job that fails
    logger.info("Creating a failing job...")
    failing_job = job_manager.create_job(
        name="Failing Job",
        description="A job that will fail",
        priority=JobPriority.HIGH,
        tags=["demo", "failure"],
        auto_start=False
    )
    
    # Manually update the job to force a failure
    async def fail_job():
        await asyncio.sleep(2)  # Wait for a moment
        job = job_manager.get_job(failing_job.job_id)
        if job:
            job.set_error(Exception("Simulated failure for demonstration"))
            job.update_status(JobStatus.FAILED)
            job_manager.job_store.update_job(job)
    
    # Start the failing job and the failure simulator
    job_manager.start_job(failing_job.job_id)
    asyncio.create_task(fail_job())
    
    # Create a job with retries
    logger.info("Creating a job with retries...")
    retry_job = job_manager.create_job(
        name="Retry Job",
        description="A job that will retry after failing",
        priority=JobPriority.MEDIUM,
        max_retries=2,
        retry_delay=1,
        tags=["demo", "retry"],
        auto_start=False
    )
    
    # Manually update the job to simulate retries
    async def retry_job_sequence():
        await asyncio.sleep(2)  # Wait for a moment
        
        # First failure
        job = job_manager.get_job(retry_job.job_id)
        if job:
            job.set_error(Exception("First failure, will retry"))
            job.update_status(JobStatus.FAILED)
            job.retry_count += 1
            job_manager.job_store.update_job(job)
            
            # Emit retry event
            event_emitter.emit(Event.from_job(
                event_type=EventType.JOB_RETRYING,
                job=job,
                retry_count=job.retry_count,
                max_retries=job.max_retries,
                retry_delay=job.retry_delay
            ))
            
            logger.info(f"Job {job.job_id} failed, retrying (1/{job.max_retries})")
            
            # Wait for retry delay
            await asyncio.sleep(job.retry_delay + 1)
            
            # Simulate retry by restarting
            job_manager.start_job(job.job_id)
            
            # Second failure
            await asyncio.sleep(2)
            job = job_manager.get_job(retry_job.job_id)
            if job:
                job.set_error(Exception("Second failure, will retry"))
                job.update_status(JobStatus.FAILED)
                job.retry_count += 1
                job_manager.job_store.update_job(job)
                
                # Emit retry event
                event_emitter.emit(Event.from_job(
                    event_type=EventType.JOB_RETRYING,
                    job=job,
                    retry_count=job.retry_count,
                    max_retries=job.max_retries,
                    retry_delay=job.retry_delay
                ))
                
                logger.info(f"Job {job.job_id} failed, retrying (2/{job.max_retries})")
                
                # Wait for retry delay
                await asyncio.sleep(job.retry_delay + 1)
                
                # Simulate retry by restarting
                job_manager.start_job(job.job_id)
                
                # This time succeed
                await asyncio.sleep(2)
                job = job_manager.get_job(job.job_id)
                if job:
                    job.result = {"status": "success", "message": "Succeeded after retries"}
                    job.update_status(JobStatus.COMPLETED)
                    job.completed_at = datetime.now()
                    job_manager.job_store.update_job(job)
                    
                    # Emit completion event
                    event_emitter.emit(Event.from_job(
                        event_type=EventType.JOB_COMPLETED,
                        job=job,
                        result=job.result
                    ))
                    
                    logger.info(f"Job {job.job_id} succeeded after {job.retry_count} retries")
    
    # Start the retry job and the retry simulator
    job_manager.start_job(retry_job.job_id)
    asyncio.create_task(retry_job_sequence())
    
    # Keep the example running to see API endpoints and events
    logger.info("Jobs created. Monitoring API is now running.")
    logger.info("📊 View metrics at http://localhost:8000/")
    
    # Update queue depth for monitoring
    monitor.update_queue_depth(len(job_manager.job_store.get_jobs(status=JobStatus.QUEUED)))
    
    # Keep the demo running
    while True:
        # Print summary every 10 seconds
        await asyncio.sleep(10)
        
        runtime = datetime.now() - start_time
        logger.info(f"📈 Demo running for {runtime.seconds} seconds")
        logger.info(f"📊 Event counts: {json.dumps(event_counts, indent=2)}")
        
        # Update queue depth
        monitor.update_queue_depth(len(job_manager.job_store.get_jobs(status=JobStatus.QUEUED)))


async def main():
    """Main entry point for the example."""
    # Initialize JobManager
    job_manager = JobManager()
    
    # Set up event handlers
    setup_event_handlers()
    
    # Mount FastAPI monitoring app to serve metrics
    app = FastAPI(
        title="OpenAgents JSON Job Monitoring Demo",
        description="Demo showcasing job events and monitoring",
        version="1.0.0"
    )
    
    # Add a redirect from the root to the monitoring API docs
    @app.get("/")
    async def root():
        return RedirectResponse(url="/docs")
    
    # Mount the monitoring API
    app.mount("/api", monitoring_app)
    
    # Mount static files for the demo UI (if available)
    try:
        app.mount("/ui", StaticFiles(directory="static", html=True), name="ui")
    except:
        logger.warning("Static UI directory not found, /ui endpoint will not be available")
    
    # Serve the API
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    
    # Run the job simulator and API server concurrently
    await asyncio.gather(
        simulate_jobs(job_manager),
        server.serve()
    )


if __name__ == "__main__":
    # Start the demo
    asyncio.run(main()) 