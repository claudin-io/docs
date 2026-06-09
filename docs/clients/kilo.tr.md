# Kilo Code

[Kilo Code](https://kilo.ai), OpenAI uyumlu bir sağlayıcı bloğu kullanır. Model
kimliği `claudinio/claudinio` (sağlayıcı/model) şeklindedir.

## Hızlı kurulum (komut dosyası)

Önce [anahtarınızı dışa aktarın](../getting-started/set-your-key.md) böylece
`$CLAUDINIO_API_KEY` ayarlanmış olur. Bu, `~/.config/kilo/kilo.jsonc` dosyasını
yazar ve varsa mevcut dosyayı yedekler:

```bash
kilo_config_install() {
  local key="$1"
  local dir="$HOME/.config/kilo"
  local file="$dir/kilo.jsonc"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Yedek: $file.claudinio.bak"
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
  echo "[ok] Yapılandırıldı: $file"
}

kilo_config_install "$CLAUDINIO_API_KEY"
unset kilo_config_install
```

Ardından `kilo` komutunu çalıştırın.

## Manuel kurulum

`~/.config/kilo/kilo.jsonc` dosyasına aşağıdakini ekleyin:

```jsonc
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "API_ANAHTARINIZ"
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

## Ortam değişkeni alternatifi

Kilo ayrıca standart OpenAI ortam değişkenlerini de okur:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Ayar | Değer |
| --- | --- |
| Temel URL | `https://api.claudin.io/v1` |
| Model | `claudinio/claudinio` |
| Araç çağrıları | etkin |