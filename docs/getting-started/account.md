# Create your account

Getting a working API key takes about a minute.

## 1. Sign in with GitHub

Go to **[claudin.io](https://claudin.io)** and click **Sign in with GitHub**.
Claudin.io uses GitHub for login — there's no separate password to manage.

The first time you sign in, your account is created automatically on the
**Free** plan, so you can try it before paying anything.

## 2. Generate your API key

Once you're in the [dashboard](https://claudin.io/dashboard):

1. Find the **API Keys** card.
2. Click **Generate key** (or **Create new key**).
3. Copy the key — it looks like `sk-...`.

!!! warning "Treat your key like a password"
    Your API key grants access to your plan's budget. Don't commit it to a
    repo, paste it in a public chat, or share it. If a key leaks, revoke it
    from the dashboard and generate a new one.

## 3. Note the two values you'll need

Every integration needs the same two things:

| Value | What it is |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Model** | `claudinio` |
| **API key** | the `sk-...` you just copied |

That's it. Next, either [make a raw API call](first-call.md) to confirm it
works, or jump straight to [connecting your tool](../clients/claude-code.md).

---

## Choosing a plan

You can stay on **Free** to try things out. When you're ready for more
headroom, upgrade from the dashboard — see [Plans & limits](../plans.md) for the
full breakdown.

Upgrades are handled through Stripe and take effect immediately.
