# Zed

O [Zed](https://zed.dev) suporta provedores compatíveis com OpenAI nativamente em `language_models.openai_compatible`.

## Configuração rápida (script)

Primeiro [exporte sua chave](../getting-started/set-your-key.md) para que `$CLAUDINIO_API_KEY` esteja definida. Isso escreve em `~/.config/zed/settings.json`, fazendo backup de qualquer arquivo existente:

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

## Configuração manual

1. Adicione o provedor em `~/.config/zed/settings.json`:

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

2. Abra o painel Agent do Zed e cole sua chave da API quando solicitado, ou defina-a como a chave da API para o provedor **Claudinio**.
3. Selecione **Claudinio** no seletor de modelos do painel Agent.

| Configuração | Valor |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Máximo de tokens | `256000` |