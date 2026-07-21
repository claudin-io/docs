# Bất kỳ client tương thích OpenAI nào

Claudin.io triển khai bề mặt API OpenAI, vì vậy **bất kỳ** công cụ, SDK hoặc thư viện nào cho phép bạn đặt URL cơ sở tùy chỉnh đều hoạt động. Nếu trình soạn thảo của bạn không được liệt kê trong phần này, hãy sử dụng các cài đặt chung này.

## Ba giá trị

| Cài đặt | Giá trị |
| --- | --- |
| URL cơ sở | `https://api.claudin.io/v1` |
| Mô hình | `claudinio` |
| Khóa API | khóa `sk-...` của bạn |

Hầu hết các công cụ gọi trường URL cơ sở là một trong: *URL cơ sở*, *API Base*, *URL cơ sở OpenAI*, *Endpoint* hoặc *URL nhà cung cấp tùy chỉnh*. Luôn bao gồm hậu tố `/v1`.

## Biến môi trường

Nhiều CLI và SDK đọc các biến OpenAI tiêu chuẩn — hãy thiết lập chúng và bạn đã xong. Nếu bạn đã [xuất khóa của mình](../getting-started/set-your-key.md), hãy dùng lại `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Các endpoint được hỗ trợ

Claudin.io định tuyến các đường dẫn kiểu OpenAI sau:

| Endpoint | Mục đích |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions (chính) |
| `POST /v1/completions` | Hoàn tất văn bản kế thừa |
| `POST /v1/messages` | Định dạng Anthropic Messages |
| `POST /v1/responses` | API Responses (dùng bởi Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Liệt kê các mô hình khả dụng |

## Xác thực

Gửi khóa của bạn dưới dạng **một trong hai**:

```http
Authorization: Bearer YOUR_API_KEY
```

hoặc

```http
x-api-key: YOUR_API_KEY
```

Cả hai đều được chấp nhận — hãy chọn bất kỳ cái nào mà client của bạn gửi.

---

Xem [tài liệu tham khảo API](../api-reference.md) đầy đủ để biết chi tiết yêu cầu/phản hồi và xử lý lỗi.