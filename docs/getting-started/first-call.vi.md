# Cuộc gọi đầu tiên của bạn

Trước khi kết nối một editor, bạn nên xác nhận key của mình hoạt động với một yêu cầu duy nhất. Claudin.io hỗ trợ định dạng **OpenAI Chat Completions** (và cả định dạng Anthropic Messages nữa).

Các ví dụ này đọc key của bạn từ `$CLAUDINIO_API_KEY` — hãy thiết lập nó một lần bằng cách [xuất key của bạn](set-your-key.md). (Trong các đoạn SDK, hãy thay thế `YOUR_API_KEY` bằng key từ [bảng điều khiển](account.md) của bạn, hoặc đọc nó từ cùng biến môi trường.)

## Với cURL

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLAUDINIO_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "user", "content": "Say hello in one short sentence."}
    ]
  }'
```

Bạn sẽ nhận được phản hồi JSON kiểu OpenAI thông thường với một mảng `choices`.

!!! tip "`x-api-key` cũng hoạt động"
    Claudin.io chấp nhận key dưới dạng `Authorization: Bearer YOUR_API_KEY` **hoặc** dưới dạng header `x-api-key: YOUR_API_KEY`. Sử dụng tùy chọn nào mà client của bạn gửi.

## Với OpenAI Python SDK

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.claudin.io/v1",
    api_key="YOUR_API_KEY",
)

resp = client.chat.completions.create(
    model="claudinio",
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)

print(resp.choices[0].message.content)
```

## Với OpenAI Node SDK

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.claudin.io/v1",
  apiKey: "YOUR_API_KEY",
});

const resp = await client.chat.completions.create({
  model: "claudinio",
  messages: [{ role: "user", content: "Say hello in one short sentence." }],
});

console.log(resp.choices[0].message.content);
```

## Streaming

Đặt `stream: true` và đọc các sự kiện từ server, giống hệt như OpenAI API:

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Authorization: Bearer $CLAUDINIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claudinio",
    "stream": true,
    "messages": [{"role": "user", "content": "Count to five."}]
  }'
```

---

Nhận được phản hồi hợp lệ? Tuyệt vời — bây giờ hãy [kết nối công cụ yêu thích của bạn](../clients/claude-code.md). Nếu có lỗi xảy ra, hãy kiểm tra [tài liệu tham khảo API](../api-reference.md#errors) để biết các lỗi phổ biến.