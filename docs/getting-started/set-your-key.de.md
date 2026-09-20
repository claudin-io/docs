# Lege deinen API-Schlüssel fest

Setze deinen Claudin.io-Schlüssel **einmalig** als Umgebungsvariable, und jedes Werkzeug in dieser Anleitung kann ihn wiederverwenden – du musst ihn nicht in jeden Client von Hand einfügen.

Hole dir deinen `sk-...`-Schlüssel vom [Dashboard](https://claudin.io/dashboard) (siehe [Konto erstellen](account.md)), und füge ihn dann deinem Shell-Profil hinzu, damit er in jedem neuen Terminal verfügbar ist.

## macOS / Linux

=== "zsh (Standard auf macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Ersetze `sk-...` durch deinen echten Schlüssel. Du weißt nicht, welche Shell du verwendest? Führe `echo $SHELL` aus.

## Überprüfen

```bash
echo $CLAUDINIO_API_KEY
```

Du solltest deinen Schlüssel zurückgesetzt sehen. Wenn er leer ist, öffne ein neues Terminal oder führe den obigen `source`-Befehl erneut aus.

## Warum das hilft

Jedes **Quick setup**-Skript im Abschnitt [Werkzeug verbinden](../clients/opencode.md) liest `$CLAUDINIO_API_KEY`, sobald es exportiert ist, kannst du jedes davon unverändert ausführen – es gibt kein `YOUR_API_KEY` zum Ersetzen. Werkzeuge, die Umgebungsvariablen direkt lesen (Codex' `env_key`, jede OpenAI-kompatible CLI), übernehmen ihn automatisch.

!!! warning "Behandle deinen Schlüssel wie ein Passwort"
    Jeder mit diesem Schlüssel kann deine Credits ausgeben. Committe deine
    `~/.zshrc` / `~/.bashrc` nicht in ein öffentliches Repo. Wenn der Schlüssel
    leakt, widerrufe ihn im Dashboard und exportiere einen neuen.

---

Schlüssel exportiert? Jetzt [ersten Aufruf tätigen](first-call.md) oder direkt zum [Werkzeug verbinden](../clients/opencode.md) springen.