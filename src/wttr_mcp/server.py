from fastmcp import FastMCP
import pywttr

mcp = FastMCP("wttr.mcp", version="0.1.0")


@mcp.tool
def get_current_weather(location: str) -> str:
    with pywttr.Wttr() as wttr:
        return wttr.weather("Paris" if not location else location).model_dump_json()

def main():
    mcp.run()

if __name__ == "__main__":
    main()
