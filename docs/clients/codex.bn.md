# Codex

[Codex](https://github.com/openai/codex) `~/.codex/config.toml`-এ একটি কাস্টম মডেল প্রোভাইডারের মাধ্যমে সংযোগ করে। Claudin.io Codex যে `responses` ওয়্যার API আশা করে তা উন্মুক্ত করে।

!!! warning "Codex CLI ব্যবহার করুন"
    এই সেটিংস **Codex CLI**-তে প্রযোজ্য। হোস্টেড Codex অ্যাপ আপনাকে একটি কাস্টম বেস URL নির্দেশ করতে নাও দিতে পারে।

## ম্যানুয়াল সেটআপ

`~/.codex/config.toml`-এ এটি যোগ করুন:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

তারপর আপনার কী এক্সপোর্ট করুন (নামটি অবশ্যই উপরের `env_key`-এর সাথে মিলতে হবে)। সবচেয়ে সহজ উপায় হল [আপনার শেল প্রোফাইলে এটি একবার সেট করা](../getting-started/set-your-key.md):

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
| কী এনভি ভেরিয়েবল | `CLAUDINIO_API_KEY` |