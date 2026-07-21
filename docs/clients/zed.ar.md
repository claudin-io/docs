# Zed

[Zed](https://zed.dev) يدعم بشكل أصلي مزودات متوافقة مع OpenAI تحت
`language_models.openai_compatible`.

## الإعداد السريع (نص برمجي)

أولاً، [قم بتصدير مفتاحك](../getting-started/set-your-key.md) حتى يتم تعيين
`$CLAUDINIO_API_KEY`. هذا يكتب `~/.config/zed/settings.json`، ويأخذ نسخة احتياطية من أي ملف موجود مسبقاً:

```bash
zed_settings_install() {
  local key="$1"
  local config_dir="$HOME/.config/zed"
  local file="$config_dir/settings.json"

  mkdir -p "$config_dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "language_models": {
    "openai_compatible": {
      "Claudinio": {
        "api_url": "https://api.claudin.io/v1",
        "available_models": [
          {
            "name": "claudinio",
            "display_name": "Claudinio",
            "max_tokens": 256000
          }
        ]
      }
    }
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

zed_settings_install "$CLAUDINIO_API_KEY"
unset zed_settings_install
```

## الإعداد اليدوي

1. أضف المزود إلى `~/.config/zed/settings.json`:

    ```json
    {
      "language_models": {
        "openai_compatible": {
          "Claudinio": {
            "api_url": "https://api.claudin.io/v1",
            "available_models": [
              {
                "name": "claudinio",
                "display_name": "Claudinio",
                "max_tokens": 256000
              }
            ]
          }
        }
      }
    }
    ```

2. افتح لوحة الوكيل في Zed والصق مفتاح API الخاص بك عندما يُطلب منك، أو قم بتعيينه كمفتاح API لمزود **Claudinio**.
3. اختر **Claudinio** في منتقي النماذج في لوحة الوكيل.

| الإعداد | القيمة |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| النموذج | `claudinio` |
| الحد الأقصى للرموز | `256000` |