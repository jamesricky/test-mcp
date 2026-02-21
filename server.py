from mcp.server.fastmcp import FastMCP
from tools.launches import launches
from tools.trending_words import most_trending_words

mcp = FastMCP("spacex")

mcp.tool()(launches)
mcp.tool()(most_trending_words)


if __name__ == "__main__":
    mcp.run()
