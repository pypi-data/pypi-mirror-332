"""
Tests for the job manager functionality.
"""

import asyncio

import pytest

from openagents_json import OpenAgentsApp


@pytest.mark.asyncio
async def test_job_creation():
    """Test creating a job with the job manager."""
    agents_app = OpenAgentsApp()

    # Register a test workflow
    agents_app.register_workflow(
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
    job = await agents_app.create_job(
        workflow_id="test-workflow", inputs={"value": "test_value"}
    )

    # Check that the job was created
    assert job["id"] is not None
    assert job["workflow_id"] == "test-workflow"
    assert job["inputs"] == {"value": "test_value"}
    assert job["status"] == "CREATED"


@pytest.mark.asyncio
async def test_job_status():
    """Test retrieving job status."""
    agents_app = OpenAgentsApp()

    # Register a test workflow
    agents_app.register_workflow(
        {
            "id": "test-workflow",
            "description": "A test workflow",
            "steps": [],
            "output": {},
        }
    )

    # Create a job
    job = await agents_app.create_job(workflow_id="test-workflow", inputs={})

    # Get job status
    status = await agents_app.get_job_status(job["id"])

    # Check that the status was retrieved
    assert status["id"] == job["id"]
    assert status["status"] == "CREATED"


@pytest.mark.asyncio
async def test_job_results():
    """Test retrieving job results."""
    agents_app = OpenAgentsApp()

    # Register a test workflow
    agents_app.register_workflow(
        {
            "id": "test-workflow",
            "description": "A test workflow",
            "steps": [],
            "output": {},
        }
    )

    # Create a job
    job = await agents_app.create_job(workflow_id="test-workflow", inputs={})

    # Manually set the job to completed with results
    job_id = job["id"]
    job_obj = agents_app.job_manager.jobs[job_id]
    job_obj["status"] = "COMPLETED"
    job_obj["outputs"] = {"result": "test_result"}

    # Get job results
    results = await agents_app.get_job_results(job_id)

    # Check that the results were retrieved
    assert results["id"] == job_id
    assert results["outputs"] == {"result": "test_result"}


@pytest.mark.asyncio
async def test_job_results_not_completed():
    """Test that retrieving results of a non-completed job raises an error."""
    agents_app = OpenAgentsApp()

    # Register a test workflow
    agents_app.register_workflow(
        {
            "id": "test-workflow",
            "description": "A test workflow",
            "steps": [],
            "output": {},
        }
    )

    # Create a job
    job = await agents_app.create_job(workflow_id="test-workflow", inputs={})

    # Try to get results of non-completed job
    with pytest.raises(ValueError, match=f"Job {job['id']} is not completed"):
        await agents_app.get_job_results(job["id"])


@pytest.mark.asyncio
async def test_job_not_found():
    """Test that retrieving a non-existent job raises an error."""
    agents_app = OpenAgentsApp()

    # Try to get status of non-existent job
    with pytest.raises(ValueError, match="Job non_existent_job not found"):
        await agents_app.get_job_status("non_existent_job")

    # Try to get results of non-existent job
    with pytest.raises(ValueError, match="Job non_existent_job not found"):
        await agents_app.get_job_results("non_existent_job")
