# FAQ

## What is Claudin.io, exactly?

An API proxy for AI coding agents. You pay a monthly plan, get a wallet of
credits that fills every month, and an OpenAI/Anthropic-compatible API key you
can drop into Claude Code, Kilo, Zed, Codex, Cursor, or any OpenAI client. A
typical coding request costs about one credit. No per-token invoice, no hourly
cap.

## Is there a limit?

Only your wallet. There is no hourly cap, no session limit and no weekly
quota — the only thing that stops your agent is an empty balance, and a top-up
fixes that instantly. Credits you don't use stay in the wallet and never
expire. See [Plans & credits](plans.md).

## Why credits instead of a flat price?

Because we measured the flat plans' hourly cap on real traffic and it cut
1 in 10 active hours on Pro — people in the middle of a task, not runaway
loops. A plan that sells capacity you cannot use when you need it is the
wrong shape. Credits are a number you can see, a heavy hour paid for by the
quiet ones, and a heavy month that is a top-up away instead of a wait.

## Can I use it for things that aren't coding?

The API is OpenAI-compatible, so any request technically works. But the
service is built for **AI programming**: routing, prompts and caching are all
tuned for coding agents. Activity that isn't programming-related — general
chat bots, non-coding automation — may get special routing and be served by a
different model or tier than coding traffic.

## What model do I use?

**`claudinio`** by default (or `claudinio/claudinio` for clients that want
`provider/model` form). The base URL is `https://api.claudin.io`. It is the
model we tune, measure and cache for coding, and the one your credits go
furthest on.

## Can I pick another model?

Yes, by name. `claudius` is our premium option, at up to 6× the credits. The
[catalogue](plans.md#the-catalogue-pick-a-model-by-name) adds eight
third-party models — Claude Sonnet 5 and Haiku 4.5, Gemini 3.1 Pro, Kimi K3,
GLM 5.3, MiniMax M3, Qwen3 Coder — each priced as a fixed multiple of the
`claudinio` credits, from 3× to 22×. Set the id in your client and only that
request pays the multiple. Every model is on every plan; we still recommend
`claudinio`.

## Do I authenticate with `Authorization` or `x-api-key`?

Either works. `Authorization: Bearer YOUR_API_KEY` or `x-api-key: YOUR_API_KEY`.

## Can I use it with a tool that isn't listed?

Yes — any tool that lets you set a custom OpenAI base URL works. Use the
[generic OpenAI setup](clients/openai-compatible.md).

## Does it support tool / function calling?

Yes. That's why it works inside agentic editors. Pass `tools` and read
`tool_calls` like with the OpenAI API.

## Can it handle images, audio, or video?

Yes, transparently. Send standard OpenAI content blocks; the proxy converts
images/audio/video to text descriptions or transcriptions before the model sees
them. Nothing special to configure.

## What's the context window?

256K tokens.

## How do I upgrade or cancel?

From your [dashboard](https://claudin.io/dashboard). Upgrades apply immediately
(via Stripe). If you cancel, you keep your paid plan until the end of the period
you already paid for. Credits already in the wallet stay yours and keep
working after the plan ends.

## Can I get a refund?

Within **48 hours of your first payment**, yes — write to
[support@claudin.io](mailto:support@claudin.io) from your account's email. The
subscription ends immediately, and you get back what you paid minus a
usage and handling fee that covers the cost of the model usage your account
made in that time (never more than you paid). Tried it for a day and it wasn't for
you? You get almost everything back. Spent the whole month's credits in two
days? Expect little or nothing. After 48 hours there are no refunds; cancelling
keeps your plan until the end of the paid period. Full wording in the
[Terms](https://claudin.io/terms).

## I got a `402 insufficient_credits`. What now?

Your wallet is empty. Buy a [top-up](plans.md#top-ups) or move to a larger
plan from the dashboard — both take effect immediately. Nothing is queued and
nothing was charged for the failed request.

## What happens to my old Essential / Pro / Ultra plan?

It keeps working exactly as before, with its hourly cap, until the end of the
period you already paid for, and does not renew after that. Monthly holders
received a courtesy of credits to try the new system; yearly holders keep
their whole year and move to credits when it ends. See
[Legacy plans](plans.md#legacy-plans-essential-pro-ultra-with-an-hourly-cap).

## A request failed with 401.

Your key is missing or wrong. Re-copy it from the dashboard and make sure
there's no extra whitespace, and that the auth header is set.

## My key leaked. What do I do?

Revoke it from the dashboard and generate a new one immediately. Treat keys like
passwords — never commit them or share them publicly.

## Where do I get help?

Open a ticket from the **Support** card in your
[dashboard](https://claudin.io/dashboard), or email support. We'll get back to
you.

