# Plans & limits

Every Claudin.io plan is **unlimited usage** with a **spend-protection cap**.
You're not billed per token or per request — you pay a flat monthly price and
use it freely. The cap exists only to stop a runaway agent (an infinite tool
loop, for example) from draining your plan.

## The plans

| Plan | Price | Spend protection | Best for |
| --- | --- | --- | --- |
| **Free** | $0 | $0.45 / day | Trying it out, light use |
| **Lite** | $5 / mo | $0.60 / hour | Hobby projects, occasional coding |
| **Essential** | $10 / mo | $1.50 / hour | Daily coding — the popular pick |
| **Pro** | $29 / mo | $4.00 / hour | Heavy agentic workflows |

!!! tip "Most people never hit the cap"
    The hourly cap is generous for normal interactive work. You typically only
    brush against it if an agent goes into a tight loop — which is exactly when
    you *want* a brake.

## How spend protection works

Each plan defines a budget **window** — a rolling period and a maximum spend
inside it:

- **Free** uses a **24-hour** window (`$0.45/day`).
- **Lite / Essential / Pro** use a **1-hour** window.

Within the window, your usage accumulates a tiny internal cost. When that
internal cost reaches the window's cap, requests pause until the window resets.
The window resets on a fixed schedule (the top of each hour, UTC, for the
hourly plans), and your remaining budget is shown **live in your dashboard**.

This is *spend protection*, not metered billing — the dollar figures are the
protection ceiling, not what you pay. Your actual bill is just the flat monthly
subscription.

## Upgrading & downgrading

- **Upgrade** any time from the [dashboard](https://claudin.io/dashboard).
  Payment is handled through Stripe and the new limits apply immediately.
- **Downgrade or cancel** from the same place. If you cancel, you keep your paid
  plan until the end of the period you already paid for, then automatically drop
  to **Free** — your account and keys are preserved.

## What counts against the cap

Only your model calls through the proxy. Each request adds to the current
window's running total based on the tokens it used. When the window resets, the
total resets with it.

If you hit the cap and get a budget error, you have two options:

1. Wait for the window to reset (shown in your dashboard).
2. Upgrade to a higher plan for a larger cap.

See [Plans-related errors](api-reference.md#errors) for what the budget error
looks like.
