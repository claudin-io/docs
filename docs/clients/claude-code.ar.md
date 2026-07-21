# Claude Code

[Claude Code](https://claude.com/claude-code) يتصل بـ Claudin.io من خلال نقطة نهاية متوافقة مع Anthropic. وجّه عنوان URL الأساسي الخاص به إلى Claudin.io واستخدم مفتاحك كرمز المصادقة.

## الإعداد السريع (نص برمجي)

أولاً [صدّر مفتاحك](../getting-started/set-your-key.md) بحيث يتم تعيين `$CLAUDINIO_API_KEY`، ثم شغّل هذا. يكتب `~/.claude/settings.json` (مع عمل نسخة احتياطية لأي ملف موجود مسبقاً):

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

ثم شغّل فقط `claude`.

## الإعداد اليدوي

قم بتحرير `~/.claude/settings.json` بنفسك:

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

!!! note "لماذا `ANTHROPIC_API_KEY` فارغ"
    Claude Code يفضّل `ANTHROPIC_API_KEY` إذا تم تعيينه. تركه فارغاً يجبره على استخدام `ANTHROPIC_AUTH_TOKEN` (مفتاح Claudin.io الخاص بك) مقابل عنوان URL الأساسي لـ Claudin.io.

## القيم المستخدمة

| الإعداد | القيمة |
| --- | --- |
| عنوان URL الأساسي | `https://api.claudin.io` |
| النموذج | `claudinio` |
| نموذج الوكيل الفرعي | `claudinio` |
| المصادقة | `ANTHROPIC_AUTH_TOKEN` = مفتاحك |

---

هل تواجه مشكلة؟ اطلع على [الأخطاء الشائعة](../api-reference.md#errors) أو [FAQ](../faq.md).