# MVP PyPI Package Structure

This document outlines the initial package structure for the OpenAgents JSON PyPI distribution during the MVP phase. The structure reflects the three-stage model: Agent Definition, Workflow Definition, and Job Management.

## MVP Package Structure

The OpenAgents JSON package follows modern Python package standards with a clean, modular structure:

```
openagents_json/
├── pyproject.toml            # Modern project configuration
├── setup.cfg                 # Package metadata and configuration
├── README.md                 # Installation and quick start
├── LICENSE                   # MIT License
├── CHANGELOG.md              # Version history
├── .env.example              # Example environment variables configuration
├── tests/                    # Basic test suite
│   ├── test_agents.py        # Tests for agent definition
│   ├── test_workflows.py     # Tests for workflow definition
│   ├── test_jobs.py          # Tests for job management
│   └── test_fastapi.py       # Tests for FastAPI integration
├── examples/                 # Example applications
│   ├── simple_agent.py       # Basic agent definition
│   ├── branching_workflow.py # Workflow with conditions
│   └── job_management.py     # Job creation and monitoring
└── openagents_json/          # Source code
    ├── __init__.py           # Package initialization
    ├── app.py                # Main application class (OpenAgentsApp)
    ├── version.py            # Version information
    ├── settings.py           # Centralized settings using Pydantic Settings
    ├── agents/               # Stage 1: Agent & Asset Definition
    │   ├── __init__.py       # Agent module initialization
    │   ├── registry.py       # Component registry
    │   ├── decorators.py     # Agent and tool decorators
    │   ├── base.py           # Base agent interfaces
    │   ├── types/            # Different agent types
    │   │   ├── __init__.py   # Types initialization
    │   │   ├── llm.py        # LLM-based agents
    │   │   ├── tool.py       # Function-based tools
    │   │   └── chain.py      # Chain-based agents
    │   └── assets/           # Asset management
    │       ├── __init__.py   # Assets initialization
    │       └── registry.py   # Asset registry
    ├── workflows/            # Stage 2: Workflow Definition
    │   ├── __init__.py       # Workflow module initialization
    │   ├── schema.py         # Workflow schema definitions
    │   ├── registry.py       # Workflow registry
    │   ├── validation.py     # Workflow validation
    │   ├── steps.py          # Step definitions
    │   └── templates/        # Workflow templates
    │       ├── __init__.py   # Templates initialization
    │       └── basic.py      # Basic templates
    ├── jobs/                 # Stage 3: Job Management
    │   ├── __init__.py       # Jobs module initialization
    │   ├── manager.py        # Job creation and control
    │   ├── state.py          # Job state management
    │   ├── execution.py      # Job execution engine
    │   ├── monitoring.py     # Job monitoring utilities
    │   └── history.py        # Job history tracking
    ├── fastapi/              # FastAPI Integration
    │   ├── __init__.py       # FastAPI module initialization
    │   ├── extension.py      # Extension integration
    │   ├── middleware.py     # Workflow middleware
    │   ├── routers/          # API routers
    │   │   ├── __init__.py   # Routers initialization
    │   │   ├── agents.py     # Agent API routes
    │   │   ├── workflows.py  # Workflow API routes
    │   │   └── jobs.py       # Job API routes
    │   └── dependencies.py   # FastAPI dependencies
    └── utils/                # Utilities
        ├── __init__.py       # Utilities initialization
        ├── logging.py        # Logging utilities
        ├── validation.py     # Generic validation utilities
        ├── templating.py     # Template processing
        └── serialization.py  # Data serialization
```

## Key Files

### pyproject.toml

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "openagents-json"
version = "0.1.0"
description = "A FastAPI extension for building AI agent workflows"
readme = "README.md"
authors = [
    {name = "OpenAgents Team", email = "openagents@example.com"}
]
license = {text = "MIT"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]
keywords = ["fastapi", "agents", "workflows", "ai", "json"]
dependencies = [
    "fastapi>=0.68.0",
    "pydantic>=2.0.0",
    "pydantic-settings>=2.0.0",
    "python-dotenv>=1.0.0",
    "uvicorn>=0.15.0",
    "jinja2>=3.0.0",
    "aiohttp>=3.8.0",
]
requires-python = ">=3.8"

