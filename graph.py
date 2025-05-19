from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from datetime import datetime


# Get today's date for system prompt
today = datetime.now().strftime("%Y-%m-%d")

# Create our system prompt
system_prompt = f"""
You are a helpful assistant that can search the web for information using the search tool. Return the latest nba news first if i ask for sports news. For news, please return the title, url, and summary of the news article.

today's date is {today}
"""

# Define our model
model = init_chat_model(
    # model_provider="google_genai", model="gemini-2.5-flash-preview-04-17"
    model_provider="anthropic",
    model="claude-3-5-haiku-20241022",
)

async def make_graph():
    client = MultiServerMCPClient(
        {
            # "math": {
            #     "command": "python",
            #     # Make sure to update to the full absolute path to your math_server.py file
            #     "args": ["/path/to/math_server.py"],
            #     "transport": "stdio",
            # },
            "search": {
                # Use the service name from docker-compose.yml instead of localhost
                "url": "http://mcp_server:8001/mcp", # set this if you are execution with docker compose
                # "url": "http://localhost:8001/mcp", # for local execution using the terminal
                "transport": "streamable_http",
            }
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(model=model, tools=tools, prompt=system_prompt)
    return agent
