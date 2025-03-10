from ai_kit.core.agents.research import ResearchAgent
from ai_kit.core.agents.utils import print_final_answer

async def research_agent_command(query: str, augment_query: bool = False):
    agent = ResearchAgent(
        model="claude-3-5-sonnet-latest",
        # max_tokens=32000,
        max_tokens=8192, # ! for 3-5
        enable_thinking=False,
        debug=False,
    )
    history = await agent.run(query, augment_query=augment_query)

    # Display the final answer using the dedicated function
    final_answer = history[-1]["content"]
    print_final_answer(final_answer)