"""
Type registry system for OpenAgents JSON.

This module provides utilities for safely serializing and deserializing types,
reducing security concerns related to eval() and improving type handling robustness.
"""

import builtins
import logging
import typing
from typing import Any, Dict, Optional, Type, Union, get_origin, get_args

logger = logging.getLogger(__name__)

# Registry of known types to avoid unsafe eval()
KNOWN_TYPES: Dict[str, Type] = {
    # Built-in types
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "set": set,
    "frozenset": frozenset,
    "bytes": bytes,
    "bytearray": bytearray,
    "None": type(None),
    "NoneType": type(None),
    
    # Common typing types
    "Any": typing.Any,
    "Optional": typing.Optional,
    "Union": typing.Union,
    "List": typing.List,
    "Dict": typing.Dict,
    "Tuple": typing.Tuple,
    "Set": typing.Set,
    "FrozenSet": typing.FrozenSet,
}

def serialize_type(param_type: Any) -> str:
    """
    Convert a Python type object into a string that can be safely deserialized.
    
    Args:
        param_type: The Python type to serialize
        
    Returns:
        A string representation of the type that can be deserialized later
    """
    # If it's already a string (fallback from prior logic), just return it
    if isinstance(param_type, str):
        return param_type
    
    # Handle None type
    if param_type is None or param_type is type(None):
        return "NoneType"
    
    # Get module and name if available
    module = getattr(param_type, '__module__', None)
    name = getattr(param_type, '__name__', None)
    
    # If it's a typing generic (like List[str])
    origin = get_origin(param_type)
    args = get_args(param_type)
    
    if origin is not None:
        # It's a generic type
        origin_str = serialize_type(origin)
        args_str = ", ".join(serialize_type(arg) for arg in args)
        return f"{origin_str}[{args_str}]"

    # If type is a built-in, just return the type's name (e.g., "str")
    if module == 'builtins' and name:
        return name

    # If we have a valid module and name, return "module.name"
    if module and name:
        return f"{module}.{name}"

    # Last resort fallback
    logger.warning(f"Couldn't properly serialize type: {param_type}, falling back to str()")
    return str(param_type)


def deserialize_type(type_str: str) -> Type:
    """
    Safely parse a string to return a Python type.
    
    Args:
        type_str: String representation of a type
        
    Returns:
        The corresponding Python type
        
    Notes:
        This function tries to avoid using eval() where possible by:
        1. Checking the KNOWN_TYPES registry
        2. Checking if it's a built-in type
        3. Using __import__ for custom module types
        4. Defaulting to str if type can't be resolved
    """
    if not isinstance(type_str, str):
        return type_str
    
    # Handle empty or None strings
    if not type_str or type_str.lower() == 'none':
        return type(None)
    
    # Check if string is in known types registry
    if type_str in KNOWN_TYPES:
        return KNOWN_TYPES[type_str]
    
    # Handle generics like List[str], Dict[str, int], etc.
    if '[' in type_str and ']' in type_str:
        # Extract the container type and parameter types
        container_type = type_str.split('[')[0].strip()
        params_str = type_str[type_str.index('[')+1:type_str.rindex(']')]
        
        # Parse parameter types
        param_types = []
        bracket_count = 0
        current_param = ""
        
        for char in params_str:
            if char == ',' and bracket_count == 0:
                param_types.append(deserialize_type(current_param.strip()))
                current_param = ""
            else:
                if char == '[':
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1
                current_param += char
        
        if current_param:
            param_types.append(deserialize_type(current_param.strip()))
        
        # Get the container type
        container = deserialize_type(container_type)
        
        # Apply the parameter types to the container
        try:
            return container[tuple(param_types)]
        except (TypeError, IndexError):
            logger.warning(f"Failed to create generic type {container}[{param_types}]")
            return container

    # Check if it's a built-in type name
    if hasattr(builtins, type_str):
        return getattr(builtins, type_str)

    # Try to import the module and get the attribute
    try:
        module_name, _, attr_name = type_str.rpartition('.')
        if module_name and attr_name:
            try:
                mod = __import__(module_name, fromlist=[attr_name])
                return getattr(mod, attr_name)
            except (ImportError, AttributeError) as e:
                logger.warning(f"Failed to import type '{type_str}': {e}")
        
        # If we can't parse or import, return str as fallback
        logger.warning(f"Could not resolve type '{type_str}', defaulting to str")
        return str
    except (ValueError, SyntaxError) as e:
        logger.warning(f"Failed to parse type string '{type_str}': {e}")
        return str 