# Workflow Validation System

This module provides a comprehensive validation system for OpenAgents JSON workflows, including schema validation, dependency checking, cycle detection, and type compatibility.

## Core Components

### Validation Framework

- **ValidationMode**: Defines validation strictness levels (STRICT, NORMAL, PERMISSIVE, NONE)
- **ValidationIssue**: Represents a single validation issue with code, message, severity, location, and suggested fix
- **ValidationResult**: Represents the result of a validation run with validity status and issues
- **ValidationPipeline**: A pipeline of validators to be run in sequence
- **ValidationRegistry**: Registry of available validators for easy access

### Built-in Validators

1. **SchemaValidator**: Validates workflows against the JSON schema
2. **SemVerValidator**: Checks semantic versioning compatibility
3. **CycleDetectionValidator**: Detects cycles in workflow connections
4. **DependencyValidator**: Ensures all step dependencies are satisfied
5. **TypeCompatibilityValidator**: Checks type compatibility in connections

## Usage Examples

### Basic Validation

```python
from openagents_json.workflow.validator import validate_workflow, ValidationMode

# Validate a workflow with default validators
result = validate_workflow(workflow_dict)

if result.valid:
    print("Workflow is valid!")
else:
    print(f"Workflow is invalid. Found {len(result.issues)} issues:")
    for issue in result.issues:
        print(f"- {issue.message} ({issue.code})")
        if issue.suggestion:
            print(f"  Suggestion: {issue.suggestion}")
```

### Custom Validation Pipeline

```python
from openagents_json.workflow.validator import (
    ValidationPipeline, ValidationMode,
    SchemaValidator, CycleDetectionValidator
)

# Create a custom pipeline with specific validators
pipeline = ValidationPipeline(
    validators=[
        SchemaValidator(),
        CycleDetectionValidator()
    ],
    mode=ValidationMode.STRICT
)

# Run validation
result = pipeline.validate(workflow_dict)
```

### Creating Custom Validators

```python
from openagents_json.workflow.validator import (
    WorkflowValidatorInterface, ValidationResult, ValidationIssue,
    ValidationLocation, ValidationSeverity, ValidationRegistry
)

@ValidationRegistry.register
class CustomValidator(WorkflowValidatorInterface):
    @property
    def id(self) -> str:
        return "custom_validator"
    
    @property
    def name(self) -> str:
        return "Custom Validator"
    
    @property
    def description(self) -> str:
        return "A custom validator for specific business rules"
    
    def validate(self, workflow, **kwargs):
        # Custom validation logic here
        valid = True
        issues = []
        
        # Example check
        if "custom_field" not in workflow:
            valid = False
            issues.append(ValidationIssue(
                code="missing_custom_field",
                message="Workflow is missing the custom_field",
                severity=ValidationSeverity.ERROR,
                location=ValidationLocation(path="/")
            ))
        
        return ValidationResult(valid=valid, issues=issues)
```

### FastAPI Integration

```python
from fastapi import FastAPI
from openagents_json.workflow.fastapi import (
    create_validation_middleware,
    apply_workflow_validation_routes,
    workflow_dependency
)
from openagents_json.workflow.validator import ValidationMode

app = FastAPI()

# Add workflow validation middleware
create_validation_middleware(app, ValidationMode.NORMAL)

# Apply workflow validation routes
apply_workflow_validation_routes(app, prefix="/workflows")

# Use the workflow dependency for endpoint validation
@app.post("/custom-workflow")
async def create_custom_workflow(workflow = workflow_dependency()):
    # The workflow is already validated at this point
    return {"status": "success", "workflow_id": workflow["id"]}
```

## OpenAPI Integration

The system supports extending OpenAPI specifications with workflow definitions using the `x-workflow` extension:

```python
from openagents_json.workflow.openapi import extend_openapi_with_workflows

# Extend OpenAPI schema with workflows
openapi_schema = app.openapi()
extended_schema = extend_openapi_with_workflows(openapi_schema, workflows)
```

## Validation Modes

- **STRICT**: Fail on all issues, including warnings
- **NORMAL**: Fail on errors only (default)
- **PERMISSIVE**: Fail only on critical errors
- **NONE**: Perform validation but don't fail (for reporting only) 