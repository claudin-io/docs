# API 키 설정

Claudin.io 키를 환경 변수에 **한 번만** 설정하면 이 가이드의 모든 도구가 해당 키를 재사용할 수 있습니다. 각 클라이언트에 수동으로 붙여넣을 필요가 없습니다.

`sk-...` 키는 [대시보드](https://claudin.io/dashboard)에서 가져오세요 ([계정 만들기](account.md) 참조). 그런 다음 셸 프로필에 추가하여 모든 새 터미널에서 사용할 수 있도록 하세요.

## macOS / Linux

=== "zsh (macOS 기본)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

`sk-...`를 실제 키로 바꾸세요. 현재 어떤 셸을 사용 중인지 모르겠다면 `echo $SHELL`을 실행하세요.

## 확인

```bash
echo $CLAUDINIO_API_KEY
```

키가 출력되는 것을 확인할 수 있습니다. 비어 있다면 새 터미널을 열거나 위의 `source` 명령을 다시 실행하세요.

## 이 방법이 도움이 되는 이유

[도구 연결하기](../clients/opencode.md) 섹션의 모든 **빠른 설정** 스크립트는 `$CLAUDINIO_API_KEY`를 읽습니다. 따라서 한 번 내보내기만 하면 모든 스크립트를 그대로 실행할 수 있습니다. `YOUR_API_KEY`를 대체할 필요가 없습니다. 환경 변수를 직접 읽는 도구(Codex의 `env_key`, 모든 OpenAI 호환 CLI)도 자동으로 인식합니다.

!!! warning "키를 비밀번호처럼 취급하세요"
    이 키를 가진 사람은 누구나 요금제 예산을 사용할 수 있습니다. `~/.zshrc` / `~/.bashrc`를 공개 저장소에 커밋하지 마세요. 키가 유출된 경우 대시보드에서 키를 폐기하고 새 키를 내보내세요.

---

키를 내보냈나요? 이제 [첫 번째 호출 만들기](first-call.md)로 가거나 바로 [도구 연결하기](../clients/opencode.md)로 이동하세요.