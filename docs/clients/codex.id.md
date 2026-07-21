# Codex

[Codex](https://github.com/openai/codex) terhubung melalui penyedia model kustom di
`~/.codex/config.toml`. Claudin.io mengekspos API wire `responses` yang diharapkan
Codex.

!!! warning "Gunakan CLI Codex"
    Pengaturan ini berlaku untuk **CLI Codex**. Aplikasi Codex yang dihosting mungkin
    tidak mengizinkan Anda mengarahkan ke URL dasar kustom.

## Pengaturan manual

Tambahkan ini ke `~/.codex/config.toml`:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Kemudian ekspor kunci Anda (nama harus cocok dengan `env_key` di atas). Cara
termudah adalah dengan [mengaturnya sekali di profil shell Anda](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Pengaturan cepat (skrip)

```bash
codex_config_install() {
  local key="$1"
  local dir="$HOME/.codex"
  local file="$dir/config.toml"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<TOMLEOF
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
TOMLEOF

  echo "[ok] Configured: $file"
  echo "[ok] Make sure CLAUDINIO_API_KEY is exported in your shell"
}

codex_config_install
unset codex_config_install
```

| Pengaturan | Nilai |
| --- | --- |
| URL Dasar | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| API Wire | `responses` |
| Variabel env kunci | `CLAUDINIO_API_KEY` |