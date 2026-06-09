# Zed

[Zed](https://zed.dev) es compatible de forma nativa con proveedores compatibles con OpenAI bajo
`language_models.openai_compatible`.

## Configuración rápida (script)

Primero [exporta tu clave](../getting-started/set-your-key.md) para que
`$CLAUDINIO_API_KEY` esté configurada. Esto escribe `~/.config/zed/settings.json`, haciendo una copia
de seguridad de cualquier archivo existente:

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

## Configuración manual

1. Añade el proveedor a `~/.config/zed/settings.json`:

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

2. Abre el panel de agente de Zed y pega tu clave API cuando se te solicite, o establécela como
   la clave API para el proveedor **Claudinio**.
3. Selecciona **Claudinio** en el selector de modelos del panel de agente.

| Configuración | Valor |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Tokens máximos | `256000` |