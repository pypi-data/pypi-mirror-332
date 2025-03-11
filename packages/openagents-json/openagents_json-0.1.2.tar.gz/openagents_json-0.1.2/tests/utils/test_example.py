"""
Example tests demonstrating how to use the testing utilities.

This file serves as documentation on how to use the various testing
utilities provided by the OpenAgents JSON testing framework.
"""

import asyncio

import pytest

from openagents_json import OpenAgentsApp
from tests.utils import (
    MockAgentClient,
    MockJobCallback,
    assert_json_structure,
    compare_dict_paths,
    create_test_agent,
    create_test_workflow,
)


# Agent Testing Example
def test_agent_with_utils():
    """Example of testing an agent using the testing utilities."""
    app = OpenAgentsApp()

    # Use the utility to create a test agent
    create_test_agent(app, agent_id="my_test_agent")

    # Verify the agent was registered correctly
    assert "my_test_agent" in app.agent_registry.agents

    # Get the agent capabilities
    agent_info = app.agent_registry.agents["my_test_agent"]

    # Verify the agent has the expected capabilities
    assert "echo" in agent_info["capabilities"]
    assert "reverse" in agent_info["capabilities"]
    assert "transform" in agent_info["capabilities"]

    # Verify the capability details
    echo_capability = agent_info["capabilities"]["echo"]
    assert echo_capability["description"] == "Echo the input"


# Workflow Testing Example
def test_workflow_with_utils():
    """Example of testing a workflow using the testing utilities."""
    app = OpenAgentsApp()

    # Create a test agent for the workflow to use
    create_test_agent(app)

    # Create a custom workflow
    workflow = create_test_workflow(
        workflow_id="custom_workflow",
        description="Custom test workflow",
        steps=[
            {
                "id": "step1",
                "component": "test_agent.echo",
                "inputs": {"text": "{{input.message}}"},
            },
            {
                "id": "step2",
                "component": "test_agent.reverse",
                "inputs": {"text": "{{step1.output}}"},
            },
        ],
        output={"original": "{{step1.output}}", "reversed": "{{step2.output}}"},
    )

    # Register the workflow
    app.workflow_registry.register(workflow)

    # Verify the workflow was registered correctly
    assert "custom_workflow" in app.workflow_registry.workflows

    # Get the registered workflow
    registered_workflow = app.workflow_registry.workflows["custom_workflow"]

    # Use the JSON structure assertion to verify the structure
    expected_structure = {
        "id": "custom_workflow",
        "steps": [{}],  # We just care about the structure, not the content
        "output": {},
    }
    assert_json_structure(registered_workflow, expected_structure)

    # Use the path comparison to verify specific fields
    assert compare_dict_paths(
        registered_workflow, workflow, ["id", "description", "steps.0.id", "steps.1.id"]
    )


# Mock Client Testing Example
@pytest.mark.asyncio
async def test_mock_agent_client():
    """Example of using the mock agent client."""
    client = MockAgentClient(
        {"hello": "Hello, world!", "weather": "The weather is sunny today."}
    )

    # Test a matching pattern
    response = await client.call("Tell me hello")
    assert response == "Hello, world!"

    # Test another matching pattern
    response = await client.call("What's the weather like?")
    assert response == "The weather is sunny today."

    # Test a non-matching pattern
    response = await client.call("Something else")
    assert "Mock response to:" in response

    # Verify call count
    assert client.get_call_count() == 3


# Job Callback Testing Example
@pytest.mark.asyncio
async def test_mock_job_callback():
    """Example of using the mock job callback."""
    callback = MockJobCallback()

    # Simulate job lifecycle events
    await callback.on_status_change("job-123", "QUEUED")
    await callback.on_status_change("job-123", "RUNNING")
    await callback.on_progress("job-123", 0.5, "Halfway done")
    await callback.on_status_change("job-123", "COMPLETED")

    # Check the recorded events
    events = callback.get_events()
    assert len(events) == 4

    # Check specific event types
    status_events = callback.get_events("status_change")
    assert len(status_events) == 3

    progress_events = callback.get_events("progress")
    assert len(progress_events) == 1
    assert progress_events[0]["progress"] == 0.5
