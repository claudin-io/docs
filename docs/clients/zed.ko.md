# Zed

[Zed](https://zed.dev)는 `language_models.openai_compatible` 아래에서 OpenAI 호환 제공자를 기본적으로 지원합니다.

## 빠른 설정 (스크립트)

먼저 [키를 내보내고](../getting-started/set-your-key.md) `$CLAUDINIO_API_KEY`가 설정되었는지 확인하세요. 이 스크립트는 `~/.config/zed/settings.json`에 작성하며, 기존 파일이 있으면 백업합니다:

```bash
zed_settings_install() {
  local key="$1"
  local config_dir="$HOME/.config/zed"
  local file="$config_dir/settings.json"

  mkdir -p "$config_dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Backup: $file.claudinio.bak"
  fi

  cat > "$file" <<JSONEOF
{
  "language_models": {
    "openai_compatible": {
      "Claudinio": {
        "api_url": "https://api.claudin.io/v1",
        "available_models": [
          {
            "name": "claudinio",
            "display_name": "Claudinio",
            "max_tokens": 256000
          }
        ]
      }
    }
  }
}
JSONEOF

  echo "[ok] Configured: $file"
}

zed_settings_install "$CLAUDINIO_API_KEY"
unset zed_settings_install
```

## 수동 설정

1. `~/.config/zed/settings.json`에 제공자를 추가합니다:

    ```json
    {
      "language_models": {
        "openai_compatible": {
          "Claudinio": {
            "api_url": "https://api.claudin.io/v1",
            "available_models": [
              {
                "name": "claudinio",
                "display_name": "Claudinio",
                "max_tokens": 256000
              }
            ]
          }
        }
      }
    }
    ```

2. Zed의 Agent 패널을 열고 메시지가 나타나면 API 키를 붙여넣거나, **Claudinio** 제공자의 API 키로 설정하세요.
3. Agent 패널의 모델 선택기에서 **Claudinio**를 선택하세요.

| 설정 | 값 |
| --- | --- |
| API URL | `https://api.claudin.io/v1` |
| 모델 | `claudinio` |
| 최대 토큰 수 | `256000` |