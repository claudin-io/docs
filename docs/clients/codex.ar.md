# Codex

يتصل [Codex](https://github.com/openai/codex) عبر مزود نموذج مخصص في `~/.codex/config.toml`. يعرض Claudin.io واجهة برمجة التطبيقات السلكية `responses` التي يتوقعها Codex.

!!! warning "استخدم سطر أوامر Codex"
    تنطبق هذه الإعدادات على **سطر أوامر Codex**. قد لا يسمح لك تطبيق Codex المستضاف بتوجيه عنوان URL أساسي مخصص.

## الإعداد اليدوي

أضف هذا إلى `~/.codex/config.toml`:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

ثم قم بتصدير مفتاحك (يجب أن يتطابق الاسم مع `env_key` أعلاه). أسهل طريقة هي [تعيينه مرة واحدة في ملف شيل الخاص بك](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## الإعداد السريع (نص برمجي)

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

| الإعداد | القيمة |
| --- | --- |
| عنوان URL الأساسي | `https://api.claudin.io/v1` |
| النموذج | `claudinio` |
| واجهة برمجة التطبيقات السلكية | `responses` |
| متغير البيئة للمفتاح | `CLAUDINIO_API_KEY` |