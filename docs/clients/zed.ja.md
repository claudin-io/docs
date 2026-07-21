# Zed

[Zed](https://zed.dev) は、OpenAI 互換プロバイダーを `language_models.openai_compatible` でネイティブにサポートしています。

## クイックセットアップ（スクリプト）

まず、[キーをエクスポート](../getting-started/set-your-key.md) して `$CLAUDINIO_API_KEY` を設定します。これにより `~/.config/zed/settings.json` に書き込まれ、既存のファイルはバックアップされます。

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

1. `~/.config/zed/settings.json` にプロバイダーを追加します：

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

2. Zed の Agent パネルを開き、プロンプトが表示されたら API キーを貼り付けるか、**Claudinio** プロバイダーの API キーとして設定します。
3. Agent パネルのモデルピッカーで **Claudinio** を選択します。

| 設定 | 値 |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |
| 最大トークン数 | `256000` |