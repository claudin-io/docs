# pi

[pi](https://github.com/parallel-web/pi) lit les fournisseurs depuis
`~/.pi/agent/models.json`. Claudin.io est enregistré en tant que fournisseur
`openai-completions`.

## Configuration rapide (script)

Commencez par [exporter votre clé](../getting-started/set-your-key.md) pour que
`$CLAUDINIO_API_KEY` soit définie. Cela écrit `~/.pi/agent/models.json`, en
sauvegardant tout fichier existant :

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

Exécutez ensuite :

```bash
pi --provider claudinio --model claudinio
```

## Configuration manuelle

Placez ceci dans `~/.pi/agent/models.json` :

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

## Alternative avec variable d'environnement

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Paramètre | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io/v1` |
| Modèle | `claudinio` |
| Type d'API | `openai-completions` |