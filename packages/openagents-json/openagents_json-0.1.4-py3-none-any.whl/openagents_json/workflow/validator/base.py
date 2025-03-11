"""
Base validator interface for workflow validation.

This module defines the base classes and interfaces for the validation system,
including the validation pipeline, validator interface, and validation results.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple, Type

from pydantic import BaseModel, Field


class ValidationSeverity(str, Enum):
    """Severity levels for validation issues."""

    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class ValidationLocation(BaseModel):
    """Location of a validation issue within a workflow."""

    path: str = Field(description="JSON path to the issue location")
    step_id: Optional[str] = Field(
        default=None, description="ID of the affected step if applicable"
    )
    connection_index: Optional[int] = Field(
        default=None, description="Index of the affected connection if applicable"
    )
    field: Optional[str] = Field(default=None, description="Name of the affected field")


class ValidationIssue(BaseModel):
    """Represents a single validation issue."""

    code: str = Field(description="Unique code identifying the issue type")
    message: str = Field(description="Human-readable description of the issue")
    severity: ValidationSeverity = Field(
        default=ValidationSeverity.ERROR, description="Severity level"
    )
    location: ValidationLocation = Field(
        description="Location of the issue in the workflow"
    )
    suggestion: Optional[str] = Field(
        default=None, description="Suggested fix for the issue"
    )
    details: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional details about the issue"
    )


class ValidationResult(BaseModel):
    """Results of a validation run."""

    valid: bool = Field(
        description="Whether the workflow is valid according to this validator"
    )
    issues: List[ValidationIssue] = Field(
        default_factory=list, description="List of validation issues found"
    )

    def __bool__(self) -> bool:
        """Return True if the validation passed, False otherwise."""
        return self.valid

    def merge(self, other: "ValidationResult") -> "ValidationResult":
        """Merge another validation result into this one."""
        return ValidationResult(
            valid=self.valid and other.valid, issues=self.issues + other.issues
        )


class ValidationMode(str, Enum):
    """Validation modes for the validation system."""

    STRICT = "strict"  # Fail on all issues, including warnings
    NORMAL = "normal"  # Fail on errors only
    PERMISSIVE = "permissive"  # Fail on critical errors only
    NONE = "none"  # No validation


class WorkflowValidatorInterface(ABC):
    """Base interface for workflow validators."""

    @property
    @abstractmethod
    def id(self) -> str:
        """Get the unique identifier for this validator."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Get the human-readable name for this validator."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Get the description of this validator."""
        pass

    @abstractmethod
    def validate(self, workflow: Dict[str, Any], **kwargs) -> ValidationResult:
        """
        Validate a workflow.

        Args:
            workflow: The workflow to validate
            **kwargs: Additional validator-specific parameters

        Returns:
            ValidationResult: The result of validation
        """
        pass


class ValidationPipeline:
    """A pipeline of validators to be run in sequence."""

    def __init__(
        self,
        validators: Optional[List[WorkflowValidatorInterface]] = None,
        mode: ValidationMode = ValidationMode.NORMAL,
    ):
        """
        Initialize a validation pipeline.

        Args:
            validators: List of validators to run
            mode: Validation mode
        """
        self.validators = validators or []
        self.mode = mode

    def add_validator(self, validator: WorkflowValidatorInterface) -> None:
        """Add a validator to the pipeline."""
        self.validators.append(validator)

    def remove_validator(self, validator_id: str) -> bool:
        """
        Remove a validator from the pipeline by its ID.

        Args:
            validator_id: ID of the validator to remove

        Returns:
            bool: True if a validator was removed, False otherwise
        """
        initial_length = len(self.validators)
        self.validators = [v for v in self.validators if v.id != validator_id]
        return len(self.validators) < initial_length

    def validate(self, workflow: Dict[str, Any], **kwargs) -> ValidationResult:
        """
        Run all validators on a workflow.

        Args:
            workflow: The workflow to validate
            **kwargs: Additional validator-specific parameters

        Returns:
            ValidationResult: The combined result of all validators
        """
        if not self.validators:
            return ValidationResult(valid=True, issues=[])

        result = ValidationResult(valid=True, issues=[])

        for validator in self.validators:
            validator_result = validator.validate(workflow, **kwargs)
            result = result.merge(validator_result)

            # In strict mode, stop on first failure
            if self.mode == ValidationMode.STRICT and not validator_result.valid:
                break

        # Apply validation mode filtering
        if self.mode == ValidationMode.PERMISSIVE:
            # Only consider errors as failures in permissive mode
            critical_issues = [
                issue
                for issue in result.issues
                if issue.severity == ValidationSeverity.ERROR
            ]
            result.valid = not critical_issues
        elif self.mode == ValidationMode.NONE:
            # Consider everything valid in NONE mode
            result.valid = True

        return result


class ValidationRegistry:
    """Registry of available validators."""

    _validators: Dict[str, Type[WorkflowValidatorInterface]] = {}

    @classmethod
    def register(
        cls, validator_class: Type[WorkflowValidatorInterface]
    ) -> Type[WorkflowValidatorInterface]:
        """
        Register a validator.

        Args:
            validator_class: The validator class to register

        Returns:
            The registered validator class
        """
        instance = validator_class()
        cls._validators[instance.id] = validator_class
        return validator_class

    @classmethod
    def get_validator(
        cls, validator_id: str
    ) -> Optional[Type[WorkflowValidatorInterface]]:
        """Get a validator by ID."""
        return cls._validators.get(validator_id)

    @classmethod
    def get_all_validators(cls) -> Dict[str, Type[WorkflowValidatorInterface]]:
        """Get all registered validators."""
        return cls._validators.copy()

    @classmethod
    def create_pipeline(
        cls,
        validator_ids: Optional[List[str]] = None,
        mode: ValidationMode = ValidationMode.NORMAL,
    ) -> ValidationPipeline:
        """
        Create a validation pipeline with specified validators.

        Args:
            validator_ids: List of validator IDs to include, or None for all validators
            mode: Validation mode

        Returns:
            ValidationPipeline: A pipeline with the requested validators
        """
        if validator_ids is None:
            validators = [v_class() for v_class in cls._validators.values()]
        else:
            validators = []
            for v_id in validator_ids:
                if v_class := cls.get_validator(v_id):
                    validators.append(v_class())

        return ValidationPipeline(validators, mode)
