# N'importe quel client compatible OpenAI

Claudin.io implémente la surface d'API OpenAI, donc **tout** outil, SDK ou bibliothèque qui vous permet de définir une URL de base personnalisée fonctionne. Si votre éditeur n'est pas répertorié dans cette section, utilisez ces paramètres génériques.

## Les trois valeurs

| Réglage | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io/v1` |
| Modèle | `claudinio` |
| Clé API | votre clé `sk-...` |

La plupart des outils nomment le champ URL de base comme l'un des suivants : *URL de base*, *API de base*, *URL de base OpenAI*, *Point de terminaison* ou *URL de fournisseur personnalisé*. Incluez toujours le suffixe `/v1`.

## Variables d'environnement

De nombreux CLI et SDK lisent les variables OpenAI standard — définissez-les et vous avez terminé. Si vous avez [exporté votre clé](../getting-started/set-your-key.md), réutilisez `$CLAUDINIO_API_KEY` :

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Points de terminaison pris en charge

Claudin.io achemine ces chemins de style OpenAI :

| Point de terminaison | Objectif |
| --- | --- |
| `POST /v1/chat/completions` | Complétions de chat (la principale) |
| `POST /v1/completions` | Complétions de texte héritées |
| `POST /v1/messages` | Format Messages Anthropic |
| `POST /v1/responses` | API Responses (utilisée par Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Lister les modèles disponibles |

## Authentification

Envoyez votre clé **soit** :

```http
Authorization: Bearer YOUR_API_KEY
```

ou

```http
x-api-key: YOUR_API_KEY
```

Les deux sont acceptés — choisissez ce que votre client émet.

---

Consultez la [référence API](../api-reference.md) complète pour les détails des requêtes/réponses et la gestion des erreurs.