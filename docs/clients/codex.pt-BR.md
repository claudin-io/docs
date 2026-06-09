# Codex

[Codex](https://github.com/openai/codex) conecta-se através de um provedor de modelo personalizado em
`~/.codex/config.toml`. O Claudin.io expõe a API wire `responses` que o Codex espera.

!!! warning "Use o Codex CLI"
    Estas configurações se aplicam ao **Codex CLI**. O aplicativo Codex hospedado pode não permitir
    que você aponte para uma URL base personalizada.

## Configuração manual

Adicione isto ao `~/.codex/config.toml`:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Em seguida, exporte sua chave (o nome deve corresponder ao `env_key` acima). A maneira mais fácil é
[defini-la uma vez no seu perfil do shell](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Configuração rápida (script)

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

| Configuração | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Wire API | `responses` |
| Variável de ambiente da chave | `CLAUDINIO_API_KEY` |