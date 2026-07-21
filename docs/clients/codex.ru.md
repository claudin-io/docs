# Codex

[Codex](https://github.com/openai/codex) подключается через пользовательского провайдера модели в `~/.codex/config.toml`. Claudin.io предоставляет wire API `responses`, который ожидает Codex.

!!! warning "Используйте Codex CLI"
    Эти настройки применимы к **Codex CLI**. Хостированное приложение Codex может не позволять указать пользовательский базовый URL.

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

Затем экспортируйте ваш ключ (имя должно совпадать с `env_key` выше). Самый простой способ — [установить его один раз в вашем shell профиле](../getting-started/set-your-key.md):

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
    echo "[ok] Резервная копия: $file.claudinio.bak"
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

  echo "[ok] Настроен: $file"
  echo "[ok] Убедитесь, что CLAUDINIO_API_KEY экспортирован в вашем shell"
}

codex_config_install
unset codex_config_install
```

| Параметр | Значение |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Модель | `claudinio` |
| Wire API | `responses` |
| Переменная окружения для ключа | `CLAUDINIO_API_KEY` |