# OpenCode

[OpenCode](https://opencode.ai) se connecte à Claudin.io en tant que fournisseur compatible OpenAI. Le chemin le plus rapide est son flux d'authentification intégré.

## Configuration rapide

1. Exécutez la commande de connexion :

    ```bash
    opencode auth login
    ```

2. Sélectionnez **Claudinio** comme fournisseur.
3. Collez votre clé API lorsqu'on vous le demande — copiez-la depuis votre [tableau de bord](https://claudin.io/dashboard).

Ensuite, démarrez OpenCode et sélectionnez le modèle **claudinio**.

## Alternative par variables d'environnement

Si vous avez déjà [exporté votre clé](../getting-started/set-your-key.md), OpenCode récupère les variables OpenAI standard — pas besoin de coller quoi que ce soit :

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Paramètre | Valeur |
| --- | --- |
| URL de base | `https://api.claudin.io/v1` |
| Modèle | `claudinio` |
| Fournisseur | OpenAI-compatible |

---

Un problème ? Consultez les [erreurs courantes](../api-reference.md#errors) ou la [FAQ](../faq.md).