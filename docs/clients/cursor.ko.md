# Cursor

[Cursor](https://cursor.com)를 사용하면 설정을 통해 OpenAI 호환 모델을 추가할 수 있습니다. Claud.inio는 OpenAI 기본 URL 재정의를 통해 연결됩니다.

## 설정

1. **Cursor → 설정 → 모델** (또는 **Cursor 설정 → AI**)을 엽니다.
2. **OpenAI API 키**로 스크롤한 후 **OpenAI 기본 URL 재정의** 옵션을 펼칩니다.
3. 다음을 입력합니다:

    | 필드 | 값 |
    | --- | --- |
    | OpenAI API 키 | `YOUR_API_KEY` |
    | 기본 URL | `https://api.claudin.io/v1` |

4. **모델** 아래에서 사용자 정의 모델 **`claudinio`** 를 추가하고 활성화합니다.
5. Cursor가 Claud.inio만 사용하도록 하려면 다른 기본 모델을 비활성화합니다.

!!! note "Cursor 자체 기능"
    Cursor의 에이전트 기능은 OpenAI 호환 채팅 모델에서 가장 잘 작동합니다.
    `claudinio`는 도구 호출을 지원하므로 Composer/Agent 흐름이 정상 작동합니다.
    일부 Cursor 고유 기능(탭 자동 완성 등)은 Cursor 자체 모델에서 실행되며
    제공자 재정의를 통해 라우팅되지 않습니다.

## 확인

Cursor에서 채팅을 열고 **claudinio**를 선택한 후 메시지를 보냅니다. 응답이 오면 설정이 완료된 것입니다. 그렇지 않으면 기본 URL이 `/v1`로 끝나는지, 키에 추가 공백 없이 붙여넣어졌는지 확인하세요.

| 설정 | 값 |
| --- | --- |
| 기본 URL | `https://api.claudin.io/v1` |
| 모델 | `claudinio` |