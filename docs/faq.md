# FAQ

## What is Claudin.io, exactly?

An API proxy for AI coding agents. You pay a flat monthly subscription and get
an OpenAI/Anthropic-compatible API key you can drop into Claude Code, Kilo, Zed,
Codex, Cursor, or any OpenAI client. No per-token billing.

## Is it really unlimited?

Usage is unlimited — there's no request counter or token meter. The only limit
is a **spend-protection cap** per time window that stops a runaway agent from
draining your plan. In normal interactive work you rarely hit it. See
[Plans & limits](plans.md).

## Can I use it for things that aren't coding?

The API is OpenAI-compatible, so any request technically works. But the
service is built for **AI programming**: routing, prompts and caching are all
tuned for coding agents. Activity that isn't programming-related — general
chat bots, non-coding automation — may get special routing and be served by a
different model or tier than coding traffic.

## What model do I use?

Always **`claudinio`** (or `claudinio/claudinio` for clients that want
`provider/model` form). The base URL is `https://api.claudin.io`.

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
you already paid for, then drop to Free automatically.

## Can I get a refund?

Within **48 hours of your first payment**, yes — write to
[support@claudin.io](mailto:support@claudin.io) from your account's email. The
subscription ends immediately, and you get back what you paid minus a
usage and handling fee that covers the cost of the model usage your account
made in that time (never more than you paid). Tried it for a day and it wasn't for
you? You get almost everything back. Ran it at the hourly ceiling for two
days? Expect little or nothing. After 48 hours there are no refunds; cancelling
keeps your plan until the end of the paid period. Full wording in the
[Terms](https://claudin.io/terms).

## I hit a budget error. What now?

You reached the current window's spend-protection cap. Either wait for the
window to reset (your dashboard shows when) or [upgrade](plans.md) for a bigger
cap.

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

