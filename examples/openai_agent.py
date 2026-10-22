"""Profile 01-openai. A local function tool with no external side effects."""
import os
from agents import Agent, Runner, function_tool
@function_tool
def add_numbers(a:int,b:int)->int:
    """Add two integers."""
    return a+b
agent=Agent(name='Research assistant',instructions='Use the addition tool for arithmetic.',model=os.environ['OPENAI_MODEL'],tools=[add_numbers])
print(Runner.run_sync(agent,'What is 12 plus 30?').final_output)
