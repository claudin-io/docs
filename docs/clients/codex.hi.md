# कोडेक्स

[कोडेक्स](https://github.com/openai/codex) एक कस्टम मॉडल प्रदाता के माध्यम से `~/.codex/config.toml` में जुड़ता है। Claudin.io `responses` वायर API को उजागर करता है जिसकी कोडेक्स को अपेक्षा होती है।

!!! warning "Codex CLI का उपयोग करें"
    ये सेटिंग्स **Codex CLI** पर लागू होती हैं। होस्ट किया गया Codex ऐप आपको कस्टम बेस URL की ओर इंगित करने की अनुमति नहीं दे सकता है।

## मैन्युअल सेटअप

इसे `~/.codex/config.toml` में जोड़ें:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

फिर अपनी कुंजी निर्यात करें (नाम ऊपर `env_key` से मेल खाना चाहिए)। सबसे आसान तरीका है [इसे अपने शेल प्रोफ़ाइल में एक बार सेट करना](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## त्वरित सेटअप (स्क्रिप्ट)

```bash
codex_config_install() {
  local key="$1"
  local dir="$HOME/.codex"
  local file="$dir/config.toml"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<TOMLEOF
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
TOMLEOF

  echo "[ok] Configured: $file"
  echo "[ok] Make sure CLAUDINIO_API_KEY is exported in your shell"
}

codex_config_install
unset codex_config_install
```

| सेटिंग | मान |
| --- | --- |
| बेस URL | `https://api.claudin.io/v1` |
| मॉडल | `claudinio` |
| वायर API | `responses` |
| कुंजी पर्यावरण चर | `CLAUDINIO_API_KEY` |