# Claude Code

[Claude Code](https://claude.com/claude-code) подключается к Claudin.io через его совместимый с Anthropic эндпоинт. Укажите его базовый URL на Claudin.io и используйте ваш ключ в качестве токена аутентификации.

## Быстрая настройка (скрипт)

Сначала [экспортируйте ваш ключ](../getting-started/set-your-key.md), чтобы была установлена переменная `$CLAUDINIO_API_KEY`, затем запустите это. Он записывает `~/.claude/settings.json` (сначала создав резервную копию существующего файла):

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

Затем просто запустите `claude`.

## Ручная настройка

Отредактируйте `~/.claude/settings.json` самостоятельно:

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

!!! note "Почему `ANTHROPIC_API_KEY` пуст"
    Claude Code предпочитает `ANTHROPIC_API_KEY`, если он установлен. Если оставить его пустым, это заставит использовать `ANTHROPIC_AUTH_TOKEN` (ваш ключ Claudin.io) с базовым URL Claudin.io.

## Используемые значения

| Настройка | Значение |
| --- | --- |
| Базовый URL | `https://api.claudin.io` |
| Модель | `claudinio` |
| Модель субагента | `claudinio` |
| Аутентификация | `ANTHROPIC_AUTH_TOKEN` = ваш ключ |

---

Проблемы? Смотрите [распространенные ошибки](../api-reference.md#errors) или [FAQ](../faq.md).