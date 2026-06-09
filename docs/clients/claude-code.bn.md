# Claude Code

[Claude Code](https://claude.com/claude-code) Claudin.io-এর সাথে তার Anthropic-সামঞ্জস্যপূর্ণ এন্ডপয়েন্টের মাধ্যমে সংযুক্ত হয়। এর বেস URL Claudin.io-তে নির্দেশ করুন এবং অথ টোকেন হিসেবে আপনার কী ব্যবহার করুন।

## দ্রুত সেটআপ (স্ক্রিপ্ট)

প্রথমে [আপনার কী এক্সপোর্ট করুন](../getting-started/set-your-key.md) যাতে `$CLAUDINIO_API_KEY` সেট থাকে, তারপর এটি চালান। এটি `~/.claude/settings.json` লিখে (প্রথমে বিদ্যমান যেকোনো ফাইল ব্যাকআপ করে):

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

তারপর শুধু `claude` চালান।

## ম্যানুয়াল সেটআপ

`~/.claude/settings.json` নিজে সম্পাদনা করুন:

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

!!! note "কেন `ANTHROPIC_API_KEY` খালি"
    Claude Code `ANTHROPIC_API_KEY` পছন্দ করে যদি এটি সেট থাকে। এটি খালি রাখলে এটি Claudin.io বেস URL-এর বিপরীতে `ANTHROPIC_AUTH_TOKEN` (আপনার Claudin.io কী) ব্যবহার করতে বাধ্য করে।

## ব্যবহৃত মান

| সেটিং | মান |
| --- | --- |
| বেস URL | `https://api.claudin.io` |
| মডেল | `claudinio` |
| সাবএজেন্ট মডেল | `claudinio` |
| অথ | `ANTHROPIC_AUTH_TOKEN` = আপনার কী |

---

সমস্যা? [সাধারণ ত্রুটি](../api-reference.md#errors) বা [FAQ](../faq.md) দেখুন।