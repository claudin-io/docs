# API reference

Claudin.io là một API **tương thích với OpenAI**. Nếu bạn đã từng sử dụng API của OpenAI,
mọi thứ ở đây đều quen thuộc — chỉ cần trỏ đến base URL của Claudin.io và sử dụng
model `claudinio`.

## Base URL

```
https://api.claudin.io
```

Các route theo phong cách OpenAI nằm dưới `/v1`.

## Xác thực

Gửi API key của bạn kèm theo mỗi request, dưới dạng header:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Model

| Model id | Cửa sổ ngữ cảnh |
| --- | --- |
| `claudinio` | 256K token |

Sử dụng `claudinio` ở mọi nơi. (Một số client mong đợi định dạng `provider/model` — đối với
các client đó, hãy sử dụng `claudinio/claudinio`.)

## Endpoint

| Method & path | Mô tả |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions — endpoint chính |
| `POST /v1/completions` | Text completions kế thừa |
| `POST /v1/messages` | Định dạng Messages của Anthropic |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Text embeddings |
| `GET /v1/models` | Danh sách các model khả dụng |

### Chat completions

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],
    "temperature": 0.7
  }'
```

Các tham số tiêu chuẩn của OpenAI được hỗ trợ: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (function calling),
`response_format`, v.v.

### `max_tokens` và khả năng suy luận

Các model Claudinio suy luận trước khi trả lời, và **các token suy luận được tính vào
`max_tokens`** — cùng một ngân sách bao gồm cả chuỗi suy nghĩ nội bộ và
phản hồi hiển thị. Do đó, một giá trị `max_tokens` nhỏ có thể bị tiêu tốn gần như hoàn toàn
vào suy luận, khiến câu trả lời bị cắt ngang giữa chừng.

Để ngăn chặn điều đó, các giá trị dưới **4000** sẽ tự động được nâng lên 4000. Các giá trị
lớn hơn được giữ nguyên, và việc bỏ qua tham số này luôn an toàn.

Nếu bạn phân tích đầu ra có cấu trúc (JSON, XML, một định dạng chặt chẽ), hãy kiểm tra
`finish_reason` trước khi phân tích — `"length"` có nghĩa là phản hồi đã chạm giới hạn
token và chưa hoàn chỉnh, do đó lỗi phân tích là điều dự kiến chứ không phải vấn đề
từ model:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # bị cắt — thử lại với max_tokens lớn hơn
data = json.loads(choice.message.content)
```

### Streaming

Đặt `"stream": true` để nhận các sự kiện do server gửi theo định dạng streaming
của OpenAI (các chunk `data: {...}` kết thúc bằng `data: [DONE]`).

### Gọi tool / function

`claudinio` hỗ trợ gọi tool. Truyền `tools` và đọc `tool_calls` từ
phản hồi, giống hệt như với API của OpenAI. Đây là điều giúp nó hoạt động bên trong
các trình soạn thảo tác nhân như Claude Code, Kilo và Cursor.

### Đầu vào đa phương thức

`claudinio` là một model văn bản, nhưng Claudin.io **xử lý minh bạch** các khối
hình ảnh, âm thanh và video: nếu bạn gửi chúng, proxy sẽ chuyển đổi chúng thành
mô tả/phiên âm văn bản trước khi model nhìn thấy. Bạn không cần làm gì
đặc biệt — chỉ cần gửi các khối nội dung chuẩn của OpenAI và nó hoạt động.

## Lỗi {#errors}

Các lỗi tuân theo cấu trúc lỗi của OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Trạng thái | Ý nghĩa | Cách xử lý |
| --- | --- | --- |
| `401` | API key không hợp lệ hoặc bị thiếu | Kiểm tra key và header xác thực |
| `403` | Endpoint không được phép | Sử dụng một trong các đường dẫn `/v1/*` được hỗ trợ |
| `429` | Đã đạt đến hạn mức ngân sách hoặc bị giới hạn tốc độ | Chờ cho đến khi reset window hoặc [nâng cấp](plans.md) |
| `400` | Request sai định dạng | Kiểm tra JSON / tham số của bạn |
| `5xx` | Trục trặc từ upstream/nhà cung cấp | Thử lại với backoff |

!!! info "Thông tin nhà cung cấp được ẩn theo thiết kế"
    Các thông báo lỗi được làm sạch để không làm lộ nhà cung cấp model
    bên dưới. Bạn sẽ luôn thấy các lỗi có thương hiệu Claudin.io, định dạng OpenAI.

### Chạm hạn mức ngân sách

Khi bạn sử dụng hết bảo vệ chi tiêu của window hiện tại, các request sẽ trả về
lỗi ngân sách (thường là `429`). Bảng điều khiển của bạn hiển thị thời gian reset
chính xác và ngân sách còn lại. Xem [Gói & giới hạn](plans.md) để biết cách các
window hoạt động.

## Giới hạn tốc độ

Claudin.io không chặn cứng việc sử dụng thông thường. Tốc độ request lạm dụng sẽ bị *làm chậm*
(một bộ điều tiết trong suốt) thay vì bị từ chối, vì vậy các client hoạt động tốt sẽ không bao giờ
bị phạt. Trên thực tế, bạn không cần làm gì — chỉ cần thử lại trong trường hợp hiếm gặp
`429`.