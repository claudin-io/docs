# Kilo Code

[Kilo Code](https://kilo.ai) একটি OpenAI-সামঞ্জস্যপূর্ণ প্রদানকারী ব্লক ব্যবহার করে। মডেল আইডি হল `claudinio/claudinio` (প্রদানকারী/মডেল)।

## দ্রুত সেটআপ (স্ক্রিপ্ট)

প্রথমে [আপনার কী এক্সপোর্ট করুন](../getting-started/set-your-key.md) যাতে `$CLAUDINIO_API_KEY` সেট থাকে। এটি `~/.config/kilo/kilo.jsonc` লেখে, বিদ্যমান কোনো ফাইল ব্যাকআপ করে:

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

তারপর `kilo` চালান।

## ম্যানুয়াল সেটআপ

এটি `~/.config/kilo/kilo.jsonc`-এ রাখুন:

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

## এনভায়রনমেন্ট-ভেরিয়েবল বিকল্প

Kilo স্ট্যান্ডার্ড OpenAI এনভায়রনমেন্ট ভেরিয়েবলও পড়ে:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| সেটিং | মান |
| --- | --- |
| বেস URL | `https://api.claudin.io/v1` |
| মডেল | `claudinio/claudinio` |
| টুল কল | সক্রিয় |