import functools
import inspect
import json
import logging
import sys

from mcp.server.fastmcp import FastMCP
from tools.launches import launches
from tools.trending_words import most_trending_words

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

mcp = FastMCP("test-mcp")


def logged_tool(func):
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def wrapper(**kwargs):
            logger.info(f"Tool called: {func.__name__}({json.dumps(kwargs, default=str)})")
            result = await func(**kwargs)
            logger.info(f"Tool finished: {func.__name__}")
            return result
    else:
        @functools.wraps(func)
        def wrapper(**kwargs):
            logger.info(f"Tool called: {func.__name__}({json.dumps(kwargs, default=str)})")
            result = func(**kwargs)
            logger.info(f"Tool finished: {func.__name__}")
            return result
    return wrapper


mcp.tool()(logged_tool(launches))
mcp.tool()(logged_tool(most_trending_words))


if __name__ == "__main__":
    mcp.run()
