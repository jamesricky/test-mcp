# Test MCP Server

A demo MCP server for testing and debugging tools.

## Requirements

- [uv](https://docs.astral.sh/uv/) — Python project manager

## Starting the Server

```bash
uv run server.py
```

The server runs over STDIO and blocks until stopped. Press `Ctrl+C` to stop it.

## Interactive Testing (MCP Inspector)

```bash
uv run mcp dev server.py
```

Opens the MCP Inspector in your browser for interactive tool testing.

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

Returns a static list of 10 currently trending words (e.g. "rizz", "glazing", "mid").

No parameters.
