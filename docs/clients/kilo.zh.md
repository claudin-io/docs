# Kilo Code

[Kilo Code](https://kilo.ai) 使用兼容OpenAI的提供者模块。模型ID是 `claudinio/claudinio` (提供者/模型)。

## 快速设置（脚本）

首先[导出你的密钥](../getting-started/set-your-key.md)，以便设置 `$CLAUDINIO_API_KEY`。这会写入 `~/.config/kilo/kilo.jsonc`，备份任何现有文件：

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

## 手动设置

将此内容放入 `~/.config/kilo/kilo.jsonc`：

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

Kilo 也会读取标准的OpenAI环境变量：

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 设置 | 值 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio/claudinio` |
| 工具调用 | 已启用 |