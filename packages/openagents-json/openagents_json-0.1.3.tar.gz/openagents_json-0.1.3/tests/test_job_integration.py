"""
Integration tests for the JobManager with the OpenAgentsApp.

These tests verify that the JobManager works correctly with the
main application class.
"""

import asyncio
from typing import Any, Dict

import pytest

from openagents_json import OpenAgentsApp
from openagents_json.job.model import JobStatus


@pytest.mark.asyncio
async def test_app_job_creation():
    """Test creating a job through the main application."""
    app = OpenAgentsApp()

    # Register a test workflow
    app.register_workflow(
        {
            "id": "test-workflow",
            "description": "A test workflow",
            "steps": [
                {
                    "id": "step1",
                    "component": "test_component",
                    "inputs": {"input1": "{{input.value}}"},
                }
            ],
            "output": {"result": "{{step1.output}}"},
        }
    )

    # Create a job
    job = await app.create_job(
        workflow_id="test-workflow", inputs={"value": "test_value"}
    )

    # Check that the job was created
    assert job.get("job_id") is not None
    assert job.get("workflow_id") == "test-workflow"
    assert job.get("inputs") == {"value": "test_value"}
    assert job.get("status") == JobStatus.CREATED.value


@pytest.mark.asyncio
async def test_app_job_execution():
    """Test executing a job through the main application."""
    app = OpenAgentsApp()

    # Register a simple test workflow
    app.register_workflow(
        {
            "id": "simple-workflow",
            "description": "A simple workflow",
            "steps": [],
            "output": {"result": "predefined_result"},
        }
    )

    # Create and start a job
    job = await app.create_job(
        workflow_id="simple-workflow", inputs={}, auto_start=True
    )

    job_id = job.get("job_id")

    # Wait for the job to complete
    max_wait = 10  # seconds
    for _ in range(max_wait * 2):
        status = await app.get_job_status(job_id)
        if status.get("status") == JobStatus.COMPLETED.value:
            break
        await asyncio.sleep(0.5)
    else:
        pytest.fail(f"Job did not complete within {max_wait} seconds")

    # Get the results
    results = await app.get_job_results(job_id)

    # Check the results
    assert results.get("job_id") == job_id
    assert "result" in results.get("outputs", {})
