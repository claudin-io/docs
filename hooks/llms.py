"""MkDocs post-build hook: expose raw Markdown + llms.txt for LLM consumption.

For every page it writes a sibling raw-Markdown file at the same path with a
`.md` extension, so `/plans/` (HTML) has `/plans.md` (source). Localized builds
get `/<locale>/plans.md` too — using the translated source when it exists, or
falling back to the default-language source (mirroring the i18n fallback).

It also emits, per language:
  - `llms.txt`       — a curated index (the emerging standard for LLM docs)
  - `llms-full.txt`  — every page concatenated as one Markdown document

No external plugins required — this is a plain MkDocs hook.
"""

from __future__ import annotations

import os
import re

_H1 = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)


def _locales(config):
    """Return (default_locale, [other_locales]) from the i18n plugin, if present."""
    try:
        i18n = config["plugins"]["i18n"]
        langs = i18n.config["languages"]
        default = "en"
        others = []
        for lang in langs:
            code = lang["locale"]
            if lang.get("default"):
                default = code
            else:
                others.append(code)
        return default, others
    except Exception:
        return "en", []


def _title(text: str, fallback: str) -> str:
    m = _H1.search(text)
    return m.group(1).strip() if m else fallback


def _strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


def on_post_build(config, **kwargs):
    docs_dir = config["docs_dir"]
    site_dir = config["site_dir"]
    default_locale, other_locales = _locales(config)
    locale_codes = {default_locale, *other_locales}

    # Match a locale suffix like "plans.pt.md" -> ("plans", "pt")
    suffix_re = re.compile(r"^(.*)\.(" + "|".join(re.escape(c) for c in locale_codes) + r")\.md$")

    # Discover page "bases": default-language .md files (no locale suffix).
    bases = []  # relative paths like "plans.md", "clients/zed.md"
    for root, _dirs, files in os.walk(docs_dir):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), docs_dir)
            if suffix_re.match(rel):
                continue  # a translation, handled per-locale below
            bases.append(rel.replace(os.sep, "/"))
    bases.sort()

    def _source_for(base: str, locale: str) -> str:
        """Path to the best source file for this base+locale (translation or fallback)."""
        if locale != default_locale:
            translated = os.path.join(docs_dir, base[:-3] + f".{locale}.md")
            if os.path.exists(translated):
                return translated
        return os.path.join(docs_dir, base)

    def _out_dir(locale: str) -> str:
        return site_dir if locale == default_locale else os.path.join(site_dir, locale)

    for locale in [default_locale, *other_locales]:
        out_root = _out_dir(locale)
        index_lines = []
        full_parts = []

        for base in bases:
            src = _source_for(base, locale)
            with open(src, "r", encoding="utf-8") as fh:
                raw = fh.read()

            # Write the raw .md alongside the HTML (same path + .md).
            dst = os.path.join(out_root, base)
            os.makedirs(os.path.dirname(dst) or out_root, exist_ok=True)
            with open(dst, "w", encoding="utf-8") as fh:
                fh.write(raw)

            body = _strip_frontmatter(raw)
            title = _title(body, fallback=base)
            index_lines.append(f"- [{title}]({base})")
            full_parts.append(body.rstrip() + "\n")

        # llms.txt — curated index
        header = (
            f"# {config['site_name']}\n\n"
            f"> {config.get('site_description', '')}\n\n"
            "Raw Markdown for every page is available at its URL with a `.md` "
            "extension (e.g. `plans.md`). The full corpus is in `llms-full.txt`.\n\n"
            "## Pages\n"
        )
        with open(os.path.join(out_root, "llms.txt"), "w", encoding="utf-8") as fh:
            fh.write(header + "\n".join(index_lines) + "\n")

        # llms-full.txt — everything concatenated
        with open(os.path.join(out_root, "llms-full.txt"), "w", encoding="utf-8") as fh:
            fh.write(f"# {config['site_name']} — full documentation\n\n")
            fh.write("\n\n---\n\n".join(full_parts) + "\n")
