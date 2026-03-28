"""Tools for the web search agent."""

import os
from typing import Literal
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def internet_search(
    query: str,
    max_results: int | str = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool | str = False,
):
    """Run a web search using Tavily API.
    
    Args:
        query: The search query string
        max_results: Maximum number of search results to return (default: 5). Can be int or str.
        topic: Search topic - "general", "news", or "finance" (default: "general")
        include_raw_content: Whether to include raw web content (default: False). Can be bool or str.
    
    Returns:
        Search results from Tavily API
    """
    if isinstance(max_results, str):
        max_results = max_results.strip()
        if max_results.isdigit():
            max_results = int(max_results)
        else:
            try:
                max_results = int(float(max_results))
            except ValueError:
                max_results = 5

    if isinstance(include_raw_content, str):
        include_raw_content = include_raw_content.strip().lower() in (
            "true",
            "1",
            "yes",
            "y",
            "on",
        )

    include_raw_content = bool(include_raw_content)

    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )
