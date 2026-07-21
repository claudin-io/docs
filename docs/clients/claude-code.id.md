# Claude Code

[Claude Code](https://claude.com/claude-code) terhubung ke Claudin.io melalui endpoint yang kompatibel dengan Anthropic. Arahkan base URL-nya ke Claudin.io dan gunakan kunci Anda sebagai token autentikasi.

## Pengaturan cepat (skrip)

Pertama [ekspor kunci Anda](../getting-started/set-your-key.md) sehingga `$CLAUDINIO_API_KEY` sudah diatur, lalu jalankan ini. Skrip ini akan menulis `~/.claude/settings.json` (mencadangkan file yang sudah ada terlebih dahulu):

```bash
claude_settings_install() {
  local key="$1"
  local dir="$HOME/.claude"
  local file="$dir/settings.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "${key}",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

claude_settings_install "$CLAUDINIO_API_KEY"
unset claude_settings_install
```

Kemudian jalankan saja `claude`.

## Pengaturan manual

Edit sendiri `~/.claude/settings.json`:

```json
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
```

!!! note "Mengapa `ANTHROPIC_API_KEY` kosong"
    Claude Code lebih memilih `ANTHROPIC_API_KEY` jika sudah diatur. Membiarkannya kosong memaksanya untuk menggunakan `ANTHROPIC_AUTH_TOKEN` (kunci Claudin.io Anda) terhadap base URL Claudin.io.

## Nilai yang digunakan

| Pengaturan | Nilai |
| --- | --- |
| URL Dasar | `https://api.claudin.io` |
| Model | `claudinio` |
| Model subagen | `claudinio` |
| Autentikasi | `ANTHROPIC_AUTH_TOKEN` = kunci Anda |

---

Ada masalah? Lihat [kesalahan umum](../api-reference.md#errors) atau [FAQ](../faq.md).