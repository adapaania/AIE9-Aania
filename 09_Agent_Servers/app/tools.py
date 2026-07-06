from __future__ import annotations

from typing import List

from langchain_tavily import TavilySearch
from langchain_community.tools.arxiv.tool import ArxivQueryRun

from app.rag import retrieve_information


def get_tool_belt() -> List:
    tavily_tool = TavilySearch(max_results=5)
    return [tavily_tool, ArxivQueryRun(), retrieve_information]
