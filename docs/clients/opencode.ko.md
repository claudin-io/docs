# OpenCode

[OpenCode](https://opencode.ai)는 Claudin.io를 OpenAI 호환 공급자로 연결합니다. 가장 빠른 방법은 내장 인증 흐름입니다.

## 빠른 설정

1. 로그인 명령을 실행하세요:

    ```bash
    opencode auth login
    ```

2. 제공자로 **Claudinio**를 선택하세요.
3. 메시지가 나타나면 API 키를 붙여넣으세요 — [대시보드](https://claudin.io/dashboard)에서 복사하세요.

그런 다음 OpenCode를 시작하고 **claudinio** 모델을 선택하세요.

## 환경 변수 대안

이미 [키를 내보냈다면](../getting-started/set-your-key.md), OpenCode는 표준 OpenAI 변수를 자동으로 인식합니다 — 아무것도 붙여넣을 필요가 없습니다:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 설정 | 값 |
| --- | --- |
| 기본 URL | `https://api.claudin.io/v1` |
| 모델 | `claudinio` |
| 제공자 | OpenAI 호환 |

---

문제가 있나요? [일반 오류](../api-reference.md#errors) 또는 [FAQ](../faq.md)를 참조하세요.