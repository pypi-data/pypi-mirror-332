"""
Unit tests for the workflow registry.
"""

import json
import os
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from openagents_json.workflow import (
    Connection,
    Parameter,
    Step,
    Workflow,
    WorkflowMetadataModel,
    WorkflowRegistry,
)


class TestWorkflowRegistry(unittest.TestCase):
    """Test cases for the workflow registry."""

    def setUp(self):
        """Set up test fixtures."""
        self.registry = WorkflowRegistry()

        # Create test workflows
        self.workflow1 = Workflow(
            id="workflow1",
            name="Workflow 1",
            description="Test workflow 1",
            version="1.0.0",
            steps=[
                Step(
                    id="step1",
                    type="input",
                    name="Input Step",
                    description="Test input step",
                    outputs=[
                        Parameter(
                            name="value",
                            type="string",
                            description="Test value",
                            required=True,
                        )
                    ],
                ),
                Step(
                    id="step2",
                    type="output",
                    name="Output Step",
                    description="Test output step",
                    inputs=[
                        Parameter(
                            name="value",
                            type="string",
                            description="Test value",
                            required=True,
                        )
                    ],
                ),
            ],
            connections=[
                Connection(
                    from_step="step1",
                    from_output="value",
                    to_step="step2",
                    to_input="value",
                )
            ],
            metadata=WorkflowMetadataModel(
                author="Test Author",
                tags=["test", "workflow1"],
                category="test-category-1",
            ),
        )

        self.workflow2 = Workflow(
            id="workflow2",
            name="Workflow 2",
            description="Test workflow 2",
            version="1.0.0",
            steps=[
                Step(
                    id="step1",
                    type="input",
                    name="Input Step",
                    description="Test input step",
                    outputs=[
                        Parameter(
                            name="value",
                            type="string",
                            description="Test value",
                            required=True,
                        )
                    ],
                ),
                Step(
                    id="step2",
                    type="output",
                    name="Output Step",
                    description="Test output step",
                    inputs=[
                        Parameter(
                            name="value",
                            type="string",
                            description="Test value",
                            required=True,
                        )
                    ],
                ),
            ],
            connections=[
                Connection(
                    from_step="step1",
                    from_output="value",
                    to_step="step2",
                    to_input="value",
                )
            ],
            metadata=WorkflowMetadataModel(
                author="Test Author",
                tags=["test", "workflow2"],
                category="test-category-2",
            ),
        )

        # Register the workflows
        self.registry.register(self.workflow1)
        self.registry.register(self.workflow2)

    def test_register_and_get(self):
        """Test registering and retrieving workflows."""
        # Get workflow by ID
        workflow = self.registry.get("workflow1")
        self.assertIsNotNone(workflow)
        self.assertEqual(workflow["id"], "workflow1")
        self.assertEqual(workflow["name"], "Workflow 1")

        # Get non-existent workflow
        workflow = self.registry.get("non_existent")
        self.assertIsNone(workflow)

    def test_list(self):
        """Test listing workflows."""
        # List all workflows
        workflows = self.registry.list()
        self.assertEqual(len(workflows), 2)

        # List workflows by tag
        workflows = self.registry.list(tag="workflow1")
        self.assertEqual(len(workflows), 1)
        self.assertEqual(workflows[0]["id"], "workflow1")

        # List workflows by category
        workflows = self.registry.list(category="test-category-2")
        self.assertEqual(len(workflows), 1)
        self.assertEqual(workflows[0]["id"], "workflow2")

        # List workflows by non-existent tag
        workflows = self.registry.list(tag="non_existent")
        self.assertEqual(len(workflows), 0)

    def test_delete(self):
        """Test deleting workflows."""
        # Delete workflow
        result = self.registry.delete("workflow1")
        self.assertTrue(result)

        # Verify workflow is deleted
        workflow = self.registry.get("workflow1")
        self.assertIsNone(workflow)

        # Delete non-existent workflow
        result = self.registry.delete("non_existent")
        self.assertFalse(result)

    def test_versioning(self):
        """Test workflow versioning."""
        # Create a new version of workflow2
        workflow2_v2 = self.workflow2.copy(update={"version": "1.1.0"})

        # Register the new version
        self.registry.register(workflow2_v2)

        # Get the latest version
        workflow = self.registry.get("workflow2")
        self.assertEqual(workflow["version"], "1.1.0")

        # Get a specific version
        workflow = self.registry.get("workflow2", version="1.0.0")
        self.assertEqual(workflow["version"], "1.0.0")

        # Get all versions
        versions = self.registry.get_versions("workflow2")
        self.assertEqual(len(versions), 2)
        self.assertIn("1.0.0", versions)
        self.assertIn("1.1.0", versions)

    def test_save_and_load(self):
        """Test saving and loading the registry to/from a file."""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name

        try:
            # Save the registry
            result = self.registry.save_to_file(temp_path)
            self.assertTrue(result)

            # Create a new registry
            new_registry = WorkflowRegistry()

            # Load the registry
            result = new_registry.load_from_file(temp_path)
            self.assertTrue(result)

            # Verify the loaded registry
            workflow = new_registry.get("workflow1")
            self.assertIsNotNone(workflow)
            self.assertEqual(workflow["id"], "workflow1")

            workflow = new_registry.get("workflow2")
            self.assertIsNotNone(workflow)
            self.assertEqual(workflow["id"], "workflow2")
        finally:
            # Clean up
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    def test_categorize(self):
        """Test categorizing workflows."""
        # Categorize workflows
        categories = self.registry.categorize()

        # Verify categories
        self.assertIn("test-category-1", categories)
        self.assertIn("test-category-2", categories)

        # Verify workflows in categories
        self.assertEqual(len(categories["test-category-1"]), 1)
        self.assertEqual(categories["test-category-1"][0]["id"], "workflow1")

        self.assertEqual(len(categories["test-category-2"]), 1)
        self.assertEqual(categories["test-category-2"][0]["id"], "workflow2")

    def test_get_by_tag(self):
        """Test getting workflows by tag."""
        # Get workflows by tag
        workflows = self.registry.get_by_tag("workflow1")
        self.assertEqual(len(workflows), 1)
        self.assertEqual(workflows[0]["id"], "workflow1")

        # Get workflows by non-existent tag
        workflows = self.registry.get_by_tag("non_existent")
        self.assertEqual(len(workflows), 0)

    def test_get_by_category(self):
        """Test getting workflows by category."""
        # Get workflows by category
        workflows = self.registry.get_by_category("test-category-1")
        self.assertEqual(len(workflows), 1)
        self.assertEqual(workflows[0]["id"], "workflow1")

        # Get workflows by non-existent category
        workflows = self.registry.get_by_category("non_existent")
        self.assertEqual(len(workflows), 0)


if __name__ == "__main__":
    unittest.main()
