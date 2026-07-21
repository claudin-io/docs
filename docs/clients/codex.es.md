# Codex

[Codex](https://github.com/openai/codex) se conecta a través de un proveedor de modelo personalizado en `~/.codex/config.toml`. Claudin.io expone la API de conexión `responses` que Codex espera.

!!! warning "Usa la CLI de Codex"
    Estos ajustes aplican a la **CLI de Codex**. Es posible que la aplicación Codex alojada no te permita apuntar a una URL base personalizada.

## Configuración manual

Añade esto a `~/.codex/config.toml`:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Luego exporta tu clave (el nombre debe coincidir con `env_key` arriba). La forma más sencilla es [configurarla una vez en tu perfil de shell](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Configuración rápida (script)

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

| Ajuste | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| API de conexión | `responses` |
| Variable de entorno de clave | `CLAUDINIO_API_KEY` |