# Cursor

[Cursor](https://cursor.com) lets you add an OpenAI-compatible model through its
settings. Claudin.io plugs in via the OpenAI base URL override.

## Setup

1. Open **Cursor → Settings → Models** (or **Cursor Settings → AI**).
2. Scroll to **OpenAI API Key** and expand the **Override OpenAI Base URL**
   option.
3. Set:

    | Field | Value |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Under **Models**, add a custom model named **`claudinio`** and enable it.
5. Disable the other default models if you want Cursor to use Claudin.io
   exclusively.

!!! note "Cursor's own features"
    Cursor's agentic features work best with an OpenAI-compatible chat model.
    `claudinio` supports tool calls, so the Composer/Agent flows work. Some
    Cursor-proprietary features (Tab autocomplete, etc.) run on Cursor's own
    models and aren't routed through your provider override.

## Verify

Open a chat in Cursor, select **claudinio**, and send a message. If you get a
reply, you're set. If not, double-check the base URL ends in `/v1` and the key
is pasted without extra spaces.

| Setting | Value |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
