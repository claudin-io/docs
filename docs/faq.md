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
