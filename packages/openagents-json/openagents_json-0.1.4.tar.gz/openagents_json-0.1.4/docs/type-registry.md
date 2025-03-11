# Type Registry System

The OpenAgents JSON library implements a robust Type Registry System to safely handle type serialization and deserialization. This system replaces the previous unsafe practice of using `str(param_type)` and `eval()` for handling types.

## Overview

When creating tools and capabilities, the system needs to extract type information from function signatures and then reconstruct those types later. The Type Registry System handles this process in a safe and consistent way.

## Key Features

1. **Safe Type Serialization**
   - Converts Python types into string representations that can be safely stored and transmitted
   - Properly handles built-in types, generics, and custom classes
   - Avoids unsafe string representations like `"<class 'str'>"`

2. **Secure Type Deserialization**
   - Reconstructs types from string representations without using unsafe `eval()`
   - Uses a registry of known types to avoid security vulnerabilities
   - Provides graceful fallbacks for unknown types

3. **Support for Complex Types**
   - Handles generic types like `List[str]`, `Dict[str, int]`, etc.
   - Supports nested generics like `List[Dict[str, List[int]]]`
   - Handles custom classes when possible

## How It Works

### Type Serialization

When a function parameter or return type is serialized:

1. If it's a built-in type (str, int, etc.), just the name is used (e.g., "str")
2. If it's a generic type, it's serialized as `container[args]` (e.g., "list[str]")
3. If it's a custom class, it's serialized as `module.name` (e.g., "mypackage.MyClass")
4. Fallbacks are provided for complex cases

```python
from typing import List, Dict
from openagents_json.agent.type_registry import serialize_type

# Basic types
serialize_type(str)  # "str"
serialize_type(int)  # "int"

# Generic types
serialize_type(List[str])  # "list[str]"
serialize_type(Dict[str, int])  # "dict[str, int]"

# Custom classes
class MyClass:
    pass

serialize_type(MyClass)  # "mypackage.MyClass"
```

### Type Deserialization

When a type string is deserialized:

1. Check if it's in the known types registry
2. If not, check if it's a built-in type
3. If it contains brackets, parse it as a generic type
4. If it contains a module path, try to import the module and get the attribute
5. Fall back to `str` if all else fails

```python
from openagents_json.agent.type_registry import deserialize_type

# Basic types
deserialize_type("str")  # <class 'str'>
deserialize_type("int")  # <class 'int'>

# Generic types
deserialize_type("list[str]")  # typing.List[str]
deserialize_type("dict[str, int]")  # typing.Dict[str, int]

# Custom classes (if importable)
deserialize_type("mypackage.MyClass")  # <class 'mypackage.MyClass'>

# Unknown types (fallback to str)
deserialize_type("UnknownType")  # <class 'str'>
```

## Benefits

- **Security**: Eliminates the use of `eval()` on potentially unsafe strings
- **Robustness**: Provides proper error handling and fallbacks
- **Maintainability**: Makes the code more readable and easier to debug
- **Compatibility**: Works with both simple and complex type systems

## Using the Type Registry

In most cases, you don't need to use the Type Registry directly. The OpenAgents JSON library handles type serialization and deserialization internally when you:

- Define tools and capabilities with typed parameters
- Access schema information for tools and capabilities
- Execute tools and capabilities with typed inputs/outputs

If you need to work with types directly, you can import the functions:

```python
from openagents_json.agent.type_registry import serialize_type, deserialize_type
```

## Error Handling

The Type Registry includes extensive error handling:

- Logs warnings when types can't be properly serialized or deserialized
- Provides reasonable defaults when exact types can't be determined
- Gracefully falls back to `str` for unknown types

This ensures that your application continues to work even when dealing with complex or custom types. 