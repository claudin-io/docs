# pi

[pi](https://github.com/parallel-web/pi) `~/.pi/agent/models.json` থেকে প্রদানকারী পড়ে। Claudin.io একটি `openai-completions` প্রদানকারী হিসেবে নিবন্ধিত।

## দ্রুত সেটআপ (স্ক্রিপ্ট)

প্রথমে [আপনার কী এক্সপোর্ট করুন](../getting-started/set-your-key.md) যাতে `$CLAUDINIO_API_KEY` সেট হয়। এটি `~/.pi/agent/models.json` লেখে, বিদ্যমান যেকোনো ফাইল ব্যাকআপ করে:

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

তারপর চালান:

```bash
pi --provider claudinio --model claudinio
```

## ম্যানুয়াল সেটআপ

এটি `~/.pi/agent/models.json` এ রাখুন:

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

## এনভায়রনমেন্ট-ভেরিয়েবল বিকল্প

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| সেটিং | মান |
| --- | --- |
| বেস URL | `https://api.claudin.io/v1` |
| মডেল | `claudinio` |
| API টাইপ | `openai-completions` |