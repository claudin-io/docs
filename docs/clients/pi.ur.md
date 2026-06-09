# pi

[pi](https://github.com/parallel-web/pi) `~/.pi/agent/models.json` سے فراہم کنندگان پڑھتا ہے۔ Claudin.io کو ایک `openai-completions` فراہم کنندہ کے طور پر رجسٹر کیا گیا ہے۔

## فوری سیٹ اپ (اسکرپٹ)

پہلے [اپنی کلید برآمد کریں](../getting-started/set-your-key.md) تاکہ `$CLAUDINIO_API_KEY` سیٹ ہو جائے۔ یہ `~/.pi/agent/models.json` لکھتا ہے اور کسی بھی موجودہ فائل کا بیک اپ لیتا ہے:

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

پھر چلائیں:

```bash
pi --provider claudinio --model claudinio
```

## دستی سیٹ اپ

اسے `~/.pi/agent/models.json` میں رکھیں:

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

## ماحولی متغیر کا متبادل

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| ترتیب | قدر |
| --- | --- |
| بنیادی URL | `https://api.claudin.io/v1` |
| ماڈل | `claudinio` |
| API کی قسم | `openai-completions` |