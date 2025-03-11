# Quick Start

This guide will walk you through creating your first AI agent workflow using OpenAgents JSON.

## Overview

We'll create a simple text processing workflow that:

1. Takes a text input
2. Processes it in different ways
3. Returns the results

## 1. Install OpenAgents JSON

First, install the package:

```bash
pip install openagents-json
```

## 2. Define Agents and Tools

Create a file named `agents.py` with the following content:

```python
from openagents_json import OpenAgentsApp

# Create the OpenAgents application
agents_app = OpenAgentsApp()

# Define a text processing agent
@agents_app.agent("text_processor", description="Processes text in various ways")
class TextProcessor:
    def __init__(self, config=None):
        self.config = config or {}
        
    @agents_app.capability("reverse", description="Reverse the text")
    async def reverse(self, text: str) -> str:
        """Reverse the text."""
        return text[::-1]
        
    @agents_app.capability("count_words", description="Count words in the text")
    async def count_words(self, text: str) -> int:
        """Count the number of words in the text."""
        return len(text.split())

# Define a standalone tool
@agents_app.tool("uppercase", description="Convert text to uppercase")
def uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()
```

## 3. Using the ComponentRegistry

The ComponentRegistry provides a central way to register, discover, and manage components. You can use it directly:

```python
from openagents_json.core import component_registry, ComponentMetadata

# Define a simple component
class TextPreprocessor:
    """A component that preprocesses text."""
    __version__ = "1.0.0"
    __author__ = "Your Name"
    __tags__ = ["text", "preprocessing"]
    
    def preprocess(self, text):
        # Clean, normalize, and transform text
        return text.strip().lower()

# Register the component
preprocessor = TextPreprocessor()
component_registry.register("text_preprocessor", preprocessor)

# Later, retrieve and use the component
text_preprocessor = component_registry.get("text_preprocessor")
cleaned_text = text_preprocessor.preprocess("  HELLO WORLD  ")
print(cleaned_text)  # Output: "hello world"
```

The registry automatically extracts metadata from your component class, including description from docstrings, version, author, and tags from class attributes.

You can also filter components by their metadata:

```python
# Find all text-related components
text_components = component_registry.find(tags=["text"])
print(f"Found {len(text_components)} text components: {text_components}")
```

The ComponentRegistry serves as the foundation for the decorator-based agent system and workflow engine in OpenAgents JSON.

## 4. Define Workflows

Add the following code to the same file:

```python
# Register a workflow
agents_app.register_workflow({
    "id": "text-analysis",
    "description": "Analyze text in multiple ways",
    "steps": [
        {
            "id": "reverse-step",
            "component": "text_processor.reverse",
            "inputs": {"text": "{{input.text}}"}
        },
        {
            "id": "count-step",
            "component": "text_processor.count_words",
            "inputs": {"text": "{{input.text}}"}
        },
        {
            "id": "uppercase-step",
            "component": "uppercase",
            "inputs": {"text": "{{input.text}}"}
        }
    ],
    "output": {
        "reversed": "{{reverse-step.output}}",
        "word_count": "{{count-step.output}}",
        "uppercase": "{{uppercase-step.output}}"
    }
})
```

## 5. Execute the Workflow

Create a file named `app.py` with the following content:

```python
import asyncio
from agents import agents_app

async def run_workflow():
    # Create a job
    job = await agents_app.create_job(
        workflow_id="text-analysis",
        inputs={"text": "Hello, OpenAgents JSON!"}
    )
    
    print(f"Created job: {job['id']}")
    
    # Simulate job execution (in a real application, this would be handled by the framework)
    job_obj = agents_app.job_manager.jobs[job["id"]]
    job_obj["status"] = "COMPLETED"
    job_obj["outputs"] = {
        "reversed": "!NOSJ stnegeAnepO ,olleH",
        "word_count": 3,
        "uppercase": "HELLO, OPENAGENTS JSON!"
    }
    
    # Get job results
    results = await agents_app.get_job_results(job["id"])
    print(f"Job results: {results['outputs']}")

if __name__ == "__main__":
    asyncio.run(run_workflow())
```

Run the application:

```bash
python app.py
```

You should see output similar to:

```
Created job: job_0
Job results: {'reversed': '!NOSJ stnegeAnepO ,olleH', 'word_count': 3, 'uppercase': 'HELLO, OPENAGENTS JSON!'}
```

## 6. Create a FastAPI Application

Now, let's create a FastAPI application that exposes our workflow as an API. Create a file named `api.py`:

```python
from fastapi import FastAPI
import uvicorn
from agents import agents_app

# Create FastAPI application
app = FastAPI(title="Text Analysis API")

# Mount OpenAgents JSON routes
agents_app.mount(app, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run the API server:

```bash
python api.py
```

You can now access:

- API documentation at http://localhost:8000/docs
- List of agents at http://localhost:8000/api/agents
- List of workflows at http://localhost:8000/api/workflows

## 7. Use the API

You can create a job using cURL:

```bash
curl -X POST http://localhost:8000/api/jobs \
    -H "Content-Type: application/json" \
    -d '{"workflow_id": "text-analysis", "inputs": {"text": "Hello, API!"}}'
```

Which will return something like:

```json
{"id":"job_0","workflow_id":"text-analysis","inputs":{"text":"Hello, API!"},"status":"CREATED","created_at":"__TIMESTAMP__"}
```

## Next Steps

Congratulations! You've created your first AI agent workflow with OpenAgents JSON. Next, you can:

- Learn about [Agent Definition](../user-guide/agent-definition.md) in detail
- Explore [Workflow Definition](../user-guide/workflow-definition.md) options
- Understand [Job Management](../user-guide/job-management.md)
- See how to [integrate with FastAPI](../user-guide/fastapi-integration.md) 