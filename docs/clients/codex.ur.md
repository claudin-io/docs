# Codex

[Codex](https://github.com/openai/codex) ایک حسب ضرورت ماڈل فراہم کنندہ کے ذریعے `~/.codex/config.toml` میں منسلک ہوتا ہے۔ Claudin.io `responses` وائر API کو ظاہر کرتا ہے جس کی Codex توقع کرتا ہے۔

!!! warning "Codex CLI استعمال کریں"
    یہ ترتیبات **Codex CLI** پر لاگو ہوتی ہیں۔ میزبان Codex ایپ آپ کو ایک حسب ضرورت بنیادی URL کی طرف اشارہ کرنے کی اجازت نہیں دے سکتی ہے۔

## دستی ترتیب

اسے `~/.codex/config.toml` میں شامل کریں:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

پھر اپنی کلید کو ایکسپورٹ کریں (نام اوپر `env_key` سے مماثل ہونا چاہیے)۔ سب سے آسان طریقہ یہ ہے کہ [اسے اپنے شیل پروفائل میں ایک بار سیٹ کریں](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## فوری ترتیب (اسکرپٹ)

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

| ترتیب | قدر |
| --- | --- |
| بنیادی URL | `https://api.claudin.io/v1` |
| ماڈل | `claudinio` |
| وائر API | `responses` |
| کلیدی ماحولیاتی متغیر | `CLAUDINIO_API_KEY` |