# pi

[pi](https://github.com/parallel-web/pi) は `~/.pi/agent/models.json` からプロバイダを読み込みます。Claudin.io は `openai-completions` プロバイダとして登録されています。

## クイックセットアップ（スクリプト）

最初に[キーをエクスポート](../getting-started/set-your-key.md)して、`$CLAUDINIO_API_KEY` が設定されていることを確認してください。これにより `~/.pi/agent/models.json` が書き込まれ、既存のファイルはバックアップされます：

```bash
pi_models_install() {
  local key="$1"
  local dir="$HOME/.pi/agent"
  local file="$dir/models.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<'JSONEOF'
{
  "providers": {
    "claudinio": {
      "baseUrl": "https://api.claudin.io/v1",
      "api": "openai-completions",
      "apiKey": "__CL_KEY__",
      "models": [
        { "id": "claudinio", "name": "Claudinio", "contextWindow": 256000 }
      ]
    }
  }
}
JSONEOF

  sed -i.bak "s/__CL_KEY__/${key}/g" "$file" && rm -f "$file.bak"
  echo "[ok] Configured: $file"
  echo "[ok] Run: pi --provider claudinio --model claudinio"
}

pi_models_install "$CLAUDINIO_API_KEY"
unset pi_models_install
```

次に実行します：

```bash
pi --provider claudinio --model claudinio
```

## 手動セットアップ

以下を `~/.pi/agent/models.json` に配置します：

```json
{
  "providers": {
    "claudinio": {
      "baseUrl": "https://api.claudin.io/v1",
      "api": "openai-completions",
      "apiKey": "YOUR_API_KEY",
      "models": [
        { "id": "claudinio", "name": "Claudinio", "contextWindow": 256000 }
      ]
    }
  }
}
```

## 環境変数による代替方法

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 設定項目 | 値 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |
| API タイプ | `openai-completions` |