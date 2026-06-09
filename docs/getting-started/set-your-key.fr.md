# Définir votre clé API

Définissez votre clé Claudin.io **une fois** en tant que variable d'environnement et chaque outil de ce guide peut la réutiliser — plus besoin de la coller manuellement dans chaque client.

Récupérez votre clé `sk-...` depuis le [tableau de bord](https://claudin.io/dashboard) (consultez [Créer votre compte](account.md)), puis ajoutez-la à votre profil shell pour qu'elle soit disponible dans chaque nouveau terminal.

## macOS / Linux

=== "zsh (par défaut sur macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Remplacez `sk-...` par votre vraie clé. Vous ne savez pas quel shell vous utilisez ? Exécutez `echo $SHELL`.

## Vérification

```bash
echo $CLAUDINIO_API_KEY
```

Vous devriez voir votre clé s'afficher. Si elle est vide, ouvrez un nouveau terminal ou ré-exécutez la commande `source` ci-dessus.

## Pourquoi cela aide

Chaque script **Quick setup** de la section [Connecter votre outil](../clients/opencode.md) lit `$CLAUDINIO_API_KEY`, donc une fois qu'elle est exportée, vous pouvez exécuter n'importe lequel d'entre eux tel quel — il n'y a pas de `YOUR_API_KEY` à remplacer. Les outils qui lisent directement les variables d'environnement (le `env_key` de Codex, toute CLI compatible OpenAI) la récupèrent aussi automatiquement.

!!! warning "Traitez votre clé comme un mot de passe"
    Quiconque possède cette clé peut dépenser le budget de votre plan. Ne commitez pas votre `~/.zshrc` / `~/.bashrc` dans un dépôt public. Si la clé fuit, révoquez-la dans le tableau de bord et exportez-en une nouvelle.

---

Clé exportée ? Passez maintenant à [votre premier appel](first-call.md) ou allez directement à [la connexion de votre outil](../clients/opencode.md).