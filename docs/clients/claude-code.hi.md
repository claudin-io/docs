# Claude Code

[Claude Code](https://claude.com/claude-code) क्लाउडिन.आईओ से इसके एंथ्रोपिक-संगत एंडपॉइंट के माध्यम से जुड़ता है। इसका बेस यूआरएल क्लाउडिन.आईओ पर पॉइंट करें और अपनी कुंजी को प्रमाणीकरण टोकन के रूप में उपयोग करें।

## त्वरित सेटअप (स्क्रिप्ट)

पहले [अपनी कुंजी निर्यात करें](../getting-started/set-your-key.md) ताकि `$CLAUDINIO_API_KEY` सेट हो जाए, फिर यह चलाएँ। यह `~/.claude/settings.json` लिखता है (पहले किसी भी मौजूदा फ़ाइल का बैकअप लेकर):

```bash
claude_settings_install() {
  local key="$1"
  local dir="$HOME/.claude"
  local file="$dir/settings.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "${key}",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

claude_settings_install "$CLAUDINIO_API_KEY"
unset claude_settings_install
```

फिर बस `claude` चलाएँ।

## मैन्युअल सेटअप

`~/.claude/settings.json` स्वयं संपादित करें:

```json
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
```

!!! note "क्यों `ANTHROPIC_API_KEY` खाली है"
    क्लॉड कोड `ANTHROPIC_API_KEY` को प्राथमिकता देता है यदि वह सेट है। इसे खाली छोड़ने पर यह क्लाउडिन.आईओ बेस यूआरएल के विरुद्ध `ANTHROPIC_AUTH_TOKEN` (आपकी क्लाउडिन.आईओ कुंजी) का उपयोग करने के लिए बाध्य होता है।

## उपयोग किए गए मान

| सेटिंग | मान |
| --- | --- |
| बेस यूआरएल | `https://api.claudin.io` |
| मॉडल | `claudinio` |
| उप-एजेंट मॉडल | `claudinio` |
| प्रमाणीकरण | `ANTHROPIC_AUTH_TOKEN` = आपकी कुंजी |

---

परेशानी? देखें [सामान्य त्रुटियाँ](../api-reference.md#errors) या [FAQ](../faq.md)।