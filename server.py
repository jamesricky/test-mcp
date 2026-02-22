import functools
import inspect
import json
import logging
import os
import sys
from datetime import datetime

from mcp.server.fastmcp import FastMCP
from tools.launches import launches
from tools.trending_words import most_trending_words

TOOLS_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

mcp = FastMCP("test-mcp", port=6767)


def _append_tool_call_to_log(tool_name: str, params: dict) -> None:
    timestamp = datetime.utcnow().isoformat() + "Z"
    params_json = json.dumps(params, default=str)
    line = f"{timestamp}\t{tool_name}\t{params_json}\n"
    try:
        with open(TOOLS_LOG_PATH, "a") as f:
            f.write(line)
    except OSError:
        logger.exception("Failed to write to tools.log")


def logged_tool(func):
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def wrapper(**kwargs):
            _append_tool_call_to_log(func.__name__, kwargs)
            logger.info(f"Tool called: {func.__name__}({json.dumps(kwargs, default=str)})")
            result = await func(**kwargs)
            logger.info(f"Tool finished: {func.__name__}")
            return result
    else:
        @functools.wraps(func)
        def wrapper(**kwargs):
            _append_tool_call_to_log(func.__name__, kwargs)
            logger.info(f"Tool called: {func.__name__}({json.dumps(kwargs, default=str)})")
            result = func(**kwargs)
            logger.info(f"Tool finished: {func.__name__}")
            return result
    return wrapper


mcp.tool()(logged_tool(launches))
mcp.tool()(logged_tool(most_trending_words))


if __name__ == "__main__":
    transport = os.environ.get("MCP_TRANSPORT", "streamable-http")
    if transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http")
