# pi

[pi](https://github.com/parallel-web/pi) đọc các provider từ
`~/.pi/agent/models.json`. Claudin.io được đăng ký như một provider
`openai-completions`.

## Thiết lập nhanh (script)

Đầu tiên [xuất key của bạn](../getting-started/set-your-key.md) để
`$CLAUDINIO_API_KEY` được thiết lập. Lệnh này ghi `~/.pi/agent/models.json`, sao lưu
bất kỳ tập tin nào hiện có:

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

Sau đó chạy:

```bash
pi --provider claudinio --model claudinio
```

## Thiết lập thủ công

Đặt nội dung này vào `~/.pi/agent/models.json`:

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

## Phương án thay thế bằng biến môi trường

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Thiết lập | Giá trị |
| --- | --- |
| URL cơ sở | `https://api.claudin.io/v1` |
| Mô hình | `claudinio` |
| Loại API | `openai-completions` |