# OpenAgents JSON: Implementation Plan

This repository contains the implementation plan for OpenAgents JSON, a FastAPI extension for building AI agent workflows distributed as a Python package via PyPI.

## Project Overview

OpenAgents JSON is designed around a three-stage model for building AI agent workflows:

1. **Agent & Asset Definition** - Define and register AI components like agents, tools, and assets
2. **Workflow Definition** - Compose agents into reusable workflows with validation and templating
3. **Job Management** - Execute, monitor, and control workflow instances as jobs

This structured approach enables developers to:

- Define AI components using simple decorators and interfaces
- Compose components into complex workflows using JSON configuration
- Execute and monitor workflows as manageable jobs
- Integrate seamlessly with existing FastAPI applications
- Configure the application easily with environment variables and `.env` files

## Three-Stage Architecture

### Stage 1: Agent & Asset Definition

This stage focuses on defining and registering the building blocks of the system:

```python
from openagents_json import OpenAgentsApp

agents_app = OpenAgentsApp()

# Register a simple tool
@agents_app.tool("echo")
def echo(message: str) -> str:
    """Echo back the message."""
    return message

# Register an LLM agent
@agents_app.agent("text_processor")
class TextProcessor:
    def __init__(self, config):
        self.model = config.get("model", "gpt-3.5-turbo")
        
    @agents_app.capability("summarize")
    async def summarize(self, text: str, max_length: int = 100) -> str:
        """Summarize text to the specified length."""
        # Implementation
        return summarized_text
```

### Stage 2: Workflow Definition

This stage handles the composition of agents into reusable workflows:

```python
# Register a workflow
agents_app.register_workflow({
    "id": "document-processing",
    "version": "1.0.0",
    "description": "Process documents with branching logic",
    "steps": [
        {
            "id": "extract-text",
            "component": "document_processor.extract_text",
            "inputs": {"document": "{{input.document}}"}
        },
        {
            "id": "analyze-sentiment",
            "component": "text_analyzer.sentiment",
            "inputs": {"text": "{{extract-text.output}}"},
            "condition": "{{extract-text.success}}"
        }
    ],
    "output": {
        "sentiment": "{{analyze-sentiment.output}}",
        "status": "{{workflow.status}}"
    }
})
```

### Stage 3: Job Management

This stage focuses on execution, monitoring, and management of workflow instances:

```python
# Create and run a job
job = await agents_app.create_job(
    workflow_id="document-processing",
    inputs={"document": "https://example.com/doc.pdf"}
)

# Monitor job status
status = await agents_app.get_job_status(job.id)

# Get job results when complete
if status.state == "COMPLETED":
    results = await agents_app.get_job_results(job.id)
```

## Package Structure

The project follows modern Python packaging best practices, with a structure that reflects the three-stage model:

```
openagents_json/
├── pyproject.toml      # Modern project configuration
├── setup.cfg           # Package metadata and configuration
├── README.md           # Project documentation
├── LICENSE             # License file
├── CHANGELOG.md        # Version history
├── .env.example        # Example environment variables configuration
├── docs/               # Documentation
├── tests/              # Test suite
├── examples/           # Example applications
└── openagents_json/    # Source code
    ├── __init__.py     # Package initialization
    ├── app.py          # Main application class
    ├── settings.py     # Centralized settings using Pydantic Settings v2
    ├── agents/         # Stage 1: Agent & Asset Definition
    │   ├── registry.py # Component registry
    │   ├── types/      # Agent types
    │   └── assets/     # Asset management
    ├── workflows/      # Stage 2: Workflow Definition
    │   ├── schema.py   # Workflow schema
    │   ├── registry.py # Workflow registry
    │   └── validation.py # Workflow validation
    ├── jobs/           # Stage 3: Job Management
    │   ├── manager.py  # Job creation and control
    │   ├── execution.py # Job execution
    │   └── monitoring.py # Job monitoring
    └── fastapi/        # FastAPI integration
        ├── extension.py # Extension integration
        ├── middleware.py # Middleware integration
        └── routers/    # Router integration
```

## Installation (Future)

