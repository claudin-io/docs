# OpenCode

[OpenCode](https://opencode.ai) kết nối tới Claudin.io như một nhà cung cấp tương thích với OpenAI. Cách nhanh nhất là sử dụng luồng xác thực tích hợp sẵn.

## Thiết lập nhanh

1. Chạy lệnh đăng nhập:

    ```bash
    opencode auth login
    ```

2. Chọn **Claudinio** làm nhà cung cấp.
3. Dán khóa API của bạn khi được yêu cầu — sao chép từ [bảng điều khiển](https://claudin.io/dashboard) của bạn.

Sau đó khởi động OpenCode và chọn mô hình **claudinio**.

## Phương pháp thay thế bằng biến môi trường

Nếu bạn đã [xuất khóa](../getting-started/set-your-key.md) của mình, OpenCode sẽ tự động nhận các biến OpenAI tiêu chuẩn — không cần phải dán gì cả:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Thiết lập | Giá trị |
| --- | --- |
| URL gốc | `https://api.claudin.io/v1` |
| Mô hình | `claudinio` |
| Nhà cung cấp | Tương thích OpenAI |

---

Gặp vấn đề? Xem [các lỗi thường gặp](../api-reference.md#errors) hoặc [FAQ](../faq.md).