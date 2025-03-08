# Figma MCP Python

[![PyPI version](https://badge.fury.io/py/figma-mcp.svg)](https://badge.fury.io/py/figma-mcp)

Allow your AI coding agents to access Figma files & prototypes directly.

## Quick Installation with pipx

```bash
pipx install figma-mcp
```

### For Cursor:

1. In settings, add an MCP server using the command:
```shell
figma-mcp --figma-api-key=your_figma_key
```

2. OR Add a `.cursor/mcp.json` file in your project:

```json
{
	"mcpServers": {
		"figma-python": {
			"command": "figma-mcp",
			"env": {
				"FIGMA_API_TOKEN": "your_figma_api_key"
			}
		}
	}
}
```

### For other IDEs like Windsurf, use an MCP configuration file (e.g., `mcp_config.json`):

```json
{
  "mcpServers": {
    "figma-python": {
      "command": "figma-mcp",
      "args": [
        "--figma-api-key=your_figma_key"
      ]
    } 
  }
}
```



# Install uv and set up the environment
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
uv sync

# Run locally
python -m figma_mcp.main
```


