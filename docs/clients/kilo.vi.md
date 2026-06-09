# Kilo Code

[Kilo Code](https://kilo.ai) sử dụng khối nhà cung cấp tương thích OpenAI. ID mô hình là `claudinio/claudinio` (nhà cung cấp/mô hình).

## Thiết lập nhanh (script)

Đầu tiên [xuất khóa của bạn](../getting-started/set-your-key.md) để `$CLAUDINIO_API_KEY` được thiết lập. Điều này ghi `~/.config/kilo/kilo.jsonc`, sao lưu bất kỳ tệp hiện có nào:

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

Sau đó chạy `kilo`.

## Thiết lập thủ công

Đặt nội dung này vào `~/.config/kilo/kilo.jsonc`:

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

## Thay thế bằng biến môi trường

Kilo cũng đọc các biến môi trường OpenAI tiêu chuẩn:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Thiết lập | Giá trị |
| --- | --- |
| URL cơ sở | `https://api.claudin.io/v1` |
| Mô hình | `claudinio/claudinio` |
| Gọi công cụ | được bật |