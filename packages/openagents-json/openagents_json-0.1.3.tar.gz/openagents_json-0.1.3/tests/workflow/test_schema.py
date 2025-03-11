"""
Unit tests for the workflow schema validation.
"""

import json
import unittest
from datetime import datetime

from openagents_json.workflow import (
    WORKFLOW_SCHEMA,
    Connection,
    Parameter,
    RetryConfig,
    Step,
    Workflow,
    WorkflowMetadata,
    WorkflowMetadataModel,
    WorkflowValidator,
    WorkflowVersion,
)


class TestWorkflowSchema(unittest.TestCase):
    """Test cases for the workflow schema validation."""

    def setUp(self):
        """Set up test fixtures."""
        self.validator = WorkflowValidator()

        # Create a valid workflow for testing
        self.valid_workflow_dict = {
            "id": "test_workflow",
            "name": "Test Workflow",
            "description": "A test workflow",
            "version": "1.0.0",
            "steps": [
                {
                    "id": "step1",
                    "type": "input",
                    "name": "Input Step",
                    "description": "Test input step",
                    "outputs": [
                        {
                            "name": "value",
                            "type": "string",
                            "description": "Test value",
                            "required": True,
                        }
                    ],
                },
                {
                    "id": "step2",
                    "type": "output",
                    "name": "Output Step",
                    "description": "Test output step",
                    "inputs": [
                        {
                            "name": "value",
                            "type": "string",
                            "description": "Test value",
                            "required": True,
                        }
                    ],
                },
            ],
            "connections": [
                {
                    "from_step": "step1",
                    "from_output": "value",
                    "to_step": "step2",
                    "to_input": "value",
                }
            ],
            "inputs": [],
            "outputs": [],
            "metadata": {
                "author": "Test Author",
                "created": datetime.utcnow().isoformat(),
                "tags": ["test", "example"],
                "category": "test",
            },
        }

    def test_schema_validation_valid(self):
        """Test that a valid workflow passes validation."""
        is_valid, error = self.validator.validate(self.valid_workflow_dict)
        self.assertTrue(is_valid, f"Expected valid workflow, got error: {error}")

    def test_schema_validation_missing_id(self):
        """Test that a workflow without an ID fails validation."""
        invalid_workflow = self.valid_workflow_dict.copy()
        del invalid_workflow["id"]

        is_valid, error = self.validator.validate(invalid_workflow)
        self.assertFalse(is_valid)
        self.assertIn("id", error)

    def test_schema_validation_missing_steps(self):
        """Test that a workflow without steps fails validation."""
        invalid_workflow = self.valid_workflow_dict.copy()
        invalid_workflow["steps"] = []

        is_valid, error = self.validator.validate(invalid_workflow)
        self.assertFalse(is_valid)
        self.assertIn("steps", error)

    def test_schema_validation_duplicate_step_ids(self):
        """Test that a workflow with duplicate step IDs fails validation."""
        invalid_workflow = self.valid_workflow_dict.copy()
        invalid_workflow["steps"] = [
            {
                "id": "step1",
                "type": "input",
                "name": "Input Step 1",
                "description": "Test input step 1",
            },
            {
                "id": "step1",  # Duplicate ID
                "type": "input",
                "name": "Input Step 2",
                "description": "Test input step 2",
            },
        ]

        is_valid, error = self.validator.validate(invalid_workflow)
        self.assertFalse(is_valid)
        self.assertIn("duplicate", error.lower())

    def test_schema_validation_invalid_connection(self):
        """Test that a workflow with an invalid connection fails validation."""
        invalid_workflow = self.valid_workflow_dict.copy()
        invalid_workflow["connections"] = [
            {
                "from_step": "non_existent_step",  # Non-existent step
                "from_output": "value",
                "to_step": "step2",
                "to_input": "value",
            }
        ]

        is_valid, error = self.validator.validate(invalid_workflow)
        self.assertFalse(is_valid)
        self.assertIn("non_existent_step", error)

    def test_version_comparison(self):
        """Test version comparison logic."""
        self.assertTrue(WorkflowVersion.compare("1.0.0", "2.0.0") < 0)
        self.assertTrue(WorkflowVersion.compare("1.1.0", "1.2.0") < 0)
        self.assertTrue(WorkflowVersion.compare("1.0.1", "1.0.2") < 0)
        self.assertEqual(WorkflowVersion.compare("1.0.0", "1.0.0"), 0)
        self.assertTrue(WorkflowVersion.compare("2.0.0", "1.0.0") > 0)

    def test_version_compatibility(self):
        """Test version compatibility checking."""
        self.assertTrue(WorkflowVersion.is_compatible("1.0.0", "1.0.1"))
        self.assertTrue(WorkflowVersion.is_compatible("1.0.0", "1.1.0"))
        self.assertFalse(WorkflowVersion.is_compatible("1.0.0", "2.0.0"))
        self.assertTrue(WorkflowVersion.is_compatible("1.0.0", "1.0.0"))

    def test_metadata_extraction(self):
        """Test metadata extraction."""
        metadata = WorkflowMetadata.extract_metadata(self.valid_workflow_dict)
        self.assertEqual(metadata.get("author"), "Test Author")
        self.assertIn("test", metadata.get("tags", []))
        self.assertEqual(metadata.get("category"), "test")

    def test_pydantic_model(self):
        """Test creating a workflow using Pydantic models."""
        # Create steps
        input_step = Step(
            id="input_step",
            type="input",
            name="Input Step",
            description="Test input step",
            outputs=[
                Parameter(
                    name="value", type="string", description="Test value", required=True
                )
            ],
        )

        output_step = Step(
            id="output_step",
            type="output",
            name="Output Step",
            description="Test output step",
            inputs=[
                Parameter(
                    name="result",
                    type="string",
                    description="Test result",
                    required=True,
                )
            ],
        )

        # Create connection
        connection = Connection(
            from_step="input_step",
            from_output="value",
            to_step="output_step",
            to_input="result",
        )

        # Create metadata
        metadata = WorkflowMetadataModel(
            author="Test Author",
            created=datetime.utcnow(),
            tags=["test"],
            category="test",
        )

        # Create workflow
        workflow = Workflow(
            id="test_workflow",
            name="Test Workflow",
            description="A test workflow",
            version="1.0.0",
            steps=[input_step, output_step],
            connections=[connection],
            metadata=metadata,
        )

        # Convert to dict and validate
        workflow_dict = workflow.to_dict()
        is_valid, error = self.validator.validate(workflow_dict)
        self.assertTrue(is_valid, f"Expected valid workflow, got error: {error}")

        # Check values
        self.assertEqual(workflow_dict["id"], "test_workflow")
        self.assertEqual(len(workflow_dict["steps"]), 2)
        self.assertEqual(len(workflow_dict["connections"]), 1)
        self.assertEqual(workflow_dict["metadata"]["author"], "Test Author")


if __name__ == "__main__":
    unittest.main()
