# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) est un agent IA en
terminal open-source de Nous Research. Il prend en charge tout endpoint compatible
OpenAI, ce qui en fait un choix parfait pour Claudin.io.

## Démarrage rapide avec l'assistant

Quittez toute session Hermes active (`Ctrl + C` ou `/quit`), puis exécutez :

```bash
hermes model
```

Sélectionnez **Custom endpoint** dans le menu et remplissez :

| Champ | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io/v1` |
| Clé API | votre clé `sk-...` |
| Nom du modèle | `claudinio` |

Hermes enregistre la configuration automatiquement dans `~/.hermes/config.yaml`.

Essayez-le :

```bash
hermes
```

## Configuration manuelle

Modifiez `~/.hermes/config.yaml` :

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

Ou définissez les valeurs directement :

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Vérifiez :

```bash
hermes config check
hermes config show
```

> **Astuce :** Pour les tâches complexes avec appel d'outils, assurez-vous que
> votre Agent Hermes utilise un modèle avec un contexte d'au moins 64K tokens
> (Claudinio le prend en charge).

## Dépannage

| Problème | Solution |
| --- | --- |
| Erreur d'authentification | Vérifiez votre clé API avec `hermes doctor` |
| Modèle introuvable | Assurez-vous que le nom du modèle est exactement `claudinio` |
| Connexion refusée | Vérifiez que `https://api.claudin.io/v1` est accessible depuis votre réseau |