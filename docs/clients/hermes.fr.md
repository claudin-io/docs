[Hermes Agent](https://github.com/NousResearch/hermes-agent) est un agent de
terminal open-source créé par Nous Research. Il prend en charge tout endpoint
compatible OpenAI, ce qui en fait un choix parfait pour Claudin.io.

## Démarrage rapide avec l'assistant

Quittez toute session Hermes active (`Ctrl + C` ou `/quit`), puis exécutez :

```bash
hermes model
```

Sélectionnez **Custom endpoint** dans le menu et renseignez :

| Champ | Valeur |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | votre clé `sk-...` |
| Model name | `claudinio` |

Hermes enregistre la configuration automatiquement dans `~/.hermes/config.yaml`.

Essayez :

```bash
hermes
```

## Configuration manuelle

Modifiez `~/.hermes/config.yaml` :

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-votre-cle-ici"
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

> **Astuce :** Pour les tâches complexes avec appels d'outils, assurez-vous
> que votre Hermes Agent utilise un modèle avec au moins 64K tokens de
> contexte (Claudinio le supporte).

## Dépannage

| Problème | Solution |
| --- | --- |
| Erreur d'authentification | Vérifiez la clé avec `hermes doctor` |
| Modèle introuvable | Assurez-vous que le nom du modèle est exactement `claudinio` |
| Connexion refusée | Vérifiez que `https://api.claudin.io/v1` est accessible |

## Commandes utiles

| Commande | Description |
| --- | --- |
| `hermes config show` | Voir la configuration actuelle |
| `hermes config edit` | Modifier interactivement |
| `hermes doctor` | Diagnostiquer les problèmes |
| `hermes model` | Changer de fournisseur |
