# OpenCode

[OpenCode](https://opencode.ai) kết nối với Claudin.io như một nhà cung cấp tương thích OpenAI. Cách nhanh nhất là sử dụng luồng xác thực tích hợp sẵn.

## Thiết lập nhanh

1. Chạy lệnh đăng nhập:

    ```bash
    opencode auth login
    ```

2. Chọn **Claudinio** làm nhà cung cấp.
3. Dán khóa API của bạn khi được nhắc — sao chép nó từ [bảng điều khiển](https://claudin.io/dashboard) của bạn.

Sau đó khởi động OpenCode và chọn mô hình **claudinio**.

## Phương án thay thế bằng biến môi trường

Nếu bạn đã [xuất khóa của mình](../getting-started/set-your-key.md), OpenCode sẽ tự động nhận các biến OpenAI tiêu chuẩn — không cần phải dán gì cả:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Cài đặt | Giá trị |
| --- | --- |
| URL gốc | `https://api.claudin.io/v1` |
| Mô hình | `claudinio` |
| Nhà cung cấp | Tương thích OpenAI |

---

Gặp sự cố? Xem [các lỗi thường gặp](../api-reference.md#errors) hoặc [FAQ](../faq.md).