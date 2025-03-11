"""
Basic example demonstrating the usage of OpenAgents JSON.

This example shows how to:
1. Define an agent with capabilities
2. Register a standalone tool
3. Define a workflow
4. Execute a job
"""

import asyncio
from fastapi import FastAPI
import uvicorn

from openagents_json import OpenAgentsApp


# Create the OpenAgents application
agents_app = OpenAgentsApp()


# Define an agent with capabilities
@agents_app.agent("text_processor", description="Processes text in various ways")
class TextProcessor:
    def __init__(self, config=None):
        self.config = config or {}
        
    @agents_app.capability("echo", description="Echo back the text")
    async def echo(self, text: str) -> str:
        """Echo back the text."""
        return text
        
    @agents_app.capability("reverse", description="Reverse the text")
    async def reverse(self, text: str) -> str:
        """Reverse the text."""
        return text[::-1]


# Define a standalone tool
@agents_app.tool("uppercase", description="Convert text to uppercase")
def uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


# Register a workflow
agents_app.register_workflow({
    "id": "text-transformation",
    "description": "Transform text in multiple ways",
    "steps": [
        {
            "id": "echo-step",
            "component": "text_processor.echo",
            "inputs": {"text": "{{input.text}}"}
        },
        {
            "id": "reverse-step",
            "component": "text_processor.reverse",
            "inputs": {"text": "{{echo-step.output}}"}
        },
        {
            "id": "uppercase-step",
            "component": "uppercase",
            "inputs": {"text": "{{reverse-step.output}}"}
        }
    ],
    "output": {
        "original": "{{echo-step.output}}",
        "reversed": "{{reverse-step.output}}",
        "final": "{{uppercase-step.output}}"
    }
})


# Define a FastAPI application
app = FastAPI(title="OpenAgents JSON Example")

# Mount the OpenAgents router
agents_app.mount(app, prefix="/api")


# Direct usage example
async def run_example():
    # Create a job
    job = await agents_app.create_job(
        workflow_id="text-transformation",
        inputs={"text": "Hello, World!"}
    )
    
    print(f"Created job: {job['id']}")
    
    # Get job status
    status = await agents_app.get_job_status(job["id"])
    print(f"Job status: {status['status']}")
    
    # In a real application, we would execute the job here
    # For this example, we'll just simulate job completion
    job = agents_app.job_manager.jobs[job["id"]]
    job["status"] = "COMPLETED"
    job["outputs"] = {
        "original": "Hello, World!",
        "reversed": "!dlroW ,olleH",
        "final": "!DLROW ,OLLEH"
    }
    
    # Get job results
    results = await agents_app.get_job_results(job["id"])
    print(f"Job results: {results['outputs']}")


if __name__ == "__main__":
    # Run the direct usage example
    asyncio.run(run_example())
    
    #Uncomment to run the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000) 