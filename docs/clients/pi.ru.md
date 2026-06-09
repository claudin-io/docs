# pi

[pi](https://github.com/parallel-web/pi) считывает провайдеров из
`~/.pi/agent/models.json`. Claudin.io зарегистрирован как провайдер
`openai-completions`.

## Быстрая настройка (скрипт)

Сначала [экспортируйте ключ](../getting-started/set-your-key.md), чтобы
`$CLAUDINIO_API_KEY` был установлен. Скрипт запишет `~/.pi/agent/models.json`, создав резервную копию существующего файла:

```bash
pi_models_install() {
  local key="$1"
  local dir="$HOME/.pi/agent"
  local file="$dir/models.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<'JSONEOF'
{
  "providers": {
    "claudinio": {
      "baseUrl": "https://api.claudin.io/v1",
      "api": "openai-completions",
      "apiKey": "__CL_KEY__",
      "models": [
        { "id": "claudinio", "name": "Claudinio", "contextWindow": 256000 }
      ]
    }
  }
}
JSONEOF

  sed -i.bak "s/__CL_KEY__/${key}/g" "$file" && rm -f "$file.bak"
  echo "[ok] Configured: $file"
  echo "[ok] Run: pi --provider claudinio --model claudinio"
}

pi_models_install "$CLAUDINIO_API_KEY"
unset pi_models_install
```

Затем выполните:

```bash
pi --provider claudinio --model claudinio
```

## Ручная настройка

Поместите это в `~/.pi/agent/models.json`:

```json
{
  "providers": {
    "claudinio": {
      "baseUrl": "https://api.claudin.io/v1",
      "api": "openai-completions",
      "apiKey": "YOUR_API_KEY",
      "models": [
        { "id": "claudinio", "name": "Claudinio", "contextWindow": 256000 }
      ]
    }
  }
}
```

## Альтернатива через переменные окружения

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Параметр | Значение |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Модель | `claudinio` |
| Тип API | `openai-completions` |