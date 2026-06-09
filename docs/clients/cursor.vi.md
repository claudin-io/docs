# Cursor

[Cursor](https://cursor.com) cho phép bạn thêm một mô hình tương thích với OpenAI thông qua
cài đặt của nó. Claudin.io kết nối thông qua ghi đè URL gốc của OpenAI.

## Thiết lập

1. Mở **Cursor → Settings → Models** (hoặc **Cursor Settings → AI**).
2. Cuộn đến **OpenAI API Key** và mở rộng tùy chọn **Override OpenAI Base URL**.
3. Đặt:

    | Trường | Giá trị |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Trong **Models**, thêm một mô hình tùy chỉnh tên là **`claudinio`** và bật nó lên.
5. Tắt các mô hình mặc định khác nếu bạn muốn Cursor chỉ sử dụng Claudin.io.

!!! note "Các tính năng riêng của Cursor"
    Các tính năng tác nhân của Cursor hoạt động tốt nhất với một mô hình chat tương thích OpenAI.
    `claudinio` hỗ trợ các cuộc gọi công cụ, vì vậy các luồng Composer/Agent hoạt động.
    Một số tính năng độc quyền của Cursor (Tab autocomplete, v.v.) chạy trên các mô hình riêng của Cursor
    và không được định tuyến qua ghi đè nhà cung cấp của bạn.

## Xác minh

Mở một cuộc trò chuyện trong Cursor, chọn **claudinio**, và gửi một tin nhắn. Nếu bạn nhận được
phản hồi, bạn đã thiết lập xong. Nếu không, hãy kiểm tra lại URL gốc kết thúc bằng `/v1` và khóa
được dán mà không có khoảng trắng thừa.

| Cài đặt | Giá trị |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |