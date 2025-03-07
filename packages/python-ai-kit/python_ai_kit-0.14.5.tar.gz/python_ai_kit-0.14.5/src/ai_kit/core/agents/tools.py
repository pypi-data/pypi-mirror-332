from ai_kit.core.web.duckduckgo import DuckDuckGoSearch
from ai_kit.core.web.fetcher import Fetcher
from ai_kit.core.web.parser import html_to_markdown
from ai_kit.core.llms.perplexity_client import PerplexityClient
from ai_kit.utils.logging import get_text
from ai_kit.shared_console import shared_console


async def search_web(query: str) -> str:
    """Pass in a query to a basic web search engine and return results with title, url, and snippets.

    Args:
        query (str): The query to search for
    """
    client = DuckDuckGoSearch()
    search_results = await client.search(query)
    return search_results


async def fetch_web(url: str) -> str:
    """Fetch the markdown version of a web page from its url.

    Args:
        url (str): The URL to fetch
    """
    async with Fetcher() as fetcher:
        results = await fetcher.batch_fetch([url])
        raw_markdown = html_to_markdown(results[0]["content"], no_links=False)
        return raw_markdown


async def perplexity_search(query: str) -> str:
    """Perplexity is an AI-powered search engine that uses natural language processing to provide an answer along with source citations. You should use this tool to get relevant sources to explore further, not to answer the user's question.

    Args:
        query (str): The query to search for

    Returns:
        str: The response from Perplexity
        list: The citations from Perplexity
    """
    perplexity_client = PerplexityClient(model="sonar-pro")
    response = await perplexity_client.chat_completion(
        [{"role": "user", "content": query}]
    )

    # full_text = ""
    # citations = []

    # async for chunk in response:
    #     text = get_text(chunk)
    #     if text:
    #         shared_console.print(text, end="", highlight=False)
    #         full_text += text

    #     # Get citations from the chunk directly
    #     chunk_citations = chunk.get("citations", [])
    #     if chunk_citations:
    #         citations = chunk_citations  # Update citations

    # # Print numbered citations at the end
    # if show_citations:
    #     shared_console.print("\nCitations:", style="yellow")
    #     for i, citation in enumerate(citations, 1):
    #         shared_console.print(f"[{i}] {citation}", style="yellow")

    # return {"response": full_text, "citations": citations}

    return {"response": response["choices"][0]["message"]["content"], "citations": response["citations"]}
