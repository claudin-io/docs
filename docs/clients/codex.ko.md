# Codex

[Codex](https://github.com/openai/codex)는 `~/.codex/config.toml`에서 사용자 정의 모델 제공자를 통해 연결됩니다. Claudin.io는 Codex가 기대하는 `responses` wire API를 노출합니다.

!!! warning "Codex CLI 사용"
    이 설정은 **Codex CLI**에 적용됩니다. 호스팅된 Codex 앱에서는 사용자 정의 기본 URL을 지정하지 못할 수 있습니다.

## 수동 설정

다음을 `~/.codex/config.toml`에 추가하세요:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

그런 다음 키를 내보내세요 (이름은 위의 `env_key`와 일치해야 합니다). 가장 쉬운 방법은 [셸 프로필에 한 번 설정](../getting-started/set-your-key.md)하는 것입니다:

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## 빠른 설정 (스크립트)

```bash
codex_config_install() {
  local key="$1"
  local dir="$HOME/.codex"
  local file="$dir/config.toml"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<TOMLEOF
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
TOMLEOF

  echo "[ok] Configured: $file"
  echo "[ok] Make sure CLAUDINIO_API_KEY is exported in your shell"
}

codex_config_install
unset codex_config_install
```

| 설정 | 값 |
| --- | --- |
| 기본 URL | `https://api.claudin.io/v1` |
| 모델 | `claudinio` |
| 와이어 API | `responses` |
| 키 환경 변수 | `CLAUDINIO_API_KEY` |