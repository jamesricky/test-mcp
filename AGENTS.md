# SpaceX MCP Server

## Project Goal

A demo MCP (Model Context Protocol) server for testing and debugging tools using an MCP server. It exposes a `launches` tool backed by the SpaceX API as a concrete example, and runs locally over STDIO for use with Claude Code, Claude Desktop, or any MCP-compatible client.

## Implementation

### Tech Stack

- **Python 3.12+** managed via `uv`
- **mcp[cli]** — official MCP Python SDK with FastMCP
- **httpx** — async HTTP client for SpaceX API requests
- **Transport**: STDIO (default)

### SpaceX API (v4)

- Base URL: `https://api.spacexdata.com/v4`
- All launches: `GET /launches`
- Filtered launches: `POST /launches/query` with MongoDB-style query body
- Docs: https://github.com/r-spacex/SpaceX-API

### Project Structure

```
test-mcp/
  pyproject.toml   # Project config and dependencies
  server.py        # MCP server entry point
  CLAUDE.md        # Points to this file
  AGENTS.md        # This file — project docs and agent instructions
```

### Tool: `launches`

- **Parameter**: `launch_year` (optional `int`)
- **When `launch_year` is set**: POST to `/v4/launches/query` filtering `date_utc` to the given year range
- **When `launch_year` is omitted**: GET `/v4/launches` returning all launches
- **Returns**: Formatted text with flight number, name, date, success status, and details

### Running the Server

```bash
uv run server.py
```

### MCP Client Configuration

```json
{
  "mcpServers": {
    "spacex": {
      "command": "uv",
      "args": ["--directory", "/Users/rickysmith/dev/test-mcp", "run", "server.py"]
    }
  }
}
```

## User Preferences

- Keep things concise and direct
- Prefer simple implementations — avoid over-engineering
- Use `uv` for Python project management
- Use type hints (e.g. `int | None`)
- No emojis unless explicitly requested

## Self-Update Instructions

When the user provides new or updated information about this project — including changes to goals, preferences, implementation details, conventions, or any other relevant context — **update this file immediately** to reflect that information. This ensures AGENTS.md always serves as the single source of truth for any agent working on this project.

Examples of when to update:
- User clarifies or changes a preference (e.g. coding style, tooling)
- New tools or endpoints are added to the server
- Project structure changes
- New conventions or patterns are established
- User corrects or refines any section of this document
