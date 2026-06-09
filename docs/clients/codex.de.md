# Codex

[Codex](https://github.com/openai/codex) verbindet sich über einen benutzerdefinierten Modellanbieter in
`~/.codex/config.toml`. Claudin.io macht die `responses`-Wire-API verfügbar, die Codex erwartet.

!!! warning "Codex CLI verwenden"
    Diese Einstellungen gelten für die **Codex CLI**. Die gehostete Codex-App erlaubt möglicherweise nicht, eine benutzerdefinierte Basis-URL anzugeben.

## Manuelle Einrichtung

Fügen Sie dies zu `~/.codex/config.toml` hinzu:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Exportieren Sie dann Ihren Schlüssel (der Name muss mit dem obigen `env_key` übereinstimmen). Der einfachste Weg ist,
ihn [einmal in Ihrem Shell-Profil zu setzen](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Schnelle Einrichtung (Skript)

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
| Wire-API | `responses` |
| Umgebungsvariable für den Schlüssel | `CLAUDINIO_API_KEY` |