# FAQ

## O que é o Claudin.io, exatamente?

Um proxy de API para agentes de codificação de IA. Você paga uma assinatura mensal fixa e obtém
uma chave de API compatível com OpenAI/Anthropic que pode usar no Claude Code, Kilo, Zed,
Codex, Cursor ou qualquer cliente OpenAI. Sem cobrança por token.

## É realmente ilimitado?

O uso é ilimitado — não há contador de solicitações ou medidor de tokens. O único limite
é um **limite de proteção de gastos** por janela de tempo que impede um agente descontrolado de
esgotar seu plano. No trabalho interativo normal, raramente o atinge. Consulte
[Planos e limites](plans.md).

## Posso usá-lo para coisas que não sejam programação?

A API é compatível com OpenAI, por isso tecnicamente qualquer pedido funciona.
Mas o serviço é feito para **programação com IA**: roteamento, prompts e cache
estão afinados para agentes de código. Atividades que não sejam de programação
— bots de chat genéricos, automação sem código — poderão ter roteamento
especial e ser servidas por um modelo ou nível diferente do tráfego de
programação.

## Que modelo devo usar?

Sempre **`claudinio`** (ou `claudinio/claudinio` para clientes que preferem
o formato `provider/model`). O URL base é `https://api.claudin.io`.

## Autentico com `Authorization` ou `x-api-key`?

Ambos funcionam. `Authorization: Bearer YOUR_API_KEY` ou `x-api-key: YOUR_API_KEY`.

## Posso usá-lo com uma ferramenta que não está listada?

Sim — qualquer ferramenta que permita definir um URL base personalizado do OpenAI funciona. Use a
[configuração genérica do OpenAI](clients/openai-compatible.md).

## Suporta chamada de ferramenta / função?

Sim. É por isso que funciona dentro de editores agênticos. Passe `tools` e leia
`tool_calls` como na API da OpenAI.

## Consegue lidar com imagens, áudio ou vídeo?

Sim, de forma transparente. Envie blocos de conteúdo padrão do OpenAI; o proxy converte
imagens/áudio/vídeo em descrições de texto ou transcrições antes que o modelo os veja.
Nada especial para configurar.

## Qual é a janela de contexto?

256K tokens.

## Como faço para atualizar ou cancelar?

No seu [painel](https://claudin.io/dashboard). As atualizações são aplicadas imediatamente
(através do Stripe). Se cancelar, mantém o seu plano pago até ao final do período
que já pagou e depois desce automaticamente para o plano Gratuito.

## Encontrei um erro de orçamento. E agora?

Atingiu o limite de proteção de gastos da janela atual. Ou aguarde a
reinicialização da janela (o seu painel mostra quando) ou [atualize](plans.md) para um limite
maior.

## Um pedido falhou com 401.

A sua chave está em falta ou errada. Re-copie-a do painel e certifique-se de que
não há espaços em branco extras e que o cabeçalho de autenticação está definido.

## A minha chave foi divulgada. O que devo fazer?

Revoque-a do painel e gere uma nova imediatamente. Trate as chaves como
palavras-passe — nunca as comprometa ou partilhe publicamente.

## Onde posso obter ajuda?

Abra um ticket a partir do cartão **Suporte** no seu
[painel](https://claudin.io/dashboard) ou envie um e-mail para o suporte. Entraremos em contacto
consigo.