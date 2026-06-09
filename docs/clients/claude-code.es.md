# Claude Code

[Claude Code](https://claude.com/claude-code) se conecta a Claudin.io a través de su endpoint compatible con Anthropic. Apunte su URL base a Claudin.io y use su clave como token de autenticación.

## Configuración rápida (script)

Primero [exporte su clave](../getting-started/set-your-key.md) para que `$CLAUDINIO_API_KEY` esté configurada, luego ejecute esto. Escribe `~/.claude/settings.json` (haciendo una copia de seguridad de cualquier archivo existente primero):

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

Luego simplemente ejecute `claude`.

## Configuración manual

Edite `~/.claude/settings.json` usted mismo:

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

!!! note "Por qué `ANTHROPIC_API_KEY` está vacío"
    Claude Code prefiere `ANTHROPIC_API_KEY` si está configurada. Dejarlo vacío lo obliga a usar `ANTHROPIC_AUTH_TOKEN` (su clave de Claudin.io) contra la URL base de Claudin.io.

## Valores utilizados

| Configuración | Valor |
| --- | --- |
| URL base | `https://api.claudin.io` |
| Modelo | `claudinio` |
| Modelo de subagente | `claudinio` |
| Autenticación | `ANTHROPIC_AUTH_TOKEN` = su clave |

---

¿Problemas? Consulte [errores comunes](../api-reference.md#errors) o las [FAQ](../faq.md).