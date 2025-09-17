from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime


def current_time() -> dict:
    """Get current time in the format YYYY-MM-DD HH:MM:SS"""
    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool Agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - current_time: Get the current time in the format YYYY-MM-DD HH:MM:SS
    """,
    tools=[current_time],
)

