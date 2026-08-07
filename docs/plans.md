# Plans & limits

Every Claudin.io plan is **unlimited usage** with a **spend-protection cap**.
You're not billed per token or per request — you pay a flat monthly price and
use it freely. The cap exists only to stop a runaway agent (an infinite tool
loop, for example) from draining your plan.

## The plans

| Plan | Price | Spend protection | Best for |
| --- | --- | --- | --- |
| **Lite** | $9 / mo | $1.00 / hour | Hobby projects, occasional coding |
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
| **claudinio** 🏆 | Fast, balanced, cost-effective | Everyday coding, hobby projects, general code | **All plans** (Lite to Ultra) |
| **claudius** ★ | Premium, deep reasoning | Complex tasks, deep reasoning, heavy agentic workflows | **All plans** (Lite to Ultra) |

### Straight talk

If you're on **Lite** ($9) — **use `claudinio` and don't look back.** 🎯

Here's the reality: `claudinio` delivers quality comparable to Claude Sonnet for everyday coding at a **fraction of the internal cost**. On the Lite plan, you can get **hundreds of requests per hour** with `claudinio` — while `claudius` would burn through your hourly budget much faster.

| Metric | claudinio | claudius |
| --- | --- | --- |
| Impact on hourly budget | Low — stretches much further | High — 6x per request |
| Use case | Daily coding, personal projects | Heavy reasoning, complex agents |

**Golden rule:** Configure your agent (Claude Code, Cursor, Continue, etc.) with `claudinio` as the default model. Only switch to `claudius` when you explicitly need more reasoning power. For hobby projects, `claudinio` is **all you need** and probably **more than you expect**.

> 💡 Tip: Both models work with all major coding agents. Just set `model=claudinio` or `model=claudius` in your agent config. `claudinio` also automatically resolves aliases like `claude-sonnet-4`, `gpt-4o`, `o3-mini` and dozens more — no need to change your agent's configuration.

## How spend protection works

Each plan defines a budget **window** — a rolling period and a maximum spend
inside it:

- **Lite**, **Essential**, **Pro**, and **Ultra** use a **1-hour** window.

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
