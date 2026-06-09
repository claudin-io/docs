# API リファレンス

Claudin.ioは**OpenAI互換**のAPIです。OpenAI APIを使ったことがあるなら、ここはすべておなじみでしょう。Claudin.ioのベースURLを指定して、`claudinio`モデルを使うだけです。

## ベースURL

```
https://api.claudin.io
```

OpenAIスタイルのルートは`/v1`以下にあります。

## 認証

リクエストごとにAPIキーを、以下のいずれかのヘッダーとして送信してください:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## モデル

| モデルID | コンテキストウィンドウ |
| --- | --- |
| `claudinio` | 256K トークン |

`claudinio`をすべての場所で使用してください。（一部のクライアントは`provider/model`形式を期待します。その場合は`claudinio/claudinio`を使用してください。）

## エンドポイント

| メソッドとパス | 説明 |
| --- | --- |
| `POST /v1/chat/completions` | チャット補完 — 主要エンドポイント |
| `POST /v1/completions` | レガシーテキスト補完 |
| `POST /v1/messages` | Anthropic Messages形式 |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | テキスト埋め込み |
| `GET /v1/models` | 利用可能なモデルを一覧表示 |

### チャット補完

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],
    "temperature": 0.7
  }'
```

標準のOpenAIパラメータがサポートされています：`messages`、`temperature`、`top_p`、`max_tokens`、`stream`、`stop`、`tools`/`tool_choice`（関数呼び出し）、`response_format`など。

### ストリーミング

`"stream": true`を設定すると、OpenAIストリーミング形式でサーバー送信イベントを受信します（`data: {...}`チャンクが`data: [DONE]`で終了します）。

### ツール/関数呼び出し

`claudinio`はツール呼び出しをサポートしています。OpenAI APIとまったく同じように、`tools`を渡してレスポンスから`tool_calls`を読み取ります。これにより、Claude Code、Kilo、Cursorなどのエージェンティックエディタ内で動作します。

### マルチモーダル入力

`claudinio`はテキストモデルですが、Claudin.ioは画像、音声、ビデオブロックを**透過的に処理**します