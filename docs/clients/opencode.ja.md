# OpenCode

[OpenCode](https://opencode.ai)は、OpenAI互換プロバイダーとしてClaudin.ioに接続します。最も簡単な方法は、組み込みの認証フローを使用することです。

## クイックセットアップ

1. ログインコマンドを実行します:

    ```bash
    opencode auth login
    ```

2. プロバイダーとして **Claudinio** を選択します。
3. プロンプトが表示されたらAPIキーを貼り付けます — [ダッシュボード](https://claudin.io/dashboard)からコピーしてください。

その後、OpenCodeを起動し、**claudinio**モデルを選択します。

## 環境変数による代替方法

すでに[キーをエクスポート](../getting-started/set-your-key.md)している場合、OpenCodeは標準のOpenAI変数を自動で認識します — 何も貼り付ける必要はありません:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 設定 | 値 |
| --- | --- |
| ベースURL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |
| プロバイダー | OpenAI互換 |

---

問題がありますか？ [一般的なエラー](../api-reference.md#errors) または [FAQ](../faq.md) を参照してください。