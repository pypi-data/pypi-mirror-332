"""
Tests for the serialization framework.

This module contains tests for the serialization framework used by the state
management system.
"""

import datetime
import json
import unittest
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Set, Any

from openagents_json.core.state.serialization import (
    JsonSerializer,
    CustomJSONEncoder,
    json_object_hook,
    get_serializer,
)


class TestEnum(Enum):
    """Test enum for serialization testing."""
    
    VALUE1 = "value1"
    VALUE2 = "value2"


@dataclass
class TestModel:
    """Test model for serialization testing."""
    
    name: str
    value: int
    tags: Set[str] = field(default_factory=set)
    
    def dict(self):
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "value": self.value,
            "tags": list(self.tags),
        }


class TestJsonSerializer(unittest.TestCase):
    """Tests for the JsonSerializer class."""
    
    def setUp(self):
        """Set up the test case."""
        self.serializer = JsonSerializer()
        
    def test_serialize_primitive_types(self):
        """Test serialization of primitive types."""
        # Test string
        self.assertEqual(self.serializer.serialize("test"), '"test"')
        
        # Test integer
        self.assertEqual(self.serializer.serialize(42), "42")
        
        # Test float
        self.assertEqual(self.serializer.serialize(3.14), "3.14")
        
        # Test boolean
        self.assertEqual(self.serializer.serialize(True), "true")
        self.assertEqual(self.serializer.serialize(False), "false")
        
        # Test None
        self.assertEqual(self.serializer.serialize(None), "null")
        
    def test_serialize_complex_types(self):
        """Test serialization of complex types."""
        # Test list
        self.assertEqual(self.serializer.serialize([1, 2, 3]), "[1, 2, 3]")
        
        # Test dictionary
        self.assertEqual(
            json.loads(self.serializer.serialize({"a": 1, "b": 2})),
            {"a": 1, "b": 2}
        )
        
    def test_serialize_datetime(self):
        """Test serialization of datetime objects."""
        dt = datetime.datetime(2023, 1, 1, 12, 0, 0)
        serialized = self.serializer.serialize(dt)
        data = json.loads(serialized)
        
        self.assertEqual(data["__type__"], "datetime")
        self.assertEqual(data["value"], "2023-01-01T12:00:00")
        
    def test_serialize_uuid(self):
        """Test serialization of UUID objects."""
        uid = uuid.UUID("12345678-1234-5678-1234-567812345678")
        serialized = self.serializer.serialize(uid)
        data = json.loads(serialized)
        
        self.assertEqual(data["__type__"], "uuid")
        self.assertEqual(data["value"], "12345678-1234-5678-1234-567812345678")
        
    def test_serialize_enum(self):
        """Test serialization of Enum objects."""
        enum_value = TestEnum.VALUE1
        serialized = self.serializer.serialize(enum_value)
        data = json.loads(serialized)
        
        self.assertEqual(data["__type__"], "enum")
        self.assertEqual(data["class"], "TestEnum")
        self.assertEqual(data["value"], "value1")
        
    def test_serialize_set(self):
        """Test serialization of Set objects."""
        set_value = {1, 2, 3}
        serialized = self.serializer.serialize(set_value)
        data = json.loads(serialized)
        
        self.assertEqual(data["__type__"], "set")
        self.assertCountEqual(data["value"], [1, 2, 3])
        
    def test_serialize_model(self):
        """Test serialization of model objects with dict method."""
        model = TestModel(name="test", value=42, tags={"tag1", "tag2"})
        serialized = self.serializer.serialize(model)
        data = json.loads(serialized)
        
        self.assertEqual(data["__type__"], "model")
        self.assertEqual(data["class"], "TestModel")
        self.assertEqual(data["value"]["name"], "test")
        self.assertEqual(data["value"]["value"], 42)
        self.assertCountEqual(data["value"]["tags"], ["tag1", "tag2"])
        
    def test_deserialize_primitive_types(self):
        """Test deserialization of primitive types."""
        # Test string
        self.assertEqual(self.serializer.deserialize('"test"'), "test")
        
        # Test integer
        self.assertEqual(self.serializer.deserialize("42"), 42)
        
        # Test float
        self.assertEqual(self.serializer.deserialize("3.14"), 3.14)
        
        # Test boolean
        self.assertEqual(self.serializer.deserialize("true"), True)
        self.assertEqual(self.serializer.deserialize("false"), False)
        
        # Test None
        self.assertEqual(self.serializer.deserialize("null"), None)
        
    def test_deserialize_complex_types(self):
        """Test deserialization of complex types."""
        # Test list
        self.assertEqual(self.serializer.deserialize("[1, 2, 3]"), [1, 2, 3])
        
        # Test dictionary
        self.assertEqual(
            self.serializer.deserialize('{"a": 1, "b": 2}'),
            {"a": 1, "b": 2}
        )
        
    def test_deserialize_datetime(self):
        """Test deserialization of datetime objects."""
        serialized = '{"__type__": "datetime", "value": "2023-01-01T12:00:00"}'
        deserialized = self.serializer.deserialize(serialized)
        
        self.assertIsInstance(deserialized, datetime.datetime)
        self.assertEqual(deserialized.year, 2023)
        self.assertEqual(deserialized.month, 1)
        self.assertEqual(deserialized.day, 1)
        self.assertEqual(deserialized.hour, 12)
        self.assertEqual(deserialized.minute, 0)
        self.assertEqual(deserialized.second, 0)
        
    def test_deserialize_uuid(self):
        """Test deserialization of UUID objects."""
        serialized = '{"__type__": "uuid", "value": "12345678-1234-5678-1234-567812345678"}'
        deserialized = self.serializer.deserialize(serialized)
        
        self.assertIsInstance(deserialized, uuid.UUID)
        self.assertEqual(str(deserialized), "12345678-1234-5678-1234-567812345678")
        
    def test_deserialize_set(self):
        """Test deserialization of Set objects."""
        serialized = '{"__type__": "set", "value": [1, 2, 3]}'
        deserialized = self.serializer.deserialize(serialized)
        
        self.assertIsInstance(deserialized, set)
        self.assertEqual(deserialized, {1, 2, 3})
        
    def test_get_serializer(self):
        """Test get_serializer function."""
        serializer = get_serializer("json")
        self.assertIsInstance(serializer, JsonSerializer)
        
        # Test with invalid serializer name
        with self.assertRaises(ValueError):
            get_serializer("invalid")


if __name__ == "__main__":
    unittest.main() 