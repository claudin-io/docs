# Kilo Code

[Kilo Code](https://kilo.ai) يستخدم كتلة مزود متوافقة مع OpenAI. معرف النموذج هو `claudinio/claudinio` (مزود/نموذج).

## الإعداد السريع (سكريبت)

أولاً [قم بتصدير مفتاحك](../getting-started/set-your-key.md) حتى يتم تعيين `$CLAUDINIO_API_KEY`. يكتب هذا الملف `~/.config/kilo/kilo.jsonc`، مع عمل نسخة احتياطية لأي ملف موجود:

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

ثم قم بتشغيل `kilo`.

## الإعداد اليدوي

ضع هذا في `~/.config/kilo/kilo.jsonc`:

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

## بديل متغيرات البيئة

يقرأ Kilo أيضًا متغيرات البيئة القياسية لـ OpenAI:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| الإعداد | القيمة |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| النموذج | `claudinio/claudinio` |
| استدعاءات الأدوات | مفعل |