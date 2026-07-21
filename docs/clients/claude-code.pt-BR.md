# Claude Code

[Claude Code](https://claude.com/claude-code) se conecta ao Claudin.io por meio de seu endpoint compatível com Anthropic. Aponte sua URL base para Claudin.io e use sua chave como token de autenticação.

## Configuração rápida (script)

Primeiro, [exporte sua chave](../getting-started/set-your-key.md) para que `$CLAUDINIO_API_KEY` esteja definida, então execute este comando. Ele escreve `~/.claude/settings.json` (fazendo backup de qualquer arquivo existente primeiro):

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

Em seguida, execute `claude`.

## Configuração manual

Edite `~/.claude/settings.json` você mesmo:

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

!!! note "Por que `ANTHROPIC_API_KEY` está vazio"
    Claude Code prefere `ANTHROPIC_API_KEY` se estiver definida. Deixá-la vazia força o uso de `ANTHROPIC_AUTH_TOKEN` (sua chave Claudin.io) contra a URL base do Claudin.io.

## Valores utilizados

| Configuração | Valor |
| --- | --- |
| URL base | `https://api.claudin.io` |
| Modelo | `claudinio` |
| Modelo do subagente | `claudinio` |
| Autenticação | `ANTHROPIC_AUTH_TOKEN` = sua chave |

---

Problemas? Veja [erros comuns](../api-reference.md#errors) ou o [FAQ](../faq.md).