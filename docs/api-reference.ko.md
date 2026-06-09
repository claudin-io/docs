# API 참조

Claudin.io는 **OpenAI 호환** API입니다. OpenAI API를 사용해 보셨다면, 여기 모든 것이 익숙할 것입니다 — Claudin.io 기본 URL을 지정하고 `claudinio` 모델을 사용하기만 하면 됩니다.

## 기본 URL

```
https://api.claudin.io
```

OpenAI 스타일 라우트는 `/v1` 아래에 있습니다.

## 인증

모든 요청에 API 키를 헤더로 보내세요:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## 모델

| 모델 ID | 컨텍스트 창 |
| --- | --- |
| `claudinio` | 256K 토큰 |

모든 곳에서 `claudinio`를 사용하세요. (일부 클라이언트는 `provider/model` 형식을 기대합니다 — 그런 경우 `claudinio/claudinio`를 사용하세요.)

## 엔드포인트

| 메서드 및 경로 | 설명 |
| --- | --- |
| `POST /v1/chat/completions` | 채팅 완성 — 주요 엔드포인트 |
| `POST /v1/completions` | 레거시 텍스트 완성 |
| `POST /v1/messages` | Anthropic Messages 형식 |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | 텍스트 임베딩 |
| `GET /v1/models` | 사용 가능한 모델 목록 |

### 채팅 완성

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

표준 OpenAI 매개변수가 지원됩니다: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (함수 호출), `response_format` 등.

### 스트리밍

`"stream": true`로 설정하면 OpenAI 스트리밍 형식으로 서버 전송 이벤트를 수신합니다 (`data: {...}` 청크가 `data: [DONE]`으로 종료됨).

### 도구 / 함수 호출

`claudinio`는