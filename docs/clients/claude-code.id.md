# Claude Code

[Claude Code](https://claude.com/claude-code) terhubung ke Claudin.io melalui endpoint yang kompatibel dengan Anthropic. Arahkan base URL-nya ke Claudin.io dan gunakan kunci Anda sebagai token autentikasi.

## Pengaturan cepat (skrip)

Pertama [ekspor kunci Anda](../getting-started/set-your-key.md) sehingga `$CLAUDINIO_API_KEY` diatur, lalu jalankan ini. Ini menulis `~/.claude/settings.json` (mencadangkan file yang sudah ada terlebih dahulu):

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

Kemudian cukup jalankan `claude`.

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
    Claude Code lebih suka `ANTHROPIC_API_KEY` jika diatur. Membiarkannya kosong memaksa untuk menggunakan `ANTHROPIC_AUTH_TOKEN` (kunci Claudin.io Anda) terhadap base URL Claudin.io.

## Nilai yang digunakan

| Pengaturan | Nilai |
| --- | --- |
| Base URL | `https://api.claudin.io` |
| Model | `claudinio` |
| Model subagent | `claudinio` |
| Autentikasi | `ANTHROPIC_AUTH_TOKEN` = kunci Anda |

---

Ada masalah? Lihat [kesalahan umum](../api-reference.md#errors) atau [FAQ](../faq.md).