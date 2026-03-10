# tools.py
from tavily import TavilyClient
import os

from dotenv import load_dotenv
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def tavily_search(query: str):

    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    results = []

    for r in response["results"]:
        results.append(
            f"Title: {r['title']}\nContent: {r['content']}\nURL: {r['url']}"
        )

    return "\n\n".join(results)