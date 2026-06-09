# Codex

[Codex](https://github.com/openai/codex) se connecte via un fournisseur de modèle personnalisé dans
`~/.codex/config.toml`. Claudin.io expose l'API filaire `responses` que Codex
attend.

!!! warning "Utilisez la CLI Codex"
    Ces paramètres s'appliquent à la **CLI Codex**. L'application Codex hébergée peut ne pas vous
    permettre de pointer vers une URL de base personnalisée.

## Configuration manuelle

Ajoutez ceci à `~/.codex/config.toml` :

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Exportez ensuite votre clé (le nom doit correspondre à `env_key` ci-dessus). La façon la plus simple est
de [la définir une fois dans votre profil shell](../getting-started/set-your-key.md) :

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Configuration rapide (script)

```bash
codex_config_install() {
  local key="$1"
  local dir="$HOME/.codex"
  local file="$dir/config.toml"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<TOMLEOF
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
TOMLEOF

  echo "[ok] Configured: $file"
  echo "[ok] Make sure CLAUDINIO_API_KEY is exported in your shell"
}

codex_config_install
unset codex_config_install
```

| Réglage | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io/v1` |
| Modèle | `claudinio` |
| API filaire | `responses` |
| Variable d'environnement de la clé | `CLAUDINIO_API_KEY` |