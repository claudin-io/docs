# pi

[pi](https://github.com/parallel-web/pi) lê provedores de
`~/.pi/agent/models.json`. Claudin.io está registrado como um
provedor `openai-completions`.

## Configuração Rápida (script)

Primeiro [exporte sua chave](../getting-started/set-your-key.md) para que
`$CLAUDINIO_API_KEY` esteja definida. Isto escreve `~/.pi/agent/models.json`, fazendo backup de
qualquer arquivo existente:

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

Em seguida, execute:

```bash
pi --provider claudinio --model claudinio
```

## Configuração Manual

Coloque isto em `~/.pi/agent/models.json`:

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

## Alternativa de Variável de Ambiente

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Configuração | Valor |
| --- | --- |
| URL Base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Tipo de API | `openai-completions` |