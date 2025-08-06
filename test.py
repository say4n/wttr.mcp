import asyncio
from fastmcp import Client

client = Client("main.py")


async def call_tool(location: str):
    async with client:
        result = await client.call_tool("get_current_weather", {"location": location})
        print(result)


asyncio.run(call_tool("London"))
