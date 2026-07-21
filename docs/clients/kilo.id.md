# Kilo Code

[Kilo Code](https://kilo.ai) menggunakan blok penyedia yang kompatibel dengan OpenAI. ID modelnya adalah `claudinio/claudinio` (penyedia/model).

## Pengaturan cepat (skrip)

Pertama [ekspor kunci Anda](../getting-started/set-your-key.md) sehingga `$CLAUDINIO_API_KEY` diatur. Ini menulis `~/.config/kilo/kilo.jsonc`, membuat cadangan file yang ada:

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

Kemudian jalankan `kilo`.

## Pengaturan manual

Taruh ini di `~/.config/kilo/kilo.jsonc`:

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

## Alternatif variabel lingkungan

Kilo juga membaca variabel lingkungan standar OpenAI:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Pengaturan | Nilai |
| --- | --- |
| URL Dasar | `https://api.claudin.io/v1` |
| Model | `claudinio/claudinio` |
| Panggilan alat | diaktifkan |