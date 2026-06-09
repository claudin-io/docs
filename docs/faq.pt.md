# FAQ

## O que é Claudin.io, exatamente?

Um proxy de API para agentes de codificação de IA. Pagas uma subscrição mensal fixa e obténs uma chave de API compatível com OpenAI/Anthropic que podes usar no Claude Code, Kilo, Zed, Codex, Cursor, ou qualquer cliente OpenAI. Sem faturação por token.

## É realmente ilimitado?

O uso é ilimitado — não há contador de pedidos ou medidor de tokens. O único limite é um **teto de proteção de gastos** por janela de tempo que impede um agente descontrolado de esgotar o teu plano. No trabalho interativo normal, raramente o atinges. Vê [Planos e limites](plans.md).

## Que modelo uso?

Sempre **`claudinio`** (ou `claudinio/claudinio` para clientes que queiram o formato `provider/model`). O URL base é `https://api.claudin.io`.

## Autentico-me com `Authorization` ou `x-api-key`?

Qualquer um funciona. `Authorization: Bearer YOUR_API_KEY` ou `x-api-key: YOUR_API_KEY`.

## Posso usá-lo com uma ferramenta que não está listada?

Sim — qualquer ferramenta que te permita definir um URL base OpenAI personalizado funciona. Usa a [configuração genérica OpenAI](clients/openai-compatible.md).

## Suporta chamada de ferramentas / funções?

Sim. É por isso que funciona dentro de editores agentic. Passa `tools` e lê `tool_calls` como com a API OpenAI.

## Consegue lidar com imagens, áudio ou vídeo?

Sim, de forma transparente. Envia blocos de conteúdo padrão OpenAI; o proxy converte imagens/áudio/vídeo em descrições de texto ou transcrições antes de o modelo os ver. Nada especial para configurar.

## Qual é a janela de contexto?

256K tokens.

## Como faço para atualizar ou cancelar?

A partir do teu [painel de controlo](https://claudin.io/dashboard). As atualizações aplicam-se imediatamente (via Stripe). Se cancelares, manténs o teu plano pago até ao final do período que já pagaste, depois cais para Free automaticamente.

## Atingi um erro de orçamento. E agora?

Atingiste o teto de proteção de gastos da janela atual. Ou espera que a janela reinicie (o teu painel mostra quando) ou [atualiza](plans.md) para um teto maior.

## Um pedido falhou com 401.

A tua chave está em falta ou errada. Volta a copiá-la do painel de controlo e certifica-te de que não há espaços em branco extra e que o cabeçalho de autenticação está definido.

## A minha chave foi exposta. O que faço?

Revoga-a no painel de controlo e gera uma nova imediatamente. Trata as chaves como palavras-passe — nunca as submetas a repositórios ou partilhes publicamente.

## Onde obtenho ajuda?

Abre um ticket a partir do cartão **Suporte** no teu [painel de controlo](https://claudin.io/dashboard), ou envia um email para o suporte. Responderemos.