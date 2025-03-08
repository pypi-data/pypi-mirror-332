#!/usr/bin/env python3

"""
This tool is used to search for academic papers on Semantic Scholar.
"""

import logging
from typing import Annotated, Any, Optional
import hydra
import requests
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langchain_core.tools.base import InjectedToolCallId
from langgraph.types import Command
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SearchInput(BaseModel):
    """Input schema for the search papers tool."""

    query: str = Field(
        description="Search query string to find academic papers."
        "Be specific and include relevant academic terms."
    )
    limit: int = Field(
        default=5, description="Maximum number of results to return", ge=1, le=100
    )
    year: Optional[str] = Field(
        default=None,
        description="Year range in format: YYYY for specific year, "
        "YYYY- for papers after year, -YYYY for papers before year, or YYYY:YYYY for range",
    )
    tool_call_id: Annotated[str, InjectedToolCallId]


# Load hydra configuration
with hydra.initialize(version_base=None, config_path="../../configs"):
    cfg = hydra.compose(config_name="config", overrides=["tools/search=default"])
    cfg = cfg.tools.search


@tool("search_tool", args_schema=SearchInput, parse_docstring=True)
def search_tool(
    query: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    limit: int = 5,
    year: Optional[str] = None,
) -> Command[Any]:
    """
    Search for academic papers on Semantic Scholar.

    Args:
        query (str): The search query string to find academic papers.
        tool_call_id (Annotated[str, InjectedToolCallId]): The tool call ID.
        limit (int, optional): The maximum number of results to return. Defaults to 2.
        year (str, optional): Year range for papers.
        Supports formats like "2024-", "-2024", "2024:2025". Defaults to None.

    Returns:
        The number of papers found on Semantic Scholar.
    """
    logger.info("Searching for papers on %s", query)
    endpoint = cfg.api_endpoint
    params = {
        "query": query,
        "limit": min(limit, 100),
        "fields": ",".join(cfg.api_fields),
    }

    # Add year parameter if provided
    if year:
        params["year"] = year

    response = requests.get(endpoint, params=params, timeout=10)
    data = response.json()
    papers = data.get("data", [])
    logger.info("Received %d papers", len(papers))
    if not papers:
        return Command(
            update={  # Place 'messages' inside 'update'
                "messages": [
                    ToolMessage(
                        content="No papers found. Please try a different search query.",
                        tool_call_id=tool_call_id,
                    )
                ]
            }
        )
    # Create a dictionary to store the papers
    filtered_papers = {
        paper["paperId"]: {
            # "semantic_scholar_id": paper["paperId"],  # Store Semantic Scholar ID
            "Title": paper.get("title", "N/A"),
            "Abstract": paper.get("abstract", "N/A"),
            "Year": paper.get("year", "N/A"),
            "Citation Count": paper.get("citationCount", "N/A"),
            "URL": paper.get("url", "N/A"),
            # "arXiv_ID": paper.get("externalIds", {}).get(
            #     "ArXiv", "N/A"
            # ),  # Extract arXiv ID
        }
        for paper in papers
        if paper.get("title") and paper.get("authors")
    }

    logger.info("Filtered %d papers", len(filtered_papers))

    # Prepare content with top 3 paper titles and years
    top_papers = list(filtered_papers.values())[:3]
    top_papers_info = "\n".join(
        [
            f"{i+1}. {paper['Title']} ({paper['Year']})"
            for i, paper in enumerate(top_papers)
        ]
    )

    content = (
        "Search was successful. Papers are attached as an artifact. "
        "Here is a summary of the search results:\n"
    )
    content += f"Number of papers found: {len(filtered_papers)}\n"
    content += f"Query: {query}\n"
    content += f"Year: {year}\n" if year else ""
    content += "Top papers:\n" + top_papers_info

    return Command(
        update={
            "papers": filtered_papers,  # Now sending the dictionary directly
            "last_displayed_papers": "papers",
            "messages": [
                ToolMessage(
                    content=content,
                    tool_call_id=tool_call_id,
                    artifact=filtered_papers,
                )
            ],
        }
    )
