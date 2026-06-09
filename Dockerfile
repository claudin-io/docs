# Builds the static MkDocs site. Dependencies are baked into the image; the
# Markdown source is bind-mounted at runtime (see the docs-builder service in
# docker-compose.yml), so refreshing docs is just a re-run — no image rebuild.
FROM python:3.13-slim

WORKDIR /docs

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Default: build the site into ./site (served read-only by Caddy at /docs).
CMD ["mkdocs", "build", "--clean"]
