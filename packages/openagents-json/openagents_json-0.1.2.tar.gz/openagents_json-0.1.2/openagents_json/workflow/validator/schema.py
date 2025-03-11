"""
Schema-based workflow validator.

This module provides a validator that checks workflow definitions against the JSON schema.
"""

import json
from typing import Any, Dict, List, Optional, Tuple

import jsonschema

from openagents_json.workflow.schema import WORKFLOW_SCHEMA
from openagents_json.workflow.validator.base import (
    ValidationIssue,
    ValidationLocation,
    ValidationRegistry,
    ValidationResult,
    ValidationSeverity,
    WorkflowValidatorInterface,
)


@ValidationRegistry.register
class SchemaValidator(WorkflowValidatorInterface):
    """Validator that checks workflow definitions against the JSON schema."""

    @property
    def id(self) -> str:
        return "schema_validator"

    @property
    def name(self) -> str:
        return "Schema Validator"

    @property
    def description(self) -> str:
        return "Validates workflow definitions against the JSON schema"

    def validate(self, workflow: Dict[str, Any], **kwargs) -> ValidationResult:
        """
        Validate a workflow against the JSON schema.

        Args:
            workflow: The workflow to validate
            schema: Optional custom schema to validate against

        Returns:
            ValidationResult: The result of validation
        """
        schema = kwargs.get("schema", WORKFLOW_SCHEMA)
        validator = jsonschema.Draft7Validator(schema)
        errors = list(validator.iter_errors(workflow))

        if not errors:
            return ValidationResult(valid=True, issues=[])

        issues = [self._create_issue_from_error(error, workflow) for error in errors]
        return ValidationResult(valid=False, issues=issues)

    def _create_issue_from_error(
        self, error: jsonschema.exceptions.ValidationError, workflow: Dict[str, Any]
    ) -> ValidationIssue:
        """Create a validation issue from a jsonschema error."""
        # Format the JSON path
        path = "/".join(str(p) for p in error.path) if error.path else "/"

        # Extract location information
        location_info = self._extract_location_info(error, workflow)

        # Create validation issue
        issue = ValidationIssue(
            code=f"schema_error.{error.validator}",
            message=error.message,
            severity=ValidationSeverity.ERROR,
            location=ValidationLocation(path=path, **location_info),
            suggestion=self._create_suggestion(error),
        )

        return issue

    def _extract_location_info(
        self, error: jsonschema.exceptions.ValidationError, workflow: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Extract step_id, connection_index, and field from an error."""
        step_id = None
        connection_index = None
        field = None

        # Check if the error is in a step
        if error.path and len(error.path) >= 2 and error.path[0] == "steps":
            try:
                step_index = error.path[1]
                if isinstance(step_index, int) and step_index < len(
                    workflow.get("steps", [])
                ):
                    step = workflow["steps"][step_index]
                    step_id = step.get("id")
                    if len(error.path) > 2:
                        field = str(error.path[-1])
            except (KeyError, IndexError, TypeError):
                pass

        # Check if the error is in a connection
        if error.path and len(error.path) >= 2 and error.path[0] == "connections":
            try:
                connection_index = error.path[1]
                if not isinstance(connection_index, int):
                    connection_index = None
                elif len(error.path) > 2:
                    field = str(error.path[-1])
            except (IndexError, TypeError):
                pass

        return {
            "step_id": step_id,
            "connection_index": connection_index,
            "field": field,
        }

    def _create_suggestion(
        self, error: jsonschema.exceptions.ValidationError
    ) -> Optional[str]:
        """Create a suggestion for fixing the error."""
        if error.validator == "required":
            missing_props = error.validator_value
            if isinstance(missing_props, list) and missing_props:
                props_str = ", ".join(f'"{prop}"' for prop in missing_props)
                return f"Add required properties: {props_str}"

        elif error.validator == "pattern":
            return f"Value must match pattern: {error.validator_value}"

        elif error.validator == "type":
            return f"Expected type: {error.validator_value}"

        return None


@ValidationRegistry.register
class SemVerValidator(WorkflowValidatorInterface):
    """Validator that checks semantic versioning compatibility."""

    @property
    def id(self) -> str:
        return "semver_validator"

    @property
    def name(self) -> str:
        return "Semantic Version Validator"

    @property
    def description(self) -> str:
        return "Validates workflow semantic versioning compatibility"

    def validate(self, workflow: Dict[str, Any], **kwargs) -> ValidationResult:
        """
        Validate workflow version compatibility.

        Args:
            workflow: The workflow to validate
            required_version: Optional required version to validate against

        Returns:
            ValidationResult: The result of validation
        """
        from openagents_json.workflow.schema import SCHEMA_VERSION, WorkflowVersion

        required_version = kwargs.get("required_version", SCHEMA_VERSION)
        workflow_version = workflow.get("version", "1.0.0")

        if not WorkflowVersion.is_compatible(required_version, workflow_version):
            issue = ValidationIssue(
                code="version_incompatible",
                message=f"Workflow version '{workflow_version}' is not compatible with required version '{required_version}'",
                severity=ValidationSeverity.ERROR,
                location=ValidationLocation(path="version", field="version"),
                suggestion=f"Update workflow version to be compatible with '{required_version}'",
            )
            return ValidationResult(valid=False, issues=[issue])

        return ValidationResult(valid=True, issues=[])