[project.optional-dependencies]
dev = [
    "pytest>=6.0.0",
    "black>=21.5b2",
    "isort>=5.9.1",
    "mypy>=0.910",
    "flake8>=3.9.2",
]
docs = [
    "sphinx>=4.0.0",
    "sphinx-rtd-theme>=1.0.0",
]

[project.urls]
"Homepage" = "https://github.com/example/openagents-json"
"Bug Tracker" = "https://github.com/example/openagents-json/issues"
```

### .env.example

```
# OpenAgents JSON Configuration
# Copy this file to .env and modify as needed

# Application settings
OPENAGENTS_DEBUG=false
OPENAGENTS_LOG_LEVEL=INFO
OPENAGENTS_SECRET_KEY=change_this_to_a_secure_random_string

# Agent settings
OPENAGENTS_DEFAULT_LLM_PROVIDER=openai
OPENAGENTS_OPENAI_API_KEY=
OPENAGENTS_ANTHROPIC_API_KEY=

# Job management settings
OPENAGENTS_JOB_RETENTION_DAYS=30
OPENAGENTS_MAX_CONCURRENT_JOBS=100

# Storage settings
OPENAGENTS_STORAGE_TYPE=memory  # Options: memory, redis, postgres
OPENAGENTS_REDIS_URL=
OPENAGENTS_DATABASE_URL=
```

### openagents_json/settings.py

```python
"""
Centralized settings management for OpenAgents JSON using Pydantic Settings v2.
"""

from typing import Literal, Optional
from pydantic import Field, field_validator, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenAgentsSettings(BaseSettings):
    """
    Centralized settings for OpenAgents JSON.
    
    Settings can be configured through environment variables or a .env file.
    Environment variables should be prefixed with OPENAGENTS_.
    """
    
    # Model config for environment variable loading
    model_config = SettingsConfigDict(
        env_prefix="OPENAGENTS_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )
    
    # Application settings
    debug: bool = Field(False, description="Enable debug mode")
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        "INFO", description="Logging level"
    )
    secret_key: SecretStr = Field(
        ..., description="Secret key for security features"
    )
    
    # Agent settings
    default_llm_provider: Literal["openai", "anthropic", "local"] = Field(
        "openai", description="Default LLM provider"
    )
    openai_api_key: Optional[SecretStr] = Field(
        None, description="OpenAI API key"
    )
    anthropic_api_key: Optional[SecretStr] = Field(
        None, description="Anthropic API key"
    )
    
    # Job management settings
    job_retention_days: int = Field(
        30, description="Number of days to retain job history"
    )
    max_concurrent_jobs: int = Field(
        100, description="Maximum number of concurrent jobs"
    )
    
    # Storage settings
    storage_type: Literal["memory", "redis", "postgres"] = Field(
        "memory", description="Storage backend type"
    )
    redis_url: Optional[str] = Field(
        None, description="Redis connection URL"
    )
    database_url: Optional[str] = Field(
        None, description="Database connection URL"
    )
    
    @field_validator("storage_type")
    def validate_storage_backends(cls, v, values):
        """Validate that required connection details are provided for the selected storage type."""
        if v == "redis" and not values.data.get("redis_url"):
            raise ValueError("Redis URL must be provided when using Redis storage")
        if v == "postgres" and not values.data.get("database_url"):
            raise ValueError("Database URL must be provided when using Postgres storage")
        return v


# Create global settings instance
settings = OpenAgentsSettings()
```

### openagents_json/app.py

```python
"""
The main OpenAgentsApp class for creating and configuring the application.
"""

from typing import Dict, Any, List, Optional, Callable, Type

from fastapi import FastAPI, APIRouter

from openagents_json.settings import settings
from openagents_json.agents.registry import ComponentRegistry
from openagents_json.workflows.registry import WorkflowRegistry
from openagents_json.jobs.manager import JobManager
from openagents_json.fastapi.extension import create_extension


