# Claude Code

[Claude Code](https://claude.com/claude-code) verbindet sich über seinen Anthropic-kompatiblen Endpunkt mit Claudin.io. Richten Sie seine Basis-URL auf Claudin.io und verwenden Sie Ihren Schlüssel als Authentifizierungstoken.

## Schnelleinrichtung (Skript)

Exportieren Sie zuerst [Ihren Schlüssel](../getting-started/set-your-key.md), damit `$CLAUDINIO_API_KEY` gesetzt ist, und führen Sie dann dies aus. Es schreibt `~/.claude/settings.json` (und erstellt zuerst eine Sicherungskopie einer vorhandenen Datei):

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

Dann führen Sie einfach `claude` aus.

## Manuelle Einrichtung

Bearbeiten Sie `~/.claude/settings.json` selbst:

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

!!! note "Warum `ANTHROPIC_API_KEY` leer ist"
    Claude Code bevorzugt `ANTHROPIC_API_KEY`, falls gesetzt. Ein leerer Wert zwingt es, `ANTHROPIC_AUTH_TOKEN` (Ihren Claudin.io-Schlüssel) gegen die Claudin.io-Basis-URL zu verwenden.

## Verwendete Werte

| Einstellung | Wert |
| --- | --- |
| Basis-URL | `https://api.claudin.io` |
| Modell | `claudinio` |
| Subagent-Modell | `claudinio` |
| Authentifizierung | `ANTHROPIC_AUTH_TOKEN` = Ihr Schlüssel |

---

Probleme? Siehe [häufige Fehler](../api-reference.md#errors) oder das [FAQ](../faq.md).