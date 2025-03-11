"""
Example of FastAPI integration with OpenAgents JSON.

This example demonstrates the three integration options:
1. OpenAgentsAPI - A FastAPI extension with integrated OpenAgents JSON capabilities
2. OpenAgentsMiddleware - Middleware for existing FastAPI applications
3. API Router - Enhanced router for FastAPI applications

Run this example with:
    uvicorn examples.fastapi_integration:app --reload
"""

import os
import sys
import asyncio
from typing import Dict, Any, List

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI, Request, Depends, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from openagents_json.api import OpenAgentsAPI, OpenAgentsMiddleware, create_api_router
from openagents_json.core.app import OpenAgentsApp
from openagents_json.workflow import Workflow, Step, Connection, Parameter, WorkflowMetadataModel
from openagents_json.workflow.examples.basic_workflow import create_basic_workflow


# Choose one of the integration options
INTEGRATION_MODE = os.environ.get("INTEGRATION_MODE", "extension").lower()

print(f"Using integration mode: {INTEGRATION_MODE}")

# Example agent and capability
class TextProcessor:
    """Example agent for text processing."""
    
    def summarize(self, text: str) -> str:
        """Summarize the given text."""
        words = text.split()
        if len(words) <= 5:
            return text
        
        # Simple summarization - take first 5 words
        return " ".join(words[:5]) + "..."


# Create the app based on the integration mode
if INTEGRATION_MODE == "extension":
    # Option 1: OpenAgentsAPI
    app = OpenAgentsAPI(
        title="OpenAgents JSON Example",
        description="Example of OpenAgents JSON integration with FastAPI",
        version="0.1.0",
        api_prefix="/api"
    )
    
    # Register the agent and capability
    @app.agent("text_processor")
    class MyTextProcessor(TextProcessor):
        @app.capability("summarize")
        def summarize_text(self, text: str) -> str:
            return super().summarize(text)
    
    # Register a sample workflow
    workflow = create_basic_workflow()
    app.register_workflow(workflow.to_dict())
    
    # Add a custom endpoint
    @app.get("/custom")
    async def custom_endpoint():
        return {"message": "This is a custom endpoint"}

elif INTEGRATION_MODE == "middleware":
    # Option 2: OpenAgentsMiddleware
    app = FastAPI(
        title="OpenAgents JSON Example",
        description="Example of OpenAgents JSON integration with FastAPI",
        version="0.1.0"
    )
    
    # Create the OpenAgentsApp instance
    openagents_app = OpenAgentsApp()
    
    # Register the agent and capability
    @openagents_app.agent("text_processor")
    class MyTextProcessor(TextProcessor):
        @openagents_app.capability("summarize")
        def summarize_text(self, text: str) -> str:
            return super().summarize(text)
    
    # Register a sample workflow
    workflow = create_basic_workflow()
    openagents_app.register_workflow(workflow.to_dict())
    
    # Add the middleware
    app.add_middleware(OpenAgentsMiddleware, openagents_app=openagents_app)
    
    # Mount the API router
    router = create_api_router(openagents_app)
    app.include_router(router, prefix="/api")
    
    # Add a custom endpoint that uses the OpenAgentsApp from the request
    @app.get("/custom")
    async def custom_endpoint(request: Request):
        # Access the OpenAgentsApp from the request
        oa_app = request.state.openagents_app
        return {"message": "This is a custom endpoint", "agents": len(await oa_app._get_agents())}

else:
    # Option 3: API Router only
    app = FastAPI(
        title="OpenAgents JSON Example",
        description="Example of OpenAgents JSON integration with FastAPI",
        version="0.1.0"
    )
    
    # Create the OpenAgentsApp instance
    openagents_app = OpenAgentsApp()
    
    # Register the agent and capability
    @openagents_app.agent("text_processor")
    class MyTextProcessor(TextProcessor):
        @openagents_app.capability("summarize")
        def summarize_text(self, text: str) -> str:
            return super().summarize(text)
    
    # Register a sample workflow
    workflow = create_basic_workflow()
    openagents_app.register_workflow(workflow.to_dict())
    
    # Mount the API router
    router = create_api_router(openagents_app)
    app.include_router(router, prefix="/api")
    
    # Add a custom endpoint
    @app.get("/custom")
    async def custom_endpoint():
        return {"message": "This is a custom endpoint"}