class OpenAgentsApp:
    """
    The main application class for OpenAgents JSON.
    
    This class provides methods for all three stages of the framework:
    1. Agent Definition - Register agents and tools
    2. Workflow Definition - Create and register workflows
    3. Job Management - Create and manage workflow execution
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize the OpenAgents application."""
        # Merge provided config with settings from environment/config files
        self.config = {**settings.model_dump(), **(config or {})}
        
        self.component_registry = ComponentRegistry()
        self.workflow_registry = WorkflowRegistry()
        self.job_manager = JobManager(
            component_registry=self.component_registry,
            workflow_registry=self.workflow_registry,
            config=self.config
        )
        
    def agent(self, name: str, description: Optional[str] = None):
        """
        Decorator for registering an agent class.
        
        Args:
            name: The name of the agent
            description: Optional description of the agent
            
        Returns:
            A decorator function
        """
        def decorator(cls: Type):
            self.component_registry.register_agent(name, cls, description)
            return cls
        return decorator
        
    def tool(self, name: str, description: Optional[str] = None):
        """
        Decorator for registering a tool function.
        
        Args:
            name: The name of the tool
            description: Optional description of the tool
            
        Returns:
            A decorator function
        """
        def decorator(func: Callable):
            self.component_registry.register_tool(name, func, description)
            return func
        return decorator
        
    def capability(self, name: str, description: Optional[str] = None):
        """
        Decorator for registering an agent capability method.
        
        Args:
            name: The name of the capability
            description: Optional description of the capability
            
        Returns:
            A decorator function
        """
        def decorator(method: Callable):
            # Implementation will be added during development
            return method
        return decorator
        
    def register_workflow(self, workflow_def: Dict[str, Any]) -> str:
        """
        Register a workflow definition.
        
        Args:
            workflow_def: The workflow definition as a dictionary
            
        Returns:
            The ID of the registered workflow
        """
        return self.workflow_registry.register(workflow_def)
        
    async def create_job(self, workflow_id: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new job from a workflow definition.
        
        Args:
            workflow_id: The ID of the workflow to execute
            inputs: The input data for the workflow
            
        Returns:
            The created job as a dictionary
        """
        return await self.job_manager.create_job(workflow_id, inputs)
        
    async def get_job_status(self, job_id: str) -> Dict[str, Any]:
        """
        Get the status of a job.
        
        Args:
            job_id: The ID of the job
            
        Returns:
            The job status as a dictionary
        """
        return await self.job_manager.get_job_status(job_id)
        
    async def get_job_results(self, job_id: str) -> Dict[str, Any]:
        """
        Get the results of a completed job.
        
        Args:
            job_id: The ID of the job
            
        Returns:
            The job results as a dictionary
        """
        return await self.job_manager.get_job_results(job_id)
        
    def include_in_app(self, app: FastAPI, prefix: str = "/agents"):
        """
        Include the OpenAgents extension in a FastAPI application.
        
        Args:
            app: The FastAPI application
            prefix: The URL prefix for the extension
        """
        extension = create_extension(self)
        app.include_router(extension, prefix=prefix)
```

## FastAPI Integration

The package provides three methods for integrating with FastAPI applications:

### 1. Extension Integration (OpenAgentsApp)

```python
from fastapi import FastAPI
from openagents_json import OpenAgentsApp

# Create FastAPI application
app = FastAPI()

# Create OpenAgents application
agents_app = OpenAgentsApp()

# Register a tool
@agents_app.tool("echo")
def echo(message: str) -> str:
    """Echo back the message."""
    return message

# Register a workflow
agents_app.register_workflow({
    "id": "echo-workflow",
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

# Include in FastAPI app
agents_app.include_in_app(app, prefix="/agents")
```

### 2. Middleware Integration

```python
from fastapi import FastAPI
from openagents_json.fastapi.middleware import WorkflowMiddleware

app = FastAPI()
app.add_middleware(
    WorkflowMiddleware,
    component_registry_path="/components",
    workflow_registry_path="/workflows",
    job_manager_path="/jobs"
)
```

### 3. Router Integration

```python
from fastapi import FastAPI
from openagents_json.fastapi.routers import agents_router, workflows_router, jobs_router

app = FastAPI()
app.include_router(agents_router, prefix="/agents")
app.include_router(workflows_router, prefix="/workflows")
app.include_router(jobs_router, prefix="/jobs")
```

## MVP Test Suite

The package includes basic tests for the three-stage model and FastAPI integration:

### FastAPI Integration Test

```python
# tests/test_fastapi.py
from fastapi.testclient import TestClient
from fastapi import FastAPI

from openagents_json import OpenAgentsApp

def test_extension_integration():
    # Create FastAPI app
    app = FastAPI()
    
    # Create OpenAgents app
    agents_app = OpenAgentsApp()
    
    # Register a simple tool
    @agents_app.tool("echo")
    def echo(message: str) -> str:
        return message
    
    # Register a simple workflow
    agents_app.register_workflow({
        "id": "echo-workflow",
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
    
    # Include in FastAPI app
    agents_app.include_in_app(app)
    
    # Create test client
    client = TestClient(app)
    
    # Test component listing
    response = client.get("/agents/components")
    assert response.status_code == 200
    components = response.json()
    assert "echo" in [comp["name"] for comp in components]
    
    # Test workflow listing
    response = client.get("/agents/workflows")
    assert response.status_code == 200
    workflows = response.json()
    assert "echo-workflow" in [wf["id"] for wf in workflows]
    
    # Test job creation
    response = client.post(
        "/agents/jobs",
        json={"workflow_id": "echo-workflow", "inputs": {"message": "Hello World"}}
    )
    assert response.status_code == 202
    job = response.json()
    job_id = job["id"]
    
    # Test job status
    response = client.get(f"/agents/jobs/{job_id}")
    assert response.status_code == 200
    status = response.json()
    assert status["workflow_id"] == "echo-workflow"
```

## Initial CI/CD Setup

The package includes a basic GitHub Actions workflow for testing:

```yaml
# .github/workflows/test.yml
name: Test

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10']

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install .[dev]
    - name: Lint
      run: |
        flake8 openagents_json tests
        mypy openagents_json
        black --check openagents_json tests
        isort --check openagents_json tests
    - name: Test
      run: |
        pytest --cov=openagents_json tests/
    - name: Upload coverage
      uses: codecov/codecov-action@v3
```

## Next Steps After MVP

After completing the MVP phase, the project will:

1. Enhance the agent definition capabilities with more sophisticated types
2. Expand the workflow definition system with advanced templating and conditions
3. Improve the job management system with persistent storage and recovery
4. Add advanced monitoring and analytics features
5. Implement more sophisticated FastAPI integration methods
6. Enhance documentation and examples for all three stages

These enhancements will be addressed in subsequent phases outlined in the implementation plan.

## Folder and File Naming Conventions

The package follows these naming conventions:

1. **Module Names**: Lower case with underscores (snake_case) for multiple words
2. **Class Names**: CamelCase (PascalCase) for class names
3. **Function/Method Names**: Lower case with underscores (snake_case)
4. **Constants**: Upper case with underscores (UPPER_SNAKE_CASE)

## Recommended Improved Naming

Based on the three-stage model, we recommend the following naming improvements:

1. Change `openagents_json/core/` to `openagents_json/agents/` to better reflect Stage 1 (Agent Definition)
2. Rename `workflow_engine.py` to `workflow_definition.py` for clarity in Stage 2
3. Create a new `jobs/` directory for Stage 3 (Job Management) instead of embedding this in the workflow engine
4. Rename `execute_workflow` method to `create_job` to better reflect the conceptual model
5. Use more descriptive names for FastAPI integration methods:
   - `include_in_app` instead of `mount`
   - `agents_router` instead of `workflow_router`
   - `register_agent` instead of `register_component`

These naming conventions will make the codebase more intuitive for developers working with the three-stage model. 