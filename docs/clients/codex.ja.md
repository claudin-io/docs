# Codex

[Codex](https://github.com/openai/codex)は、`~/.codex/config.toml`内のカスタムモデルプロバイダーを介して接続します。Claudin.ioは、Codexが期待する`responses`ワイヤーAPIを公開しています。

!!! warning "Codex CLIを使用する"
    これらの設定は**Codex CLI**に適用されます。ホストされているCodexアプリでは、カスタムベースURLを指定できない場合があります。

## 手動セットアップ

これを`~/.codex/config.toml`に追加します：

```toml
model = "claudinio"
model_provider = "claudinio"

[model_providers.claudinio]
name = "Claudinio"
base_url = "https://api.claudin.io/v1"
env_key = "CLAUDINIO_API_KEY"
wire_api = "responses"
```

次に、キーをエクスポートします（名前は上記の`env_key`と一致する必要があります）。最も簡単な方法は、[シェルプロファイルに一度設定する](../getting-started/set-your-key.md)ことです：

```bash
export CLAUDINIO_API_KEY="sk-..."
```

## クイックセットアップ（スクリプト）

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

| 設定 | 値 |
| --- | --- |
| ベースURL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |
| ワイヤーAPI | `responses` |
| キー環境変数 | `CLAUDINIO_API_KEY` |