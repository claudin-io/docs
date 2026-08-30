# Plans & limits

Every Claudin.io plan is **unlimited usage** with a **spend-protection cap**.
You're not billed per token or per request — you pay a flat monthly price and
use it freely. The cap exists only to stop a runaway agent (an infinite tool
loop, for example) from draining your plan.

## The plans

| Plan | Price | Spend protection | Best for |
| --- | --- | --- | --- |
| **Essential** | $19 / mo or $189 / yr | $2.00 / hour | Quality for everyday use |
| **Pro** ★ | $39 / mo or $389 / yr | $4.00 / hour | Heavy agentic workflows |
| **Ultra** | $99 / mo or $989 / yr | $10.00 / hour | Maximum power, teams & production |

!!! tip "Most people never hit the cap"
    The hourly cap is generous for normal interactive work. You typically only
    brush against it if an agent goes into a tight loop — which is exactly when
    you *want* a brake.

## Which model should you choose? Claudinio vs Claudius

We offer two main models for your coding agent:

| Model | Backend | Use case | Recommended for |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Fast, balanced, cost-effective | Everyday coding, hobby projects, general code | **All plans** (Essential to Ultra) |
| **claudius** ★ | Premium, deep reasoning | Complex tasks, deep reasoning, heavy agentic workflows | **Pro and Ultra** |
!!! warning "`claudius` is included in Pro and Ultra"
    On **Essential**, a request that names `claudius` is not rejected — it is served by `claudinio` and billed at `claudinio` rates. Your agent keeps working and you are never charged the premium rate on a plan that does not include it.

    On **Pro** and **Ultra**, remember the cap is measured **in dollars, not requests**: the same work on `claudius` uses roughly six times as much of it. On Pro ($4/hour) that is about 70 premium requests before the hour is gone; on Ultra ($10/hour), about 175. Keep `claudinio` as your agent's default and reach for `claudius` when you actually need the reasoning.

### Straight talk

If you're on **Essential** ($19) — same answer, and you have twice the cap to
spend on it. `claudius` is not part of this plan; if your agent asks for it,
`claudinio` answers and you pay `claudinio` rates.

If you're on **Pro** ($39) or **Ultra** ($99) — `claudius` is yours, but treat
it as a tool you reach for deliberately, not your default. The most effective
setup we see is **plan with `claudius`, implement with `claudinio`**: the
reasoning is where the premium model earns its cost, and the implementation
loop is where the volume lives.

Here's the reality: `claudinio` delivers quality comparable to Claude Sonnet for everyday coding at a **fraction of the internal cost**. On the Essential plan, you can get **hundreds of requests per hour** with it — which is why it is the model every plan is built around.

| Metric | claudinio | claudius |
| --- | --- | --- |
| Impact on hourly budget | Low — stretches much further | High — up to 6x per request |
| Use case | Daily coding, personal projects | Heavy reasoning, complex agents |

**Golden rule:** Configure your agent (Claude Code, Cursor, Continue, etc.) with `claudinio` as the default model. Only switch to `claudius` when you explicitly need more reasoning power. For hobby projects, `claudinio` is **all you need** and probably **more than you expect**.

**If you go over your hourly cap and you hold credit**, we don't block you — the
request is served and the excess comes out of your credit balance. The dashboard
meter says so while it is happening, and we email you the first time it happens
in a day. Nothing is taken silently.

> 💡 Tip: Both models work with all major coding agents. Set `model=claudinio` in your agent config — or `model=claudius` if you are on Pro or Ultra. `claudinio` also automatically resolves aliases like `claude-sonnet-4`, `gpt-4o`, `o3-mini` and dozens more — no need to change your agent's configuration.

## How spend protection works

Each plan defines a budget **window** — a rolling period and a maximum spend
inside it:

- **Essential**, **Pro**, and **Ultra** use a **1-hour** window.

Within the window, your usage accumulates a tiny internal cost. When that
internal cost reaches the window's cap, requests pause until the window resets.

Only your model calls through the proxy. Each request adds to the current
window's running total based on the tokens it used. When the window resets, the
total resets with it.

If you hit the cap and get a budget error, you have two options:

1. Wait for the window to reset (shown in your dashboard).
2. Upgrade to a higher plan for a larger cap.

See [Plans-related errors](api-reference.md#errors) for what the budget error
looks like.
