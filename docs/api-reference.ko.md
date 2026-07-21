# API 참조

Claudin.io는 **OpenAI 호환** API입니다. OpenAI API를 사용해본 적이 있다면
여기의 모든 것이 익숙할 것입니다 — Claudin.io 기본 URL을 가리키고
`claudinio` 모델을 사용하기만 하면 됩니다.

## 기본 URL

```
https://api.claudin.io
```

OpenAI 스타일의 라우트는 `/v1` 아래에 있습니다.

## 인증

모든 요청에 API 키를 헤더로 보내세요:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## 모델

| 모델 ID | 컨텍스트 윈도우 |
| --- | --- |
| `claudinio` | 256K 토큰 |

모든 곳에서 `claudinio`를 사용하세요. (일부 클라이언트는 `provider/model` 형식을 기대합니다 — 그런 경우에는 `claudinio/claudinio`를 사용하세요.)

## 엔드포인트

| 메서드 및 경로 | 설명 |
| --- | --- |
| `POST /v1/chat/completions` | 채팅 완성 — 기본 엔드포인트 |
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

표준 OpenAI 파라미터가 지원됩니다: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (함수 호출),
`response_format` 등.

### `max_tokens` 및 추론

Claudinio 모델은 답변하기 전에 추론하며, **추론 토큰은 `max_tokens`에 포함됩니다** — 동일한 예산이 내부 사고 과정과 표시되는 응답을 모두 포함합니다. 따라서 작은 `max_tokens` 값은 거의 전부 추론에 소모되어 응답이 문장 중간에 잘릴 수 있습니다.

이를 방지하기 위해 **4000 미만** 값은 자동으로 4000으로 올라갑니다. 더 큰 값은 그대로 전달되며, 파라미터를 생략해도 항상 괜찮습니다.

구조화된 출력(JSON, XML, 엄격한 형식)을 파싱하는 경우, 파싱 전에 `finish_reason`을 확인하세요 — `"length"`는 응답이 토큰 한도에 도달하여 불완전함을 의미하므로, 모델 문제가 아닌 예상된 파싱 실패입니다:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # 잘렸습니다 — 더 큰 max_tokens로 재시도
data = json.loads(choice.message.content)
```

### 스트리밍

`"stream": true`로 설정하면 OpenAI 스트리밍 형식으로 서버 전송 이벤트를 수신합니다 (`data: {...}` 청크가 `data: [DONE]`으로 종료됨).

### 도구 / 함수 호출

`claudinio`는 도구 호출을 지원합니다. `tools`를 전달하고 응답에서 `tool_calls`를 읽어오세요, 정확히 OpenAI API와 동일합니다. 이것이 Claude Code, Kilo, Cursor와 같은 에이전틱 편집기 내에서 작동하게 하는 기능입니다.

### 멀티모달 입력

`claudinio`는 텍스트 모델이지만, Claudin.io는 이미지, 오디오 및 비디오 블록을 **투명하게 처리**합니다: 이를 보내면 프록시가 모델이 보기 전에 텍스트 설명/전사로 변환합니다. 특별한 작업이 필요하지 않습니다 — 표준 OpenAI 콘텐츠 블록을 보내기만 하면 작동합니다.

## 오류 {#errors}

오류는 OpenAI 오류 형태를 따릅니다:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| 상태 | 의미 | 조치 |
| --- | --- | --- |
| `401` | 유효하지 않거나 누락된 API 키 | 키와 인증 헤더 확인 |
| `403` | 엔드포인트가 허용되지 않음 | 지원되는 `/v1/*` 경로 중 하나 사용 |
| `429` | 예산 한도 도달 또는 속도 제한 | 윈도우 리셋 대기 또는 [업그레이드](plans.md) |
| `400` | 잘못된 요청 | JSON / 파라미터 확인 |
| `5xx` | 업스트림/공급자 문제 | 백오프 후 재시도 |

!!! info "공급자 세부 정보는 의도적으로 숨겨져 있습니다"
    오류 메시지는 정리되어 기본 모델 공급자가 드러나지 않습니다. 항상 Claudin.io 브랜드의 OpenAI 형태 오류를 보게 됩니다.

### 예산 한도 도달

현재 윈도우의 지출 보호를 모두 소진하면 요청이 예산 오류(일반적으로 `429`)를 반환합니다. 대시보드에 정확한 리셋 시간과 남은 예산이 표시됩니다. 윈도우 작동 방식에 대한 자세한 내용은 [요금제 및 한도](plans.md)를 참조하세요.

## 속도 제한

Claudin.io는 정상적인 사용을 강제로 차단하지 않습니다. 남용적인 요청 속도는 거부되지 않고 *느려집니다* (투명한 스로틀링). 따라서 올바르게 동작하는 클라이언트는 불이익을 받지 않습니다. 실제로는 아무것도 할 필요가 없습니다 — 드물게 발생하는 `429`에 대해 재시도만 하면 됩니다.