# pi

[pi](https://github.com/parallel-web/pi) lê fornecedores de
`~/.pi/agent/models.json`. Claudin.io está registado como um
fornecedor `openai-completions`.

## Configuração rápida (script)

Primeiro [exporte a sua chave](../getting-started/set-your-key.md) para que
`$CLAUDINIO_API_KEY` esteja definida. Isto escreve `~/.pi/agent/models.json`,
fazendo backup de qualquer ficheiro existente:

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

Depois execute:

```bash
pi --provider claudinio --model claudinio
```

## Configuração manual

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

## Alternativa com variáveis de ambiente

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Definição | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Tipo de API | `openai-completions` |