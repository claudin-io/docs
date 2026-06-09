# Kilo Code

[Kilo Code](https://kilo.ai) utilizza un blocco provider compatibile con OpenAI. L'ID del modello è `claudinio/claudinio` (provider/modello).

## Configurazione rapida (script)

Prima [esporta la tua chiave](../getting-started/set-your-key.md) in modo che `$CLAUDINIO_API_KEY` sia impostata. Questo scrive `~/.config/kilo/kilo.jsonc`, facendo il backup di qualsiasi file esistente:

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

Poi esegui `kilo`.

## Configurazione manuale

Metti questo in `~/.config/kilo/kilo.jsonc`:

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

## Alternativa con variabili d'ambiente

Kilo legge anche le variabili d'ambiente standard di OpenAI:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Impostazione | Valore |
| --- | --- |
| URL di base | `https://api.claudin.io/v1` |
| Modello | `claudinio/claudinio` |
| Chiamate agli strumenti | abilitato |