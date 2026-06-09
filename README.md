# Claudin.io Documentation

User-facing documentation for [Claudin.io](https://claudin.io), built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

This is a self-contained MkDocs project. Everything lives under `docs/` so it
doesn't interfere with the main application.

## Local preview

```bash
cd docs
python3 -m venv .venv && source .venv/bin/activate   # optional but recommended
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. The site rebuilds live as you edit Markdown.

## Build the static site

```bash
cd docs
mkdocs build          # outputs to docs/site/ (gitignored)
```

The `site/` folder is a fully static site — host it anywhere (GitHub Pages,
Cloudflare Pages, Netlify, or behind the existing Caddy/NPM stack).

## Structure

```
docs/
├── mkdocs.yml            # site config, theme, nav
├── requirements.txt      # mkdocs-material
└── docs/                 # Markdown content (docs_dir)
    ├── index.md
    ├── getting-started/
    ├── clients/
    ├── plans.md
    ├── api-reference.md
    └── faq.md
```

## Localization (i18n)

Localization is handled by
[`mkdocs-static-i18n`](https://ultrabug.github.io/mkdocs-static-i18n/) using the
**suffix** structure:

- `index.md` → default language (English), served at `/`
- `index.pt.md` → Portuguese version, served at `/pt/`

A **language switcher** appears in the header automatically. Untranslated pages
**fall back to English**, so you can translate incrementally — only the pages
you actually create a `.pt.md` for get a translation; the rest reuse English.

### Translate a page

1. Copy the English file and add the locale suffix:

    ```bash
    cp docs/clients/claude-code.md docs/clients/claude-code.pt.md
    ```

2. Translate the body. Keep code blocks, URLs, and `{placeholder}` tokens intact.
3. Rebuild — the `pt` version is picked up automatically.

### Add another language

Add a block under `plugins.i18n.languages` in `mkdocs.yml` (e.g. `es`, `fr`),
then create `*.es.md` files. The nav labels are translated via the
`nav_translations` map per language.

> The main app supports 17 locales. You don't need to mirror all of them here —
> docs for dev tooling are commonly English-first. If you do want full coverage,
> the body text can be machine-translated through the LiteLLM proxy the same way
> `scripts/translate_locale.py` does for the app, then reviewed.

## Editing

- Content is plain Markdown in `docs/docs/`.
- Navigation order is controlled by the `nav:` block in `mkdocs.yml`.
- Brand colors / fonts are tweaked in `docs/docs/stylesheets/extra.css`.

The API base URL referenced throughout is `https://api.claudin.io`. If that
changes, update it across the `clients/` pages and `api-reference.md`.
