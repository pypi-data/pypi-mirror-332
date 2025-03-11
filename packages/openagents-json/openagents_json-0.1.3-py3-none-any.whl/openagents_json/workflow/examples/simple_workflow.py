"""
Simple workflow example for testing purposes.
"""

from openagents_json.workflow.models import Workflow

# Define a simple workflow for testing visualization
simple_workflow = {
    "id": "simple_test_workflow",
    "name": "Simple Test Workflow",
    "description": "A simple workflow for testing visualization",
    "version": "1.0.0",
    "steps": [
        {
            "id": "step1",
            "name": "Step 1",
            "description": "First step in the workflow",
            "component": "test.component1",
            "inputs": {"input1": "workflow.input1"},
            "outputs": {"output1": "step1_output"},
        },
        {
            "id": "step2",
            "name": "Step 2",
            "description": "Second step in the workflow",
            "component": "test.component2",
            "inputs": {"input1": "step1.output1"},
            "outputs": {"output1": "step2_output"},
        },
        {
            "id": "step3",
            "name": "Step 3",
            "description": "Final step in the workflow",
            "component": "test.component3",
            "inputs": {"input1": "step2.output1"},
            "outputs": {"output1": "workflow.output1"},
        },
    ],
    "connections": [
        {"source": "step1.output1", "target": "step2.input1"},
        {"source": "step2.output1", "target": "step3.input1"},
    ],
    "inputs": {
        "input1": {
            "type": "string",
            "description": "Input for the workflow",
            "required": True,
        }
    },
    "outputs": {
        "output1": {"type": "string", "description": "Output from the workflow"}
    },
    "metadata": {
        "author": "Test Author",
        "created": "2025-03-07T00:00:00Z",
        "tags": ["test", "example"],
        "category": "testing",
    },
}

# Create a workflow instance
test_workflow = Workflow.from_dict(simple_workflow)
