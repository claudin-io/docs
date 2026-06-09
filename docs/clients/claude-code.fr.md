# Claude Code

[Claude Code](https://claude.com/claude-code) se connecte à Claudin.io via son endpoint compatible avec Anthropic. Pointez son URL de base vers Claudin.io et utilisez votre clé comme jeton d'authentification.

## Configuration rapide (script)

Commencez par [exporter votre clé](../getting-started/set-your-key.md) pour que `$CLAUDINIO_API_KEY` soit définie, puis exécutez ceci. Il écrit `~/.claude/settings.json` (en sauvegardant d'abord tout fichier existant) :

```bash
claude_settings_install() {
  local key="$1"
  local dir="$HOME/.claude"
  local file="$dir/settings.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "${key}",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

claude_settings_install "$CLAUDINIO_API_KEY"
unset claude_settings_install
```

Ensuite, exécutez simplement `claude`.

## Configuration manuelle

Modifiez `~/.claude/settings.json` vous-même :

```json
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
```

!!! note "Pourquoi `ANTHROPIC_API_KEY` est vide"
    Claude Code préfère `ANTHROPIC_API_KEY` si elle est définie. La laisser vide le force à utiliser `ANTHROPIC_AUTH_TOKEN` (votre clé Claudin.io) avec l'URL de base de Claudin.io.

## Valeurs utilisées

| Paramètre | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io` |
| Modèle | `claudinio` |
| Modèle du sous-agent | `claudinio` |
| Authentification | `ANTHROPIC_AUTH_TOKEN` = votre clé |

---

Un problème ? Consultez les [erreurs courantes](../api-reference.md#errors) ou la [FAQ](../faq.md).