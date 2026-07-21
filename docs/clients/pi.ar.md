# pi

[pi](https://github.com/parallel-web/pi) يقرأ المزوّدين من
`~/.pi/agent/models.json`. Claudin.io مسجّل كمزوّد
`openai-completions`.

## الإعداد السريع (سكريبت)

أوّلاً [صدّر مفتاحك](../getting-started/set-your-key.md) ليتم
تعيين `$CLAUDINIO_API_KEY`. يقوم هذا بكتابة `~/.pi/agent/models.json` مع أخذ
نسخة احتياطية من أي ملف موجود:

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

ثم شغّل:

```bash
pi --provider claudinio --model claudinio
```

## الإعداد اليدوي

ضع هذا في `~/.pi/agent/models.json`:

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

## بديل متغيرات البيئة

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| الإعداد | القيمة |
| --- | --- |
| الرابط الأساسي (Base URL) | `https://api.claudin.io/v1` |
| النموذج (Model) | `claudinio` |
| نوع API | `openai-completions` |