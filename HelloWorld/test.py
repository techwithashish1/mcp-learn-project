from mcp.server.fastmcp import FastMCP
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

mcp = FastMCP(name="Test", debug=True)

@mcp.tool()
def get_sample(test: str) -> str:
    """A sample tool that returns a greeting message."""
    return "This is a sample tool."

if __name__ == "__main__":
    try:
        mcp.run()  # FastMCP doesn't take host and port parameters
    except Exception as e:
        logging.error(f"Error starting server: {e}")
