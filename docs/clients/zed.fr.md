# Zed

[Zed](https://zed.dev) prend en charge nativement les fournisseurs compatibles OpenAI sous `language_models.openai_compatible`.

## Configuration rapide (script)

D'abord, [exportez votre clé](../getting-started/set-your-key.md) pour que `$CLAUDINIO_API_KEY` soit définie. Cela écrit dans `~/.config/zed/settings.json`, en sauvegardant tout fichier existant :

```bash
zed_settings_install() {
  local key="$1"
  local config_dir="$HOME/.config/zed"
  local file="$config_dir/settings.json"

  mkdir -p "$config_dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "language_models": {
    "openai_compatible": {
      "Claudinio": {
        "api_url": "https://api.claudin.io/v1",
        "available_models": [
          {
            "name": "claudinio",
            "display_name": "Claudinio",
            "max_tokens": 256000
          }
        ]
      }
    }
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

zed_settings_install "$CLAUDINIO_API_KEY"
unset zed_settings_install
```

## Configuration manuelle

1. Ajoutez le fournisseur dans `~/.config/zed/settings.json` :

    ```json
    {
      "language_models": {
        "openai_compatible": {
          "Claudinio": {
            "api_url": "https://api.claudin.io/v1",
            "available_models": [
              {
                "name": "claudinio",
                "display_name": "Claudinio",
                "max_tokens": 256000
              }
            ]
          }
        }
      }
    }
    ```

2. Ouvrez le panneau Agent de Zed et collez votre clé API lorsque vous y êtes invité, ou définissez-la comme clé API pour le fournisseur **Claudinio**.
3. Sélectionnez **Claudinio** dans le sélecteur de modèle du panneau agent.

| Paramètre | Valeur |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Modèle | `claudinio` |
| Max tokens | `256000` |