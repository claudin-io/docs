# OpenAI互換クライアントについて

Claudin.io は OpenAI API サーフェスを実装しているため、カスタムベース URL を設定できる**あらゆる**ツール、SDK、ライブラリが動作します。お使いのエディタがこのセクションに記載されていない場合は、こちらの汎用設定を使用してください。

## 3つの設定値

| 設定 | 値 |
| --- | --- |
| ベース URL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |
| API キー | あなたの `sk-...` キー |

ほとんどのツールでは、ベース URL フィールドを *Base URL*、*API Base*、*OpenAI Base URL*、*Endpoint*、*Custom provider URL* などの名称で呼びます。常に `/v1` サフィックスを含めてください。

## 環境変数

多くの CLI や SDK は標準の OpenAI 変数を読み取ります。これらを設定すれば完了です。[キーをエクスポート](../getting-started/set-your-key.md)している場合は、`$CLAUDINIO_API_KEY` を再利用してください：

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## サポートされているエンドポイント

Claudin.io は以下の OpenAI スタイルのパスをルーティングします：

| エンドポイント | 用途 |
| --- | --- |
| `POST /v1/chat/completions` | チャット補完（メイン） |
| `POST /v1/completions` | レガシーテキスト補完 |
| `POST /v1/messages` | Anthropic Messages 形式 |
| `POST /v1/responses` | Responses API（Codex が使用） |
| `POST /v1/embeddings` | 埋め込み |
| `GET /v1/models` | 利用可能なモデル一覧 |

## 認証

キーは**次のいずれか**で送信します：

```http
Authorization: Bearer YOUR_API_KEY
```

または

```http
x-api-key: YOUR_API_KEY
```

どちらも受け付けられます。お使いのクライアントが送信する方を選んでください。

---

リクエスト/レスポンスの詳細とエラーハンドリングについては、完全な [API リファレンス](../api-reference.md) を参照してください。