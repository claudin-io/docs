[Hermes Agent](https://github.com/NousResearch/hermes-agent) là một tác nhân
terminal mã nguồn mở của Nous Research. Nó hỗ trợ mọi endpoint tương thích
với OpenAI, rất phù hợp để sử dụng với Claudin.io.

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
| Model name | `claudinio` |

Hermes tự động lưu cấu hình vào `~/.hermes/config.yaml`.

Dùng thử:

```bash
hermes
```

## Cấu hình thủ công

Sửa `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-khoa-cua-ban"
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

> **Mẹo:** Đối với các tác vụ phức tạp có gọi công cụ, hãy đảm bảo Hermes
> Agent của bạn sử dụng mô hình có ít nhất 64K token ngữ cảnh (Claudinio hỗ trợ điều này).

## Xử lý sự cố

| Vấn đề | Giải pháp |
| --- | --- |
| Lỗi xác thực | Kiểm tra khóa API với `hermes doctor` |
| Không tìm thấy mô hình | Đảm bảo tên mô hình chính xác là `claudinio` |
| Kết nối bị từ chối | Xác minh `https://api.claudin.io/v1` có thể truy cập được |

## Lệnh hữu ích

| Lệnh | Mô tả |
| --- | --- |
| `hermes config show` | Xem cấu hình hiện tại |
| `hermes config edit` | Chỉnh sửa tương tác |
| `hermes doctor` | Chẩn đoán sự cố |
| `hermes model` | Chuyển đổi nhà cung cấp |
