# OpenCode

[OpenCode](https://opencode.ai) conecta-se ao Claudin.io como um provedor compatível com OpenAI. O caminho mais rápido é seu fluxo de autenticação integrado.

## Configuração rápida

1. Execute o comando de login:

    ```bash
    opencode auth login
    ```

2. Selecione **Claudinio** como provedor.
3. Cole sua chave de API quando solicitado — copie-a do seu [painel](https://claudin.io/dashboard).

Em seguida, inicie o OpenCode e selecione o modelo **claudinio**.

## Alternativa com variáveis de ambiente

Se você já [exportou sua chave](../getting-started/set-your-key.md), o OpenCode capta as variáveis padrão do OpenAI — não é necessário colar nada:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Configuração | Valor |
| --- | --- |
| URL Base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Provedor | Compatível com OpenAI |

---

Problemas? Consulte [erros comuns](../api-reference.md#errors) ou o [FAQ](../faq.md).