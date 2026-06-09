# Claude Code

[Claude Code](https://claude.com/claude-code) अपने Anthropic-संगत एंडपॉइंट के माध्यम से Claudin.io से जुड़ता है। इसके base URL को Claudin.io पर इंगित करें और अपनी कुंजी को प्रमाणीकरण टोकन के रूप में उपयोग करें।

## त्वरित सेटअप (स्क्रिप्ट)

पहले [अपनी कुंजी निर्यात करें](../getting-started/set-your-key.md) ताकि `$CLAUDINIO_API_KEY` सेट हो, फिर इसे चलाएं। यह `~/.claude/settings.json` लिखता है (पहले किसी भी मौजूदा फ़ाइल का बैकअप लेता है):

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

फिर बस `claude` चलाएं।

## मैन्युअल सेटअप

`~/.claude/settings.json` को स्वयं संपादित करें:

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
    Claude Code `ANTHROPIC_API_KEY` को प्राथमिकता देता है यदि वह सेट है। इसे खाली छोड़ने पर यह Claudin.io base URL के विरुद्ध `ANTHROPIC_AUTH_TOKEN` (आपकी Claudin.io कुंजी) का उपयोग करने के लिए मजबूर होता है।

## उपयोग किए गए मान

| सेटिंग | मान |
| --- | --- |
| बेस URL | `https://api.claudin.io` |
| मॉडल | `claudinio` |
| सबएजेंट मॉडल | `claudinio` |
| प्रमाणीकरण | `ANTHROPIC_AUTH_TOKEN` = आपकी कुंजी |

---

समस्या? [सामान्य त्रुटिय