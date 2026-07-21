# Kilo Code

[Kilo Code](https://kilo.ai)는 OpenAI 호환 제공자 블록을 사용합니다. 모델 ID는 `claudinio/claudinio` (제공자/모델)입니다.

## 빠른 설정 (스크립트)

먼저 [키를 내보내세요](../getting-started/set-your-key.md) 그러면 `$CLAUDINIO_API_KEY`가 설정됩니다. 이 작업은 기존 파일을 백업한 후 `~/.config/kilo/kilo.jsonc`를 작성합니다:

```bash
kilo_config_install() {
  local key="$1"
  local dir="$HOME/.config/kilo"
  local file="$dir/kilo.jsonc"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<'JSONCEOF'
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "__CL_KEY__"
      },
      "models": {
        "claudinio": {
          "name": "Claudinio",
          "tool_call": true,
          "limit": { "context": 128000, "output": 16384 }
        }
      }
    }
  }
}
JSONCEOF

  sed -i.bak "s/__CL_KEY__/${key}/g" "$file" && rm -f "$file.bak"
  echo "[ok] Configured: $file"
}

kilo_config_install "$CLAUDINIO_API_KEY"
unset kilo_config_install
```

그런 다음 `kilo`를 실행하세요.

## 수동 설정

이 내용을 `~/.config/kilo/kilo.jsonc`에 넣으세요:

```jsonc
{
  "$schema": "https://app.kilo.ai/config.json",
  "model": "claudinio/claudinio",
  "provider": {
    "claudinio": {
      "name": "Claudinio",
      "options": {
        "baseURL": "https://api.claudin.io/v1",
        "apiKey": "YOUR_API_KEY"
      },
      "models": {
        "claudinio": {
          "name": "Claudinio",
          "tool_call": true,
          "limit": { "context": 128000, "output": 16384 }
        }
      }
    }
  }
}
```

## 환경 변수 대안

Kilo는 표준 OpenAI 환경 변수도 읽습니다:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 설정 | 값 |
| --- | --- |
| 기본 URL | `https://api.claudin.io/v1` |
| 모델 | `claudinio/claudinio` |
| 도구 호출 | 활성화됨 |