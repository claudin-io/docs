# Cursor

[Cursor](https://cursor.com) vous permet d'ajouter un modèle compatible OpenAI via ses paramètres. Claudin.io se connecte via la substitution de l'URL de base OpenAI.

## Configuration

1. Ouvrez **Cursor → Paramètres → Modèles** (ou **Paramètres Cursor → IA**).
2. Faites défiler jusqu'à **Clé API OpenAI** et développez l'option **Substituer l'URL de base OpenAI**.
3. Définissez :

    | Champ | Valeur |
    | --- | --- |
    | Clé API OpenAI | `YOUR_API_KEY` |
    | URL de base | `https://api.claudin.io/v1` |

4. Sous **Modèles**, ajoutez un modèle personnalisé nommé **`claudinio`** et activez-le.
5. Désactivez les autres modèles par défaut si vous souhaitez que Cursor utilise exclusivement Claudin.io.

!!! note "Fonctionnalités propres à Cursor"
    Les fonctionnalités agentiques de Cursor fonctionnent mieux avec un modèle de discussion compatible OpenAI. `claudinio` prend en charge les appels d'outils, donc les flux Composer/Agent fonctionnent. Certaines fonctionnalités propriétaires de Cursor (Tab autocomplete, etc.) s'exécutent sur les propres modèles de Cursor et ne sont pas routées via votre substitution de fournisseur.

## Vérification

Ouvrez un chat dans Cursor, sélectionnez **claudinio**, et envoyez un message. Si vous obtenez une réponse, tout est configuré. Sinon, vérifiez que l'URL de base se termine par `/v1` et que la clé est collée sans espaces supplémentaires.

| Paramètre | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io/v1` |
| Modèle | `claudinio` |