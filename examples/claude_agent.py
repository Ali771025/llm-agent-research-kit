"""Profile 04-claude-agent. Read-only tool permissions for this example."""
import asyncio,os
from claude_agent_sdk import query,ClaudeAgentOptions
async def main():
 async for message in query(prompt='Explain the Python files in this directory briefly. Do not modify files.',options=ClaudeAgentOptions(cwd=os.getcwd(),allowed_tools=['Read','Glob','Grep'],permission_mode='default',max_turns=3)):
  print(message)
asyncio.run(main())
