# کوڈیکس

[کوڈیکس](https://github.com/openai/codex) ایک حسب ضرورت ماڈل فراہم کنندہ کے ذریعے `~/.codex/config.toml` میں جڑتا ہے۔ Claudin.io وائر API `responses` کو ظاہر کرتا ہے جس کی توقع کوڈیکس کرتا ہے۔

!!! warning "کوڈیکس CLI استعمال کریں"
    یہ ترتیبات **کوڈیکس CLI** پر لاگو ہوتی ہیں۔ میزبان کوڈیکس ایپ آپ کو کسٹم بیس URL کی طرف اشارہ کرنے کی اجازت نہیں دے سکتی۔

## دستی سیٹ اپ

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

پھر اپنی کلید ایکسپورٹ کریں (نام اوپر `env_key` سے مماثل ہونا چاہیے)۔ سب سے آسان طریقہ یہ ہے کہ [اسے ایک بار اپنے شیل پروفائل میں سیٹ کریں](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## فوری سیٹ اپ (اسکرپٹ)

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
| بیس URL | `https://api.claudin.io/v1` |
| ماڈل | `claudinio` |
| وائر API | `responses` |
| کلیدی ماحولی متغیر | `CLAUDINIO_API_KEY` |