# Agente Hermes

[Agente Hermes](https://github.com/NousResearch/hermes-agent) é um agente de IA
de terminal open-source da Nous Research. Ele suporta qualquer endpoint
compatível com OpenAI, sendo uma escolha perfeita para o Claudin.io.

## Início rápido com o assistente

Saia de qualquer sessão ativa do Hermes (`Ctrl + C` ou `/quit`), então execute:

```bash
hermes model
```

Selecione **Custom endpoint** no menu e preencha:

| Campo | Valor |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | sua chave `sk-...` |
| Nome do modelo | `claudinio` |

O Hermes salva a configuração automaticamente em `~/.hermes/config.yaml`.

Teste:

```bash
hermes
```

## Configuração manual

Edite o arquivo `~/.hermes/config.yaml`:

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

> **Dica:** Para tarefas complexas com chamadas de ferramentas, certifique-se
> de que seu Agente Hermes está usando um modelo com pelo menos 64K de
> contexto de tokens (o Claudinio suporta isso).

## Solução de problemas

| Problema | Solução |
| --- | --- |
| Erro de autenticação | Verifique sua chave de API com `hermes doctor` |
| Modelo não encontrado | Certifique-se de que o nome do modelo é exatamente `claudinio` |
| Conexão recusada | Verifique se `https://api.claudin.io/v1` está acessível a partir da sua rede |