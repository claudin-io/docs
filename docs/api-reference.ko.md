# API 참조

Claudin.io는 **OpenAI 호환** API입니다. OpenAI API를 사용해 본 적이 있다면 여기의 모든 것이 익숙할 것입니다. Claudin.io 기본 URL을 지정하고 `claudinio` 모델을 사용하기만 하면 됩니다.

## 기본 URL

```
https://api.claudin.io
```

OpenAI 스타일 라우트는 `/v1` 아래에 있습니다.

## 인증

모든 요청에 API 키를 다음 헤더 중 하나로 보내세요:

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

어디서나 `claudinio`를 사용하세요. (일부 클라이언트는 `provider/model` 형식을 기대합니다. 그런 경우 `claudinio/claudinio`를 사용하세요.)

## 엔드포인트

| 메서드 및 경로 | 설명 |
| --- | --- |
| `POST /v1/chat/completions` | 채팅 완성 — 기본 엔드포인트 |
| `POST /v1/completions` | 레거시 텍스트 완성 |
| `POST /v1/messages` | Anthropic Messages 형식 |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | 텍스트 임베딩 |
| `GET /v1/models` | 사용 가능한 모델 나열 |

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

표준 OpenAI 매개변수가 지원됩니다: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (함수 호출), `response_format` 등. 그중 두 가지는 보내기 전에 알아두어야 할 제한이 있습니다: [`max_tokens`](#max_tokens-and-reasoning)는 최소값과 최대값 사이로 제한되며, [`n`](#multiple-completions-n)은 `1`이어야 합니다.

### `max_tokens` 및 추론 {#max_tokens-and-reasoning}

Claudinio 모델은 답변하기 전에 추론하며, **추론 토큰은 `max_tokens`에 포함됩니다** — 동일한 예산이 내부 사고 과정과 표시되는 답변을 모두 포함합니다. 따라서 작은 `max_tokens` 값은 거의 전부 추론에 소진되어 답변이 문장 중간에서 잘릴 수 있습니다.

이를 방지하기 위해 **4000** 미만의 값은 자동으로 4000으로 올려집니다. 반대로 **393216**을 초과하는 값은 모델이 허용하는 최대값인 393216으로 낮춰집니다. 더 큰 숫자는 "원하는 만큼"으로 처리되지 않고 즉시 거부되기 때문입니다. 두 값 사이의 값은 변경 없이 그대로 전달되며, 매개변수를 생략해도 항상 괜찮습니다.

`max_tokens`는 예약이 아닌 상한선입니다: 실제 생성된 토큰에 대해서만 비용이 청구되므로 넉넉한 값은 추가 비용이 들지 않습니다.

구조화된 출력(JSON, XML, 엄격한 형식)을 파싱하는 경우 파싱 전에 `finish_reason`을 확인하세요 — `"length"`는 응답이 토큰 한도에 도달하여 불완전하다는 뜻이므로, 파싱 실패는 모델 문제가 아니라 예상된 결과입니다:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### 다중 완성 (`n`) {#multiple-completions-n}

**`n = 1`**만 지원됩니다. 1보다 큰 `n`을 보내면 `400`과 함께 `"code": "unsupported_parameter"`가 반환됩니다. 매개변수를 생략해도 항상 안전합니다.

Claudinio 모델은 답변하기 전에 추론하며, 추론 과정은 단 하나의 사고 경로를 생성합니다. 이를 여러 독립적인 후보로 분기할 수 있는 저렴한 방법이 없으므로 업스트림에서도 제공하지 않습니다. 둘 이상의 후보가 필요하면 요청을 여러 번 보내세요(더 높은 `temperature`는 다양한 결과를 제공합니다). 각 요청은 별도로 청구됩니다.

우리는 단일 결과를 조용히 반환하는 대신 `n > 1`을 거부합니다. 네 개를 요청하고 하나를 받은 클라이언트는 일반적으로 나중에 자체 코드 내부에서 실패하며, 그 이유를 설명해 줄 오류도 받지 못합니다.

### 스트리밍

OpenAI 스트리밍 형식으로 서버 전송 이벤트를 수신하려면 `"stream": true`로 설정하세요(`data: {...}` 청크는 `data: [DONE]`로 종료됩니다).

### 도구 / 함수 호출

`claudinio`는 도구 호출을 지원합니다. OpenAI API에서와 동일하게 `tools`를 전달하고 응답에서 `tool_calls`를 읽어오면 됩니다. 이것이 Claude Code, Kilo, Cursor 같은 에이전트형 편집기에서 작동하는 이유입니다.

### 멀티모달 입력

`claudinio`는 텍스트 모델이지만 Claudin.io는 이미지, 오디오, 비디오 블록을 **투명하게 처리합니다**: 전송하면 프록시가 모델이 보기 전에 이를 텍스트 설명/전사로 변환합니다. 특별한 작업은 필요 없습니다 — 표준 OpenAI 콘텐츠 블록을 보내기만 하면 됩니다.

## 오류 {#errors}

오류는 OpenAI 오류 형식을 따릅니다:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| 상태 | 의미 | 조치 |
| --- | --- | --- |
| `401` | API 키가 잘못되었거나 누락됨 | 키와 인증 헤더를 확인하세요 |
| `403` | 엔드포인트가 허용되지 않음 | 지원되는 `/v1/*` 경로 중 하나를 사용하세요 |
| `402` | 활성 구독 없음 | [구독하기](https://claudin.io/dashboard) — 재시도해도 소용없습니다 |
| `429` | 예산 한도 도달 또는 속도 제한 | 윈도우 초기화를 기다리거나(`Retry-After` 헤더 참조) [업그레이드](plans.md)하세요 |
| `400` | 잘못된 형식의 요청 | JSON / 매개변수를 확인하세요 — [`max_tokens`](#max_tokens-and-reasoning) 및 [`n`](#multiple-completions-n) 참조 |
| `5xx` | 업스트림/공급자 일시적 오류 | 백오프를 적용하여 재시도하세요 |

!!! info "공급자 세부 정보는 설계상 숨겨져 있습니다"
    오류 메시지는 내부 모델 공급자가 드러나지 않도록 정화됩니다. 항상 Claudin.io 브랜드의 OpenAI 형식 오류가 표시됩니다.

### 예산 한도에 도달한 경우

현재 윈도우의 지출 보호 한도를 모두 사용하면 요청은 `429`를 반환하며 `Retry-After` 헤더에 윈도우가 초기화될 때까지의 초가 표시됩니다. 대시보드에서 정확한 초기화 시간과 남은 예산을 확인할 수 있습니다. 즉시 재시도하는 대신 해당 헤더에 따라 대기하세요. 윈도우 작동 방식은 [요금제 및 한도](plans.md)를 참조하세요.

### `429` 대신 메시지를 받는 경우 {#cap-alternative-response}

소수의 계정에서 같은 상황에 대한 다른 응답을 시험하고 있습니다. 오류 대신 요청이
정상적으로 완료되고, 응답 본문이 직접 상한에 도달했다는 사실과 재설정 시점을
설명합니다. 에이전트가 조용히 삼켜 버리는 오류보다 이 방식이 사람에게 더 확실히
전달되는지, 그리고 분명히 알렸을 때 알맞은 요금제로 옮기고 싶어 하는지를 측정하고
있습니다.

**자동화를 만들고 있다면 `2xx`를 "작업이 처리됨"으로 읽지 마세요.** 상한에
도달했다고 말하는 응답은 실제로 상한에 도달한 것으로 처리하고, 창이 재설정될
때까지 기다리세요. 위의 `429`는 여전히 기본 동작이며 거의 모든 계정이 받는 응답
입니다.

## 속도 제한

Claudin.io는 정상적인 사용을 강제로 차단하지 않습니다. 과도한 요청 속도는 거부되는 대신 *지연*됩니다(투명한 스로틀). 따라서 정상적으로 동작하는 클라이언트는 불이익을 받지 않습니다. 실제로 특별히 할 일은 없습니다 — 드물게 발생하는 `429`에 대해 재시도만 하면 됩니다.
