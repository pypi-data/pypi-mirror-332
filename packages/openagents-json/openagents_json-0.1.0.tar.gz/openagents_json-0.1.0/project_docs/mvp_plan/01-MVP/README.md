# OpenAgents JSON: Minimum Viable Product (MVP)

This document outlines the Minimum Viable Product (MVP) for OpenAgents JSON, a FastAPI extension for building AI agent workflows distributed as a Python package. The MVP focuses on delivering core functionality with excellent developer experience in a timeframe of 3-5 months.

## MVP Goals

The primary goals for the MVP phase are:

1. **Implement Three-Stage Workflow System**: Create a complete system for defining agents, building workflows, and managing execution
2. **Streamline Core Functionality**: Focus on essential features with reliable execution
3. **Enhance Developer Experience**: Reduce learning curve and time-to-first-workflow
4. **Stabilize API Surface**: Provide a clean, consistent API for developers
5. **Establish Quality Framework**: Create a robust testing approach
6. **Distribute via PyPI**: Package the extension for easy installation

## Three-Stage Architecture

The OpenAgents JSON framework is structured around three distinct stages:

### Stage 1: Agent & Asset Definition

This stage focuses on defining the building blocks of the system:

- **Agent Registration**: Simple decorators for registering AI agents and tools
- **Component Metadata**: Rich metadata for discoverability and documentation
- **Capability Management**: Registration of agent capabilities with input/output schemas
- **Asset Management**: Shared resources that can be used across agents

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
        self.config = config
        
    @agents_app.capability("summarize")
    async def summarize(self, text: str, max_length: int = 100) -> str:
        """Summarize text to the specified length."""
        # Implementation
        return summarized_text
```

### Stage 2: Workflow Definition

This stage handles the composition of agents into reusable workflows:

- **Workflow Schema**: JSON-based workflow definitions with steps and connections
- **Workflow Validation**: Comprehensive validation of workflow structure and component compatibility
- **Template System**: Templates for common workflow patterns
- **Conditional Logic**: Support for branching and conditional execution

```python
# Register a workflow
agents_app.register_workflow({
    "id": "document-processing",
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

- **Job Creation**: Converting workflow definitions into executable jobs
- **Execution Control**: Starting, pausing, resuming, and cancelling jobs
- **State Management**: Tracking and persistence of job state
- **Monitoring & Analytics**: Insights into job performance and results
- **History & Logging**: Comprehensive logging and history tracking

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

## MVP Components

The MVP consists of four key components, each building on the three-stage architecture:

### 1. Essential Workflow Engine (1-2 months)

Focused on reliable execution of basic workflows in a single environment:

- Streamlined registry system for agent and asset definition
- Robust validation with helpful error messages
- Basic in-memory state management for job execution
- Comprehensive tests for core functionality

### 2. Developer Experience Enhancement (1 month)

Focused on reducing time-to-first-workflow to under 30 minutes:

- Step-by-step getting started guide for all three stages
- Example workflows of increasing complexity
- CLI tools for workflow creation, validation, and job management
- Workflow and job visualization capabilities

### 3. API Stabilization (1 month)

Focused on creating a clean, consistent API surface:

- Core FastAPI routes with comprehensive validation
- Simplified facades for common operations across the three stages
- Helper methods for typical workflow patterns
- OpenAPI documentation with examples

### 4. MVP Testing Framework (2 weeks)

Focused on enabling effective testing of workflows and components:

- Unit testing patterns for agents and components
- Integration test framework for workflows and jobs
- CI pipeline for automated testing
- Mocking utilities for external dependencies

## Key Metrics for MVP Success

| Metric | Current | Target | Description |
|--------|---------|--------|-------------|
| Time-to-First-Workflow | 2-4 hours | < 30 minutes | Time for a new developer to create first workflow |
| Documentation Coverage | Partial | 90%+ | Percentage of functionality with clear documentation |
| Example Workflows | Limited | 10+ | Number of example workflows of varying complexity |
| Test Coverage | Unknown | 90%+ | Test coverage percentage for core components |
| API Response Time | Variable | < 100ms | Response time for typical API operations |
| Job Creation Time | Unknown | < 50ms | Time to create a job from a workflow definition |
| Developer Satisfaction | Unknown | > 4/5 | Developer satisfaction rating from user testing |

## MVP Deliverables

1. **Codebase**:
   - Agent & component registry system
   - Workflow definition and validation engine
   - Job management and execution system
   - FastAPI extension with clean integration points

2. **Documentation**:
   - Getting started guide for the three-stage model
   - Agent creation guide with examples
   - Workflow definition and composition guide
   - Job management and monitoring documentation

3. **Tools**:
   - CLI for workflow management and job control
   - Workflow and job visualization tools
   - Validation helpers for all three stages
   - Component and workflow scaffolding

4. **Testing**:
   - Test framework for all three stages
   - Unit tests for core components
   - Integration tests for workflows and jobs
   - CI pipeline configuration

## Timeline

| Phase | Description | Duration | Start | End |
|-------|-------------|----------|-------|-----|
| 1 | Essential Workflow Engine | 1-2 months | Month 1, Week 1 | Month 2, Week 4 |
| 2 | Developer Experience Enhancement | 1 month | Month 3, Week 1 | Month 3, Week 4 |
| 3 | API Stabilization | 1 month | Month 4, Week 1 | Month 4, Week 4 |
| 4 | MVP Testing Framework | 2 weeks | Month 5, Week 1 | Month 5, Week 2 |

## Resources

The MVP phase requires the following resources:

- 2x Senior Backend Developers (Python, FastAPI, async programming)
- 1x Full Stack Developer (Python, React, API development)
- 1x Technical Writer (documentation)
- Basic development and testing infrastructure 