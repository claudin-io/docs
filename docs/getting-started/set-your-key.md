# Set your API key

Set your Claudin.io key **once** as an environment variable and every tool in
this guide can reuse it — no need to paste it into each client by hand.

Grab your `sk-...` key from the [dashboard](https://claudin.io/dashboard) (see
[Create your account](account.md)), then add it to your shell profile so it's
available in every new terminal.

## macOS / Linux

=== "zsh (default on macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Replace `sk-...` with your real key. Not sure which shell you're on? Run
`echo $SHELL`.

## Verify

```bash
echo $CLAUDINIO_API_KEY
```

You should see your key printed back. If it's empty, open a new terminal or
re-run the `source` command above.

## Why this helps

Every **Quick setup** script in the [Connect your tool](../clients/opencode.md)
section reads `$CLAUDINIO_API_KEY`, so once it's exported you can run any of them
as-is — there's no `YOUR_API_KEY` to replace. Tools that read environment
variables directly (Codex's `env_key`, any OpenAI-compatible CLI) pick it up
automatically too.

!!! warning "Treat your key like a password"
    Anyone with this key can spend your plan's budget. Don't commit your
    `~/.zshrc` / `~/.bashrc` to a public repo. If the key leaks, revoke it in the
    dashboard and export a fresh one.

---

Key exported? Now [make your first call](first-call.md) or jump straight to
[connecting your tool](../clients/opencode.md).
