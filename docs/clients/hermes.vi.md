# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) là một tác nhân AI terminal mã nguồn mở của Nous Research. Nó hỗ trợ mọi endpoint tương thích với OpenAI, khiến nó trở thành lựa chọn hoàn hảo cho Claudin.io.

## Bắt đầu nhanh với trình hướng dẫn

Thoát khỏi mọi phiên Hermes đang hoạt động (`Ctrl + C` hoặc `/quit`), sau đó chạy:

```bash
hermes model
```

Chọn **Custom endpoint** từ menu và điền:

| Trường | Giá trị |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | khóa `sk-...` của bạn |
| Tên mô hình | `claudinio` |

Hermes tự động lưu cấu hình vào `~/.hermes/config.yaml`.

Thử ngay:

```bash
hermes
```

## Cấu hình thủ công

Sửa `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

Hoặc đặt giá trị trực tiếp:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Xác minh:

```bash
hermes config check
hermes config show
```

> **Mẹo:** Đối với các tác vụ phức tạp có gọi công cụ, hãy đảm bảo Hermes Agent của bạn đang sử dụng mô hình có ít nhất ngữ cảnh 64K token (Claudinio hỗ trợ điều này).

## Khắc phục sự cố

| Sự cố | Cách khắc phục |
| --- | --- |
| Lỗi xác thực | Kiểm tra lại API key của bạn bằng `hermes doctor` |
| Không tìm thấy mô hình | Đảm bảo tên mô hình chính xác là `claudinio` |
| Kết nối bị từ chối | Xác minh `https://api.claudin.io/v1` có thể truy cập được từ mạng của bạn |