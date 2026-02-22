# Test MCP Server

A demo MCP server for testing and debugging tools.

## Requirements

- [uv](https://docs.astral.sh/uv/) — Python project manager

## Running the Server

Start the server locally:

```bash
uv run server.py
```

The server listens at **`http://127.0.0.1:6767/mcp`** (streamable HTTP). Connect from Claude Desktop or Claude in the browser via **Add custom connector** and enter:

```
http://127.0.0.1:6767/mcp
```

No config file is needed for this URL-based connection.

## Claude Desktop (config file)

To use the server via Claude Desktop's config file (command/args), Claude spawns the process and talks over STDIO. Set `MCP_TRANSPORT=stdio` in the server's `env` so the server uses STDIO when spawned. Do not run `uv run server.py` manually when using this flow.

Example (add to your Claude Desktop config, e.g. `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
"mcpServers": {
  "test-mcp": {
    "command": "uv",
    "args": ["--directory", "/path/to/test-mcp", "run", "server.py"],
    "env": {
      "MCP_TRANSPORT": "stdio"
    }
  }
}
```

## Interactive Testing (MCP Inspector)

```bash
uv run mcp dev server.py
```

Opens the MCP Inspector in your browser. With the server using streamable-http, the Inspector can connect to the same URL (`http://127.0.0.1:6767/mcp`) once the server is running, or the CLI may start the server in a compatible mode.

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
