# Claude Code

[Claude Code](https://claude.com/claude-code), Anthropic uyumlu uç noktası üzerinden Claudin.io'ya bağlanır. Taban URL'sini Claudin.io'ya yönlendirin ve kimlik doğrulama token'ı olarak anahtarınızı kullanın.

## Hızlı kurulum (komut dosyası)

Öncelikle [anahtarınızı dışa aktarın](../getting-started/set-your-key.md) böylece `$CLAUDINIO_API_KEY` ayarlanır, ardından bunu çalıştırın. `~/.claude/settings.json` dosyasını oluşturur (önce varsa mevcut dosyayı yedekler):

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

Ardından sadece `claude` komutunu çalıştırın.

## Manuel kurulum

`~/.claude/settings.json` dosyasını kendiniz düzenleyin:

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

!!! note "Neden `ANTHROPIC_API_KEY` boş"
    Claude Code, ayarlanmışsa `ANTHROPIC_API_KEY`'i tercih eder. Boş bırakmak, Claudin.io taban URL'sine karşı `ANTHROPIC_AUTH_TOKEN`'ı (Claudin.io anahtarınız) kullanmaya zorlar.

## Kullanılan değerler

| Ayar | Değer |
| --- | --- |
| Taban URL | `https://api.claudin.io` |
| Model | `claudinio` |
| Alt ajan modeli | `claudinio` |
| Kimlik doğrulama | `ANTHROPIC_AUTH_TOKEN` = anahtarınız |

---

Sorun mu var? [Sık karşılaşılan hatalar](../api-reference.md#errors) veya [FAQ](../faq.md) sayfasına bakın.