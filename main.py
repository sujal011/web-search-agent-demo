from deepagents import create_deep_agent

from tools import internet_search
from prompt import research_instructions
from dotenv import load_dotenv
import os
load_dotenv()

agent = create_deep_agent(
    model="groq:meta-llama/llama-4-scout-17b-16e-instruct",
    tools=[internet_search],
    system_prompt=research_instructions,
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

# Print the agent's response
print(result["messages"][-1].content)