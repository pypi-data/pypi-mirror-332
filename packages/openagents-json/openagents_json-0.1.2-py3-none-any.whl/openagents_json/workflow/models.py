"""
Pydantic models for workflows.

This module provides Pydantic models for working with workflow definitions,
making it easier to create, validate, and manipulate workflows in code.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Union

from pydantic import BaseModel, Field, root_validator, validator


class RetryConfig(BaseModel):
    """Retry configuration for workflow steps."""

    max_attempts: int = Field(
        default=3, description="Maximum number of retry attempts", ge=0
    )
    delay_seconds: int = Field(
        default=5, description="Delay between retries in seconds", ge=0
    )
    backoff_multiplier: float = Field(
        default=1.0, description="Multiplier for exponential backoff", ge=1.0
    )


class Parameter(BaseModel):
    """Parameter definition for workflow inputs and outputs."""

    type: str = Field(description="Data type of the parameter")
    description: Optional[str] = Field(
        default=None, description="Description of the parameter"
    )
    default: Optional[Any] = Field(
        default=None, description="Default value for the parameter"
    )
    required: bool = Field(
        default=False, description="Whether the parameter is required"
    )
    enum: Optional[List[Any]] = Field(
        default=None, description="Enumeration of allowed values"
    )
    pattern: Optional[str] = Field(
        default=None, description="Regex pattern for string validation"
    )
    minimum: Optional[float] = Field(
        default=None, description="Minimum value for number validation"
    )
    maximum: Optional[float] = Field(
        default=None, description="Maximum value for number validation"
    )
    format: Optional[str] = Field(default=None, description="Format specifier")

    @validator("type")
    def validate_type(cls, v):
        """Validate parameter type."""
        allowed_types = [
            "string",
            "number",
            "integer",
            "boolean",
            "object",
            "array",
            "any",
        ]
        if v not in allowed_types:
            raise ValueError(
                f"Parameter type must be one of: {', '.join(allowed_types)}"
            )
        return v


class CustomMetadata(BaseModel):
    """Custom metadata for workflows or steps."""

    class Config:
        extra = "allow"


class WorkflowMetadataModel(BaseModel):
    """Metadata for workflows."""

    author: Optional[str] = Field(default=None, description="Author of the workflow")
    created: Optional[datetime] = Field(default=None, description="Creation timestamp")
    updated: Optional[datetime] = Field(
        default=None, description="Last update timestamp"
    )
    tags: List[str] = Field(default_factory=list, description="Tags for categorization")
    category: Optional[str] = Field(default=None, description="Primary category")
    license: Optional[str] = Field(default=None, description="License information")
    custom: Optional[Dict[str, Any]] = Field(
        default=None, description="Custom metadata fields"
    )


class Step(BaseModel):
    """Step in a workflow."""

    id: str = Field(description="Unique identifier for the step")
    component: str = Field(description="Component reference (agent.capability or tool)")
    name: Optional[str] = Field(
        default=None, description="Human-readable name for the step"
    )
    description: Optional[str] = Field(
        default=None, description="Detailed description of the step"
    )
    inputs: Dict[str, str] = Field(
        default_factory=dict, description="Input mappings for the step"
    )
    outputs: Dict[str, str] = Field(
        default_factory=dict, description="Output mappings from the step"
    )
    condition: Optional[str] = Field(
        default=None, description="Condition for step execution"
    )
    retry: Optional[RetryConfig] = Field(
        default=None, description="Retry configuration for the step"
    )
    timeout: Optional[int] = Field(
        default=None, description="Timeout for step execution in seconds", ge=0
    )
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional metadata for the step"
    )

    @validator("id")
    def validate_id(cls, v):
        """Validate step ID."""
        if not v:
            raise ValueError("Step ID cannot be empty")
        if not v.replace("_", "").replace("-", "").isalnum():
            raise ValueError(
                "Step ID can only contain alphanumeric characters, underscores, and hyphens"
            )
        return v


class Connection(BaseModel):
    """Connection between steps in a workflow."""

    source: str = Field(description="Source step ID and output")
    target: str = Field(description="Target step ID and input")
    condition: Optional[str] = Field(
        default=None, description="Condition for connection activation"
    )
    transform: Optional[str] = Field(
        default=None, description="Transformation to apply to the data"
    )


class Workflow(BaseModel):
    """Workflow definition."""

    id: str = Field(description="Unique identifier for the workflow")
    version: str = Field(
        default="1.0.0", description="Semantic version of the workflow"
    )
    name: Optional[str] = Field(
        default=None, description="Human-readable name for the workflow"
    )
    description: Optional[str] = Field(
        default=None, description="Detailed description of the workflow"
    )
    steps: List[Step] = Field(description="Sequential steps in the workflow")
    connections: List[Connection] = Field(
        default_factory=list, description="Connections between steps"
    )
    inputs: Dict[str, Parameter] = Field(
        default_factory=dict, description="Input definition for the workflow"
    )
    outputs: Dict[str, Parameter] = Field(
        default_factory=dict, description="Output definition for the workflow"
    )
    metadata: Optional[WorkflowMetadataModel] = Field(
        default=None, description="Additional metadata for the workflow"
    )

    @validator("id")
    def validate_id(cls, v):
        """Validate workflow ID."""
        if not v:
            raise ValueError("Workflow ID cannot be empty")
        if not v.replace("_", "").replace("-", "").isalnum():
            raise ValueError(
                "Workflow ID can only contain alphanumeric characters, underscores, and hyphens"
            )
        return v

    @validator("version")
    def validate_version(cls, v):
        """Validate workflow version."""
        import re

        pattern = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
        if not re.match(pattern, v):
            raise ValueError(
                "Version must follow semantic versioning format (major.minor.patch)"
            )
        return v

    @root_validator
    def validate_step_ids_unique(cls, values):
        """Validate that step IDs are unique."""
        if "steps" in values:
            step_ids = [step.id for step in values["steps"]]
            if len(step_ids) != len(set(step_ids)):
                raise ValueError("Step IDs must be unique within a workflow")
        return values

    def to_dict(self) -> Dict[str, Any]:
        """Convert workflow to dictionary for schema validation."""
        return self.dict(exclude_none=True)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Workflow":
        """Create workflow from dictionary."""
        # Convert inputs and outputs to Parameter objects
        if "inputs" in data:
            for key, value in data["inputs"].items():
                if not isinstance(value, dict):
                    data["inputs"][key] = {"type": "any", "description": str(value)}

        if "outputs" in data:
            for key, value in data["outputs"].items():
                if not isinstance(value, dict):
                    data["outputs"][key] = {"type": "any", "description": str(value)}

        # Convert steps if they are dictionaries
        if "steps" in data and isinstance(data["steps"], list):
            for i, step in enumerate(data["steps"]):
                if (
                    isinstance(step, dict)
                    and "retry" in step
                    and isinstance(step["retry"], dict)
                ):
                    data["steps"][i]["retry"] = RetryConfig(**step["retry"])

        return cls(**data)
