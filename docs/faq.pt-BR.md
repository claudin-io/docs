# FAQ

## O que é o Claudin.io, exatamente?

Um proxy de API para agentes de codificação de IA. Você paga uma assinatura mensal fixa e recebe
uma chave de API compatível com OpenAI/Anthropic que pode ser usada no Claude Code, Kilo, Zed,
Codex, Cursor ou qualquer cliente OpenAI. Sem cobrança por token.

## É realmente ilimitado?

O uso é ilimitado — não há contador de requisições ou medidor de tokens. O único limite
é um **teto de proteção de gastos** por janela de tempo que impede um agente descontrolado de
esgotar seu plano. No trabalho interativo normal, raramente você o atinge. Veja
[Planos e limites](plans.md).

## Qual modelo devo usar?

Sempre **`claudinio`** (ou `claudinio/claudinio` para clientes que esperam o
formato `provedor/modelo`). A URL base é `https://api.claudin.io`.

## Devo autenticar com `Authorization` ou `x-api-key`?

Ambos funcionam. `Authorization: Bearer SUA_CHAVE_API` ou `x-api-key: SUA_CHAVE_API`.

## Posso usar com uma ferramenta que não está listada?

Sim — qualquer ferramenta que permita definir uma URL base personalizada do OpenAI funciona. Use a
[configuração genérica do OpenAI](clients/openai-compatible.md).

## Ele suporta chamadas de ferramenta / função?

Sim. É por isso que funciona dentro de editores de agente. Passe `tools` e leia
`tool_calls` como na API OpenAI.

## Ele pode lidar com imagens, áudio ou vídeo?

Sim, de forma transparente. Envie blocos de conteúdo padrão do OpenAI; o proxy converte
imagens/áudio/vídeo em descrições de texto ou transcrições antes que o modelo os veja.
Nada especial para configurar.

## Qual é a janela de contexto?

256K tokens.

## Como faço para fazer upgrade ou cancelar?

Pelo seu [painel de controle](https://claudin.io/dashboard). Upgrades são aplicados imediatamente
(via Stripe). Se você cancelar, manterá seu plano pago até o final do período
que já pagou, e então cairá automaticamente para o plano Gratuito.

## Encontrei um erro de orçamento. E agora?

Você atingiu o teto de proteção de gastos da janela atual. Aguarde a
reinicialização da janela (seu painel mostra quando) ou [faça upgrade](plans.md) para um
teto maior.

## Uma requisição falhou com 401.

Sua chave está ausente ou incorreta. Copie-a novamente do painel e verifique se
não há espaços extras e se o cabeçalho de autenticação está configurado.

## Minha chave vazou. O que devo fazer?

Revogue-a pelo painel e gere uma nova imediatamente. Trate as chaves como
senhas — nunca as confirme em commits ou as compartilhe publicamente.

## Onde obtenho ajuda?

Abra um ticket através do cartão **Suporte** no seu
[painel de controle](https://claudin.io/dashboard), ou envie um e-mail para o suporte. Entraremos em contato com você.