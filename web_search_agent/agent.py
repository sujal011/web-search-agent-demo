"""Main agent construction for the web search agent."""

from deepagents import create_deep_agent

from web_search_agent.utils import internet_search


# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.

- `max_results`: integer (e.g. 5)
- `include_raw_content`: boolean (`true`/`false`)

The tool wrapper supports string forms for robustness, but prefer correctly typed values to avoid validation issues.
"""


def create_web_search_agent():
    """Create and return the web search agent.
    
    Returns:
        An agent configured with Groq LLM, internet search tools, and research instructions.
    """
    agent = create_deep_agent(
        model="groq:meta-llama/llama-4-scout-17b-16e-instruct",
        tools=[internet_search],
        system_prompt=research_instructions,
    )
    return agent


# Create the agent instance for LangGraph
agent = create_web_search_agent()


if __name__ == "__main__":
    # Example usage
    from dotenv import load_dotenv
    
    load_dotenv()
    
    result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})
    
    # Print the agent's response
    print(result["messages"][-1].content)
