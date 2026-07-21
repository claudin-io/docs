# Cursor

[Cursor](https://cursor.com) cho phép bạn thêm một mô hình tương thích OpenAI thông qua cài đặt của nó. Claudin.io kết nối thông qua tùy chọn ghi đè Base URL OpenAI.

## Thiết lập

1. Mở **Cursor → Settings → Models** (hoặc **Cursor Settings → AI**).
2. Cuộn đến **OpenAI API Key** và mở rộng tùy chọn **Override OpenAI Base URL**.
3. Thiết lập:

    | Trường | Giá trị |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Dưới **Models**, thêm một mô hình tùy chỉnh có tên **`claudinio`** và bật nó lên.
5. Tắt các mô hình mặc định khác nếu bạn muốn Cursor chỉ sử dụng Claudin.io.

!!! note "Tính năng riêng của Cursor"
    Các tính năng agent của Cursor hoạt động tốt nhất với một mô hình chat tương thích OpenAI.
    `claudinio` hỗ trợ gọi công cụ (tool calls), vì vậy các luồng Composer/Agent hoạt động. Một số
    tính năng độc quyền của Cursor (Tab tự động hoàn thành, v.v.) chạy trên mô hình riêng của Cursor
    và không được định tuyến qua ghi đè nhà cung cấp của bạn.

## Xác minh

Mở một chat trong Cursor, chọn **claudinio**, và gửi một tin nhắn. Nếu bạn nhận được phản hồi, bạn đã sẵn sàng. Nếu không, hãy kiểm tra lại base URL kết thúc bằng `/v1` và khóa (key) được dán không có khoảng trắng thừa.

| Thiết lập | Giá trị |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |