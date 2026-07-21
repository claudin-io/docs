# Cursor

[Cursor](https://cursor.com) permite adicionar um modelo compatível com OpenAI através das suas definições. O Claudin.io liga-se através da substituição da URL base da OpenAI.

## Configuração

1. Abra **Cursor → Definições → Modelos** (ou **Definições do Cursor → IA**).
2. Desça até **OpenAI API Key** e expanda a opção **Substituir URL base da OpenAI**.
3. Defina:

    | Campo | Valor |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Em **Modelos**, adicione um modelo personalizado chamado **`claudinio`** e ative-o.
5. Desative os outros modelos predefinidos se quiser que o Cursor utilize apenas o Claudin.io.

!!! nota "Funcionalidades próprias do Cursor"
    As funcionalidades agênticas do Cursor funcionam melhor com um modelo de chat compatível com OpenAI. O `claudinio` suporta chamadas de ferramentas, por isso os fluxos de Composer/Agent funcionam. Algumas funcionalidades proprietárias do Cursor (Tab autocomplete, etc.) são executadas nos modelos próprios do Cursor e não são roteadas através da sua substituição de fornecedor.

## Verificar

Abra um chat no Cursor, selecione **claudinio** e envie uma mensagem. Se receber uma resposta, está configurado. Caso contrário, verifique novamente se a URL base termina em `/v1` e se a chave foi colada sem espaços extras.

| Definição | Valor |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |