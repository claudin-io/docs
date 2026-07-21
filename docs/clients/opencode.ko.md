# OpenCode

[OpenCode](https://opencode.ai)는 Claudin.io에 OpenAI 호환 제공자로 연결됩니다. 가장 빠른 방법은 내장 인증 흐름입니다.

## 빠른 설정

1. 로그인 명령어를 실행하세요:

    ```bash
    opencode auth login
    ```

2. **Claudinio**를 제공자로 선택하세요.
3. API 키를 입력하라는 메시지가 표시되면 붙여넣으세요 — [대시보드](https://claudin.io/dashboard)에서 복사합니다.

그런 다음 OpenCode를 시작하고 **claudinio** 모델을 선택하세요.

## 환경 변수 대안

이미 [키를 내보냈다면](../getting-started/set-your-key.md), OpenCode는 표준 OpenAI 변수를 인식합니다 — 아무것도 붙여넣을 필요가 없습니다:

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