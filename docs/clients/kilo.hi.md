# किलो कोड

[किलो कोड](https://kilo.ai) एक OpenAI-संगत प्रदाता ब्लॉक का उपयोग करता है। मॉडल आईडी `claudinio/claudinio` (प्रदाता/मॉडल) है।

## त्वरित सेटअप (स्क्रिप्ट)

पहले [अपनी कुंजी निर्यात करें](../getting-started/set-your-key.md) ताकि `$CLAUDINIO_API_KEY` सेट हो जाए। यह `~/.config/kilo/kilo.jsonc` लिखता है, किसी भी मौजूदा फ़ाइल का बैकअप लेता है:

```bash
kilo_config_install() {
  local key="$1"
  local dir="$HOME/.config/kilo"
  local file="$dir/kilo.jsonc"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<'JSONCEOF'
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "__CL_KEY__"
      },
      "models": {
        "claudinio": {
          "name": "Claudinio",
          "tool_call": true,
          "limit": { "context": 128000, "output": 16384 }
        }
      }
    }
  }
}
JSONCEOF

  sed -i.bak "s/__CL_KEY__/${key}/g" "$file" && rm -f "$file.bak"
  echo "[ok] Configured: $file"
}

kilo_config_install "$CLAUDINIO_API_KEY"
unset kilo_config_install
```

फिर `kilo` चलाएँ।

## मैन्युअल सेटअप

इसे `~/.config/kilo/kilo.jsonc` में डालें:

```jsonc
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "YOUR_API_KEY"
      },
      "models": {
        "claudinio": {
          "name": "Claudinio",
          "tool_call": true,
          "limit": { "context": 128000, "output": 16384 }
        }
      }
    }
  }
}
```

## पर्यावरण-चर विकल्प

किलो मानक OpenAI पर्यावरण चर भी पढ़ता है:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| सेटिंग | मान |
| --- | --- |
| आधार URL | `https://api.claudin.io/v1` |
| मॉडल | `claudinio/claudinio` |
| टूल कॉल्स | सक्षम |