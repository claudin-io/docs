[Hermes Agent](https://github.com/NousResearch/hermes-agent)는 Nous Research가
개발한 오픈소스 터미널 에이전트입니다. OpenAI 호환 엔드포인트를 모두 지원하므로
Claudin.io와 완벽하게 사용할 수 있습니다.

## 마법사로 빠르게 시작하기

활성 Hermes 세션을 종료하고(`Ctrl + C` 또는 `/quit`), 다음을 실행하세요:

```bash
hermes model
```

메뉴에서 **Custom endpoint**를 선택하고 입력하세요:

| 필드 | 값 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | 사용자의 `sk-...` 키 |
| Model name | `claudinio` |

Hermes가 자동으로 `~/.hermes/config.yaml`에 설정을 저장합니다.

테스트:

```bash
hermes
```

## 수동 설정

`~/.hermes/config.yaml`을 편집하세요:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-dangsin-ui-key"
  default: "claudinio"
```

또는 직접 값을 설정하세요:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

확인:

```bash
hermes config check
hermes config show
```

> **팁:** 복잡한 도구 호출 작업의 경우 Hermes Agent가 최소 64K 토큰
> 컨텍스트의 모델을 사용하는지 확인하세요 (Claudinio가 지원합니다).

## 문제 해결

| 문제 | 해결책 |
| --- | --- |
| 인증 오류 | `hermes doctor`로 API 키 확인 |
| 모델을 찾을 수 없음 | 모델 이름이 정확히 `claudinio`인지 확인 |
| 연결 거부 | `https://api.claudin.io/v1`에 접근 가능한지 확인 |

## 유용한 명령어

| 명령어 | 설명 |
| --- | --- |
| `hermes config show` | 현재 설정 보기 |
| `hermes config edit` | 대화형으로 편집 |
| `hermes doctor` | 문제 진단 |
| `hermes model` | 제공자 변경 |
