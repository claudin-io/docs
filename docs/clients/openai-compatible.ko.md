# 모든 OpenAI 호환 클라이언트

Claudin.io는 OpenAI API 표면을 구현하므로 사용자 정의 기본 URL을 설정할 수 있는 **모든** 도구, SDK 또는 라이브러리가 작동합니다. 편집기가 이 섹션에 나열되지 않은 경우 이 일반 설정을 사용하십시오.

## 세 가지 값

| 설정 | 값 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| API key | your `sk-...` key |

대부분의 도구는 Base URL 필드를 *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint*, 또는 *Custom provider URL* 중 하나로 부릅니다. 항상 `/v1` 접미사를 포함하십시오.

## 환경 변수

많은 CLI와 SDK는 표준 OpenAI 변수를 읽습니다. 이것들을 설정하면 완료입니다. [키를 내보냈다면](../getting-started/set-your-key.md), `$CLAUDINIO_API_KEY`를 재사용하십시오:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## 지원되는 엔드포인트

Claudin.io는 다음 OpenAI 스타일 경로를 라우팅합니다:

| 엔드포인트 | 목적 |
| --- | --- |
| `POST /v1/chat/completions` | 채팅 완성 (주요 항목) |
| `POST /v1/completions` | 레거시 텍스트 완성 |
| `POST /v1/messages` | Anthropic 메시지 형식 |
| `POST /v1/responses` | Responses API (Codex에서 사용) |
| `POST /v1/embeddings` | 임베딩 |
| `GET /v1/models` | 사용 가능한 모델 목록 |

## 인증

키를 **다음 중 하나**로 전송하십시오:

```http
Authorization: Bearer YOUR_API_KEY
```

또는

```http
x-api-key: YOUR_API_KEY
```

둘 다 허용됩니다. 클라이언트가 보내는 것을 선택하십시오.

---

전체 [API 참조](../api-reference.md)를 참조하여 요청/응답 세부 정보와 오류 처리를 확인하세요.