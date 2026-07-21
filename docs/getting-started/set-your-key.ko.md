# API 키 설정

Claudin.io 키를 **한 번** 환경 변수로 설정하면 이 가이드의 모든 도구가 이를 재사용할 수 있으므로 각 클라이언트에 수동으로 붙여넣을 필요가 없습니다.

[대시보드](https://claudin.io/dashboard)에서 `sk-...` 키를 가져온 다음 ([계정 만들기](account.md) 참조) 셸 프로필에 추가하여 새 터미널마다 사용할 수 있도록 하세요.

## macOS / Linux

=== "zsh (macOS 기본값)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

`sk-...`를 실제 키로 바꾸세요. 어떤 셸을 사용 중인지 모르겠다면 `echo $SHELL`을 실행하세요.

## 확인

```bash
echo $CLAUDINIO_API_KEY
```

키가 다시 출력되어야 합니다. 비어 있으면 새 터미널을 열거나 위의 `source` 명령을 다시 실행하세요.

## 도움이 되는 이유

[도구 연결](../clients/opencode.md) 섹션의 모든 **빠른 설정** 스크립트는 `$CLAUDINIO_API_KEY`를 읽습니다. 따라서 한 번 내보내면 그대로 실행할 수 있으며, `YOUR_API_KEY`를 바꿀 필요가 없습니다. 환경 변수를 직접 읽는 도구(Codex의 `env_key`, 모든 OpenAI 호환 CLI)도 자동으로 이를 인식합니다.

!!! warning "키를 비밀번호처럼 취급하세요"
    이 키가 있는 사람은 누구나 요금제 예산을 사용할 수 있습니다. `~/.zshrc` / `~/.bashrc`를 공개 저장소에 커밋하지 마세요. 키가 유출된 경우 대시보드에서 취소하고 새 키를 내보내세요.

---

키를 내보냈나요? 이제 [첫 번째 호출](first-call.md)을 하거나 [도구 연결](../clients/opencode.md)로 바로 이동하세요.