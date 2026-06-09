# Tout client compatible OpenAI

Claudin.io implémente la surface d'API OpenAI, donc **tous** les outils, SDK ou bibliothèques qui permettent de définir une URL de base personnalisée fonctionnent. Si votre éditeur n'est pas listé dans cette section, utilisez ces paramètres génériques.

## Les trois valeurs

| Paramètre | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io/v1` |
| Modèle | `claudinio` |
| Clé API | votre clé `sk-...` |

La plupart des outils appellent le champ URL de base par l'un des noms suivants : *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint*, ou *Custom provider URL*. Incluez toujours le suffixe `/v1`.

## Variables d'environnement

De nombreux CLI et SDK lisent les variables OpenAI standard — définissez-les et c'est fait. Si vous avez [exporté votre clé](../getting-started/set-your-key.md), réutilisez `$CLAUDINIO_API_KEY` :

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Points de terminaison pris en charge

Claudin.io achemine ces chemins de type OpenAI :

| Point de terminaison | Objectif |
| --- | --- |
| `POST /v1/chat/completions` | Complétions de chat (la principale) |
| `POST /v1/completions` | Complétions de texte héritées |
| `POST /v1/messages` | Format Messages d'Anthropic |
| `POST /v1/responses` | API Responses (utilisée par Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Liste des modèles disponibles |

## Authentification

Envoyez votre clé **soit** :

```http
Authorization: Bearer YOUR_API_KEY
```

ou

```http
x-api-key: YOUR_API_KEY
```

Les deux sont acceptés — choisissez celui que votre client émet.

---

Voir la [référence API](../api-reference.md) complète pour les détails des requêtes/réponses et la gestion des erreurs.