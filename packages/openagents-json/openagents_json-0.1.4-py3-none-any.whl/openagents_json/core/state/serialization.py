"""
Serialization framework for state management.

This module provides classes and utilities for serializing and deserializing
state objects for persistent storage.
"""

import abc
import datetime
import json
import uuid
from enum import Enum
from typing import Any, Dict, Optional, Type, Set

from openagents_json.core.state.base import StateSerializationError, StateDeserializationError


class Serializer(abc.ABC):
    """Interface for serializing/deserializing objects."""
    
    @abc.abstractmethod
    def serialize(self, value: Any) -> Any:
        """
        Convert object to serialized format.
        
        Args:
            value: Object to serialize
            
        Returns:
            Serialized representation of the object
            
        Raises:
            StateSerializationError: If serialization fails
        """
        pass
        
    @abc.abstractmethod
    def deserialize(self, data: Any, cls: Optional[Type] = None) -> Any:
        """
        Convert serialized data back to object.
        
        Args:
            data: Serialized data to deserialize
            cls: Optional class type hint for deserialization
            
        Returns:
            Deserialized object
            
        Raises:
            StateDeserializationError: If deserialization fails
        """
        pass
        
    @abc.abstractmethod
    def supports_type(self, cls: Type) -> bool:
        """
        Check if serializer supports a type.
        
        Args:
            cls: Class to check
            
        Returns:
            True if the serializer supports the type, False otherwise
        """
        pass


class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for handling complex Python types."""
    
    def default(self, obj):
        """Handle non-standard JSON types."""
        if isinstance(obj, datetime.datetime):
            return {"__type__": "datetime", "value": obj.isoformat()}
        if isinstance(obj, datetime.date):
            return {"__type__": "date", "value": obj.isoformat()}
        if isinstance(obj, uuid.UUID):
            return {"__type__": "uuid", "value": str(obj)}
        if isinstance(obj, Enum):
            return {"__type__": "enum", "class": obj.__class__.__name__, "value": obj.value}
        if isinstance(obj, set):
            return {"__type__": "set", "value": list(obj)}
        if isinstance(obj, bytes):
            return {"__type__": "bytes", "value": obj.hex()}
        if hasattr(obj, "__serialize__") and callable(obj.__serialize__):
            return obj.__serialize__()
        if hasattr(obj, "dict") and callable(obj.dict):
            # Support for Pydantic models
            return {"__type__": "model", "class": obj.__class__.__name__, "value": obj.dict()}
            
        return super().default(obj)


def json_object_hook(obj):
    """Handle special types during JSON deserialization."""
    if not isinstance(obj, dict) or "__type__" not in obj:
        return obj
        
    obj_type = obj["__type__"]
    
    if obj_type == "datetime":
        return datetime.datetime.fromisoformat(obj["value"])
    if obj_type == "date":
        return datetime.date.fromisoformat(obj["value"])
    if obj_type == "uuid":
        return uuid.UUID(obj["value"])
    if obj_type == "set":
        return set(obj["value"])
    if obj_type == "bytes":
        return bytes.fromhex(obj["value"])
        
    # More complex types might need a registry for proper reconstruction
    return obj


class JsonSerializer(Serializer):
    """JSON serializer for human-readable state storage."""
    
    def serialize(self, value: Any) -> str:
        """Serialize to JSON string."""
        try:
            return json.dumps(value, cls=CustomJSONEncoder)
        except TypeError as e:
            raise StateSerializationError(f"Cannot serialize {type(value).__name__}: {e}")
            
    def deserialize(self, data: str, cls: Optional[Type] = None) -> Any:
        """Deserialize from JSON string."""
        if not data:
            return None
            
        try:
            return json.loads(data, object_hook=json_object_hook)
        except json.JSONDecodeError as e:
            raise StateDeserializationError(f"Cannot deserialize JSON: {e}")
            
    def supports_type(self, cls: Type) -> bool:
        """Check if type is JSON-serializable."""
        # Most types can be serialized to JSON with our custom encoder
        return True


# Registry of serializers by name
_serializers = {
    "json": JsonSerializer(),
}


def get_serializer(name: str = "json") -> Serializer:
    """
    Get a serializer by name.
    
    Args:
        name: Name of the serializer
        
    Returns:
        Serializer instance
        
    Raises:
        ValueError: If the serializer is not found
    """
    if name not in _serializers:
        raise ValueError(f"Serializer '{name}' not found")
    return _serializers[name]


def register_serializer(name: str, serializer: Serializer) -> None:
    """
    Register a serializer with a name.
    
    Args:
        name: Name to register the serializer under
        serializer: Serializer instance
    """
    _serializers[name] = serializer 