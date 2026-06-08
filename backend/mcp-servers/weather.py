from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Get weather by the location"""
    return f"It is always raining in {location}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")