# Zed

O [Zed](https://zed.dev) suporta provedores compatíveis com OpenAI nativamente sob `language_models.openai_compatible`.

## Configuração rápida (script)

Primeiro, [exporte a sua chave](../getting-started/set-your-key.md) para que `$CLAUDINIO_API_KEY` esteja definida. Isto escreve em `~/.config/zed/settings.json`, criando uma cópia de segurança do ficheiro existente, se houver:

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

1. Adicione o fornecedor em `~/.config/zed/settings.json`:

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

2. Abra o painel do Agent do Zed e cole a sua chave de API quando solicitado, ou defina-a como a chave de API para o fornecedor **Claudinio**.
3. Selecione **Claudinio** no seletor de modelos do painel do Agent.

| Configuração | Valor |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Tokens máximos | `256000` |