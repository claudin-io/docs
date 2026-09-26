# Tài liệu tham khảo API

Claudin.io là một API **tương thích với OpenAI**. Nếu bạn đã từng dùng API OpenAI,
mọi thứ ở đây đều quen thuộc — chỉ cần trỏ đến base URL của Claudin.io và dùng
model `claudinio`.

## URL gốc

```
https://api.claudin.io
```

Các route kiểu OpenAI nằm dưới `/v1`.

## Xác thực

Gửi API key của bạn kèm theo mọi yêu cầu, ở một trong hai header sau:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Model

| ID model | Cửa sổ ngữ cảnh |
| --- | --- |
| `claudinio` | 256K tokens |

Hãy dùng `claudinio` ở mọi nơi. (Một số client mong đợi dạng `provider/model` — với
những client đó, hãy dùng `claudinio/claudinio`.)

## Các endpoint

| Phương thức & đường dẫn | Mô tả |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions — endpoint chính |
| `POST /v1/completions` | Text completions kế thừa |
| `POST /v1/messages` | Định dạng Anthropic Messages |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Text embeddings |
| `GET /v1/models` | Liệt kê các model khả dụng |

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

Các tham số chuẩn của OpenAI đều được hỗ trợ: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (gọi hàm),
`response_format`, v.v. Có hai tham số có giới hạn đáng để bạn biết trước khi gửi:
[`max_tokens`](#max_tokens-and-reasoning) bị kẹp giữa một mức sàn và một mức trần,
còn [`n`](#multiple-completions-n) phải là `1`.

### `max_tokens` và suy luận {#max_tokens-and-reasoning}

Các model Claudinio suy luận trước khi trả lời, và **các token suy luận được tính
vào `max_tokens`** — cùng một ngân sách bao gồm cả chuỗi suy nghĩ nội bộ lẫn câu
trả lời hiển thị. Do đó, một giá trị `max_tokens` nhỏ có thể bị tiêu gần như toàn
bộ vào suy luận, khiến câu trả lời bị cắt cụt giữa chừng.

Để ngăn điều đó, các giá trị dưới **32000** sẽ tự động được nâng lên 32000. Ở đầu
còn lại, các giá trị trên **393216** sẽ bị hạ xuống 393216 — mức tối đa mà các
model chấp nhận — bởi vì một con số lớn hơn sẽ bị từ chối thẳng thừng thay vì được
coi là "càng nhiều càng tốt". Mọi giá trị nằm giữa hai mốc này đều được truyền qua
nguyên vẹn, và việc bỏ qua tham số này luôn ổn.

`max_tokens` là một mức trần, không phải một khoản đặt trước: bạn chỉ bị tính phí
cho các token thực sự được sinh ra, vì vậy một giá trị rộng rãi không tốn thêm gì.

Nếu bạn phân tích cú pháp đầu ra có cấu trúc (JSON, XML, một định dạng chặt chẽ),
hãy kiểm tra `finish_reason` trước khi phân tích — `"length"` nghĩa là phản hồi đã
chạm giới hạn token và chưa hoàn chỉnh, vì vậy việc phân tích thất bại là điều có
thể dự đoán thay vì là vấn đề model bị lỗi:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Nhiều completions (`n`) {#multiple-completions-n}

Chỉ **`n = 1`** được hỗ trợ. Gửi `n` lớn hơn 1 sẽ trả về `400` kèm
`"code": "unsupported_parameter"`; bỏ qua tham số này luôn an toàn.

Các model Claudinio suy luận trước khi trả lời, và lượt suy luận chỉ tạo ra một
luồng suy nghĩ duy nhất — không có cách nào rẻ để tách nó thành nhiều ứng viên độc
lập, vì vậy phía upstream cũng không cung cấp. Nếu bạn muốn nhiều hơn một ứng viên,
hãy gửi yêu cầu nhiều lần (`temperature` cao hơn sẽ cho bạn sự đa dạng), và lưu ý
rằng mỗi lần gửi đều bị tính phí riêng.

Chúng tôi từ chối `n > 1` thay vì âm thầm trả về một lựa chọn duy nhất: một client
yêu cầu bốn nhưng nhận được một thường sẽ lỗi ở giai đoạn sau, ngay trong mã của
chính nó, mà không có lỗi nào từ phía chúng tôi để giải thích lý do.

### Streaming

Đặt `"stream": true` để nhận các server-sent events theo định dạng streaming của
OpenAI (các khối `data: {...}` được kết thúc bằng `data: [DONE]`).

### Tool / function calling

`claudinio` hỗ trợ tool calls. Truyền `tools` và đọc lại `tool_calls` từ phản hồi,
giống hệt như với API OpenAI. Đây chính là điều giúp nó hoạt động bên trong các
trình soạn thảo agentic như Claude Code, Kilo và Cursor.

### Đầu vào đa phương thức

`claudinio` là một model văn bản, nhưng Claudin.io **xử lý một cách trong suốt**
các khối hình ảnh, âm thanh và video: nếu bạn gửi chúng, proxy sẽ chuyển đổi thành
các mô tả/bản phiên âm văn bản trước khi model nhìn thấy. Bạn không cần làm gì đặc
biệt — chỉ cần gửi các content blocks chuẩn của OpenAI là nó hoạt động.

## Lỗi {#errors}

Các lỗi tuân theo cấu trúc lỗi của OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Trạng thái | Ý nghĩa | Việc cần làm |
| --- | --- | --- |
| `401` | API key không hợp lệ hoặc bị thiếu | Kiểm tra key và header xác thực |
| `403` | Endpoint không được phép | Dùng một trong các đường dẫn `/v1/*` được hỗ trợ |
| `402` | Không có gói đang hoạt động, hoặc ví trống (`code: insufficient_credits`) | [Đăng ký, nạp thêm hoặc đổi gói](https://claudin.io/dashboard) — thử lại sẽ không giúp gì |
| `429` | Bị giới hạn tốc độ, hoặc (chỉ gói cũ) giới hạn theo giờ | Chờ theo header `Retry-After` |
| `400` | Yêu cầu sai định dạng | Kiểm tra JSON / tham số của bạn — xem [`max_tokens`](#max_tokens-and-reasoning) và [`n`](#multiple-completions-n) |
| `5xx` | Sự cố thoáng qua từ upstream/nhà cung cấp | Thử lại với backoff |

!!! info "Chi tiết nhà cung cấp được ẩn đi có chủ đích"
    Các thông báo lỗi được làm sạch để không làm lộ nhà cung cấp model bên dưới.
    Bạn sẽ luôn thấy các lỗi mang thương hiệu Claudin.io và có cấu trúc kiểu OpenAI.

### Ví trống

Khi số dư tín dụng của bạn về không, yêu cầu trả về `402` và
`code: insufficient_credits`:

```json
{ "error": { "message": "Claudinio: Your credit balance is empty. Buy a top-up pack or change plan at https://claudin.io/dashboard — the next month's credits arrive with your next invoice.", "type": "insufficient_credits", "code": "insufficient_credits" } }
```

Không có gì xếp hàng, không có gì bị tính phí. Một gói
[nạp thêm](plans.md#top-ups) hoặc đổi gói có hiệu lực ngay; nếu không, thử lại
sẽ không giúp gì. Không có cửa sổ thời gian nào để chờ — gói tín dụng không có
giới hạn theo giờ.

### Gói cũ: giới hạn theo giờ {#cap-alternative-response}

Các tài khoản ở gói giá cố định trước đây (Essential, Pro, Ultra) giữ giới hạn
theo giờ của gói đó. Ở đó, giới hạn cạn sẽ trả về `429` với header `Retry-After`
cho biết số giây đến khi cửa sổ đặt lại; hãy chờ theo header đó thay vì thử lại
ngay. Trên một số ít tài khoản này, yêu cầu thay vào đó hoàn tất với một phản
hồi nói rằng đã chạm giới hạn — **nếu bạn xây tự động hóa, đừng đọc `2xx` là
"việc đã xong"**; hãy coi phản hồi đó là đã chạm giới hạn.

## Giới hạn tốc độ

Claudin.io không chặn cứng việc sử dụng bình thường. Tốc độ yêu cầu ở mức lạm dụng
sẽ bị *làm chậm lại* (một cơ chế throttle minh bạch) thay vì bị từ chối, vì vậy các
client hoạt động tốt sẽ không bao giờ bị phạt. Trên thực tế, bạn không cần làm gì cả
— chỉ cần thử lại trong trường hợp hiếm gặp `429`.
