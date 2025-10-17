from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import logging

server_params = StdioServerParameters(
    command="uv",
    args=["run", "weather.py"]
)

logging.basicConfig(level=logging.INFO)

async def run():
    async with stdio_client(server_params) as (read, write):
        print("Client connected to server.")
        async with ClientSession(read, write) as session:
            print("Client session started.")

            await session.initialize()
            print("Client session initialized.")

            print("Listing tools..")
            tools = await session.list_tools()
            print(f"Available tools: {tools}")

            print("Calling tools")
            result = await session.call_tool("get_weather", arguments={"location": "New York"})
            print(f"Weather Tool Result: {result}")

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except Exception as e:
        logging.error(f"Error in client: {e}")