# Codex

[Codex](https://github.com/openai/codex) verbindet sich über einen benutzerdefinierten Modellanbieter in
`~/.codex/config.toml`. Claudin.io stellt die `responses`-Draht-API bereit, die Codex erwartet.

!!! warning "Verwende die Codex CLI"
    Diese Einstellungen gelten für die **Codex CLI**. Die gehostete Codex-App ermöglicht es möglicherweise nicht,
    eine benutzerdefinierte Basis-URL anzugeben.

## Manuelle Einrichtung

Füge dies zu `~/.codex/config.toml` hinzu:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Exportiere dann deinen Schlüssel (der Name muss mit `env_key` oben übereinstimmen). Der einfachste Weg ist,
ihn [einmal in deinem Shell-Profil zu setzen](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Schnelleinrichtung (Skript)

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

| Einstellung | Wert |
| --- | --- |
| Basis-URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |
| Wire API | `responses` |
| Schlüssel-Umgebungsvariable | `CLAUDINIO_API_KEY` |