# 任意のOpenAI互換クライアント

Claudin.io は OpenAI API サーフェスを実装しているため、カスタムベース URL を設定できる**あらゆる**ツール、SDK、またはライブラリが動作します。お使いのエディターがこのセクションに記載されていない場合は、以下の汎用設定を使用してください。

## 3つの値

| 設定 | 値 |
| --- | --- |
| ベースURL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |
| APIキー | あなたの `sk-...` キー |

ほとんどのツールは、ベースURLフィールドを *Base URL*、*API Base*、*OpenAI Base URL*、*Endpoint*、または *Custom provider URL* のいずれかで呼びます。常に `/v1` サフィックスを含めてください。

## 環境変数

多くの CLI や SDK は標準の OpenAI 変数を読み取ります — これらを設定すれば完了です。キーを [エクスポート済み](../getting-started/set-your-key.md) の場合は、`$CLAUDINIO_API_KEY` を再利用してください：

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## サポートされているエンドポイント

Claudin.io は次の OpenAI 形式のパスをルーティングします：

| エンドポイント | 目的 |
| --- | --- |
| `POST /v1/chat/completions` | チャット補完（メイン） |
| `POST /v1/completions` | レガシーテキスト補完 |
| `POST /v1/messages` | Anthropic Messages 形式 |
| `POST /v1/responses` | Responses API（Codex で使用） |
| `POST /v1/embeddings` | 埋め込み |
| `GET /v1/models` | 利用可能なモデルの一覧 |

## 認証

キーを **次のいずれか** として送信します：

```http
Authorization: Bearer YOUR_API_KEY
```

または

```http
x-api-key: YOUR_API_KEY
```

どちらも受け入れられます — お使いのクライアントが送出する方を選んでください。

---

リクエスト/レスポンスの詳細とエラーハンドリングについては、完全な [APIリファレンス](../api-reference.md) を参照してください。