# pi

[pi](https://github.com/parallel-web/pi) `~/.pi/agent/models.json` से प्रदाताओं को पढ़ता है। Claudin.io एक `openai-completions` प्रदाता के रूप में पंजीकृत है।

## त्वरित सेटअप (स्क्रिप्ट)

पहले [अपनी कुंजी निर्यात करें](../getting-started/set-your-key.md) ताकि `$CLAUDINIO_API_KEY` सेट हो जाए। यह `~/.pi/agent/models.json` लिखता है, किसी भी मौजूदा फ़ाइल का बैकअप लेता है:

```bash
pi_models_install() {
  local key="$1"
  local dir="$HOME/.pi/agent"
  local file="$dir/models.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<'JSONEOF'
{
  "providers": {
    "claudinio": {
      "baseUrl": "https://api.claudin.io/v1",
      "api": "openai-completions",
      "apiKey": "__CL_KEY__",
      "models": [
        { "id": "claudinio", "name": "Claudinio", "contextWindow": 256000 }
      ]
    }
  }
}
JSONEOF

  sed -i.bak "s/__CL_KEY__/${key}/g" "$file" && rm -f "$file.bak"
  echo "[ok] Configured: $file"
  echo "[ok] Run: pi --provider claudinio --model claudinio"
}

pi_models_install "$CLAUDINIO_API_KEY"
unset pi_models_install
```

फिर चलाएँ:

```bash
pi --provider claudinio --model claudinio
```

## मैन्युअल सेटअप

इसे `~/.pi/agent/models.json` में रखें:

```json
{
  "providers": {
    "claudinio": {
      "baseUrl": "https://api.claudin.io/v1",
      "api": "openai-completions",
      "apiKey": "YOUR_API_KEY",
      "models": [
        { "id": "claudinio", "name": "Claudinio", "contextWindow": 256000 }
      ]
    }
  }
}
```

## पर्यावरण-चर विकल्प

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| सेटिंग | मान |
| --- | --- |
| बेस URL | `https://api.claudin.io/v1` |
| मॉडल | `claudinio` |
| API प्रकार | `openai-completions` |