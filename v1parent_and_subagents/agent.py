import os
from dotenv import load_dotenv
from google.adk import Agent

from google.genai import types
from typing import Optional, List, Dict

from google.adk.tools.tool_context import ToolContext

load_dotenv()
model_name = os.getenv("MODEL")

# Tools


# Agents
# root_agent -|
#             |- travel_brainstormer
#             |- attractions_planner

attractions_planner = Agent(
    name="attractions_planner",
    model=model_name,
    description="Build a list of attractions to visit in a country.",
    instruction="""
        - Provide the user options for attractions to visit within their selected country.
        """,
    )

travel_brainstormer = Agent(
    name="travel_brainstormer",
    model=model_name,
    description="Help a user decide what country to visit.",
    instruction="""
        Provide a few suggestions of popular countries for travelers.
        
        Help a user identify their primary goals of travel:
        adventure, leisure, learning, shopping, or viewing art

        Identify countries that would make great destinations
        based on their priorities.
        """,
)

root_agent = Agent(
    name="travel_greeter",
    model=model_name,
    description="Start a user on a travel adventure.",
    instruction="""
        Ask the user if they know where they'd like to travel
        or if they need some help deciding.
        If they need help deciding, send them to
        'travel_brainstormer'.
        If they know what country they'd like to visit,
        send them to the 'attractions_planner'.
        """,
    sub_agents=[travel_brainstormer, attractions_planner]

)
