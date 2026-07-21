# Hermes エージェント

[Hermes Agent](https://github.com/NousResearch/hermes-agent) は、Nous Research によるオープンソースのターミナル AI エージェントです。OpenAI 互換のエンドポイントをサポートしており、Claudin.io に最適です。

## ウィザードを使用したクイックスタート

アクティブな Hermes セッションを終了して（`Ctrl + C` または `/quit`）、次のコマンドを実行します：

```bash
hermes model
```

メニューから **カスタムエンドポイント** を選択し、次の項目を入力します：

| フィールド | 値 |
| --- | --- |
| ベースURL | `https://api.claudin.io/v1` |
| APIキー | あなたの `sk-...` キー |
| モデル名 | `claudinio` |

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
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

または値を直接設定します：

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

> **ヒント：** ツール呼び出しを伴う複雑なタスクの場合は、Hermes Agent が少なくとも 64K トークンコンテキストをサポートするモデルを使用していることを確認してください（Claudinio はこれをサポートしています）。

## トラブルシューティング

| 問題 | 修正方法 |
| --- | --- |
| 認証エラー | `hermes doctor` で API キーを再確認してください |
| モデルが見つからない | モデル名が正確に `claudinio` であることを確認してください |
| 接続が拒否された | ネットワークから `https://api.claudin.io/v1` にアクセスできるか確認してください |