# Tham khảo API

Claudin.io là một **API tương thích với OpenAI**. Nếu bạn đã từng sử dụng OpenAI API, mọi thứ ở đây đều quen thuộc — chỉ cần trỏ đến URL gốc của Claudin.io và sử dụng mô hình `claudinio`.

## URL gốc

```
https://api.claudin.io
```

Các đường dẫn kiểu OpenAI nằm dưới `/v1`.

## Xác thực

Gửi khóa API của bạn trong mỗi yêu cầu, dưới dạng một trong các header sau:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Mô hình

| Mã mô hình | Cửa sổ ngữ cảnh |
| --- | --- |
| `claudinio` | 256K tokens |

Sử dụng `claudinio` ở mọi nơi. (Một số máy khách mong đợi định dạng `provider/model` — đối với những máy khách đó, hãy sử dụng `claudinio/claudinio`.)

## Điểm cuối

| Phương thức & đường dẫn | Mô tả |
| --- | --- |
| `POST /v1/chat/completions` | Hoàn thiện trò chuyện — điểm cuối chính |
| `POST /v1/completions` | Hoàn thiện văn bản kế thừa |
| `POST /v1/messages` | Định dạng Anthropic Messages |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Nhúng văn bản |
| `GET /v1/models` | Liệt kê các mô hình khả dụng |

### Hoàn thiện trò chuyện

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a ha