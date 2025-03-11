"""
OpenAPI integration for workflows.

This module provides functions to integrate workflow definitions with OpenAPI.
"""

import json
from typing import Any, Dict, List, Optional, Set, Tuple

import jsonschema
from pydantic import BaseModel, Field

from openagents_json.workflow.models import Connection, Step, Workflow
from openagents_json.workflow.schema import WORKFLOW_SCHEMA


class WorkflowOpenAPIExtension(BaseModel):
    """Definition of the x-workflow OpenAPI extension."""

    id: str = Field(description="Unique identifier for the workflow")
    version: str = Field(description="Semantic version of the workflow")
    name: Optional[str] = Field(
        default=None, description="Human-readable name for the workflow"
    )
    description: Optional[str] = Field(
        default=None, description="Detailed description of the workflow"
    )
    steps: List[Dict[str, Any]] = Field(description="Sequential steps in the workflow")
    connections: List[Dict[str, Any]] = Field(
        default_factory=list, description="Connections between steps"
    )
    inputs: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict, description="Input definition for the workflow"
    )
    outputs: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict, description="Output definition for the workflow"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional metadata for the workflow"
    )


def workflow_to_openapi_extension(workflow: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert a workflow to an OpenAPI extension.

    Args:
        workflow: The workflow to convert

    Returns:
        Dict[str, Any]: The workflow as an OpenAPI extension
    """
    # Validate the workflow against the schema
    try:
        jsonschema.validate(workflow, WORKFLOW_SCHEMA)
    except jsonschema.exceptions.ValidationError as e:
        raise ValueError(f"Invalid workflow: {e}") from e

    # Convert to OpenAPI extension
    extension = {
        "x-workflow": {
            "id": workflow["id"],
            "version": workflow.get("version", "1.0.0"),
        }
    }

    # Copy optional fields
    for field in [
        "name",
        "description",
        "steps",
        "connections",
        "inputs",
        "outputs",
        "metadata",
    ]:
        if field in workflow:
            extension["x-workflow"][field] = workflow[field]

    return extension


def extract_workflows_from_openapi(
    openapi_spec: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """
    Extract workflows from an OpenAPI specification.

    Args:
        openapi_spec: The OpenAPI specification

    Returns:
        List[Dict[str, Any]]: List of workflows found in the specification
    """
    workflows = []

    # Check paths for workflow extensions
    paths = openapi_spec.get("paths", {})
    for path, path_item in paths.items():
        for method, operation in path_item.items():
            if method in [
                "get",
                "post",
                "put",
                "delete",
                "options",
                "head",
                "patch",
                "trace",
            ]:
                if "x-workflow" in operation:
                    workflow = operation["x-workflow"]
                    workflow["path"] = path
                    workflow["method"] = method
                    workflows.append(workflow)

    # Check components for workflow extensions
    components = openapi_spec.get("components", {})
    schemas = components.get("schemas", {})
    for schema_name, schema in schemas.items():
        if "x-workflow" in schema:
            workflow = schema["x-workflow"]
            workflow["schema"] = schema_name
            workflows.append(workflow)

    return workflows


def _create_parameter_schema(param_def: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create an OpenAPI schema for a parameter definition.

    Args:
        param_def: The parameter definition

    Returns:
        Dict[str, Any]: The OpenAPI schema
    """
    schema = {
        "type": param_def.get("type", "string"),
        "description": param_def.get("description", ""),
    }

    # Add format if specified
    if "format" in param_def:
        schema["format"] = param_def["format"]

    # Add enum if specified
    if "enum" in param_def:
        schema["enum"] = param_def["enum"]

    # Add default if specified
    if "default" in param_def:
        schema["default"] = param_def["default"]

    return schema


def extend_openapi_with_workflows(
    openapi_spec: Dict[str, Any], workflows: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Extend an OpenAPI specification with workflow definitions.

    Args:
        openapi_spec: The OpenAPI specification to extend
        workflows: The workflows to add

    Returns:
        Dict[str, Any]: The extended OpenAPI specification
    """
    # Create a deep copy to avoid modifying the input
    spec = json.loads(json.dumps(openapi_spec))

    # Ensure components section exists
    if "components" not in spec:
        spec["components"] = {}

    if "schemas" not in spec["components"]:
        spec["components"]["schemas"] = {}

    # Add workflow schema definitions
    for workflow in workflows:
        workflow_id = workflow["id"]

        # Add workflow as a schema
        spec["components"]["schemas"][f"Workflow_{workflow_id}"] = {
            "type": "object",
            "x-workflow": workflow,
            "properties": {
                "id": {
                    "type": "string",
                    "description": "Workflow identifier",
                    "example": workflow_id,
                }
            },
        }

        # Add workflow inputs as a schema if they exist
        if "inputs" in workflow and workflow["inputs"]:
            input_properties = {}
            required = []

            for input_name, input_def in workflow["inputs"].items():
                # Convert parameter definition to OpenAPI schema
                input_properties[input_name] = _create_parameter_schema(input_def)

                # Add to required list if required
                if input_def.get("required", False):
                    required.append(input_name)

            input_schema = {"type": "object", "properties": input_properties}

            if required:
                input_schema["required"] = required

            spec["components"]["schemas"][f"WorkflowInput_{workflow_id}"] = input_schema

        # Add workflow outputs as a schema if they exist
        if "outputs" in workflow and workflow["outputs"]:
            output_properties = {}

            for output_name, output_def in workflow["outputs"].items():
                # Convert parameter definition to OpenAPI schema
                output_properties[output_name] = _create_parameter_schema(output_def)

            spec["components"]["schemas"][f"WorkflowOutput_{workflow_id}"] = {
                "type": "object",
                "properties": output_properties,
            }

    # Ensure x-workflows extension at the root
    workflow_ids = [w["id"] for w in workflows]
    spec["x-workflows"] = workflow_ids

    return spec
