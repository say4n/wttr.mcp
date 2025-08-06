from fastmcp import FastMCP
import pywttr

mcp = FastMCP("wttr.mcp", version="0.1.0")


@mcp.tool(description="Get current weather for a location")
def get_current_weather(location: str) -> dict:
    with pywttr.Wttr() as wttr:
        return wttr.weather("Paris" if not location else location)

def main():
    mcp.run()

if __name__ == "__main__":
    main()
