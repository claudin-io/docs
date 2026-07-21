# Codex

[Codex](https://github.com/openai/codex) si connette tramite un provider di modello personalizzato in `~/.codex/config.toml`. Claudin.io espone l'API wire `responses` che Codex si aspetta.

!!! warning "Usa la CLI di Codex"
    Queste impostazioni si applicano alla **CLI di Codex**. L'app Codex ospitata potrebbe non permetterti di puntare a un URL base personalizzato.

## Configurazione manuale

Aggiungi questo a `~/.codex/config.toml`:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Poi esporta la tua chiave (il nome deve corrispondere a `env_key` sopra). Il modo più semplice è [impostarla una volta nel tuo profilo shell](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Configurazione rapida (script)

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

| Impostazione | Valore |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modello | `claudinio` |
| Wire API | `responses` |
| Variabile d'ambiente della chiave | `CLAUDINIO_API_KEY` |