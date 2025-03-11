"""
Workflow schema definitions and validation.

This module defines the schema for workflows, including structure, validation,
versioning, metadata, and categorization.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import jsonschema
import semver
from pydantic import BaseModel, Field, validator

# Semantic version regex pattern
SEMVER_PATTERN = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"

# Workflow Schema Version
SCHEMA_VERSION = "1.0.0"

# Core Workflow Schema
WORKFLOW_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "OpenAgents JSON Workflow Schema",
    "description": "Schema for defining workflows in OpenAgents JSON",
    "version": SCHEMA_VERSION,
    "type": "object",
    "required": ["id", "steps"],
    "properties": {
        "id": {
            "type": "string",
            "description": "Unique identifier for the workflow",
            "pattern": "^[a-zA-Z0-9-_]+$",
        },
        "version": {
            "type": "string",
            "description": "Semantic version of the workflow",
            "pattern": SEMVER_PATTERN,
            "default": "1.0.0",
        },
        "name": {
            "type": "string",
            "description": "Human-readable name for the workflow",
        },
        "description": {
            "type": "string",
            "description": "Detailed description of the workflow",
        },
        "steps": {
            "type": "array",
            "description": "Sequential steps in the workflow",
            "minItems": 1,
            "items": {"$ref": "#/definitions/step"},
        },
        "connections": {
            "type": "array",
            "description": "Connections between steps",
            "items": {"$ref": "#/definitions/connection"},
        },
        "inputs": {
            "type": "object",
            "description": "Input definition for the workflow",
            "additionalProperties": {"$ref": "#/definitions/parameter"},
        },
        "outputs": {
            "type": "object",
            "description": "Output definition for the workflow",
            "additionalProperties": {"$ref": "#/definitions/parameter"},
        },
        "metadata": {
            "type": "object",
            "description": "Additional metadata for the workflow",
            "properties": {
                "author": {"type": "string", "description": "Author of the workflow"},
                "created": {
                    "type": "string",
                    "description": "Creation timestamp (ISO 8601)",
                    "format": "date-time",
                },
                "updated": {
                    "type": "string",
                    "description": "Last update timestamp (ISO 8601)",
                    "format": "date-time",
                },
                "tags": {
                    "type": "array",
                    "description": "Tags for categorization",
                    "items": {"type": "string"},
                },
                "category": {"type": "string", "description": "Primary category"},
                "license": {"type": "string", "description": "License information"},
                "custom": {
                    "type": "object",
                    "description": "Custom metadata fields",
                    "additionalProperties": True,
                },
            },
        },
    },
    "definitions": {
        "step": {
            "type": "object",
            "required": ["id", "component"],
            "properties": {
                "id": {
                    "type": "string",
                    "description": "Unique identifier for the step",
                    "pattern": "^[a-zA-Z0-9-_]+$",
                },
                "component": {
                    "type": "string",
                    "description": "Component reference (agent.capability or tool)",
                },
                "name": {
                    "type": "string",
                    "description": "Human-readable name for the step",
                },
                "description": {
                    "type": "string",
                    "description": "Detailed description of the step",
                },
                "inputs": {
                    "type": "object",
                    "description": "Input mappings for the step",
                    "additionalProperties": {
                        "type": "string",
                        "description": "Template string or direct value",
                    },
                },
                "outputs": {
                    "type": "object",
                    "description": "Output mappings from the step",
                    "additionalProperties": {
                        "type": "string",
                        "description": "Template string or direct value",
                    },
                },
                "condition": {
                    "type": "string",
                    "description": "Condition for step execution (template string that evaluates to boolean)",
                },
                "retry": {
                    "type": "object",
                    "description": "Retry configuration for the step",
                    "properties": {
                        "max_attempts": {
                            "type": "integer",
                            "description": "Maximum number of retry attempts",
                            "minimum": 0,
                        },
                        "delay_seconds": {
                            "type": "integer",
                            "description": "Delay between retries in seconds",
                            "minimum": 0,
                        },
                        "backoff_multiplier": {
                            "type": "number",
                            "description": "Multiplier for exponential backoff",
                            "minimum": 1,
                        },
                    },
                },
                "timeout": {
                    "type": "integer",
                    "description": "Timeout for step execution in seconds",
                    "minimum": 0,
                },
                "metadata": {
                    "type": "object",
                    "description": "Additional metadata for the step",
                    "additionalProperties": True,
                },
            },
        },
        "connection": {
            "type": "object",
            "required": ["source", "target"],
            "properties": {
                "source": {
                    "type": "string",
                    "description": "Source step ID and output (format: stepId.output or stepId)",
                },
                "target": {
                    "type": "string",
                    "description": "Target step ID and input (format: stepId.input or stepId)",
                },
                "condition": {
                    "type": "string",
                    "description": "Condition for connection activation (template string that evaluates to boolean)",
                },
                "transform": {
                    "type": "string",
                    "description": "Transformation to apply to the data (template string)",
                },
            },
        },
        "parameter": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "Data type of the parameter",
                    "enum": [
                        "string",
                        "number",
                        "integer",
                        "boolean",
                        "object",
                        "array",
                        "any",
                    ],
                },
                "description": {
                    "type": "string",
                    "description": "Description of the parameter",
                },
                "default": {"description": "Default value for the parameter"},
                "required": {
                    "type": "boolean",
                    "description": "Whether the parameter is required",
                    "default": False,
                },
                "enum": {
                    "type": "array",
                    "description": "Enumeration of allowed values",
                },
                "pattern": {
                    "type": "string",
                    "description": "Regex pattern for string validation",
                },
                "minimum": {
                    "type": "number",
                    "description": "Minimum value for number validation",
                },
                "maximum": {
                    "type": "number",
                    "description": "Maximum value for number validation",
                },
                "format": {
                    "type": "string",
                    "description": "Format specifier (e.g., date-time, email, uri)",
                },
            },
        },
    },
}


class WorkflowValidator:
    """Validator for workflow schemas."""

    def __init__(self, schema: Optional[Dict[str, Any]] = None):
        """
        Initialize a workflow validator.

        Args:
            schema: Custom schema to use for validation (defaults to WORKFLOW_SCHEMA)
        """
        self.schema = schema or WORKFLOW_SCHEMA

    def validate(self, workflow: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate a workflow against the schema.

        Args:
            workflow: Workflow definition to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            jsonschema.validate(instance=workflow, schema=self.schema)
            return True, None
        except jsonschema.exceptions.ValidationError as e:
            return False, str(e)

    def validate_step(self, step: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate a step against the schema.

        Args:
            step: Step definition to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            step_schema = self.schema["definitions"]["step"]
            jsonschema.validate(instance=step, schema=step_schema)
            return True, None
        except jsonschema.exceptions.ValidationError as e:
            return False, str(e)


class WorkflowVersion:
    """Handles workflow versioning."""

    @staticmethod
    def compare(version1: str, version2: str) -> int:
        """
        Compare two semantic versions.

        Args:
            version1: First version string
            version2: Second version string

        Returns:
            -1 if version1 < version2, 0 if equal, 1 if version1 > version2
        """
        return semver.compare(version1, version2)

    @staticmethod
    def is_compatible(required_version: str, actual_version: str) -> bool:
        """
        Check if the actual version is compatible with the required version.

        Args:
            required_version: Version requirement (e.g., ">=1.2.0")
            actual_version: Actual version to check

        Returns:
            True if compatible, False otherwise
        """
        try:
            return semver.match(actual_version, required_version)
        except ValueError:
            # Handle invalid version strings
            return False

    @staticmethod
    def increment(version: str, release_type: str = "patch") -> str:
        """
        Increment a version according to semantic versioning.

        Args:
            version: Version to increment
            release_type: Type of release (major, minor, patch)

        Returns:
            Incremented version string
        """
        if release_type == "major":
            return str(semver.VersionInfo.parse(version).bump_major())
        elif release_type == "minor":
            return str(semver.VersionInfo.parse(version).bump_minor())
        else:  # patch by default
            return str(semver.VersionInfo.parse(version).bump_patch())


class WorkflowMetadata:
    """Handles workflow metadata extraction and manipulation."""

    @staticmethod
    def extract(workflow: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract metadata from a workflow.

        Args:
            workflow: Workflow definition

        Returns:
            Dictionary of metadata
        """
        # Get the metadata section or create empty dict if not present
        metadata = workflow.get("metadata", {})

        # Add standard fields from the workflow
        result = {
            "id": workflow.get("id", ""),
            "version": workflow.get("version", "1.0.0"),
            "name": workflow.get("name", ""),
            "description": workflow.get("description", ""),
            "step_count": len(workflow.get("steps", [])),
        }

        # Add metadata fields
        result.update(
            {
                "author": metadata.get("author", ""),
                "created": metadata.get("created", ""),
                "updated": metadata.get("updated", ""),
                "tags": metadata.get("tags", []),
                "category": metadata.get("category", ""),
                "license": metadata.get("license", ""),
            }
        )

        # Add custom metadata if present
        if "custom" in metadata:
            result["custom"] = metadata["custom"]

        return result

    @staticmethod
    def get_tags(workflow: Dict[str, Any]) -> List[str]:
        """
        Get tags from a workflow.

        Args:
            workflow: Workflow definition

        Returns:
            List of tags
        """
        if "metadata" in workflow and "tags" in workflow["metadata"]:
            return workflow["metadata"]["tags"]
        return []

    @staticmethod
    def categorize(workflows: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Categorize workflows by their category.

        Args:
            workflows: List of workflow definitions

        Returns:
            Dictionary of {category: [workflows]}
        """
        categories: Dict[str, List[Dict[str, Any]]] = {}

        for workflow in workflows:
            category = "uncategorized"
            if "metadata" in workflow and "category" in workflow["metadata"]:
                category = workflow["metadata"]["category"]

            if category not in categories:
                categories[category] = []

            categories[category].append(workflow)

        return categories
