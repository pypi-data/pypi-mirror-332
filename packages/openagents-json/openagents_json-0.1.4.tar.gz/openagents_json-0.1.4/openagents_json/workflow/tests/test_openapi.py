"""
Tests for the OpenAPI integration.

This module tests the integration of workflow validation with OpenAPI.
"""

import json
import unittest
from typing import Any, Dict, List

from openagents_json.workflow.openapi import (
    extend_openapi_with_workflows,
    extract_workflows_from_openapi,
    workflow_to_openapi_extension,
)


class TestOpenAPIIntegration(unittest.TestCase):
    """Test the OpenAPI integration."""

    def setUp(self):
        """Set up test fixtures."""
        # Sample workflow
        self.workflow = {
            "id": "test_workflow",
            "version": "1.0.0",
            "name": "Test Workflow",
            "description": "A test workflow",
            "steps": [
                {
                    "id": "step1",
                    "component": "test.component",
                    "inputs": {"input1": "value1"},
                    "outputs": {"output1": "result1"},
                },
                {
                    "id": "step2",
                    "component": "test.component2",
                    "inputs": {"input2": "value2"},
                    "outputs": {"output2": "result2"},
                },
            ],
            "connections": [{"source": "step1.output1", "target": "step2.input2"}],
            "inputs": {
                "workflow_input": {
                    "type": "string",
                    "description": "Workflow input",
                    "required": True,
                }
            },
            "outputs": {
                "workflow_output": {"type": "string", "description": "Workflow output"}
            },
        }

        # Sample OpenAPI specification
        self.openapi_spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {
                "/test": {
                    "post": {
                        "summary": "Test endpoint",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/TestInput"}
                                }
                            }
                        },
                        "responses": {
                            "200": {
                                "description": "Successful response",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/TestOutput"
                                        }
                                    }
                                },
                            }
                        },
                    }
                }
            },
            "components": {
                "schemas": {
                    "TestInput": {
                        "type": "object",
                        "properties": {"input": {"type": "string"}},
                    },
                    "TestOutput": {
                        "type": "object",
                        "properties": {"output": {"type": "string"}},
                    },
                }
            },
        }

    def test_workflow_to_openapi_extension(self):
        """Test converting a workflow to an OpenAPI extension."""
        extension = workflow_to_openapi_extension(self.workflow)

        # Check the extension structure
        self.assertIn("x-workflow", extension)
        self.assertEqual(extension["x-workflow"]["id"], self.workflow["id"])
        self.assertEqual(extension["x-workflow"]["version"], self.workflow["version"])
        self.assertEqual(extension["x-workflow"]["name"], self.workflow["name"])
        self.assertEqual(
            extension["x-workflow"]["description"], self.workflow["description"]
        )
        self.assertEqual(extension["x-workflow"]["steps"], self.workflow["steps"])
        self.assertEqual(
            extension["x-workflow"]["connections"], self.workflow["connections"]
        )
        self.assertEqual(extension["x-workflow"]["inputs"], self.workflow["inputs"])
        self.assertEqual(extension["x-workflow"]["outputs"], self.workflow["outputs"])

    def test_extend_openapi_with_workflows(self):
        """Test extending an OpenAPI specification with workflows."""
        extended_spec = extend_openapi_with_workflows(
            self.openapi_spec, [self.workflow]
        )

        # Check the extended specification
        self.assertIn("x-workflows", extended_spec)
        self.assertEqual(extended_spec["x-workflows"], [self.workflow["id"]])

        # Check that workflow schemas were added
        self.assertIn(
            f"Workflow_{self.workflow['id']}", extended_spec["components"]["schemas"]
        )
        self.assertIn(
            f"WorkflowInput_{self.workflow['id']}",
            extended_spec["components"]["schemas"],
        )
        self.assertIn(
            f"WorkflowOutput_{self.workflow['id']}",
            extended_spec["components"]["schemas"],
        )

        # Check that the workflow schema has the x-workflow extension
        workflow_schema = extended_spec["components"]["schemas"][
            f"Workflow_{self.workflow['id']}"
        ]
        self.assertIn("x-workflow", workflow_schema)
        self.assertEqual(workflow_schema["x-workflow"]["id"], self.workflow["id"])

    def test_extract_workflows_from_openapi(self):
        """Test extracting workflows from an OpenAPI specification."""
        # First extend the specification with a workflow
        extended_spec = extend_openapi_with_workflows(
            self.openapi_spec, [self.workflow]
        )

        # Then extract the workflows from the extended specification
        workflows = extract_workflows_from_openapi(extended_spec)

        # Check that the workflow was extracted
        self.assertEqual(len(workflows), 1)
        self.assertEqual(workflows[0]["id"], self.workflow["id"])
        self.assertEqual(workflows[0]["schema"], f"Workflow_{self.workflow['id']}")

    def test_extend_openapi_with_multiple_workflows(self):
        """Test extending an OpenAPI specification with multiple workflows."""
        # Create a second workflow
        workflow2 = dict(self.workflow)
        workflow2["id"] = "test_workflow2"

        # Extend the specification with both workflows
        extended_spec = extend_openapi_with_workflows(
            self.openapi_spec, [self.workflow, workflow2]
        )

        # Check that both workflows were added
        self.assertIn("x-workflows", extended_spec)
        self.assertEqual(
            set(extended_spec["x-workflows"]), {self.workflow["id"], workflow2["id"]}
        )

        # Check that both workflow schemas were added
        self.assertIn(
            f"Workflow_{self.workflow['id']}", extended_spec["components"]["schemas"]
        )
        self.assertIn(
            f"Workflow_{workflow2['id']}", extended_spec["components"]["schemas"]
        )


if __name__ == "__main__":
    unittest.main()
