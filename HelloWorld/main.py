from mcp.server.fastmcp import FastMCPServer

mcp = FastMCPServer("HelloWorld")

@mcp.tool()
def get_sample(test: str) -> str:
    """A sample tool that returns a greeting message."""
    return "This is a sample tool."

if __name__ == "__main__":
    mcp.run()
