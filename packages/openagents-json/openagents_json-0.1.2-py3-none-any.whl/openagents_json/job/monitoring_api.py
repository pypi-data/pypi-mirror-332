"""
REST API for job monitoring in the OpenAgents JSON framework.

This module provides a FastAPI-based REST API for accessing monitoring and
observability data from the job system. The API exposes endpoints for retrieving
job metrics, worker status, and system health information.
"""

import json
import logging
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from openagents_json.job.events import EventType
from openagents_json.job.monitoring import monitor

logger = logging.getLogger(__name__)

# Create FastAPI app
monitoring_app = FastAPI(
    title="OpenAgents JSON Monitoring API",
    description="API for monitoring job execution and system health",
    version="1.0.0",
)

# Add CORS middleware
monitoring_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production use
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@monitoring_app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "name": "OpenAgents JSON Monitoring API",
        "version": "1.0.0",
        "description": "API for monitoring job execution and system health",
    }


@monitoring_app.get("/status", tags=["System"])
async def get_status():
    """Get complete system status with all metrics."""
    try:
        return monitor.get_complete_status()
    except Exception as e:
        logger.error(f"Error getting system status: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting system status: {str(e)}"
        )


@monitoring_app.get("/jobs/summary", tags=["Jobs"])
async def get_job_summary():
    """Get summary of job metrics."""
    try:
        return monitor.job_metrics.get_summary()
    except Exception as e:
        logger.error(f"Error getting job summary: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting job summary: {str(e)}"
        )


@monitoring_app.get("/jobs/recent", tags=["Jobs"])
async def get_recent_jobs(limit: int = Query(10, ge=1, le=100)):
    """
    Get recent job executions.

    Args:
        limit: Maximum number of recent jobs to return
    """
    try:
        return monitor.job_metrics.get_recent_jobs(limit=limit)
    except Exception as e:
        logger.error(f"Error getting recent jobs: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting recent jobs: {str(e)}"
        )


@monitoring_app.get("/jobs/tags", tags=["Jobs"])
async def get_job_tag_metrics():
    """Get metrics grouped by job tags."""
    try:
        return monitor.job_metrics.get_tag_metrics()
    except Exception as e:
        logger.error(f"Error getting job tag metrics: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting job tag metrics: {str(e)}"
        )


@monitoring_app.get("/jobs/priorities", tags=["Jobs"])
async def get_job_priority_metrics():
    """Get metrics grouped by job priority."""
    try:
        return monitor.job_metrics.get_priority_metrics()
    except Exception as e:
        logger.error(f"Error getting job priority metrics: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting job priority metrics: {str(e)}"
        )


@monitoring_app.get("/workers", tags=["Workers"])
async def get_all_workers():
    """Get status information for all workers."""
    try:
        return {
            "active_count": monitor.worker_metrics.get_active_workers_count(),
            "workers": monitor.worker_metrics.get_all_workers(),
        }
    except Exception as e:
        logger.error(f"Error getting all workers: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting all workers: {str(e)}"
        )


@monitoring_app.get("/workers/{worker_id}", tags=["Workers"])
async def get_worker_status(worker_id: str):
    """
    Get status information for a specific worker.

    Args:
        worker_id: ID of the worker to retrieve
    """
    try:
        worker_status = monitor.worker_metrics.get_worker_status(worker_id)
        if not worker_status:
            raise HTTPException(status_code=404, detail=f"Worker {worker_id} not found")
        return worker_status
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting worker {worker_id} status: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting worker status: {str(e)}"
        )


@monitoring_app.get("/system", tags=["System"])
async def get_system_metrics():
    """Get system-wide metrics."""
    try:
        return monitor.system_metrics.get_system_metrics()
    except Exception as e:
        logger.error(f"Error getting system metrics: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting system metrics: {str(e)}"
        )


@monitoring_app.get("/system/events", tags=["System"])
async def get_event_counts():
    """Get counts of all events by type."""
    try:
        return monitor.system_metrics.get_event_counts()
    except Exception as e:
        logger.error(f"Error getting event counts: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error getting event counts: {str(e)}"
        )


@monitoring_app.post("/system/reset", tags=["System"])
async def reset_metrics():
    """Reset all metrics collectors."""
    try:
        monitor.reset()
        return {"status": "success", "message": "All metrics have been reset"}
    except Exception as e:
        logger.error(f"Error resetting metrics: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error resetting metrics: {str(e)}"
        )


@monitoring_app.post("/system/enable", tags=["System"])
async def enable_monitoring():
    """Enable metrics collection."""
    try:
        monitor.enable()
        return {"status": "success", "message": "Monitoring enabled"}
    except Exception as e:
        logger.error(f"Error enabling monitoring: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error enabling monitoring: {str(e)}"
        )


@monitoring_app.post("/system/disable", tags=["System"])
async def disable_monitoring():
    """Disable metrics collection."""
    try:
        monitor.disable()
        return {"status": "success", "message": "Monitoring disabled"}
    except Exception as e:
        logger.error(f"Error disabling monitoring: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error disabling monitoring: {str(e)}"
        )


def get_app():
    """Get the FastAPI application instance."""
    return monitoring_app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(monitoring_app, host="127.0.0.1", port=8000)
