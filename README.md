# Test MCP Server

A demo MCP server for testing and debugging tools.

## Requirements

- [uv](https://docs.astral.sh/uv/) — Python project manager

## Running the Server

`uv run server.py` is the command that **MCP clients** (e.g. Claude Desktop, Cursor) use when they spawn the server via their MCP config. The server runs over STDIO and is not meant to be run interactively in a terminal.

If you run `uv run server.py` directly in a terminal, it may fail with a JSON parse error because stdin can receive non-JSON input (e.g. a newline from the TTY).

**For interactive testing** in a terminal, use the MCP Inspector instead:

```bash
uv run mcp dev server.py
```

This opens the MCP Inspector in your browser. The CLI starts the server as a subprocess and sends only valid JSON-RPC over STDIO, so the server runs correctly.

## MCP Client Configuration

Add to your Claude Code or Claude Desktop MCP config:

```json
{
  "mcpServers": {
    "test-mcp": {
      "command": "uv",
      "args": ["--directory", "/Users/rickysmith/dev/test-mcp", "run", "server.py"]
    }
  }
}
```

## Available Tools

### `launches`

Get launches, optionally filtered by year.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `launch_year` | `int` | No | Filter to a specific year (e.g. `2020`). Omit for all launches. |

### `most_trending_words`

Returns a list of currently trending words.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `language` | `str` | No | Language for trending words: `"english"` (default) or `"german"`. |
| `limit` | `int` | No | Maximum number of words to return. Omit for all words. |
