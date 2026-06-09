# OpenCode

O [OpenCode](https://opencode.ai) conecta-se ao Claudin.io como um fornecedor compatível com OpenAI. O caminho mais rápido é o seu fluxo de autenticação integrado.

## Configuração rápida

1. Execute o comando de início de sessão:

    ```bash
    opencode auth login
    ```

2. Selecione **Claudinio** como o fornecedor.
3. Cole a sua chave API quando solicitado — copie-a do seu [painel de controlo](https://claudin.io/dashboard).

Depois, inicie o OpenCode e escolha o modelo **claudinio**.

## Alternativa de variável de ambiente

Se já [exportou a sua chave](../getting-started/set-your-key.md), o OpenCode deteta as variáveis padrão da OpenAI — não é necessário colar nada:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Definição | Valor |
| --- | --- |
| URL Base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Fornecedor | Compatível com OpenAI |

---

Problemas? Consulte [erros comuns](../api-reference.md#errors) ou as [FAQ](../faq.md).