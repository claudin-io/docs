# Claude Code

[Claude Code](https://claude.com/claude-code)は、Anthropic互換のエンドポイントを通じてClaudin.ioに接続します。ベースURLをClaudin.ioに向け、あなたのキーを認証トークンとして使用します。

## クイックセットアップ（スクリプト）

まず[キーをエクスポート](../getting-started/set-your-key.md)して`$CLAUDINIO_API_KEY`を設定し、次にこれを実行します。`~/.claude/settings.json`に書き込みます（既存のファイルがあれば最初にバックアップします）：

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

その後、`claude`を実行するだけです。

## 手動セットアップ

自分で`~/.claude/settings.json`を編集します：

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

!!! note "`ANTHROPIC_API_KEY`が空である理由"
    Claude Codeは設定されている場合、`ANTHROPIC_API_KEY`を優先します。空のままにしておくと、Claudin.ioのベースURLに対して`ANTHROPIC_AUTH_TOKEN`（あなたのClaudin.ioキー）を使用するように強制されます。

## 使用される値

| 設定 | 値 |
| --- | --- |
| Base URL | `https://api.claudin.io` |
| Model | `claudinio` |
| サブエージェントモデル | `claudinio` |
| Auth | `ANTHROPIC_AUTH_TOKEN` = あなたのキー |

---

問題が発生しましたか？ [よくあるエラー](../api-reference.md#errors) または [FAQ](../faq.md) をご覧ください。