# Claude Code

[Claude Code](https://claude.com/claude-code) 通过其兼容 Anthropic 的端点连接到 Claudin.io。将其基础 URL 指向 Claudin.io，并使用您的密钥作为身份验证令牌。

## 快速设置（脚本）

首先[导出您的密钥](../getting-started/set-your-key.md)，以便设置 `$CLAUDINIO_API_KEY`，然后运行以下脚本。它会写入 `~/.claude/settings.json`（如有现有文件，会先备份）：

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

然后直接运行 `claude` 即可。

## 手动设置

自行编辑 `~/.claude/settings.json`：

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

!!! note "为什么 `ANTHROPIC_API_KEY` 为空"
    Claude Code 优先使用 `ANTHROPIC_API_KEY`（如果已设置）。将其留空会强制使用 `ANTHROPIC_AUTH_TOKEN`（您的 Claudin.io 密钥）连接到 Claudin.io 基础 URL。

## 使用的值

| 设置 | 值 |
| --- | --- |
| 基础 URL | `https://api.claudin.io` |
| 模型 | `claudinio` |
| 子代理模型 | `claudinio` |
| 身份验证 | `ANTHROPIC_AUTH_TOKEN` = 您的密钥 |

---

遇到问题？请参阅[常见错误](../api-reference.md#errors)或[常见问题](../faq.md)。