```bash
pip install openagents-json
```

## Configuration

OpenAgents JSON uses a centralized settings management approach based on Pydantic Settings v2:

1. Create a `.env` file based on the provided `.env.example`:

```
# Copy from .env.example and customize
cp .env.example .env
```

2. Edit the `.env` file with your configuration:

```
# Application settings
OPENAGENTS_DEBUG=true
OPENAGENTS_LOG_LEVEL=INFO
OPENAGENTS_SECRET_KEY=your_secret_key

# Add your API keys
OPENAGENTS_OPENAI_API_KEY=sk-...
```

3. The settings are automatically loaded and available throughout the application:

```python
from openagents_json.settings import settings

# Access settings in a type-safe way
if settings.debug:
    print("Debug mode is enabled")
```

## FastAPI Integration

OpenAgents JSON integrates with FastAPI applications in three primary ways:

### Extension Integration (Recommended)

```python
from fastapi import FastAPI
from openagents_json import OpenAgentsApp

# Create a FastAPI application
app = FastAPI()

# Initialize OpenAgents JSON
agents_app = OpenAgentsApp()

# Stage 1: Register agents and tools
@agents_app.tool("echo")
def echo(message: str) -> str:
    """Echo back the message."""
    return message

# Stage 2: Register workflows
agents_app.register_workflow({
    "id": "simple-workflow",
    "steps": [
        {
            "id": "echo-step",
            "component": "echo",
            "inputs": {
                "message": "{{input.message}}"
            }
        }
    ],
    "output": "{{echo-step.output}}"
})

# Include in FastAPI app (provides Stage 3 endpoints)
agents_app.include_in_app(app, prefix="/agents")

# Stage 3: Access job management via endpoints
# POST /agents/jobs - Create a new job
# GET /agents/jobs/{job_id} - Get job status
# GET /agents/jobs/{job_id}/results - Get job results
```

### Middleware Integration

```python
from fastapi import FastAPI
from openagents_json.fastapi.middleware import WorkflowMiddleware

app = FastAPI()
app.add_middleware(
    WorkflowMiddleware,
    component_registry_path="/components",  # Stage 1
    workflow_registry_path="/workflows",    # Stage 2
    job_manager_path="/jobs"               # Stage 3
)
```

### Router Integration

```python
from fastapi import FastAPI
from openagents_json.fastapi.routers import agents_router, workflows_router, jobs_router

app = FastAPI()
app.include_router(agents_router, prefix="/agents")      # Stage 1
app.include_router(workflows_router, prefix="/workflows") # Stage 2
app.include_router(jobs_router, prefix="/jobs")          # Stage 3
```

## Implementation Phases

The implementation is structured into six phases, each enhancing all three stages of the framework:

1. [MVP (1-2 months)](01-MVP/README.md)
   - Basic implementation of all three stages
   - Initial PyPI package with core functionality

2. [Essential Workflow Engine (2-3 months)](02-Essential_Workflow_Engine/README.md)
   - Enhanced implementation of all three stages
   - Improved validation, state management, and monitoring

3. [Developer Experience Enhancement (1-2 months)](03-Developer_Experience_Enhancement/README.md)
   - Tools and utilities for all three stages
   - Improved documentation and examples

4. [API Stabilization (1-2 months)](04-API_Stabilization/README.md)
   - Stable API for all three stages
   - Comprehensive documentation and examples

5. [MVP Testing Framework (1-2 months)](05-MVP_Testing_Framework/README.md)
   - Testing utilities for all three stages
   - CI/CD pipeline and test coverage

6. [Scaling Path (6-9 months)](06-Scaling_Path/README.md)
   - Enterprise features for all three stages
   - Performance optimizations and scaling capabilities

## Key Documents

- [Executive Summary](executive-summary.md) - High-level overview of the project
- [Implementation Strategy](implementation-strategy.md) - Detailed implementation approach
- [Package Distribution Guide](package-distribution-guide.md) - PyPI distribution guide
- [Roadmap Index](index.md) - Index of all implementation documents

## License

This project will be licensed under the MIT License. 