# Zed

[Zed](https://zed.dev) مقامی طور پر OpenAI کے ساتھ مطابقت رکھنے والے فراہم کنندگان کو
`language_models.openai_compatible` کے تحت سپورٹ کرتا ہے۔

## فوری سیٹ اپ (اسکرپٹ)

پہلے [اپنی کلید ایکسپورٹ کریں](../getting-started/set-your-key.md) تاکہ
`$CLAUDINIO_API_KEY` سیٹ ہو جائے۔ یہ `~/.config/zed/settings.json` لکھتا ہے، کسی بھی موجودہ فائل کا بیک اپ لے کر:

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

## دستی سیٹ اپ

1. فراہم کنندہ کو `~/.config/zed/settings.json` میں شامل کریں:

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

2. Zed کا ایجنٹ پینل کھولیں اور جب اشارہ کیا جائے تو اپنی API کلید پیسٹ کریں، یا اسے **Claudinio** فراہم کنندہ کے لیے API کلید کے طور پر سیٹ کریں۔
3. ایجنٹ پینل کے ماڈل چناؤ میں **Claudinio** منتخب کریں۔

| سیٹنگ | قدر |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| ماڈل | `claudinio` |
| زیادہ سے زیادہ ٹوکن | `256000` |