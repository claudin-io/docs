# Codex

[Codex](https://github.com/openai/codex) se conecta mediante un proveedor de modelo personalizado en
`~/.codex/config.toml`. Claudin.io expone la API wire `responses` que Codex
espera.

!!! warning "Usa la CLI de Codex"
    Estos ajustes se aplican a la **CLI de Codex**. La aplicación Codex alojada puede no
    permitirte apuntar a una URL base personalizada.

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

Luego exporta tu clave (el nombre debe coincidir con `env_key` de arriba). La forma
más fácil es [configurarla una vez en tu perfil de shell](../getting-started/set-your-key.md):

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

  echo "[ok] Configurado: $file"
  echo "[ok] Asegúrate de que CLAUDINIO_API_KEY esté exportada en tu shell"
}

codex_config_install
unset codex_config_install
```

| Configuración | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| API wire | `responses` |
| Variable de entorno de clave | `CLAUDINIO_API_KEY` |