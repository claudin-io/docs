# pi

[pi](https://github.com/parallel-web/pi) legge i provider da
`~/.pi/agent/models.json`. Claudin.io è registrato come provider
`openai-completions`.

## Configurazione rapida (script)

Prima [esporta la tua chiave](../getting-started/set-your-key.md) in modo che
`$CLAUDINIO_API_KEY` sia impostata. Questo scrive `~/.pi/agent/models.json`, creando un backup
di qualsiasi file esistente:

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
  echo "[ok] Configurato: $file"
  echo "[ok] Esegui: pi --provider claudinio --model claudinio"
}

pi_models_install "$CLAUDINIO_API_KEY"
unset pi_models_install
```

Quindi esegui:

```bash
pi --provider claudinio --model claudinio
```

## Configurazione manuale

Inserisci questo in `~/.pi/agent/models.json`:

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

## Alternativa tramite variabili d'ambiente

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Impostazione | Valore |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Modello | `claudinio` |
| Tipo API | `openai-completions` |