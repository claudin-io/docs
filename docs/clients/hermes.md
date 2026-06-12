# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) is an open-source
terminal AI agent by Nous Research. It supports any OpenAI-compatible endpoint,
making it a perfect fit for Claudin.io.

## Quick start with the wizard

Exit any active Hermes session (`Ctrl + C` or `/quit`), then run:

```bash
hermes model
```

Select **Custom endpoint** from the menu and fill in:

| Field | Value |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | your `sk-...` key |
| Model name | `claudinio` |

Hermes saves the configuration automatically to `~/.hermes/config.yaml`.

Try it:

```bash
hermes
```

## Manual configuration

Edit `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

Or set values directly:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Verify:

```bash
hermes config check
hermes config show
```

> **Tip:** For complex tasks with tool calling, make sure your Hermes Agent is
> using a model with at least 64K token context (Claudinio supports this).

## Troubleshooting

| Issue | Fix |
| --- | --- |
| Authentication error | Double-check your API key with `hermes doctor` |
| Model not found | Make sure the model name is exactly `claudinio` |
| Connection refused | Verify `https://api.claudin.io/v1` is reachable from your network |
