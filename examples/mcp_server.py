"""Profile 13-mcp. stdio server for an MCP client, Ctrl+C to stop."""
from mcp.server.fastmcp import FastMCP
mcp=FastMCP('research-demo')
@mcp.tool()
def add(a:int,b:int)->int:
    """Add two integers."""
    return a+b
if __name__=='__main__':mcp.run(transport='stdio')
