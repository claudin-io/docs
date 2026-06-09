# pi

[pi](https://github.com/parallel-web/pi) 从 `~/.pi/agent/models.json` 读取提供商。Claudin.io 已注册为一个 `openai-completions` 提供商。

## 快速设置（脚本）

首先[导出你的密钥](../getting-started/set-your-key.md)从而设置 `$CLAUDINIO_API_KEY`。这将写入 `~/.pi/agent/models.json`，并备份任何已存在的文件：

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

然后运行：

```bash
pi --provider claudinio --model claudinio
```

## 手动设置

将以下内容放入 `~/.pi/agent/models.json` 中：

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

## 环境变量替代方案

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 设置 | 值 |
| --- | --- |
| 基础 URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio` |
| API 类型 | `openai-completions` |