# Claude Code

[Claude Code](https://claude.com/claude-code) si connette a Claudin.io tramite il suo endpoint compatibile con Anthropic. Punta il suo URL base a Claudin.io e usa la tua chiave come token di autenticazione.

## Configurazione rapida (script)

Prima [esporta la tua chiave](../getting-started/set-your-key.md) in modo che `$CLAUDINIO_API_KEY` sia impostata, poi esegui questo. Scrive `~/.claude/settings.json` (creando un backup di qualsiasi file esistente prima):

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

Poi esegui semplicemente `claude`.

## Configurazione manuale

Modifica tu stesso `~/.claude/settings.json`:

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

!!! note "Perché `ANTHROPIC_API_KEY` è vuota"
    Claude Code preferisce `ANTHROPIC_API_KEY` se è impostata. Lasciandola vuota lo forza a usare `ANTHROPIC_AUTH_TOKEN` (la tua chiave Claudin.io) con l'URL base di Claudin.io.

## Valori utilizzati

| Impostazione | Valore |
| --- | --- |
| URL base | `https://api.claudin.io` |
| Modello | `claudinio` |
| Modello subagente | `claudinio` |
| Autenticazione | `ANTHROPIC_AUTH_TOKEN` = la tua chiave |

---

Problemi? Vedi [errori comuni](../api-reference.md#errors) o le [FAQ](../faq.md).