# Add a simple HTML page to test the API
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>OpenAgents JSON API Example</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                }
                .endpoint {
                    margin-bottom: 20px;
                    border: 1px solid #ccc;
                    padding: 10px;
                    border-radius: 5px;
                }
                .method {
                    font-weight: bold;
                    display: inline-block;
                    width: 60px;
                }
                .url {
                    color: #0066cc;
                }
                .description {
                    color: #666;
                    margin-top: 5px;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 5px 10px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
                pre {
                    background-color: #f5f5f5;
                    padding: 10px;
                    border-radius: 4px;
                    overflow-x: auto;
                }
                #response {
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>OpenAgents JSON API Example</h1>
            <p>This is an example of OpenAgents JSON integration with FastAPI.</p>
            
            <h2>Available endpoints:</h2>
            
            <div class="endpoint">
                <div><span class="method">GET</span> <span class="url">/api/agents</span></div>
                <div class="description">List all registered agents</div>
                <button onclick="fetchEndpoint('GET', '/api/agents')">Try it</button>
            </div>
            
            <div class="endpoint">
                <div><span class="method">GET</span> <span class="url">/api/workflows</span></div>
                <div class="description">List all registered workflows</div>
                <button onclick="fetchEndpoint('GET', '/api/workflows')">Try it</button>
            </div>
            
            <div class="endpoint">
                <div><span class="method">GET</span> <span class="url">/api/workflows/basic_text_processing</span></div>
                <div class="description">Get a specific workflow</div>
                <button onclick="fetchEndpoint('GET', '/api/workflows/basic_text_processing')">Try it</button>
            </div>
            
            <div class="endpoint">
                <div><span class="method">POST</span> <span class="url">/api/jobs</span></div>
                <div class="description">Create a new job</div>
                <button onclick="createJob()">Try it</button>
            </div>
            
            <div class="endpoint">
                <div><span class="method">GET</span> <span class="url">/api/health</span></div>
                <div class="description">Health check</div>
                <button onclick="fetchEndpoint('GET', '/api/health')">Try it</button>
            </div>
            
            <div class="endpoint">
                <div><span class="method">GET</span> <span class="url">/custom</span></div>
                <div class="description">Custom endpoint</div>
                <button onclick="fetchEndpoint('GET', '/custom')">Try it</button>
            </div>
            
            <div id="response">
                <h3>Response:</h3>
                <pre id="responseBody">Click a button to see the response</pre>
            </div>
            
            <script>
                async function fetchEndpoint(method, url) {
                    try {
                        const response = await fetch(url, { method });
                        const data = await response.json();
                        document.getElementById('responseBody').textContent = JSON.stringify(data, null, 2);
                    } catch (error) {
                        document.getElementById('responseBody').textContent = 'Error: ' + error.message;
                    }
                }
                
                async function createJob() {
                    try {
                        const response = await fetch('/api/jobs', { 
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                workflow_id: 'basic_text_processing',
                                inputs: {
                                    input_text: 'This is a test input for the workflow example. Let\'s see how it works!'
                                }
                            })
                        });
                        const data = await response.json();
                        document.getElementById('responseBody').textContent = JSON.stringify(data, null, 2);
                        
                        // If successful, fetch the status after 1 second
                        if (response.ok && data.id) {
                            setTimeout(async () => {
                                const statusResponse = await fetch(`/api/jobs/${data.id}/status`);
                                const statusData = await statusResponse.json();
                                document.getElementById('responseBody').textContent += '\n\nStatus:\n' + JSON.stringify(statusData, null, 2);
                            }, 1000);
                        }
                    } catch (error) {
                        document.getElementById('responseBody').textContent = 'Error: ' + error.message;
                    }
                }
            </script>
        </body>
    </html>
    """


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 