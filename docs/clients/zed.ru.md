# Zed

[Zed](https://zed.dev) поддерживает провайдеров, совместимых с OpenAI, нативно под `language_models.openai_compatible`.

## Быстрая настройка (скрипт)

Сначала [экспортируйте ваш ключ](../getting-started/set-your-key.md), чтобы была установлена переменная `$CLAUDINIO_API_KEY`. Это запишет `~/.config/zed/settings.json`, создав резервную копию существующего файла:

```bash
zed_settings_install() {
  local key="$1"
  local config_dir="$HOME/.config/zed"
  local file="$config_dir/settings.json"

  mkdir -p "$config_dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "language_models": {
    "openai_compatible": {
      "Claudinio": {
        "api_url": "https://api.claudin.io/v1",
        "available_models": [
          {
            "name": "claudinio",
            "display_name": "Claudinio",
            "max_tokens": 256000
          }
        ]
      }
    }
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

zed_settings_install "$CLAUDINIO_API_KEY"
unset zed_settings_install
```

## Ручная настройка

1. Добавьте провайдера в `~/.config/zed/settings.json`:

    ```json
    {
      "language_models": {
        "openai_compatible": {
          "Claudinio": {
            "api_url": "https://api.claudin.io/v1",
            "available_models": [
              {
                "name": "claudinio",
                "display_name": "Claudinio",
                "max_tokens": 256000
              }
            ]
          }
        }
      }
    }
    ```

2. Откройте панель Agent в Zed и вставьте ваш API-ключ по запросу, или установите его как API-ключ для провайдера **Claudinio**.
3. Выберите **Claudinio** в выборе модели панели Agent.

| Настройка | Значение |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| Max tokens | `256000` |