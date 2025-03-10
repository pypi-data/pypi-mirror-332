from ai_kit.core.agents.core import Agent
from ai_kit.core.agents.tools import perplexity_search, search_web, fetch_web
import asyncio
from ai_kit.shared_console import shared_console
from ai_kit.core.agents.utils import (
    generate_augmented_research_query,
    print_final_answer,
)

RESEARCH_AGENT_SYSTEM_PROMPT = """
<Your Goal>
- Your goal is to research the user's query and provide a detailed REPORT of your findings.
- Your report should always include content from multiple sources. Your reponse should include detailsed information fetched directly from each source, not just a summary.
- Your report should provide enough information for the user to take action. Be thourough and detailed, compiling and curating information to provide a comprehensive report on the query.
- You should include a number of relevant code examples from relevant documentation in your report, if applicable.
</Your Goal>

<Your Toolset>
Your toolset contains the following tools:
- perplexity_search: Use Perplexity to search the web. Perplexity is an AI-powered search engine that uses natural language processing to provide an answer along with source citations. You should use this tool to get relevant sources to explore further, not to answer the user's question.
- search_web: Use DuckDuckGo to search the web.
- fetch_web: Fetch the markdown version of a web page from its url.
</Your Toolset>

<Example Tool Call Flow>
A good example flow would be:
1. use perplexity_search to get a list of relevant sources
2. use fetch_web to review a few of the most promising sources
3. use search_web for any additional web search queries
4. Iterate as needed until you have enough information to answer the user's question.
</Example Tool Call Flow>
"""


class ResearchAgent(Agent):
    def __init__(
        self,
        model: str = "claude-3-5-sonnet-latest",
        max_tokens: int = 32000,
        enable_thinking: bool = False,
        debug: bool = False,
    ):
        self.functions = [perplexity_search, search_web, fetch_web]
        super().__init__(model, self.functions, max_tokens, enable_thinking, debug)

    async def run(
        self, query: str, max_iterations: int = 10, augment_query: bool = False
    ):
        if augment_query:
            with shared_console.status("[bold blue]Augmenting query...[/bold blue]"):
                augmented_query = await generate_augmented_research_query(
                    query
                )  # this will print the stream to the console
                query = augmented_query
        shared_console.print("[bold blue]Running Research Agent...[/bold blue]")
        messages = [
            {"role": "system", "content": RESEARCH_AGENT_SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ]
        return await super().run(messages, max_iterations)


async def main():
    agent = ResearchAgent(
        model="claude-3-7-sonnet-latest",
        max_tokens=32000,
        # max_tokens=8192, # ! for 3-5
        enable_thinking=True,
        debug=True,
    )
    test_queries = [
        "what is the most optimal way to preprocess images for a multimodal LLM with vision capibiliy, for signature extracton from images of PDF",
        "who is donald trump?",
        "what is the capital of the moon?",
    ]
    query = test_queries[0]
    history = await agent.run(query, augment_query=False)

    # Display the final answer using the dedicated function
    final_answer = history[-1]["content"]
    print_final_answer(final_answer)


if __name__ == "__main__":
    asyncio.run(main())
