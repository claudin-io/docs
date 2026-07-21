# Claude Code

O [Claude Code](https://claude.com/claude-code) liga-se ao Claudin.io através do seu endpoint compatível com Anthropic. Aponte o URL base para Claudin.io e use a sua chave como token de autenticação.

## Configuração rápida (script)

Primeiro [exporte a sua chave](../getting-started/set-your-key.md) para que `$CLAUDINIO_API_KEY` esteja definida, depois execute isto. Este script escreve `~/.claude/settings.json` (criando uma cópia de segurança de qualquer ficheiro existente primeiro):

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

Depois execute apenas `claude`.

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

!!! note "Por que `ANTHROPIC_API_KEY` está vazia"
    O Claude Code prefere `ANTHROPIC_API_KEY` se estiver definida. Deixá-la vazia
    força-o a usar `ANTHROPIC_AUTH_TOKEN` (a sua chave Claudin.io) com o
    URL base do Claudin.io.

## Valores usados

| Configuração | Valor |
| --- | --- |
| URL base | `https://api.claudin.io` |
| Modelo | `claudinio` |
| Modelo do subagente | `claudinio` |
| Autenticação | `ANTHROPIC_AUTH_TOKEN` = a sua chave |

---

Problemas? Consulte [erros comuns](../api-reference.md#errors) ou as [FAQ](../faq.md).