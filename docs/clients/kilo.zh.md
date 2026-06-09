# Kilo Code

[Kilo Code](https://kilo.ai) 使用兼容 OpenAI 的 provider 块。模型 ID 为 `claudinio/claudinio`（provider/模型）。

## 快速配置（脚本）

首先[导出你的密钥](../getting-started/set-your-key.md)，确保 `$CLAUDINIO_API_KEY` 已设置。此脚本会写入 `~/.config/kilo/kilo.jsonc`，并备份已有的文件：

```bash
kilo_config_install() {
  local key="$1"
  local dir="$HOME/.config/kilo"
  local file="$dir/kilo.jsonc"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<'JSONCEOF'
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "__CL_KEY__"
      },
      "models": {
        "claudinio": {
          "name": "Claudinio",
          "tool_call": true,
          "limit": { "context": 128000, "output": 16384 }
        }
      }
    }
  }
}
JSONCEOF

  sed -i.bak "s/__CL_KEY__/${key}/g" "$file" && rm -f "$file.bak"
  echo "[ok] Configured: $file"
}

kilo_config_install "$CLAUDINIO_API_KEY"
unset kilo_config_install
```

然后运行 `kilo`。

## 手动配置

将以下内容放入 `~/.config/kilo/kilo.jsonc`：

```jsonc
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "YOUR_API_KEY"
      },
      "models": {
        "claudinio": {
          "name": "Claudinio",
          "tool_call": true,
          "limit": { "context": 128000, "output": 16384 }
        }
      }
    }
  }
}
```

## 环境变量替代方案

Kilo 也支持读取标准的 OpenAI 环境变量：

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 设置项 | 值 |
| --- | --- |
| 基础 URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio/claudinio` |
| 工具调用 | 已启用 |