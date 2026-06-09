# Bất kỳ client tương thích với OpenAI nào

Claudin.io triển khai bề mặt API của OpenAI, vì vậy **bất kỳ** công cụ, SDK hoặc thư viện nào cho phép bạn đặt URL cơ sở tùy chỉnh đều hoạt động. Nếu trình soạn thảo của bạn không được liệt kê trong phần này, hãy sử dụng các cài đặt chung này.

## Ba giá trị

| Thiết lập | Giá trị |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| API key | khóa `sk-...` của bạn |

Hầu hết các công cụ gọi trường Base URL bằng một trong các tên: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint*, hoặc *Custom provider URL*. Luôn bao gồm hậu tố `/v1`.

## Biến môi trường

Nhiều CLI và SDK đọc các biến OpenAI tiêu chuẩn — thiết lập chúng là xong. Nếu bạn đã [xuất khóa của bạn](../getting-started/set-your-key.md), hãy sử dụng lại `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Các điểm cuối được hỗ trợ

Claudin.io định tuyến các đường dẫn kiểu OpenAI sau:

| Điểm cuối | Mục đích |
| --- | --- |
| `POST /v1/chat/completions` | Hoàn thiện trò chuyện (chính) |
| `POST /v1/completions` | Hoàn thiện văn bản kế thừa |
| `POST /v1/messages` | Định dạng Anthropic Messages |
| `POST /v1/responses` | API Responses (được Codex sử dụng) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Liệt kê các mô hình có sẵn |

## Xác thực

Gửi khóa của bạn dưới **một trong hai** dạng:

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