[Hermes Agent](https://github.com/NousResearch/hermes-agent) é um agente de
terminal open-source da Nous Research. Suporta qualquer endpoint compatível com
OpenAI, sendo perfeito para usar com o Claudin.io.

## Método mais fácil: wizard interativo

Saia de qualquer sessão ativa do Hermes (`Ctrl + C` ou `/quit`) e execute:

```bash
hermes model
```

No menu, selecione **Custom endpoint** e informe:

| Campo | Valor |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | a sua chave `sk-...` |
| Model name | `claudinio` |

O Hermes guarda a configuração automaticamente em `~/.hermes/config.yaml`.

Teste:

```bash
hermes
```

## Configuração manual

Edite `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-a-sua-chave"
  default: "claudinio"
```

Ou configure diretamente:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Verifique:

```bash
hermes config check
hermes config show
```

> **Dica:** Para tarefas complexas com tool calling, certifique-se de usar um
> modelo com pelo menos 64K tokens de contexto (o Claudinio suporta).

## Comandos úteis

| Comando | Descrição |
| --- | --- |
| `hermes config show` | Ver configuração atual |
| `hermes config edit` | Editar interativamente |
| `hermes doctor` | Diagnosticar problemas |
| `hermes model` | Alternar provedores |

## Problemas comuns

| Problema | Solução |
| --- | --- |
| Erro de autenticação | Verifique a chave com `hermes doctor` |
| Modelo não encontrado | Confirme que o nome é exatamente `claudinio` |
| Conexão recusada | Verifique se `https://api.claudin.io/v1` está acessível |
