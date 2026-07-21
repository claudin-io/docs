# Zed

[Zed](https://zed.dev) mendukung penyedia yang kompatibel dengan OpenAI secara native di bawah `language_models.openai_compatible`.

## Pengaturan cepat (skrip)

Pertama [ekspor kunci Anda](../getting-started/set-your-key.md) sehingga `$CLAUDINIO_API_KEY` diatur. Ini akan menulis `~/.config/zed/settings.json`, dengan membuat cadangan file yang sudah ada (jika ada):

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

## Pengaturan manual

1. Tambahkan penyedia ke `~/.config/zed/settings.json`:

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

2. Buka panel Agen Zed dan tempel kunci API Anda saat diminta, atau atur sebagai kunci API untuk penyedia **Claudinio**.
3. Pilih **Claudinio** di pemilih model panel agen.

| Pengaturan | Nilai |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| Token maksimum | `256000` |