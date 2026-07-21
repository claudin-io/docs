# Cursor

O [Cursor](https://cursor.com) permite que você adicione um modelo compatível com OpenAI através de suas configurações. O Claudin.io se conecta através da substituição da URL base da OpenAI.

## Configuração

1. Abra **Cursor → Configurações → Modelos** (ou **Configurações do Cursor → IA**).
2. Role até **Chave da API OpenAI** e expanda a opção **Substituir URL Base da OpenAI**.
3. Defina:

    | Campo | Valor |
    | --- | --- |
    | Chave da API OpenAI | `YOUR_API_KEY` |
    | URL Base | `https://api.claudin.io/v1` |

4. Em **Modelos**, adicione um modelo personalizado chamado **`claudinio`** e ative-o.
5. Desative os outros modelos padrão se quiser que o Cursor use o Claudin.io exclusivamente.

!!! note "Recursos próprios do Cursor"
    Os recursos agentivos do Cursor funcionam melhor com um modelo de chat compatível com OpenAI.
    `claudinio` suporta chamadas de ferramentas, então os fluxos do Composer/Agent funcionam. Alguns
    recursos proprietários do Cursor (autocompletar de Tab, etc.) são executados nos próprios modelos
    do Cursor e não passam pela sua substituição de provedor.

## Verificação

Abra um chat no Cursor, selecione **claudinio** e envie uma mensagem. Se você receber uma resposta, está pronto. Caso contrário, verifique novamente se a URL base termina em `/v1` e se a chave foi colada sem espaços extras.

| Configuração | Valor |
| --- | --- |
| URL Base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |