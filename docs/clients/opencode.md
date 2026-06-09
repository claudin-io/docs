# OpenCode

[OpenCode](https://opencode.ai) connects to Claudin.io as an OpenAI-compatible
provider. The quickest path is its built-in auth flow.

## Quick setup

1. Run the login command:

    ```bash
    opencode auth login
    ```

2. Select **Claudinio** as the provider.
3. Paste your API key when prompted — copy it from your
   [dashboard](https://claudin.io/dashboard).

Then start OpenCode and pick the **claudinio** model.

## Environment-variable alternative

If you've already [exported your key](../getting-started/set-your-key.md),
OpenCode picks up the standard OpenAI variables — no need to paste anything:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Setting | Value |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| Provider | OpenAI-compatible |

---

Trouble? See [common errors](../api-reference.md#errors) or the [FAQ](../faq.md).
