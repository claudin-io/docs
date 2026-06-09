# Zed

[Zed](https://zed.dev) OpenAI-সামঞ্জস্যপূর্ণ প্রদানকারীকে নেটিভভাবে সমর্থন করে `language_models.openai_compatible` এর অধীনে।

## দ্রুত সেটআপ (স্ক্রিপ্ট)

প্রথমে [আপনার কী এক্সপোর্ট করুন](../getting-started/set-your-key.md) যাতে `$CLAUDINIO_API_KEY` সেট হয়। এটি `~/.config/zed/settings.json` লেখে, কোনো বিদ্যমান ফাইল ব্যাকআপ করে:

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

## ম্যানুয়াল সেটআপ

1. প্রদানকারী যোগ করুন `~/.config/zed/settings.json` এ:

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

2. Zed-এর Agent প্যানেল খুলুন এবং অনুরোধ করা হলে আপনার API কী পেস্ট করুন, অথবা **Claudinio** প্রদানকারীর জন্য API কী হিসাবে সেট করুন।
3. Agent প্যানেলের মডেল পিকার থেকে **Claudinio** নির্বাচন করুন।

| সেটিং | মান |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| মডেল | `claudinio` |
| সর্বোচ্চ টোকেন | `256000` |