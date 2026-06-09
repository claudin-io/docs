# Cursor

[Cursor](https://cursor.com) permite adicionar um modelo compatível com OpenAI através das suas definições. Claudin.io liga-se através da substituição da URL base da OpenAI.

## Configuração

1. Abra **Cursor → Definições → Modelos** (ou **Definições do Cursor → IA**).
2. Desloque-se até **OpenAI API Key** e expanda a opção **Override OpenAI Base URL**.
3. Defina:

    | Campo | Valor |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Em **Modelos**, adicione um modelo personalizado chamado **`claudinio`** e ative-o.
5. Desative os outros modelos predefinidos se quiser que o Cursor use exclusivamente o Claudin.io.

!!! note "Funcionalidades próprias do Cursor"
    As funcionalidades agênticas do Cursor funcionam melhor com um modelo de chat compatível com OpenAI. O `claudinio` suporta chamadas de ferramentas, portanto os fluxos do Composer/Agent funcionam. Algumas funcionalidades proprietárias do Cursor (autocompletar Tab, etc.) são executadas nos próprios modelos do Cursor e não são roteadas através da sua substituição de fornecedor.

## Verificar

Abra um chat no Cursor, selecione **claudinio** e envie uma mensagem. Se receber uma resposta, está pronto. Caso contrário, verifique novamente se a URL base termina em `/v1` e se a chave foi colada sem espaços extra.

| Definição | Valor |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |