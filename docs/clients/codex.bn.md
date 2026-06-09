# Codex

[Codex](https://github.com/openai/codex) একটি কাস্টম মডেল প্রদানকারীর মাধ্যমে `~/.codex/config.toml`-এ সংযোগ করে। Claudin.io `responses` ওয়্যার API উন্মুক্ত করে যা Codex প্রত্যাশা করে।

!!! warning "Codex CLI ব্যবহার করুন"
    এই সেটিংসগুলি **Codex CLI**-তে প্রযোজ্য। হোস্টেড Codex অ্যাপ আপনাকে একটি কাস্টম বেস URL নির্দেশ করতে দিতে পারে না।

## ম্যানুয়াল সেটআপ

এটি `~/.codex/config.toml`-এ যোগ করুন:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

তারপর আপনার কী এক্সপোর্ট করুন (নামটি উপরের `env_key`-এর সাথে মিলতে হবে)। সবচেয়ে সহজ উপায় হল [এটি আপনার শেল প্রোফাইলে একবার সেট করুন](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## দ্রুত সেটআপ (স্ক্রিপ্ট)

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

| সেটিং | মান |
| --- | --- |
| বেস URL | `https://api.claudin.io/v1` |
| মডেল | `claudinio` |
| ওয়্যার API | `responses` |
| কী এনভ ভেরিয়েবল | `CLAUDINIO_API_KEY` |