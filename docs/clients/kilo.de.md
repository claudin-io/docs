# Kilo Code

[Kilo Code](https://kilo.ai) verwendet einen OpenAI-kompatiblen Provider-Block. Die Modell-ID ist `claudinio/claudinio` (Provider/Modell).

## Schnelleinrichtung (Skript)

Exportieren Sie zuerst [Ihren Schlüssel](../getting-started/set-your-key.md), damit `$CLAUDINIO_API_KEY` gesetzt ist. Dies schreibt `~/.config/kilo/kilo.jsonc` und sichert eine vorhandene Datei:

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

Führen Sie dann `kilo` aus.

## Manuelle Einrichtung

Fügen Sie dies in `~/.config/kilo/kilo.jsonc` ein:

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

## Alternativ: Umgebungsvariablen

Kilo liest auch die Standard-OpenAI-Umgebungsvariablen:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Einstellung | Wert |
| --- | --- |
| Basis-URL | `https://api.claudin.io/v1` |
| Modell | `claudinio/claudinio` |
| Tool-Aufrufe | aktiviert |