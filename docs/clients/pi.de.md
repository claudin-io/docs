# pi

[pi](https://github.com/parallel-web/pi) liest Provider aus
`~/.pi/agent/models.json` aus. Claudin.io ist als
`openai-completions`-Provider registriert.

## Schnelleinrichtung (Skript)

Exportieren Sie zuerst [Ihren Schlüssel](../getting-started/set-your-key.md), damit
`$CLAUDINIO_API_KEY` gesetzt ist. Dies schreibt `~/.pi/agent/models.json` und sichert eine
eventuell vorhandene Datei:

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

Führen Sie dann aus:

```bash
pi --provider claudinio --model claudinio
```

## Manuelle Einrichtung

Fügen Sie dies in `~/.pi/agent/models.json` ein:

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

## Umgebungsvariable-Alternative

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Einstellung | Wert |
| --- | --- |
| Basis-URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |
| API-Typ | `openai-completions` |