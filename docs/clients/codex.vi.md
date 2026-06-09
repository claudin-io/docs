# Codex

[Codex](https://github.com/openai/codex) kết nối thông qua một nhà cung cấp mô hình tùy chỉnh trong
`~/.codex/config.toml`. Claudin.io hiển thị `responses` wire API mà Codex mong đợi.

!!! warning "Sử dụng Codex CLI"
    Các cài đặt này áp dụng cho **Codex CLI**. Ứng dụng Codex được lưu trữ có thể không cho phép
    bạn trỏ đến một base URL tùy chỉnh.

## Thiết lập thủ công

Thêm nội dung này vào `~/.codex/config.toml`:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Sau đó export key của bạn (tên phải khớp với `env_key` ở trên). Cách dễ nhất là
[thiết lập nó một lần trong hồ sơ shell của bạn](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Thiết lập nhanh (script)

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

| Thiết lập | Giá trị |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Mô hình | `claudinio` |
| Wire API | `responses` |
| Biến môi trường key | `CLAUDINIO_API_KEY` |