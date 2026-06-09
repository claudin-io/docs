# Cursor

[Cursor](https://cursor.com) vous permet d'ajouter un modèle compatible OpenAI via ses paramètres. Claudin.io se branche via la redirection de l'URL de base OpenAI.

## Configuration

1. Ouvrez **Cursor → Paramètres → Modèles** (ou **Paramètres de Cursor → IA**).
2. Faites défiler jusqu'à **Clé API OpenAI** et développez l'option **Redirection de l'URL de base OpenAI**.
3. Configurez :

    | Champ | Valeur |
    | --- | --- |
    | Clé API OpenAI | `YOUR_API_KEY` |
    | URL de base | `https://api.claudin.io/v1` |

4. Sous **Modèles**, ajoutez un modèle personnalisé nommé **`claudinio`** et activez-le.
5. Désactivez les autres modèles par défaut si vous souhaitez que Cursor utilise exclusivement Claudin.io.

!!! note "Fonctionnalités propres à Cursor"
    Les fonctionnalités agentiques de Cursor fonctionnent mieux avec un modèle de chat compatible OpenAI. `claudinio` prend en charge les appels d'outils, donc les flux Composer/Agent fonctionnent. Certaines fonctionnalités propriétaires de Cursor (autocomplétion Tab, etc.) s'exécutent sur les propres modèles de Cursor et ne sont pas routées via votre redirection de fournisseur.

## Vérification

Ouvrez une discussion dans Cursor, sélectionnez **claudinio**, et envoyez un message. Si vous obtenez une réponse, tout est bon. Sinon, vérifiez que l'URL de base se termine par `/v1` et que la clé est collée sans espaces supplémentaires.

| Paramètre | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io/v1` |
| Modèle | `claudinio` |