"""
Example of a basic workflow using the OpenAgents JSON workflow schema.

This example demonstrates how to create a simple workflow with multiple steps
and connections between them.
"""

import json
from datetime import datetime
from pathlib import Path

from openagents_json.workflow import (
    Connection,
    Parameter,
    RetryConfig,
    Step,
    Workflow,
    WorkflowMetadataModel,
)


def create_basic_workflow() -> Workflow:
    """
    Create a basic workflow that processes text.

    The workflow has three steps:
    1. Text input - accepts text from the user
    2. Text processing - processes the text (e.g., summarizes it)
    3. Text output - returns the processed text

    Returns:
        A Workflow instance
    """
    # Define workflow metadata
    metadata = WorkflowMetadataModel(
        author="OpenAgents Team",
        created=datetime.utcnow(),
        tags=["example", "text-processing", "basic"],
        category="text-processing",
        description="A basic workflow that processes text",
        version_notes="Initial version of the basic text processing workflow",
    )

    # Define workflow steps
    input_step = Step(
        id="text_input",
        type="input",
        name="Text Input",
        description="Accepts text input from the user",
        outputs=[
            Parameter(
                name="text",
                type="string",
                description="The input text to process",
                required=True,
            )
        ],
    )

    process_step = Step(
        id="text_processor",
        type="agent",
        name="Text Processor",
        description="Processes the input text",
        agent="text_processor",
        capability="summarize",
        inputs=[
            Parameter(
                name="text",
                type="string",
                description="The text to process",
                required=True,
            )
        ],
        outputs=[
            Parameter(
                name="processed_text",
                type="string",
                description="The processed text",
                required=True,
            )
        ],
        retry=RetryConfig(
            max_attempts=3,
            delay_seconds=2,
            backoff_multiplier=1.5,
        ),
    )

    output_step = Step(
        id="text_output",
        type="output",
        name="Text Output",
        description="Returns the processed text",
        inputs=[
            Parameter(
                name="result",
                type="string",
                description="The processed text to return",
                required=True,
            )
        ],
    )

    # Define connections between steps
    connections = [
        Connection(
            from_step="text_input",
            from_output="text",
            to_step="text_processor",
            to_input="text",
        ),
        Connection(
            from_step="text_processor",
            from_output="processed_text",
            to_step="text_output",
            to_input="result",
        ),
    ]

    # Create the workflow
    workflow = Workflow(
        id="basic_text_processing",
        name="Basic Text Processing",
        description="A basic workflow that processes text",
        version="1.0.0",
        steps=[input_step, process_step, output_step],
        connections=connections,
        inputs=[
            Parameter(
                name="input_text",
                type="string",
                description="The input text to process",
                required=True,
            )
        ],
        outputs=[
            Parameter(
                name="processed_text",
                type="string",
                description="The processed text",
                required=True,
            )
        ],
        metadata=metadata,
    )

    return workflow


def save_workflow_to_file(workflow: Workflow, file_path: str) -> None:
    """
    Save a workflow to a JSON file.

    Args:
        workflow: The workflow to save
        file_path: The path to save the workflow to
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        json.dump(workflow.to_dict(), f, indent=2)

    print(f"Workflow saved to {file_path}")


if __name__ == "__main__":
    # Create a basic workflow
    workflow = create_basic_workflow()

    # Save the workflow to a file
    save_workflow_to_file(workflow, "examples/workflows/basic_text_processing.json")

    # Print the workflow as JSON
    print(json.dumps(workflow.to_dict(), indent=2))
