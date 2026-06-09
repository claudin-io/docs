# Codex

[Codex](https://github.com/openai/codex) подключается через собственного провайдера модели в `~/.codex/config.toml`. Claudin.io предоставляет wire-интерфейс `responses`, который ожидает Codex.

!!! warning "Используйте Codex CLI"
    Эти настройки применяются к **Codex CLI**. Хостируемое приложение Codex может не позволить указать собственный базовый URL.

## Ручная настройка

Добавьте это в `~/.codex/config.toml`:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Затем экспортируйте ваш ключ (имя должно совпадать с `env_key` выше). Самый простой способ — [установить его один раз в вашем профиле оболочки](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Быстрая настройка (скрипт)

```bash
codex_config_install() {
  local key="$1"
  local dir="$HOME/.codex"
  local file="$dir/config.toml"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<TOMLEOF
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
TOMLEOF

  echo "[ok] Configured: $file"
  echo "[ok] Make sure CLAUDINIO_API_KEY is exported in your shell"
}

codex_config_install
unset codex_config_install
```

| Настройка | Значение |
| --- | --- |
| Базовый URL | `https://api.claudin.io/v1` |
| Модель | `claudinio` |
| Wire API | `responses` |
| Переменная окружения ключа | `CLAUDINIO_API_KEY` |