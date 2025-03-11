"""
Workflow validation components.

This package provides a comprehensive validation system for workflows,
including schema validation, dependency checking, and type compatibility.
"""

from openagents_json.workflow.validator.base import (
    ValidationIssue,
    ValidationLocation,
    ValidationMode,
    ValidationPipeline,
    ValidationRegistry,
    ValidationResult,
    ValidationSeverity,
    WorkflowValidatorInterface,
)
from openagents_json.workflow.validator.logic import (
    CycleDetectionValidator,
    DependencyValidator,
    TypeCompatibilityValidator,
)
from openagents_json.workflow.validator.schema import SchemaValidator, SemVerValidator

# Re-export for convenience
__all__ = [
    "ValidationMode",
    "ValidationSeverity",
    "ValidationLocation",
    "ValidationIssue",
    "ValidationResult",
    "WorkflowValidatorInterface",
    "ValidationPipeline",
    "ValidationRegistry",
    "SchemaValidator",
    "SemVerValidator",
    "CycleDetectionValidator",
    "DependencyValidator",
    "TypeCompatibilityValidator",
    "create_default_pipeline",
    "validate_workflow",
]


def create_default_pipeline(
    mode: ValidationMode = ValidationMode.NORMAL,
) -> ValidationPipeline:
    """
    Create a default validation pipeline with all registered validators.

    Args:
        mode: Validation mode for the pipeline

    Returns:
        ValidationPipeline: A pipeline with all registered validators
    """
    return ValidationRegistry.create_pipeline(mode=mode)


def validate_workflow(
    workflow: dict, mode: ValidationMode = ValidationMode.NORMAL
) -> ValidationResult:
    """
    Validate a workflow using the default validation pipeline.

    Args:
        workflow: The workflow to validate
        mode: Validation mode

    Returns:
        ValidationResult: The result of validation
    """
    pipeline = create_default_pipeline(mode)
    return pipeline.validate(workflow)
