# Codex

[Codex](https://github.com/openai/codex) 通过 `~/.codex/config.toml` 中的自定义模型提供程序进行连接。Claudin.io 提供了 Codex 所期望的 `responses` 线路 API。

!!! warning "使用 Codex CLI"
    这些设置适用于 **Codex CLI**。托管的 Codex 应用可能不允许你指向自定义基础 URL。

## 手动设置

将以下内容添加到 `~/.codex/config.toml`：

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

然后导出你的密钥（名称必须与上面的 `env_key` 匹配）。最简单的方法是在你的 shell 配置文件中[设置一次](../getting-started/set-your-key.md)：

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## 快速设置（脚本）

```bash
codex_config_install() {
  local key="$1"
  local dir="$HOME/.codex"
  local file="$dir/config.toml"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<TOMLEOF
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
TOMLEOF

  echo "[ok] Configured: $file"
  echo "[ok] Make sure CLAUDINIO_API_KEY is exported in your shell"
}

codex_config_install
unset codex_config_install
```

| 设置项 | 值 |
| --- | --- |
| 基础 URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio` |
| 线路 API | `responses` |
| 密钥环境变量 | `CLAUDINIO_API_KEY` |