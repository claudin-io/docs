# Zed

[Zed](https://zed.dev) supporta provider compatibili con OpenAI nativamente sotto `language_models.openai_compatible`.

## Configurazione rapida (script)

Prima [esporta la tua chiave](../getting-started/set-your-key.md) in modo che `$CLAUDINIO_API_KEY` sia impostata. Questo scrive `~/.config/zed/settings.json`, creando un backup di eventuali file esistenti:

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

## Configurazione manuale

1. Aggiungi il provider a `~/.config/zed/settings.json`:

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

2. Apri il pannello Agent di Zed e incolla la tua chiave API quando richiesto, oppure impostala come chiave API per il provider **Claudinio**.
3. Seleziona **Claudinio** nel selettore del modello del pannello Agent.

| Impostazione | Valore |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Modello | `claudinio` |
| Token massimi | `256000` |