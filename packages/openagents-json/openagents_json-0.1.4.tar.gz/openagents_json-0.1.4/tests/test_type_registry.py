"""
Tests for the type registry module.

This module tests the serialization and deserialization of various types,
including built-in types, custom classes, and generics.
"""

import unittest
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from openagents_json.agent.type_registry import serialize_type, deserialize_type


@dataclass
class CustomClass:
    """Custom class for testing type serialization/deserialization."""
    name: str
    value: int


class TypeRegistryTests(unittest.TestCase):
    """Test cases for the type registry module."""

    def test_serialize_builtin_types(self):
        """Test serialization of built-in types."""
        # Test basic Python types
        self.assertEqual(serialize_type(str), "str")
        self.assertEqual(serialize_type(int), "int")
        self.assertEqual(serialize_type(float), "float")
        self.assertEqual(serialize_type(bool), "bool")
        self.assertEqual(serialize_type(list), "list")
        self.assertEqual(serialize_type(dict), "dict")
        self.assertEqual(serialize_type(tuple), "tuple")
        self.assertEqual(serialize_type(set), "set")
        
        # Test None type
        self.assertEqual(serialize_type(type(None)), "NoneType")
        self.assertEqual(serialize_type(None), "NoneType")

    def test_serialize_generic_types(self):
        """Test serialization of generic types."""
        # Test generic container types
        self.assertEqual(serialize_type(List[str]), "list[str]")
        self.assertEqual(serialize_type(Dict[str, int]), "dict[str, int]")
        self.assertEqual(serialize_type(Set[float]), "set[float]")
        self.assertEqual(serialize_type(Tuple[int, str]), "tuple[int, str]")
        
        # Test nested generics
        self.assertEqual(serialize_type(List[Dict[str, int]]), "list[dict[str, int]]")
        self.assertEqual(serialize_type(Dict[str, List[int]]), "dict[str, list[int]]")
        
        # Test Optional and Union
        self.assertEqual(serialize_type(Optional[str]), "Union[str, NoneType]")
        self.assertEqual(serialize_type(Union[int, str]), "Union[int, str]")

    def test_serialize_custom_class(self):
        """Test serialization of custom classes."""
        # Test custom class
        serialized = serialize_type(CustomClass)
        self.assertTrue(serialized.endswith(".CustomClass"))
        self.assertTrue("test_type_registry" in serialized)

    def test_deserialize_builtin_types(self):
        """Test deserialization of built-in types."""
        # Test basic Python types
        self.assertEqual(deserialize_type("str"), str)
        self.assertEqual(deserialize_type("int"), int)
        self.assertEqual(deserialize_type("float"), float)
        self.assertEqual(deserialize_type("bool"), bool)
        self.assertEqual(deserialize_type("list"), list)
        self.assertEqual(deserialize_type("dict"), dict)
        
        # Test None type
        self.assertEqual(deserialize_type("NoneType"), type(None))
        self.assertEqual(deserialize_type("None"), type(None))
        
        # Test non-string input
        self.assertEqual(deserialize_type(str), str)

    def test_deserialize_generic_types(self):
        """Test deserialization of generic types."""
        # Note: This test may be more complex as exact equality for generics
        # might not work directly. We check more for functional equivalence.
        list_str = deserialize_type("list[str]")
        self.assertEqual(list_str.__origin__, list)
        self.assertEqual(list_str.__args__[0], str)
        
        dict_str_int = deserialize_type("dict[str, int]")
        self.assertEqual(dict_str_int.__origin__, dict)
        self.assertEqual(dict_str_int.__args__[0], str)
        self.assertEqual(dict_str_int.__args__[1], int)

    def test_deserialize_custom_class(self):
        """Test deserialization of custom classes."""
        # Register CustomClass in globals() for this test
        globals()["CustomClass"] = CustomClass
        
        # Test deserializing full module path
        module_name = CustomClass.__module__
        result = deserialize_type(f"{module_name}.CustomClass")
        self.assertEqual(result, CustomClass)

    def test_unknown_type_fallback(self):
        """Test fallback behavior for unknown types."""
        # Should return str for unknown types
        self.assertEqual(deserialize_type("UnknownType"), str)
        self.assertEqual(deserialize_type("unknown.module.Class"), str)

    def test_roundtrip(self):
        """Test round-trip serialization and deserialization."""
        # Test basic types
        for type_obj in [str, int, float, bool, list, dict, tuple, set]:
            serialized = serialize_type(type_obj)
            deserialized = deserialize_type(serialized)
            self.assertEqual(deserialized, type_obj)
        
        # Test None
        serialized = serialize_type(type(None))
        deserialized = deserialize_type(serialized)
        self.assertEqual(deserialized, type(None))
        
        # Register CustomClass in globals()
        globals()["CustomClass"] = CustomClass
        
        # Test custom class
        serialized = serialize_type(CustomClass)
        deserialized = deserialize_type(serialized)
        self.assertEqual(deserialized, CustomClass)


if __name__ == "__main__":
    unittest.main() 