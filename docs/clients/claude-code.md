# Claude Code

[Claude Code](https://claude.com/claude-code) connects to Claudin.io through its
Anthropic-compatible endpoint. Point its base URL at Claudin.io and use your key
as the auth token.

## Quick setup (script)

First [export your key](../getting-started/set-your-key.md) so
`$CLAUDINIO_API_KEY` is set, then run this. It writes `~/.claude/settings.json`
(backing up any existing file first):

```bash
claude_settings_install() {
  local key="$1"
  local dir="$HOME/.claude"
  local file="$dir/settings.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "${key}",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

claude_settings_install "$CLAUDINIO_API_KEY"
unset claude_settings_install
```

Then just run `claude`.

## Manual setup

Edit `~/.claude/settings.json` yourself:

```json
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
```

!!! note "Why `ANTHROPIC_API_KEY` is empty"
    Claude Code prefers `ANTHROPIC_API_KEY` if it's set. Leaving it empty
    forces it to use `ANTHROPIC_AUTH_TOKEN` (your Claudin.io key) against the
    Claudin.io base URL.

## Values used

| Setting | Value |
| --- | --- |
| Base URL | `https://api.claudin.io` |
| Model | `claudinio` |
| Subagent model | `claudinio` |
| Auth | `ANTHROPIC_AUTH_TOKEN` = your key |

---

Trouble? See [common errors](../api-reference.md#errors) or the [FAQ](../faq.md).
