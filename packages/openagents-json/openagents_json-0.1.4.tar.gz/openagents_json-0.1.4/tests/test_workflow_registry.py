"""
Tests for the workflow registry functionality.
"""

import pytest

from openagents_json import OpenAgentsApp


def test_workflow_registration():
    """Test registering a workflow with the registry."""
    agents_app = OpenAgentsApp()

    workflow_def = {
        "id": "test-workflow",
        "description": "A test workflow",
        "steps": [
            {
                "id": "step1",
                "component": "test_component",
                "inputs": {"input1": "value1"},
            }
        ],
        "output": {"result": "{{step1.output}}"},
    }

    agents_app.register_workflow(workflow_def)

    # Check that the workflow was registered
    assert "test-workflow" in agents_app.workflow_registry.workflows
    assert (
        agents_app.workflow_registry.workflows["test-workflow"]["description"]
        == "A test workflow"
    )


def test_workflow_registration_without_id():
    """Test that registering a workflow without an ID raises an error."""
    agents_app = OpenAgentsApp()

    workflow_def = {
        "description": "A test workflow",
        "steps": [
            {
                "id": "step1",
                "component": "test_component",
                "inputs": {"input1": "value1"},
            }
        ],
        "output": {"result": "{{step1.output}}"},
    }

    with pytest.raises(
        ValueError, match="Workflow definition must include an 'id' field"
    ):
        agents_app.register_workflow(workflow_def)


def test_multiple_workflow_registration():
    """Test registering multiple workflows."""
    agents_app = OpenAgentsApp()

    workflow1 = {
        "id": "workflow1",
        "description": "First workflow",
        "steps": [],
        "output": {},
    }

    workflow2 = {
        "id": "workflow2",
        "description": "Second workflow",
        "steps": [],
        "output": {},
    }

    agents_app.register_workflow(workflow1)
    agents_app.register_workflow(workflow2)

    # Check that both workflows were registered
    assert "workflow1" in agents_app.workflow_registry.workflows
    assert "workflow2" in agents_app.workflow_registry.workflows
    assert (
        agents_app.workflow_registry.workflows["workflow1"]["description"]
        == "First workflow"
    )
    assert (
        agents_app.workflow_registry.workflows["workflow2"]["description"]
        == "Second workflow"
    )


def test_workflow_overwrite():
    """Test that registering a workflow with the same ID overwrites the previous one."""
    agents_app = OpenAgentsApp()

    workflow1 = {
        "id": "test-workflow",
        "description": "Original workflow",
        "steps": [],
        "output": {},
    }

    workflow2 = {
        "id": "test-workflow",
        "description": "Updated workflow",
        "steps": [],
        "output": {},
    }

    agents_app.register_workflow(workflow1)
    agents_app.register_workflow(workflow2)

    # Check that the workflow was updated
    assert (
        agents_app.workflow_registry.workflows["test-workflow"]["description"]
        == "Updated workflow"
    )
