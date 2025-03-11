"""
Example demonstrating the usage of enhanced decorators in OpenAgents JSON.

This example shows how to:
1. Define class-based and function-based agents
2. Use decorator configuration options
3. Create agent capabilities with metadata
4. Register tools with input/output schemas
5. Extract metadata from docstrings and type hints
"""

import asyncio
from typing import Dict, List, Optional, Union
from fastapi import FastAPI
import uvicorn

from openagents_json import OpenAgentsApp


# Create the OpenAgents application
agents_app = OpenAgentsApp()


# Class-based agent with capabilities
@agents_app.agent(
    "text_processor",
    version="1.0.0",
    description="Processes text in various ways",
    tags={"text", "processing"},
    model="gpt-4"
)
class TextProcessor:
    """
    An agent that processes text in various ways.
    
    This agent provides capabilities for manipulating text data,
    including echo, reverse, and summarize operations.
    """
    
    def __init__(self, config=None):
        self.config = config or {}
        self.model = self.config.get("model") or "gpt-4"
        
    @agents_app.capability(
        "echo",
        description="Echo back the text",
        examples=[
            {"inputs": {"text": "Hello, World!"}, "outputs": "Hello, World!"}
        ]
    )
    async def echo(self, text: str) -> str:
        """
        Echo back the text.
        
        Args:
            text: The text to echo
            
        Returns:
            The original text unchanged
        """
        return text
        
    @agents_app.capability(
        "reverse",
        description="Reverse the text",
        examples=[
            {"inputs": {"text": "Hello"}, "outputs": "olleH"}
        ]
    )
    async def reverse(self, text: str) -> str:
        """
        Reverse the text.
        
        Args:
            text: The text to reverse
            
        Returns:
            The reversed text
        """
        return text[::-1]
        
    @agents_app.capability(
        "tokenize",
        description="Split text into tokens"
    )
    async def tokenize(self, text: str, delimiter: str = " ") -> List[str]:
        """
        Split text into tokens.
        
        Args:
            text: The text to tokenize
            delimiter: The delimiter to split on (default: space)
            
        Returns:
            List of tokens
        """
        return text.split(delimiter)


# Function-based agent
@agents_app.agent(
    "calculator",
    version="0.5.0",
    description="Performs mathematical calculations"
)
async def calculate(operation: str, a: float, b: float) -> float:
    """
    Perform a mathematical calculation.
    
    Args:
        operation: The operation to perform (add, subtract, multiply, divide)
        a: First number
        b: Second number
        
    Returns:
        Result of the calculation
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")


# Standalone tool with explicit schema
@agents_app.tool(
    "uppercase",
    description="Convert text to uppercase",
    version="1.1.0",
    examples=[
        {"inputs": {"text": "hello"}, "outputs": "HELLO"},
        {"inputs": {"text": "Example Text"}, "outputs": "EXAMPLE TEXT"}
    ]
)
def uppercase(text: str) -> str:
    """
    Convert text to uppercase.
    
    Args:
        text: The text to convert
        
    Returns:
        Uppercase version of the text
    """
    return text.upper()


# Tool with complex input/output types
@agents_app.tool(
    "filter_items",
    description="Filter items based on criteria"
)
def filter_items(
    items: List[Dict[str, Union[str, int, float]]],
    field: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    contains: Optional[str] = None
) -> List[Dict[str, Union[str, int, float]]]:
    """
    Filter a list of items based on criteria.
    
    Args:
        items: List of items to filter
        field: Field to filter on
        min_value: Minimum value for numerical fields
        max_value: Maximum value for numerical fields
        contains: Substring to match for string fields
        
    Returns:
        Filtered list of items
    """
    result = []
    
    for item in items:
        if field not in item:
            continue
            
        value = item[field]
        
        # Check numerical constraints
        if min_value is not None and isinstance(value, (int, float)):
            if value < min_value:
                continue
                
        if max_value is not None and isinstance(value, (int, float)):
            if value > max_value:
                continue
                
        # Check string constraints
        if contains is not None and isinstance(value, str):
            if contains not in value:
                continue
                
        result.append(item)
        
    return result


# Helper function to print metadata
async def print_metadata():
    """Print metadata for registered agents, capabilities, and tools."""
    print("\n=== REGISTERED AGENTS ===")
    for name, info in agents_app.agent_registry.agents.items():
        print(f"Agent: {name}")
        print(f"  Class: {info['cls'].__name__}")
        print(f"  Metadata:")
        for key, value in info['metadata'].items():
            if key != 'capabilities':
                print(f"    {key}: {value}")
        
        print("  Capabilities:")
        for cap_name, cap_info in info['capabilities'].items():
            print(f"    - {cap_name}")
            if 'input_schema' in cap_info:
                print(f"      Input Schema: {cap_info['input_schema']}")
            if 'output_schema' in cap_info:
                print(f"      Output Schema: {cap_info['output_schema']}")
    
    print("\n=== REGISTERED TOOLS ===")
    for name, func in agents_app.agent_registry.tools.items():
        metadata = getattr(func, "__metadata__", {})
        print(f"Tool: {name}")
        print(f"  Function: {func.__name__}")
        print(f"  Metadata:")
        for key, value in metadata.items():
            print(f"    {key}: {value}")


# Main example
async def run_example():
    # Print metadata for all registered components
    await print_metadata()
    
    # Create an instance of the TextProcessor agent
    text_processor = TextProcessor({"model": "gpt-3.5-turbo"})
    
    # Use capabilities
    original_text = "Hello, OpenAgents JSON!"
    echo_result = await text_processor.echo(original_text)
    reverse_result = await text_processor.reverse(original_text)
    tokenize_result = await text_processor.tokenize(original_text)
    
    print("\n=== TEXT PROCESSOR RESULTS ===")
    print(f"Echo: {echo_result}")
    print(f"Reverse: {reverse_result}")
    print(f"Tokenize: {tokenize_result}")
    
    # Use function-based agent
    calc_result_add = await calculate("add", 5, 3)
    calc_result_multiply = await calculate("multiply", 4, 7)
    
    print("\n=== CALCULATOR RESULTS ===")
    print(f"5 + 3 = {calc_result_add}")
    print(f"4 * 7 = {calc_result_multiply}")
    
    # Use standalone tools
    uppercase_result = uppercase("convert me to uppercase")
    
    items = [
        {"id": 1, "name": "Apple", "price": 1.20, "category": "fruit"},
        {"id": 2, "name": "Banana", "price": 0.50, "category": "fruit"},
        {"id": 3, "name": "Carrot", "price": 0.75, "category": "vegetable"},
        {"id": 4, "name": "Donut", "price": 2.00, "category": "pastry"}
    ]
    
    filtered_items = filter_items(items, "price", min_value=1.00)
    
    print("\n=== TOOL RESULTS ===")
    print(f"Uppercase: {uppercase_result}")
    print(f"Filtered items (price >= 1.00): {filtered_items}")


if __name__ == "__main__":
    asyncio.run(run_example()) 