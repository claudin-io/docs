# Claude Code

[Claude Code](https://claude.com/claude-code) kết nối với Claudin.io thông qua endpoint tương thích với Anthropic. Trỏ URL gốc của nó về Claudin.io và sử dụng key của bạn làm mã thông báo xác thực.

## Thiết lập nhanh (script)

Đầu tiên, [export key của bạn](../getting-started/set-your-key.md) để `$CLAUDINIO_API_KEY` được thiết lập, sau đó chạy lệnh sau. Nó sẽ ghi vào `~/.claude/settings.json` (sao lưu bất kỳ tệp nào hiện có trước đó):

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

Sau đó chỉ cần chạy `claude`.

## Thiết lập thủ công

Tự chỉnh sửa `~/.claude/settings.json`:

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

!!! note "Tại sao `ANTHROPIC_API_KEY` lại trống"
    Claude Code ưu tiên sử dụng `ANTHROPIC_API_KEY` nếu nó được thiết lập. Để trống nó sẽ buộc Claude Code sử dụng `ANTHROPIC_AUTH_TOKEN` (key Claudin.io của bạn) với URL gốc Claudin.io.

## Các giá trị được sử dụng

| Thiết lập | Giá trị |
| --- | --- |
| Base URL | `https://api.claudin.io` |
| Model | `claudinio` |
| Subagent model | `claudinio` |
| Xác thực | `ANTHROPIC_AUTH_TOKEN` = key của bạn |

---

Gặp sự cố? Xem [các lỗi thường gặp](../api-reference.md#errors) hoặc [FAQ](../faq.md).