# pi

[pi](https://github.com/parallel-web/pi), sağlayıcılarını `~/.pi/agent/models.json` dosyasından okur. Claudin.io, bir `openai-completions` sağlayıcısı olarak kayıtlıdır.

## Hızlı kurulum (script)

Öncelikle [anahtarınızı dışa aktarın](../getting-started/set-your-key.md) ki `$CLAUDINIO_API_KEY` ayarlanmış olsun. Bu komut, `~/.pi/agent/models.json` dosyasını oluşturur ve varsa mevcut dosyayı yedekler:

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

Ardından çalıştırın:

```bash
pi --provider claudinio --model claudinio
```

## Manuel kurulum

Bunu `~/.pi/agent/models.json` dosyasına koyun:

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

## Ortam değişkeni alternatifi

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Ayar | Değer |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| API türü | `openai-completions` |