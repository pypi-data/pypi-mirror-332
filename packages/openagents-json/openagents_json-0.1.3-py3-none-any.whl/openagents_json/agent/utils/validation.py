"""
Validation utilities for OpenAgents JSON agents.

This module provides utilities for validating agent inputs and outputs,
including schema validation and type checking.
"""

import json
import logging
from typing import Any, Callable, Dict, List, Optional, Type, Union, get_type_hints, cast

import jsonschema
from pydantic import BaseModel, ValidationError, create_model

logger = logging.getLogger(__name__)


def validate_inputs(
    func: Callable[..., Any],
    inputs: Dict[str, Any],
    schema: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Validate inputs against a function's type hints or schema.
    
    Args:
        func: The function to validate inputs for
        inputs: The input values to validate
        schema: Optional JSON schema to validate against
        
    Returns:
        The validated inputs
        
    Raises:
        ValueError: If inputs are invalid
    """
    if schema:
        # Validate against provided schema
        try:
            jsonschema.validate(instance=inputs, schema=schema)
            return dict(inputs)  # Return a copy
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(f"Input validation failed: {str(e)}")
    
    # Create a Pydantic model from function type hints
    type_hints = get_type_hints(func)
    input_fields: Dict[str, Any] = {}
    
    # Extract parameter types and defaults from function signature
    for param_name in getattr(func, "__annotations__", {}):
        if param_name == "return":
            continue
            
        param_type = type_hints.get(param_name, Any)
        
        # Check if parameter has a default value
        default = ...  # This means the field is required
        if hasattr(func, "__defaults__") and func.__defaults__:
            code_varnames = getattr(func, "__code__", None)
            if code_varnames and hasattr(code_varnames, "co_varnames"):
                if param_name in code_varnames.co_varnames:
                    idx = code_varnames.co_varnames.index(param_name) - (code_varnames.co_argcount - len(func.__defaults__))
                    if 0 <= idx < len(func.__defaults__):
                        default = func.__defaults__[idx]
        
        input_fields[param_name] = (param_type, default)
    
    # If there are no input fields, return the inputs as is
    if not input_fields:
        # Create a new dict and explicitly cast it to Dict[str, Any] for type checker
        result: Dict[str, Any] = {}
        for key, value in inputs.items():
            result[key] = value
        return result
    
    # Create a model with the input fields
    model = create_model("InputModel", **input_fields)
    
    try:
        # Validate inputs against the model
        validated = model(**inputs)
        # In Pydantic v2, use model_dump() instead of dict()
        return validated.model_dump()
    except ValidationError as e:
        raise ValueError(f"Input validation failed: {str(e)}")


def validate_outputs(
    outputs: Any,
    schema: Optional[Dict[str, Any]] = None,
    expected_type: Optional[Type[Any]] = None,
) -> Any:
    """
    Validate outputs against a schema or expected type.
    
    Args:
        outputs: The output values to validate
        schema: Optional JSON schema to validate against
        expected_type: Optional expected type
        
    Returns:
        The validated outputs
        
    Raises:
        ValueError: If outputs are invalid
    """
    if schema:
        # Validate against provided schema
        try:
            jsonschema.validate(instance=outputs, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(f"Output validation failed: {str(e)}")
    
    if expected_type:
        # Check if outputs match the expected type
        if not isinstance(outputs, expected_type):
            raise ValueError(f"Output validation failed: expected {expected_type.__name__}, got {type(outputs).__name__}")
    
    return outputs


def create_schema_from_type(type_hint: Type[Any]) -> Dict[str, Any]:
    """
    Create a JSON schema from a type hint.
    
    Args:
        type_hint: The type hint to convert
        
    Returns:
        JSON schema for the type
    """
    # Handle basic types
    if type_hint == int:
        return {"type": "integer"}
    elif type_hint == float:
        return {"type": "number"}
    elif type_hint == str:
        return {"type": "string"}
    elif type_hint == bool:
        return {"type": "boolean"}
    elif type_hint == list or type_hint == List:
        return {"type": "array"}
    elif type_hint == dict or type_hint == Dict:
        return {"type": "object"}
    
    # Handle Pydantic models
    if isinstance(type_hint, type) and issubclass(type_hint, BaseModel):
        schema: Dict[str, Any] = {"type": "object", "properties": {}, "required": []}
        
        # In Pydantic v2, use model_fields instead of __fields__
        for field_name, field in type_hint.model_fields.items():
            # Make sure field.annotation is not None before passing it to create_schema_from_type
            if hasattr(field, "annotation") and field.annotation is not None:
                field_schema = create_schema_from_type(cast(Type[Any], field.annotation))
                schema["properties"][field_name] = field_schema
                
                if hasattr(field, "is_required") and callable(field.is_required) and field.is_required():
                    if "required" not in schema:
                        schema["required"] = []
                    schema["required"].append(field_name)
        
        return schema
    
    # Default to "any" type
    return {}


def validate_agent_config(config: Dict[str, Any], schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate an agent configuration against a schema.
    
    Args:
        config: The agent configuration
        schema: JSON schema to validate against
        
    Returns:
        The validated configuration
        
    Raises:
        ValueError: If the configuration is invalid
    """
    try:
        jsonschema.validate(instance=config, schema=schema)
        return config
    except jsonschema.exceptions.ValidationError as e:
        raise ValueError(f"Agent configuration validation failed: {str(e)}") 