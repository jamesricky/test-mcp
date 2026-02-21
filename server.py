from mcp.server.fastmcp import FastMCP
from tools.launches import launches

mcp = FastMCP("spacex")

mcp.tool()(launches)


if __name__ == "__main__":
    mcp.run()
