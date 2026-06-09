# Claude Code

[Claude Code](https://claude.com/claude-code)는 Anthropic 호환 엔드포인트를 통해 Claudin.io에 연결됩니다. 기본 URL을 Claudin.io로 설정하고 인증 토큰으로 당신의 키를 사용하세요.

## 빠른 설정 (스크립트)

먼저 [키를 내보내기](../getting-started/set-your-key.md)하여 `$CLAUDINIO_API_KEY`가 설정되도록 한 다음, 이 스크립트를 실행하세요. 이 스크립트는 `~/.claude/settings.json` 파일을 작성합니다 (기존 파일이 있으면 먼저 백업합니다):

```bash
claude_settings_install() {
  local key="$1"
  local dir="$HOME/.claude"
  local file="$dir/settings.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "${key}",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

claude_settings_install "$CLAUDINIO_API_KEY"
unset claude_settings_install
```

그런 다음 `claude`를 실행하기만 하면 됩니다.

## 수동 설정

직접 `~/.claude/settings.json`를 편집하세요:

```json
{
  "model": "claudinio",
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.claudin.io",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claudinio",
    "ANTHROPIC_API_KEY": ""
  }
}
```

!!! note "`ANTHROPIC_API_KEY`가 비어 있는 이유"
    Claude Code는 설정된 경우 `ANTHROPIC_API_KEY`를 선호합니다. 이를 비워두면 Claudin.io 기본 URL에 대해 `ANTHROPIC_AUTH_TOKEN` (당신의 Claudin.io 키)을 사용하도록 강제합니다.

## 사용된 값

| 설정 | 값 |
| --- | --- |
| 기본 URL | `https://api.claudin.io` |
| 모델 | `claudinio` |
| 서브에이전트 모델 | `claudinio` |
| 인증 | `ANTHROPIC_AUTH_TOKEN` = 당신의 키 |

---

문제가 있나요? [일반 오류](../api-reference.md#errors) 또는 [FAQ](../faq.md)를 참조하세요.