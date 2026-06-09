# Kilo Code

[Kilo Code](https://kilo.ai) использует блок провайдера, совместимый с OpenAI.
Идентификатор модели: `claudinio/claudinio` (провайдер/модель).

## Быстрая настройка (скрипт)

Сначала [экспортируйте ваш ключ](../getting-started/set-your-key.md), чтобы была
установлена `$CLAUDINIO_API_KEY`. Этот скрипт записывает файл `~/.config/kilo/kilo.jsonc`, создавая резервную копию любого существующего файла:

```bash
kilo_config_install() {
  local key="$1"
  local dir="$HOME/.config/kilo"
  local file="$dir/kilo.jsonc"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<'JSONCEOF'
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "__CL_KEY__"
      },
      "models": {
        "claudinio": {
          "name": "Claudinio",
          "tool_call": true,
          "limit": { "context": 128000, "output": 16384 }
        }
      }
    }
  }
}
JSONCEOF

  sed -i.bak "s/__CL_KEY__/${key}/g" "$file" && rm -f "$file.bak"
  echo "[ok] Configured: $file"
}

kilo_config_install "$CLAUDINIO_API_KEY"
unset kilo_config_install
```

Затем запустите `kilo`.

## Ручная настройка

Поместите это в `~/.config/kilo/kilo.jsonc`:

```jsonc
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "YOUR_API_KEY"
      },
      "models": {
        "claudinio": {
          "name": "Claudinio",
          "tool_call": true,
          "limit": { "context": 128000, "output": 16384 }
        }
      }
    }
  }
}
```

## Альтернатива с переменными окружения

Kilo также использует стандартные переменные окружения OpenAI:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Настройка | Значение |
| --- | --- |
| Базовый URL | `https://api.claudin.io/v1` |
| Модель | `claudinio/claudinio` |
| Вызовы инструментов | включены |