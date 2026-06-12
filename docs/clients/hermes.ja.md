[Hermes Agent](https://github.com/NousResearch/hermes-agent) は Nous Research
によるオープンソースのターミナルエージェントです。OpenAI 互換のエンドポイントを
すべてサポートしており、Claudin.io に最適です。

## ウィザードを使ったクイックスタート

アクティブな Hermes セッションを終了し（`Ctrl + C` または `/quit`）、次を実行します：

```bash
hermes model
```

メニューから **Custom endpoint** を選択し、以下を入力します：

| フィールド | 値 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | あなたの `sk-...` キー |
| Model name | `claudinio` |

Hermes は設定を自動的に `~/.hermes/config.yaml` に保存します。

試してみてください：

```bash
hermes
```

## 手動設定

`~/.hermes/config.yaml` を編集します：

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-anata-no-key"
  default: "claudinio"
```

または直接値を設定します：

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

確認：

```bash
hermes config check
hermes config show
```

> **ヒント：** 複雑なツール呼び出しタスクでは、Hermes Agent が少なくとも
> 64K トークンのコンテキストを持つモデルを使用していることを確認してください
>（Claudinio はこれをサポートしています）。

## トラブルシューティング

| 問題 | 解決策 |
| --- | --- |
| 認証エラー | `hermes doctor` で API キーを確認 |
| モデルが見つからない | モデル名が正確に `claudinio` であることを確認 |
| 接続拒否 | `https://api.claudin.io/v1` がアクセス可能か確認 |

## 便利なコマンド

| コマンド | 説明 |
| --- | --- |
| `hermes config show` | 現在の設定を表示 |
| `hermes config edit` | インタラクティブに編集 |
| `hermes doctor` | 問題を診断 |
| `hermes model` | プロバイダーを切り替え |
