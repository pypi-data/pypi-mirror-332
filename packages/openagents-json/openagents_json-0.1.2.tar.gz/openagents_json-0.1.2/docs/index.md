# OpenAgents JSON

A FastAPI extension for building AI agent workflows, distributed as a Python package.

## Project Overview

OpenAgents JSON provides a structured framework for building intelligent workflows using a three-stage model:

1. **Agent & Asset Definition** - Define and register AI components like agents, tools, and assets
2. **Workflow Definition** - Compose agents into reusable workflows with validation and templating
3. **Job Management** - Execute, monitor, and control workflow instances as jobs

This approach enables developers to build sophisticated AI applications by composing components into workflows and managing their execution with minimal boilerplate code.

## Key Features

- **Simple Decorator-Based API**: Register agents and their capabilities with simple decorators
- **JSON Workflow Schema**: Define workflows as JSON objects with templating and validation
- **Comprehensive Job Management**: Create, monitor, and control workflow execution
- **Component Registry**: Centralized registration and discovery of agents, tools, and assets
- **FastAPI Integration**: Seamlessly integrate with FastAPI applications
- **Minimal Dependencies**: Built with a focus on lightweight dependencies

## Getting Started

### Installation

```bash
pip install openagents-json
```

### Basic Usage

```python
from openagents_json import OpenAgentsApp

# Create the OpenAgents application
agents_app = OpenAgentsApp()

# Define an agent with capabilities
@agents_app.agent("text_processor", description="Processes text in various ways")
class TextProcessor:
    def __init__(self, config=None):
        self.config = config or {}
        
    @agents_app.capability("summarize", description="Summarize text")
    async def summarize(self, text: str, max_length: int = 100) -> str:
        """Summarize text to the specified length."""
        # Implementation
        return summarized_text

# Define a workflow
agents_app.register_workflow({
    "id": "text-processing",
    "description": "Process text with various operations",
    "steps": [
        {
            "id": "summarize-step",
            "component": "text_processor.summarize",
            "inputs": {"text": "{{input.document}}", "max_length": 200}
        }
    ],
    "output": {
        "summary": "{{summarize-step.output}}"
    }
})

# Create and run a job
job = await agents_app.create_job(
    workflow_id="text-processing",
    inputs={"document": "Lorem ipsum dolor sit amet..."}
)

# Get job results when complete
results = await agents_app.get_job_results(job["id"])
```

## Benefits

### For Developers

- **Reduce Boilerplate**: Focus on agent logic rather than wiring components together
- **Standardized Approach**: Consistent patterns for component definition and composition
- **FastAPI Integration**: Seamlessly integrate with FastAPI applications
- **Flexible Validation**: Comprehensive validation with helpful error messages

### For Teams

- **Clear Separation of Concerns**: Distinct stages for agent definition, workflow composition, and execution
- **Documentation Generation**: Automatic documentation from component metadata
- **Testable Components**: Easy-to-test agents and workflows
- **Reusable Patterns**: Build a library of reusable workflows

## Next Steps

- [Installation Guide](getting-started/installation.md)
- [Quick Start Tutorial](getting-started/quick-start.md)
- [Agent Definition Guide](user-guide/agent-definition.md)
- [Workflow Definition Guide](user-guide/workflow-definition.md)
- [Job Management Guide](user-guide/job-management.md)
- [ComponentRegistry Guide](component_registry.md)
- [Execution Control](execution_control.md)
- [Monitoring and Observability](monitoring.md) 