# Zed

[Zed](https://zed.dev) 原生支持 OpenAI 兼容的提供商，位于 `language_models.openai_compatible` 下。

## 快速设置（脚本）

首先[导出你的密钥](../getting-started/set-your-key.md)以确保设置了 `$CLAUDINIO_API_KEY`。这会将配置写入 `~/.config/zed/settings.json`，并备份已有文件：

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

## 手动设置

1. 将提供商添加到 `~/.config/zed/settings.json`：

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

2. 打开 Zed 的 Agent 面板，在提示时粘贴你的 API 密钥，或者将其设置为 **Claudinio** 提供商的 API 密钥。
3. 在 Agent 面板的模型选择器中选择 **Claudinio**。

| 设置 | 值 |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio` |
| 最大令牌数 | `256000` |