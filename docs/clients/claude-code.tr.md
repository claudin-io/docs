# Claude Code

[Claude Code](https://claude.com/claude-code), Claudin.io'ya Anthropic uyumlu uç noktası üzerinden bağlanır. Temel URL'sini Claudin.io'ya yönlendirin ve kimlik doğrulama token'ı olarak anahtarınızı kullanın.

## Hızlı kurulum (script)

İlk olarak [anahtarınızı dışa aktarın](../getting-started/set-your-key.md) böylece
`$CLAUDINIO_API_KEY` ayarlanır, ardından bunu çalıştırın. Bu, `~/.claude/settings.json` dosyasını yazar
(önce mevcut dosyayı yedekleyerek):

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

!!! note "Neden `ANTHROPIC_API_KEY` boş?"
    Claude Code, eğer ayarlanmışsa `ANTHROPIC_API_KEY`'i tercih eder. Onu boş bırakmak,
    Claudin.io temel URL'sine karşı `ANTHROPIC_AUTH_TOKEN` (sizin Claudin.io anahtarınız)
    kullanmaya zorlar.

## Kullanılan değerler

| Ayar | Değer |
| --- | --- |
| Temel URL | `https://api.claudin.io` |
| Model | `claudinio` |
| Alt aracı modeli | `claudinio` |
| Kimlik doğrulama | `ANTHROPIC_AUTH_TOKEN` = anahtarınız |

---

Sorun mu var? [Sık karşılaşılan hatalar](../api-reference.md#errors) veya [FAQ](../faq.md) bölümüne bakın.