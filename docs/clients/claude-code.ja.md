# Claude Code

[Claude Code](https://claude.com/claude-code) は、Anthropic 互換のエンドポイントを介して Claudin.io に接続します。ベースURLを Claudin.io に向け、あなたのキーを認証トークンとして使用します。

## クイックセットアップ（スクリプト）

最初に[キーをエクスポート](../getting-started/set-your-key.md)して `$CLAUDINIO_API_KEY` が設定されていることを確認し、次にこれを実行します。これにより `~/.claude/settings.json` が書き込まれます（既存のファイルがあれば最初にバックアップします）：

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

その後、単に `claude` を実行します。

## 手動セットアップ

自分で `~/.claude/settings.json` を編集します：

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

!!! note "`ANTHROPIC_API_KEY` が空の理由"
    Claude Code は、設定されている場合、`ANTHROPIC_API_KEY` を優先します。これを空のままにすると、Claudin.io のベースURLに対して `ANTHROPIC_AUTH_TOKEN`（あなたの Claudin.io キー）を使用するよう強制されます。

## 使用される値

| 設定 | 値 |
| --- | --- |
| ベースURL | `https://api.claudin.io` |
| モデル | `claudinio` |
| サブエージェントモデル | `claudinio` |
| 認証 | `ANTHROPIC_AUTH_TOKEN` = あなたのキー |

---

問題がありますか？ [一般的なエラー](../api-reference.md#errors) または [FAQ](../faq.md) をご覧ください。