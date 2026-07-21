# Hermes 에이전트

[Hermes 에이전트](https://github.com/NousResearch/hermes-agent)는 Nous Research의 오픈소스
터미널 AI 에이전트입니다. 모든 OpenAI 호환 엔드포인트를 지원하므로 Claudin.io에 완벽하게 적합합니다.

## 위저드를 사용한 빠른 시작

활성 Hermes 세션을 종료한 후(`Ctrl + C` 또는 `/quit`), 다음을 실행하십시오:

```bash
hermes model
```

메뉴에서 **사용자 정의 엔드포인트**를 선택하고 다음을 입력하세요:

| 필드 | 값 |
| --- | --- |
| 기본 URL | `https://api.claudin.io/v1` |
| API 키 | `sk-...` 키 |
| 모델 이름 | `claudinio` |

Hermes가 자동으로 설정을 `~/.hermes/config.yaml`에 저장합니다.

시도해보세요:

```bash
hermes
```

## 수동 설정

`~/.hermes/config.yaml`을 편집하세요:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

또는 값을 직접 설정하세요:

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

> **팁:** 도구 호출이 포함된 복잡한 작업의 경우, Hermes 에이전트가 최소 64K 토큰 컨텍스트를 가진 모델을 사용하고 있는지 확인하세요(Claudinio는 이를 지원합니다).

## 문제 해결

| 이슈 | 해결 방법 |
| --- | --- |
| 인증 오류 | `hermes doctor`로 API 키를 다시 확인하세요 |
| 모델을 찾을 수 없음 | 모델 이름이 정확히 `claudinio`인지 확인하세요 |
| 연결 거부됨 | 네트워크에서 `https://api.claudin.io/v1`에 연결할 수 있는지 확인하세요 |