# Claude Code

O [Claude Code](https://claude.com/claude-code) se conecta ao Claudin.io através do seu
endpoint compatível com Anthropic. Aponte a URL base dele para o Claudin.io e use sua chave
como token de autenticação.

## Configuração rápida (script)

Primeiro [exporte sua chave](../getting-started/set-your-key.md) para que
`$CLAUDINIO_API_KEY` esteja definida, então execute isto. Ele cria `~/.claude/settings.json`
(fazendo backup de qualquer arquivo existente primeiro):

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

Depois é só executar `claude`.

## Configuração manual

Edite o `~/.claude/settings.json` você mesmo(a):

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

!!! note "Por que `ANTHROPIC_API_KEY` está vazia"
    O Claude Code prefere `ANTHROPIC_API_KEY` se ela estiver definida. Deixá-la vazia
    força o uso de `ANTHROPIC_AUTH_TOKEN` (sua chave do Claudin.io) contra a
    URL base do Claudin.io.

## Valores utilizados

| Configuração | Valor |
| --- | --- |
| URL base | `https://api.claudin.io` |
| Modelo | `claudinio` |
| Modelo do subagente | `claudinio` |
| Autenticação | `ANTHROPIC_AUTH_TOKEN` = sua chave |

---

Problemas? Consulte [erros comuns](../api-reference.md#errors) ou o [FAQ](../faq.md).