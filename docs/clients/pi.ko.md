# pi

[pi](https://github.com/parallel-web/pi)는 `~/.pi/agent/models.json`에서 공급자를 읽습니다. Claudin.io는 `openai-completions` 공급자로 등록되어 있습니다.

## 빠른 설정 (스크립트)

먼저 [키를 내보내](../getting-started/set-your-key.md) `$CLAUDINIO_API_KEY`가 설정되도록 합니다. 이렇게 하면 `~/.pi/agent/models.json`이 작성되며, 기존 파일은 백업됩니다.

```bash
pi_models_install() {
  local key="$1"
  local dir="$HOME/.pi/agent"
  local file="$dir/models.json"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<'JSONEOF'
{
  "providers": {
    "claudinio": {
      "baseUrl": "https://api.claudin.io/v1",
      "api": "openai-completions",
      "apiKey": "__CL_KEY__",
      "models": [
        { "id": "claudinio", "name": "Claudinio", "contextWindow": 256000 }
      ]
    }
  }
}
JSONEOF

  sed -i.bak "s/__CL_KEY__/${key}/g" "$file" && rm -f "$file.bak"
  echo "[ok] Configured: $file"
  echo "[ok] Run: pi --provider claudinio --model claudinio"
}

pi_models_install "$CLAUDINIO_API_KEY"
unset pi_models_install
```

그런 다음 실행:

```bash
pi --provider claudinio --model claudinio
```

## 수동 설정

다음을 `~/.pi/agent/models.json`에 넣으세요:

```json
{
  "providers": {
    "claudinio": {
      "baseUrl": "https://api.claudin.io/v1",
      "api": "openai-completions",
      "apiKey": "YOUR_API_KEY",
      "models": [
        { "id": "claudinio", "name": "Claudinio", "contextWindow": 256000 }
      ]
    }
  }
}
```

## 환경 변수 대안

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 설정 | 값 |
| --- | --- |
| 기본 URL | `https://api.claudin.io/v1` |
| 모델 | `claudinio` |
| API 유형 | `openai-completions` |