# Claude Code

[Claude Code](https://claude.com/claude-code) Claudin.io سے اپنے Anthropic-مطابق اختتامی نقطے کے ذریعے جڑتا ہے۔ اس کی بنیادی URL Claudin.io پر رکھیں اور اپنی کلید کو تصدیقی ٹوکن کے طور پر استعمال کریں۔

## فوری سیٹ اپ (اسکرپٹ)

پہلے [اپنی کلید برآمد کریں](../getting-started/set-your-key.md) تاکہ `$CLAUDINIO_API_KEY` سیٹ ہو، پھر یہ چلائیں۔ یہ `~/.claude/settings.json` لکھتا ہے (پہلے کسی موجودہ فائل کا بیک اپ لے کر):

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

پھر صرف `claude` چلائیں۔

## دستی سیٹ اپ

خود `~/.claude/settings.json` میں ترمیم کریں:

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

!!! note "کیوں `ANTHROPIC_API_KEY` خالی ہے"
    Claude Code اگر `ANTHROPIC_API_KEY` سیٹ ہو تو اسے ترجیح دیتا ہے۔ اسے خالی چھوڑنے سے یہ Claudin.io کے بنیادی URL کے خلاف `ANTHROPIC_AUTH_TOKEN` (آپ کی Claudinio کلید) استعمال کرنے پر مجبور ہوتا ہے۔

## استعمال کردہ اقدار

| ترتیب | قدر |
| --- | --- |
| بنیادی URL | `https://api.claudin.io` |
| ماڈل | `claudinio` |
| سب ایجنٹ ماڈل | `claudinio` |
| تصدیق | `ANTHROPIC_AUTH_TOKEN` = آپ کی کلید |

---

پریشانی؟ [عام غلطیاں](../api-reference.md#errors) یا [FAQ](../faq.md) دیکھیں۔