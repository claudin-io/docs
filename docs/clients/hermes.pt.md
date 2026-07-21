# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) é um agente de IA
para terminal de código aberto desenvolvido pela Nous Research. Suporta qualquer
endpoint compatível com OpenAI, tornando-o ideal para o Claudin.io.

## Introdução rápida com o assistente

Saia de qualquer sessão ativa do Hermes (`Ctrl + C` ou `/quit`) e execute:

```bash
hermes model
```

Selecione **Custom endpoint** no menu e preencha:

| Campo | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Chave da API | a sua chave `sk-...` |
| Nome do modelo | `claudinio` |

O Hermes guarda a configuração automaticamente em `~/.hermes/config.yaml`.

Experimente:

```bash
hermes
```

## Configuração manual

Edite o ficheiro `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

Ou defina valores diretamente:

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

> **Dica:** Para tarefas complexas com chamadas de ferramentas, certifique-se de que o seu Hermes Agent
> está a usar um modelo com pelo menos 64K tokens de contexto (o Claudinio suporta isto).

## Resolução de problemas

| Problema | Solução |
| --- | --- |
| Erro de autenticação | Verifique novamente a sua chave de API com `hermes doctor` |
| Modelo não encontrado | Confirme que o nome do modelo é exatamente `claudinio` |
| Conexão recusada | Verifique se `https://api.claudin.io/v1` está acessível a partir da sua rede |