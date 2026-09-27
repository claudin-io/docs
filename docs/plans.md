# Plans & credits

Every Claudin.io plan is a **wallet of credits** that fills every month. A
request costs credits for the tokens it used — about **one credit** for a
typical coding request on `claudinio`. **Your plan's credits renew every month
— they are that month's allowance and do not accumulate. Credits you buy as
top-ups never expire. There is no hourly cap.**

## The plans

| Plan | Price | Credits / month | Best for |
| --- | --- | --- | --- |
| **Start** | $19 / mo | 3,000 | Trying it, light daily use |
| **Solo** ★ | $39 / mo | 7,000 | One developer, every day |
| **Pro** | $99 / mo | 18,000 | Heavy agentic workflows |
| **Studio** | $199 / mo | 36,000 | Several agents, all day |
| **Max** | $399 / mo | 72,000 | Production, teams, bots |

Every credit plan includes every model: `claudinio`, `claudius` and the whole
[catalogue](#the-catalogue-pick-a-model-by-name). The plans differ only in how
many credits arrive each month — and the larger the plan, the less each credit
costs. The earlier hourly plans run on `claudinio` — see
[Legacy plans](#legacy-plans-essential-pro-ultra-with-an-hourly-cap).

!!! tip "Which plan fits a month"
    A typical request on `claudinio` costs about one credit, measured on
    thousands of real requests. Count your agent's requests on a busy day,
    multiply by 22 working days, and pick the rung that holds it. If you are
    between two, take the smaller one — a top-up covers the odd heavy month.

### Top-ups

Need more before the next month arrives? A **top-up** adds credits to the same
wallet, instantly, on any plan:

| Top-up | Credits |
| --- | --- |
| $10 | 1,200 |
| $25 | 3,000 |
| $50 | 6,000 |

Top-up credits land in the same wallet as your plan credits, and every model
spends them. Requests spend the month's plan credits first; the top-up credits
you bought are kept, and they never expire.

## Why credits (and no hourly cap)

Our plans used to be a flat price with a **spend cap per hour** — a brake
against an agent stuck in a loop, we said. Before changing anything, we measured it on
three days of real traffic: **1 in 10 active hours on Pro** (11.1%) ended with
the cap cutting a developer off in the middle of a task, and 1 in 13 on
Essential. Those were not infinite loops. They were people at work.

A plan that sells capacity you cannot use when you need it is the wrong shape.
So the cap is gone. A plan is a number of credits a month; a heavy hour is paid
for by the quiet ones; a heavy month is a top-up away instead of a wait. The
only thing that stops your agent is an empty wallet, and the dashboard shows the
balance at all times.

## What a credit buys

One credit is worth the same on every axis. On `claudinio`:

| | Credits per 1M tokens |
| --- | --- |
| Input (cache miss) | 40 |
| Input (cache hit) | 6 |
| Output | 80 |

Almost all of an agent's tokens are prompt tokens, and almost all of those are
served from the cache on a working session — which is why a typical request
lands near one credit, and why long sessions are cheaper per request than
short ones.

## Which model? `claudinio`, `claudius` and the catalogue

| Model | What it is | Cost in credits | Included in |
| --- | --- | --- | --- |
| **claudinio** 🏆 | The model we tune, measure and cache for coding | 1× — about one credit a request | Every plan |
| **claudius** ★ | Our premium option, for deep reasoning | up to 6x the claudinio credits (3× input, 4× output, 6× cache reads) | Every credit plan (Start, Solo, Pro, Studio, Max) |

**Our recommendation is `claudinio`.** It is the model every plan is built
around: the one we tune the prompt for, the one every evaluation scored, and
the one a credit goes furthest on. The most effective setup we see is **plan
with `claudius`, implement with `claudinio`** — reasoning is where the premium
model earns its multiple, and the implementation loop is where the volume
lives.

### The catalogue: pick a model by name

You can also ask for a third-party model by name. A catalogue model is served
**raw** — the vendor's model, your client's own system prompt, no Claudinio
tuning — and costs a fixed whole multiple of the `claudinio` credits on every
axis, so the price reads as one number:

| Model id | Model | Vendor | Credits vs `claudinio` |
| --- | --- | --- | --- |
| `qwen3-coder-flash` | Qwen3 Coder Flash | Qwen | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `qwen3-coder-plus` | Qwen3 Coder Plus | Qwen | 10× |
| `haiku-4.5` | Claude Haiku 4.5 | Anthropic | 11× |
| `glm-5.3` | GLM 5.3 | Z.ai | 13× |
| `kimi-k3` | Kimi K3 | Moonshot | 18× |
| `sonnet-5` | Claude Sonnet 5 | Anthropic | 21× |
| `gemini-3.1-pro` | Gemini 3.1 Pro | Google | 22× |

Set `model=sonnet-5` (or any id above) in your client and only that request
pays the multiple — the rest of your session keeps costing `claudinio` rates.
Every catalogue model is available on every plan.

!!! note "Why we still recommend `claudinio`"
    The catalogue exists for the developer who wants to choose, not because
    any entry measured better for coding. `claudinio` is the model we evaluate
    against, the one the prompt cache is built around, and — at 3× to 22× less
    per request — the one your credits go furthest on. Reach for a catalogue
    model deliberately, for the task that needs it.

> 💡 Tip: `claudinio` also resolves the aliases coding agents send by default —
> `claude-sonnet-4`, `gpt-4o`, `o3-mini` and dozens more — so you don't need
> to change your agent's configuration to use it.

## When the wallet is empty

Requests answer `402` with the code `insufficient_credits` (see
[Errors](api-reference.md#errors)). Nothing is queued and nothing is charged.
You have two options, both instant:

1. **Buy a top-up** from the [dashboard](https://claudin.io/dashboard).
2. **Move to a larger plan** — the new month's credits arrive with the invoice.

The dashboard shows your balance, the day's spend and a low-balance warning
before you get there, and we email you once when the balance runs low.

## Legacy plans (Essential, Pro, Ultra with an hourly cap)

The credit plans above are what new accounts sign up for. If you already
subscribed to one of the earlier plans (Essential, Pro, Ultra), you keep it **exactly as before: same price, same hourly cap, and
it keeps renewing normally**. You can still switch between Essential, Pro and
Ultra from the [dashboard](https://claudin.io/dashboard), your API key does not
change, and [top-ups](#top-ups) keep paying for use beyond the hourly cap, as
they always did.

The earlier hourly plans use `claudinio`. `claudius` and the
[catalogue](#the-catalogue-pick-a-model-by-name) come with the credit plans: on
an hourly plan, a request that names one of them is served by `claudinio` — it
is not refused and returns no error.
