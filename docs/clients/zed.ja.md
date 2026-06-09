# Zed

[Zed](https://zed.dev) は `language_models.openai_compatible` の下で OpenAI 互換プロバイダーをネイティブにサポートしています。

## クイックセットアップ（スクリプト）

まず [キーをエクスポート](../getting-started/set-your-key.md) して `$CLAUDINIO_API_KEY` が設定されていることを確認します。これにより `~/.config/zed/settings.json` が書き込まれ、既存のファイルはバックアップされます：

```bash
zed_settings_install() {
  local key="$1"
  local config_dir="$HOME/.config/zed"
  local file="$config_dir/settings.json"

  mkdir -p "$config_dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "language_models": {
    "openai_compatible": {
      "Claudinio": {
        "api_url": "https://api.claudin.io/v1",
        "available_models": [
          {
            "name": "claudinio",
            "display_name": "Claudinio",
            "max_tokens": 256000
          }
        ]
      }
    }
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

zed_settings_install "$CLAUDINIO_API_KEY"
unset zed_settings_install
```

## 手動セットアップ

1. プロバイダーを `~/.config/zed/settings.json` に追加します：

    ```json
    {
      "language_models": {
        "openai_compatible": {
          "Claudinio": {
            "api_url": "https://api.claudin.io/v1",
            "available_models": [
              {
                "name": "claudinio",
                "display_name": "Claudinio",
                "max_tokens": 256000
              }
            ]
          }
        }
      }
    }
    ```

2. ZedのAgentパネルを開き、プロンプトが表示されたらAPIキーを貼り付けるか、**Claudinio**プロバイダーのAPIキーとして設定します。
3. エージェントパネルのモデルピッカーで **Claudinio** を選択します。

| 設定 | 値 |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |
| 最大トークン | `256000` |