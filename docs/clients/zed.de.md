# Zed

[Zed](https://zed.dev) unterstützt nativ OpenAI-kompatible Anbieter unter
`language_models.openai_compatible`.

## Schnelleinrichtung (Skript)

Exportieren Sie zunächst [Ihren Schlüssel](../getting-started/set-your-key.md), damit `$CLAUDINIO_API_KEY` gesetzt ist. Dies schreibt `~/.config/zed/settings.json` und sichert vorhandene Dateien:

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

2. Öffnen Sie das Zed-Agent-Panel und fügen Sie Ihren API-Schlüssel ein, wenn Sie dazu aufgefordert werden, oder legen Sie ihn als API-Schlüssel für den Anbieter **Claudinio** fest.
3. Wählen Sie **Claudinio** im Modellauswahl des Agent-Panels aus.

| Einstellung | Wert |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |
| Maximale Token | `256000` |