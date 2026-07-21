# Zed

[Zed](https://zed.dev), `language_models.openai_compatible` altında OpenAI uyumlu sağlayıcıları yerel olarak destekler.

## Hızlı kurulum (betik)

Önce [anahtarınızı dışa aktarın](../getting-started/set-your-key.md) böylece `$CLAUDINIO_API_KEY` ayarlanır. Bu, `~/.config/zed/settings.json` dosyasını yazar ve var olan dosyayı yedekler:

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

## Manuel kurulum

1. Sağlayıcıyı `~/.config/zed/settings.json` dosyasına ekleyin:

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

2. Zed'in Ajan panelini açın ve istendiğinde API anahtarınızı yapıştırın veya **Claudinio** sağlayıcısı için API anahtarı olarak ayarlayın.
3. Ajan panelindeki model seçiciden **Claudinio**'yu seçin.

| Ayar | Değer |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| Maks. token | `256000` |