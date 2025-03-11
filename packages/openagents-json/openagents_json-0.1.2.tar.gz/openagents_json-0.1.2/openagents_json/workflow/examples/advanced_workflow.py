"""
Example of an advanced workflow using the OpenAgents JSON workflow schema.

This example demonstrates how to create a more complex workflow with
conditional branching, multiple agents, data transformations, and error handling.
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


def create_advanced_workflow() -> Workflow:
    """
    Create an advanced workflow for content creation and analysis.

    The workflow has multiple steps with branching:
    1. Content request - accepts content request from the user
    2. Content classification - determines the type of content needed
    3. Branching based on content type:
       a. Text content generation
       b. Image content generation
    4. Content analysis - analyzes the generated content
    5. Content enhancement - enhances the content based on analysis
    6. Final output - returns the enhanced content

    Returns:
        A Workflow instance
    """
    # Define workflow metadata
    metadata = WorkflowMetadataModel(
        author="OpenAgents Team",
        created=datetime.utcnow(),
        tags=["advanced", "content-creation", "multi-modal"],
        category="content-creation",
        description="An advanced workflow for content creation and analysis",
        version_notes="Initial version of the advanced content creation workflow",
        custom_metadata={
            "complexity_level": "advanced",
            "estimated_runtime": "30-60 seconds",
            "use_cases": ["marketing", "social media", "blogging"],
            "required_capabilities": [
                "text_generation",
                "image_generation",
                "content_analysis",
            ],
        },
    )

    # Define workflow steps
    request_step = Step(
        id="content_request",
        type="input",
        name="Content Request",
        description="Accepts content request from the user",
        outputs=[
            Parameter(
                name="request",
                type="string",
                description="The content request",
                required=True,
            ),
            Parameter(
                name="tone",
                type="string",
                description="The desired tone of the content",
                required=False,
                default="neutral",
            ),
            Parameter(
                name="length",
                type="integer",
                description="The approximate length of the content",
                required=False,
                default=500,
            ),
        ],
    )

    classification_step = Step(
        id="content_classification",
        type="agent",
        name="Content Classification",
        description="Determines the type of content needed",
        agent="content_classifier",
        capability="classify",
        inputs=[
            Parameter(
                name="request",
                type="string",
                description="The content request to classify",
                required=True,
            )
        ],
        outputs=[
            Parameter(
                name="content_type",
                type="string",
                description="The type of content needed (text or image)",
                required=True,
            ),
            Parameter(
                name="category",
                type="string",
                description="The category of the content",
                required=True,
            ),
            Parameter(
                name="keywords",
                type="array",
                description="Keywords extracted from the request",
                required=True,
                items_type="string",
            ),
        ],
        retry=RetryConfig(
            max_attempts=2,
            delay_seconds=1,
            backoff_multiplier=2.0,
        ),
    )

    text_generation_step = Step(
        id="text_generation",
        type="agent",
        name="Text Generation",
        description="Generates text content based on the request",
        agent="text_generator",
        capability="generate",
        inputs=[
            Parameter(
                name="request",
                type="string",
                description="The content request",
                required=True,
            ),
            Parameter(
                name="tone",
                type="string",
                description="The desired tone of the content",
                required=True,
            ),
            Parameter(
                name="length",
                type="integer",
                description="The approximate length of the content",
                required=True,
            ),
            Parameter(
                name="category",
                type="string",
                description="The category of the content",
                required=True,
            ),
            Parameter(
                name="keywords",
                type="array",
                description="Keywords to include in the content",
                required=True,
                items_type="string",
            ),
        ],
        outputs=[
            Parameter(
                name="text_content",
                type="string",
                description="The generated text content",
                required=True,
            ),
            Parameter(
                name="title",
                type="string",
                description="The title for the content",
                required=True,
            ),
        ],
        retry=RetryConfig(
            max_attempts=3,
            delay_seconds=2,
            backoff_multiplier=1.5,
        ),
        condition="inputs.content_type == 'text'",
    )

    image_generation_step = Step(
        id="image_generation",
        type="agent",
        name="Image Generation",
        description="Generates image content based on the request",
        agent="image_generator",
        capability="generate",
        inputs=[
            Parameter(
                name="request",
                type="string",
                description="The content request",
                required=True,
            ),
            Parameter(
                name="category",
                type="string",
                description="The category of the content",
                required=True,
            ),
            Parameter(
                name="keywords",
                type="array",
                description="Keywords to visualize in the image",
                required=True,
                items_type="string",
            ),
        ],
        outputs=[
            Parameter(
                name="image_url",
                type="string",
                description="The URL of the generated image",
                required=True,
            ),
            Parameter(
                name="image_caption",
                type="string",
                description="A caption for the generated image",
                required=True,
            ),
        ],
        retry=RetryConfig(
            max_attempts=3,
            delay_seconds=2,
            backoff_multiplier=1.5,
        ),
        condition="inputs.content_type == 'image'",
    )

    text_analysis_step = Step(
        id="text_analysis",
        type="agent",
        name="Text Analysis",
        description="Analyzes the generated text content",
        agent="content_analyzer",
        capability="analyze",
        inputs=[
            Parameter(
                name="text_content",
                type="string",
                description="The text content to analyze",
                required=True,
            ),
            Parameter(
                name="title",
                type="string",
                description="The title of the content",
                required=True,
            ),
        ],
        outputs=[
            Parameter(
                name="readability_score",
                type="number",
                description="The readability score of the content",
                required=True,
            ),
            Parameter(
                name="sentiment_score",
                type="number",
                description="The sentiment score of the content",
                required=True,
            ),
            Parameter(
                name="improvement_suggestions",
                type="array",
                description="Suggestions for improving the content",
                required=True,
                items_type="string",
            ),
        ],
    )

    text_enhancement_step = Step(
        id="text_enhancement",
        type="agent",
        name="Text Enhancement",
        description="Enhances the text content based on analysis",
        agent="text_enhancer",
        capability="enhance",
        inputs=[
            Parameter(
                name="text_content",
                type="string",
                description="The original text content",
                required=True,
            ),
            Parameter(
                name="title",
                type="string",
                description="The title of the content",
                required=True,
            ),
            Parameter(
                name="readability_score",
                type="number",
                description="The readability score of the content",
                required=True,
            ),
            Parameter(
                name="sentiment_score",
                type="number",
                description="The sentiment score of the content",
                required=True,
            ),
            Parameter(
                name="improvement_suggestions",
                type="array",
                description="Suggestions for improving the content",
                required=True,
                items_type="string",
            ),
        ],
        outputs=[
            Parameter(
                name="enhanced_text",
                type="string",
                description="The enhanced text content",
                required=True,
            ),
            Parameter(
                name="enhanced_title",
                type="string",
                description="The enhanced title",
                required=True,
            ),
        ],
    )

    image_caption_step = Step(
        id="image_caption_enhancement",
        type="agent",
        name="Image Caption Enhancement",
        description="Enhances the image caption",
        agent="text_enhancer",
        capability="enhance",
        inputs=[
            Parameter(
                name="image_caption",
                type="string",
                description="The original image caption",
                required=True,
            ),
        ],
        outputs=[
            Parameter(
                name="enhanced_caption",
                type="string",
                description="The enhanced image caption",
                required=True,
            ),
        ],
    )

    output_step = Step(
        id="content_output",
        type="output",
        name="Content Output",
        description="Returns the final content",
        inputs=[
            Parameter(
                name="content_type",
                type="string",
                description="The type of content (text or image)",
                required=True,
            ),
            Parameter(
                name="text_content",
                type="string",
                description="The enhanced text content",
                required=False,
            ),
            Parameter(
                name="title",
                type="string",
                description="The enhanced title",
                required=False,
            ),
            Parameter(
                name="image_url",
                type="string",
                description="The URL of the generated image",
                required=False,
            ),
            Parameter(
                name="image_caption",
                type="string",
                description="The enhanced image caption",
                required=False,
            ),
        ],
    )

    # Define connections between steps
    connections = [
        # Connect request to classification
        Connection(
            from_step="content_request",
            from_output="request",
            to_step="content_classification",
            to_input="request",
        ),
        # Connect classification to text generation
        Connection(
            from_step="content_classification",
            from_output="content_type",
            to_step="text_generation",
            to_input="content_type",
            is_control_flow=True,
        ),
        Connection(
            from_step="content_request",
            from_output="request",
            to_step="text_generation",
            to_input="request",
        ),
        Connection(
            from_step="content_request",
            from_output="tone",
            to_step="text_generation",
            to_input="tone",
        ),
        Connection(
            from_step="content_request",
            from_output="length",
            to_step="text_generation",
            to_input="length",
        ),
        Connection(
            from_step="content_classification",
            from_output="category",
            to_step="text_generation",
            to_input="category",
        ),
        Connection(
            from_step="content_classification",
            from_output="keywords",
            to_step="text_generation",
            to_input="keywords",
        ),
        # Connect classification to image generation
        Connection(
            from_step="content_classification",
            from_output="content_type",
            to_step="image_generation",
            to_input="content_type",
            is_control_flow=True,
        ),
        Connection(
            from_step="content_request",
            from_output="request",
            to_step="image_generation",
            to_input="request",
        ),
        Connection(
            from_step="content_classification",
            from_output="category",
            to_step="image_generation",
            to_input="category",
        ),
        Connection(
            from_step="content_classification",
            from_output="keywords",
            to_step="image_generation",
            to_input="keywords",
        ),
        # Connect text generation to text analysis
        Connection(
            from_step="text_generation",
            from_output="text_content",
            to_step="text_analysis",
            to_input="text_content",
        ),
        Connection(
            from_step="text_generation",
            from_output="title",
            to_step="text_analysis",
            to_input="title",
        ),
        # Connect text analysis to text enhancement
        Connection(
            from_step="text_analysis",
            from_output="readability_score",
            to_step="text_enhancement",
            to_input="readability_score",
        ),
        Connection(
            from_step="text_analysis",
            from_output="sentiment_score",
            to_step="text_enhancement",
            to_input="sentiment_score",
        ),
        Connection(
            from_step="text_analysis",
            from_output="improvement_suggestions",
            to_step="text_enhancement",
            to_input="improvement_suggestions",
        ),
        Connection(
            from_step="text_generation",
            from_output="text_content",
            to_step="text_enhancement",
            to_input="text_content",
        ),
        Connection(
            from_step="text_generation",
            from_output="title",
            to_step="text_enhancement",
            to_input="title",
        ),
        # Connect image generation to caption enhancement
        Connection(
            from_step="image_generation",
            from_output="image_caption",
            to_step="image_caption_enhancement",
            to_input="image_caption",
        ),
        # Connect to output
        Connection(
            from_step="content_classification",
            from_output="content_type",
            to_step="content_output",
            to_input="content_type",
        ),
        Connection(
            from_step="text_enhancement",
            from_output="enhanced_text",
            to_step="content_output",
            to_input="text_content",
        ),
        Connection(
            from_step="text_enhancement",
            from_output="enhanced_title",
            to_step="content_output",
            to_input="title",
        ),
        Connection(
            from_step="image_generation",
            from_output="image_url",
            to_step="content_output",
            to_input="image_url",
        ),
        Connection(
            from_step="image_caption_enhancement",
            from_output="enhanced_caption",
            to_step="content_output",
            to_input="image_caption",
        ),
    ]

    # Create the workflow
    workflow = Workflow(
        id="advanced_content_creation",
        name="Advanced Content Creation",
        description="An advanced workflow for content creation and analysis",
        version="1.0.0",
        steps=[
            request_step,
            classification_step,
            text_generation_step,
            image_generation_step,
            text_analysis_step,
            text_enhancement_step,
            image_caption_step,
            output_step,
        ],
        connections=connections,
        inputs=[
            Parameter(
                name="content_request",
                type="string",
                description="The request for content creation",
                required=True,
            ),
            Parameter(
                name="tone",
                type="string",
                description="The desired tone of the content",
                required=False,
                default="neutral",
            ),
            Parameter(
                name="length",
                type="integer",
                description="The approximate length of the content (for text)",
                required=False,
                default=500,
            ),
        ],
        outputs=[
            Parameter(
                name="content_type",
                type="string",
                description="The type of content created (text or image)",
                required=True,
            ),
            Parameter(
                name="text_content",
                type="string",
                description="The enhanced text content (if text type)",
                required=False,
            ),
            Parameter(
                name="title",
                type="string",
                description="The enhanced title (if text type)",
                required=False,
            ),
            Parameter(
                name="image_url",
                type="string",
                description="The URL of the generated image (if image type)",
                required=False,
            ),
            Parameter(
                name="image_caption",
                type="string",
                description="The enhanced image caption (if image type)",
                required=False,
            ),
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
    # Create an advanced workflow
    workflow = create_advanced_workflow()

    # Save the workflow to a file
    save_workflow_to_file(workflow, "examples/workflows/advanced_content_creation.json")
