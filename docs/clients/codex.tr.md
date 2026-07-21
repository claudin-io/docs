# Codex

[Codex](https://github.com/openai/codex), `~/.codex/config.toml` dosyasında özel bir model sağlayıcısı aracılığıyla bağlanır. Claudin.io, Codex'in beklediği `responses` kablo API'sini sunar.

!!! warning "Codex CLI'yi Kullanın"
    Bu ayarlar **Codex CLI** için geçerlidir. Barındırılan Codex uygulaması, özel bir temel URL'yi işaret etmenize izin vermeyebilir.

## Manuel kurulum

Bunu `~/.codex/config.toml` dosyasına ekleyin:

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

Ardından anahtarınızı dışa aktarın (adı yukarıdaki `env_key` ile eşleşmelidir). En kolay yol, [kabuk profilinize bir kez ayarlamaktır](../getting-started/set-your-key.md):

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## Hızlı kurulum (betik)

```bash
codex_config_install() {
  local key="$1"
  local dir="$HOME/.codex"
  local file="$dir/config.toml"

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    cp "$file" "$file.claudinio.bak"
    echo "[ok] Yedek: $file.claudinio.bak"
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

  echo "[ok] Yapılandırıldı: $file"
  echo "[ok] CLAUDINIO_API_KEY'in kabuğunuzda dışa aktarıldığından emin olun"
}

codex_config_install
unset codex_config_install
```

| Ayar | Değer |
| --- | --- |
| Temel URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| Kablo API | `responses` |
| Anahtar ortam değişkeni | `CLAUDINIO_API_KEY` |