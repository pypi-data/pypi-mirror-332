"""
Tool Agent Examples for OpenAgents JSON.

This module demonstrates how to create tool-based agents
using the decorator pattern.
"""

import asyncio
import json
import logging
from typing import Dict, Any, List, Optional

from openagents_json.agent.base import ToolAgent
from openagents_json.agent.tools import Tool

logger = logging.getLogger(__name__)


class WebSearchAgent(ToolAgent):
    """
    An agent that performs web searches and related operations.
    
    This agent demonstrates how to use tools for web-related tasks
    like searching, fetching content, and parsing data.
    """
    
    def __init__(self, name: str, **kwargs):
        """
        Initialize the web search agent.
        
        Args:
            name: Name of the agent
            **kwargs: Additional configuration parameters
        """
        super().__init__(name, **kwargs)
        
        # Register tools
        self.add_tool("search", self.search_web)
        self.add_tool("fetch_page", self.fetch_page)
        self.add_tool("extract_links", self.extract_links)
        self.add_tool("summarize", self.summarize_content)
    
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent with the given inputs.
        
        Args:
            inputs: Dictionary with the following possible keys:
                - tool: The tool to use
                - query: Search query (for search tool)
                - url: URL to fetch (for fetch_page tool)
                - content: Content to process (for extract_links and summarize tools)
                
        Returns:
            Dictionary with the results of the tool execution
        """
        if not self._initialized:
            await self.initialize()
        
        tool_name = inputs.get("tool")
        
        # If no specific tool is requested, try to determine the appropriate tool
        if not tool_name:
            if "query" in inputs:
                tool_name = "search"
            elif "url" in inputs:
                tool_name = "fetch_page"
            elif "content" in inputs and "links" in inputs.get("content", "").lower():
                tool_name = "extract_links"
            elif "content" in inputs:
                tool_name = "summarize"
            else:
                return {
                    "error": "No tool specified and couldn't determine appropriate tool",
                    "available_tools": list(self.tools.keys())
                }
        
        # Check if the requested tool exists
        if tool_name not in self.tools:
            return {
                "error": f"Unknown tool: {tool_name}",
                "available_tools": list(self.tools.keys())
            }
        
        try:
            # Call the tool with the inputs
            result = await self.call_tool(tool_name, **inputs)
            return {"result": result, "tool": tool_name}
        except Exception as e:
            logger.error(f"Error executing tool {tool_name}: {str(e)}")
            return {"error": str(e), "tool": tool_name}
    
    @Tool.register(name="search", category="web", tags={"search", "web"})
    async def search_web(self, query: str, num_results: int = 5) -> List[Dict[str, str]]:
        """
        Search the web for the given query.
        
        Args:
            query: The search query
            num_results: Number of results to return
            
        Returns:
            List of search results with title, url, and snippet
        """
        logger.info(f"Searching web for: {query}")
        
        # This is a mock implementation
        # In a real implementation, this would call a search API
        await asyncio.sleep(0.5)  # Simulate API call latency
        
        # Return mock results
        results = []
        for i in range(min(num_results, 5)):
            results.append({
                "title": f"Result {i+1} for {query}",
                "url": f"https://example.com/result{i+1}",
                "snippet": f"This is a snippet for result {i+1} about {query}..."
            })
        
        return results
    
    @Tool.register(name="fetch_page", category="web", tags={"fetch", "web"})
    async def fetch_page(self, url: str) -> Dict[str, Any]:
        """
        Fetch content from a URL.
        
        Args:
            url: The URL to fetch
            
        Returns:
            Dictionary with the page title, content, and metadata
        """
        logger.info(f"Fetching page: {url}")
        
        # This is a mock implementation
        # In a real implementation, this would use a library like aiohttp
        await asyncio.sleep(0.7)  # Simulate network latency
        
        # Return mock content
        return {
            "title": f"Page title for {url}",
            "content": f"This is the content of the page at {url}. It contains information that would be useful for the user.",
            "metadata": {
                "url": url,
                "fetched_at": "2023-01-01T00:00:00Z",
                "content_type": "text/html"
            }
        }
    
    @Tool.register(name="extract_links", category="web", tags={"extract", "links", "web"})
    async def extract_links(self, content: str) -> List[Dict[str, str]]:
        """
        Extract links from content.
        
        Args:
            content: The content to extract links from
            
        Returns:
            List of extracted links with text and url
        """
        logger.info(f"Extracting links from content: {content[:50]}...")
        
        # This is a mock implementation
        # In a real implementation, this would use a library like BeautifulSoup
        await asyncio.sleep(0.3)  # Simulate processing time
        
        # Return mock links
        return [
            {"text": "Link 1", "url": "https://example.com/link1"},
            {"text": "Link 2", "url": "https://example.com/link2"},
            {"text": "Link 3", "url": "https://example.com/link3"}
        ]
    
    @Tool.register(name="summarize", category="content", tags={"summarize", "content"})
    async def summarize_content(self, content: str, max_length: int = 100) -> str:
        """
        Summarize content.
        
        Args:
            content: The content to summarize
            max_length: Maximum length of the summary
            
        Returns:
            Summarized content
        """
        logger.info(f"Summarizing content: {content[:50]}...")
        
        # This is a mock implementation
        # In a real implementation, this might use an LLM or a summarization library
        await asyncio.sleep(0.5)  # Simulate processing time
        
        # Return mock summary
        summary = f"This is a summary of the provided content, limited to {max_length} characters."
        return summary[:max_length]


# Example usage
async def example():
    """Example of using the WebSearchAgent."""
    agent = WebSearchAgent("example_web_agent")
    
    # Initialize the agent
    await agent.initialize()
    
    # Search the web
    search_result = await agent.execute({
        "tool": "search",
        "query": "OpenAgents JSON framework"
    })
    print(f"Search result: {json.dumps(search_result, indent=2)}")
    
    # Fetch a page
    fetch_result = await agent.execute({
        "tool": "fetch_page",
        "url": "https://example.com/openagents"
    })
    print(f"Fetch result: {json.dumps(fetch_result, indent=2)}")
    
    # Extract links
    extract_result = await agent.execute({
        "tool": "extract_links",
        "content": "Here are some links: <a href='https://example.com'>Example</a>"
    })
    print(f"Extract result: {json.dumps(extract_result, indent=2)}")
    
    # Summarize content
    summarize_result = await agent.execute({
        "tool": "summarize",
        "content": "This is a long piece of content that needs to be summarized. It contains multiple sentences and ideas that should be condensed into a shorter form.",
        "max_length": 50
    })
    print(f"Summarize result: {json.dumps(summarize_result, indent=2)}")


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Run the example
    asyncio.run(example()) 