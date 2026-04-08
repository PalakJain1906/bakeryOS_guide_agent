import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.langchain_tool import LangchainTool

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# --- Setup Logging and Environment ---
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()
model_name = os.getenv("MODEL")

# Tool to save the user's question into the agent's memory (State)
def add_prompt_to_state(
    tool_context: ToolContext, prompt: str
) -> dict[str, str]:
    """Saves the user's bakery inquiry to the state."""
    tool_context.state["PROMPT"] = prompt
    logging.info(f"[BakeryOS State] User Query Saved: {prompt}")
    return {"status": "success"}

# Tool to allow the agent to research information on Wikipedia
wikipedia_tool = LangchainTool(
    tool=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
)

# 1. Bakery Researcher Agent
bakery_researcher = Agent(
    name="bakery_researcher",
    model=model_name,
    description="Researches ingredient science, baking chemistry, and nutritional facts.",
    instruction="""
    You are a professional Food Scientist. Your goal is to research the technical details of the user's PROMPT.
    
    - Use Wikipedia to find facts about ingredients (e.g., cocoa types, protein powders, organic sweeteners).
    - Focus on the science: How do these ingredients react? What are their health benefits?
    - Synthesize your findings into technical notes.

    PROMPT:
    { PROMPT }
    """,
    tools=[wikipedia_tool],
    output_key="research_data" 
)

# 2. Bakery Response Formatter Agent
bakery_formatter = Agent(
    name="bakery_formatter",
    model=model_name,
    description="Converts technical data into friendly advice for bakery customers.",
    instruction="""
    You are the expert head baker at an organic, home-based bakery in Surat. 
    Your task is to take the RESEARCH_DATA and present it to the user.

    - Translate technical science into simple, helpful baking advice.
    - Focus on how it helps make their cookies or treats better (texture, taste, health).
    - Maintain a professional, warm, and engaging tone.

    RESEARCH_DATA:
    { research_data }
    """
)

# The Main Workflow
bakery_workflow = SequentialAgent(
    name="bakery_workflow",
    description="The process of researching and then formatting bakery advice.",
    sub_agents=[
        bakery_researcher, 
        bakery_formatter,   
    ]
)

# The Entry Point (Root Agent)
root_agent = Agent(
    name="bakery_manager",
    model=model_name,
    description="The main entry point for BakeryOS.",
    instruction="""
    - Greet the user as their BakeryOS Assistant and ask how you can help with their baking science today.
    - When the user asks a question, use the 'add_prompt_to_state' tool to save it.
    - Immediately transfer control to the 'bakery_workflow' to get them an answer.
    """,
    tools=[add_prompt_to_state],
    sub_agents=[bakery_workflow]
) # <--- Make sure this bracket is closed
