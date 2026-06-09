# Zed

[Zed](https://zed.dev) unterstützt OpenAI-kompatible Anbieter nativ unter `language_models.openai_compatible`.

## Schnelleinrichtung (Skript)

Exportieren Sie zuerst [Ihren Schlüssel](../getting-started/set-your-key.md), damit `$CLAUDINIO_API_KEY` gesetzt ist. Dies schreibt `~/.config/zed/settings.json` und erstellt eine Sicherungskopie einer vorhandenen Datei:

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

## Manuelle Einrichtung

1. Fügen Sie den Anbieter zu `~/.config/zed/settings.json` hinzu:

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

2. Öffnen Sie das Agent-Panel von Zed und fügen Sie Ihren API-Schlüssel ein, wenn Sie dazu aufgefordert werden, oder setzen Sie ihn als API-Schlüssel für den **Claudinio**-Anbieter.
3. Wählen Sie **Claudinio** im Modellauswahl des Agent-Panels aus.

| Einstellung | Wert |
| --- | --- |
| API-URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |
| Maximale Tokens | `256000` |