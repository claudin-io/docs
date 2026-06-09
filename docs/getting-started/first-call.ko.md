# 첫 번째 호출

편집기를 연결하기 전에, 단일 요청으로 키가 작동하는지 확인하는 것이 좋습니다. Claudin.io는 **OpenAI Chat Completions** 형식(및 Anthropic Messages 형식도)을 지원합니다.

이 예제들은 `$CLAUDINIO_API_KEY`에서 키를 읽습니다 — [키 내보내기](set-your-key.md)를 통해 한 번 설정하세요. (SDK 스니펫에서는 `YOUR_API_KEY`를 [대시보드](account.md)의 키로 바꾸거나, 같은 환경 변수에서 읽어오세요.)

## cURL 사용하기

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

정상적인 OpenAI 스타일 JSON 응답과 `choices` 배열을 받게 됩니다.

!!! tip "`x-api-key`도 작동합니다"
    Claudin.io는 키를 `Authorization: Bearer YOUR_API_KEY` **또는** `x-api-key: YOUR_API_KEY` 헤더로 받습니다. 클라이언트가 보내는 방식을 사용하세요.

## OpenAI Python SDK 사용하기

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

## OpenAI Node SDK 사용하기

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

## 스트리밍

`stream: true`로 설정하고 서버 전송 이벤트를 읽습니다. OpenAI API와 동일합니다:

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

유효한 응답을 받았나요? 좋습니다 — 이제 [자주 사용하는 도구 연결](../clients/claude-code.md)로 넘어가세요. 실패했다면 [API 참조](../api-reference.md#errors)에서 일반적인 오류를 확인하세요.