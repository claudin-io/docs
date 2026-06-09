# Zed

[Zed](https://zed.dev) hỗ trợ các nhà cung cấp tương thích OpenAI một cách tự nhiên trong
`language_models.openai_compatible`.

## Thiết lập nhanh (script)

Đầu tiên [xuất khóa của bạn](../getting-started/set-your-key.md) để
`$CLAUDINIO_API_KEY` được thiết lập. Điều này ghi `~/.config/zed/settings.json`, sao lưu
bất kỳ tệp hiện có nào:

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

## Thiết lập thủ công

1. Thêm nhà cung cấp vào `~/.config/zed/settings.json`:

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

2. Mở bảng điều khiển Agent của Zed và dán khóa API của bạn khi được nhắc, hoặc đặt nó làm
   khóa API cho nhà cung cấp **Claudinio**.
3. Chọn **Claudinio** trong bộ chọn mô hình của bảng điều khiển agent.

| Cài đặt | Giá trị |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| Max tokens | `256000` |