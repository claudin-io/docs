# OpenCode

[OpenCode](https://opencode.ai) は、OpenAI 互換のプロバイダとして Claudin.io に接続します。最も簡単な方法は、組み込みの認証フローを使用することです。

## クイックセットアップ

1. 以下のコマンドでログインします：

    ```bash
    opencode auth login
    ```

2. プロバイダとして **Claudinio** を選択します。
3. プロンプトが表示されたら、APIキーを貼り付けます。APIキーは[ダッシュボード](https://claudin.io/dashboard)からコピーできます。

その後、OpenCode を起動し、**claudinio** モデルを選択します。

## 環境変数による代替方法

すでに[キーをエクスポート](../getting-started/set-your-key.md)している場合、OpenCode は標準の OpenAI 変数を自動で認識します。何も貼り付ける必要はありません。

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 設定 | 値 |
| --- | --- |
| ベースURL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |
| プロバイダ | OpenAI互換 |

---

問題が発生しましたか？[よくあるエラー](../api-reference.md#errors)または[FAQ](../faq.md)を参照してください。