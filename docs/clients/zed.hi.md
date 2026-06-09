# Zed

[Zed](https://zed.dev) मूल रूप से `language_models.openai_compatible` के तहत OpenAI-संगत प्रदाताओं का समर्थन करता है।

## त्वरित सेटअप (स्क्रिप्ट)

पहले [अपनी कुंजी निर्यात करें](../getting-started/set-your-key.md) ताकि `$CLAUDINIO_API_KEY` सेट हो जाए। यह किसी भी मौजूदा फ़ाइल का बैकअप लेते हुए `~/.config/zed/settings.json` लिखता है:

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

## मैन्युअल सेटअप

1. प्रदाता को `~/.config/zed/settings.json` में जोड़ें:

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

2. Zed का एजेंट पैनल खोलें और संकेत मिलने पर अपनी API कुंजी पेस्ट करें, या इसे **Claudinio** प्रदाता के लिए API कुंजी के रूप में सेट करें।
3. एजेंट पैनल के मॉडल पिकर में **Claudinio** चुनें।

| सेटिंग | मान |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| मॉडल | `claudinio` |
| अधिकतम टोकन | `256000` |