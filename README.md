# wttr.mcp

a mcp server for wttr.in

## usage

### cli

```bash
uvx --from git+https://github.com/say4n/wttr.mcp.git wttr-mcp
```

### mcp.json

```json
{
    "mcpServers": {
        "wttr-weather": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/say4n/wttr.mcp.git",
                "wttr-mcp"
            ]
        }
    }
}
```
