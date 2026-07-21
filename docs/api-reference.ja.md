# APIリファレンス

Claudin.ioは**OpenAI互換**のAPIです。OpenAIのAPIを使ったことがあれば、すべてなじみ深いでしょう — Claudin.ioのベースURLを指定して、`claudinio`モデルを使うだけです。

## ベースURL

```
https://api.claudin.io
```

OpenAIスタイルのルートは`/v1`以下にあります。

## 認証

すべてのリクエストにAPIキーを送信してください。ヘッダーは次のいずれかです：

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## モデル

| モデルID | コンテキストウィンドウ |
| --- | --- |
| `claudinio` | 256Kトークン |

`claudinio`をどこでも使用してください。（一部のクライアントは`provider/model`形式を期待します — その場合は`claudinio/claudinio`を使用してください。）

## エンドポイント

| メソッドとパス | 説明 |
| --- | --- |
| `POST /v1/chat/completions` | チャット補完 — プライマリエンドポイント |
| `POST /v1/completions` | レガシーテキスト補完 |
| `POST /v1/messages` | Anthropicメッセージ形式 |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | テキスト埋め込み |
| `GET /v1/models` | 利用可能なモデルの一覧 |

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

標準のOpenAIパラメータがサポートされています：`messages`、`temperature`、`top_p`、`max_tokens`、`stream`、`stop`、`tools` / `tool_choice`（関数呼び出し）、`response_format`など。

### `max_tokens`と推論

Claudinioモデルは回答する前に推論を行い、**推論トークンは`max_tokens`にカウントされます** — 同じ予算が内部の思考連鎖と可視の応答の両方をカバーします。そのため、`max_tokens`が小さいと、ほとんどすべてが推論に消費され、回答が文の途中で途切れる可能性があります。

これを防ぐため、**4000**未満の値は自動的に4000に引き上げられます。より大きな値はそのまま渡され、パラメータを省略しても問題ありません。

構造化出力（JSON、XML、厳密な形式）を解析する場合は、解析前に`finish_reason`を確認してください — `"length"`はレスポンスがトークン制限に達して不完全であることを意味するため、パースの失敗はモデルの問題ではなく想定内です：

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### ストリーミング

`"stream": true`を設定すると、OpenAIストリーミング形式でサーバー送信イベントを受信します（`data: {...}`チャンクが`data: [DONE]`で終了します）。

### ツール / 関数呼び出し

`claudinio`はツール呼び出しをサポートしています。OpenAI APIとまったく同じように、`tools`を渡し、レスポンスから`tool_calls`を読み取ります。これにより、Claude Code、Kilo、Cursorなどのエージェントエディタ内部で動作します。

### マルチモーダル入力

`claudinio`はテキストモデルですが、Claudin.ioは画像、音声、動画ブロックを**透過的に処理**します：それらを送信すると、プロキシがモデルに渡す前にテキスト説明/文字起こしに変換します。特別なことをする必要はありません — 標準のOpenAIコンテンツブロックを送信するだけで動作します。

## エラー {#errors}

エラーはOpenAIのエラー形式に従います：

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| ステータス | 意味 | 対処法 |
| --- | --- | --- |
| `401` | APIキーが無効または不足 | キーと認証ヘッダーを確認 |
| `403` | 許可されていないエンドポイント | サポートされている`/v1/*`パスのいずれかを使用 |
| `429` | 予算上限に達したかレート制限 | ウィンドウのリセットを待つか[アップグレード](plans.md) |
| `400` | 不正なリクエスト | JSON/パラメータを確認 |
| `5xx` | 上流/プロバイダーの一時的な問題 | バックオフで再試行 |

!!! info "プロバイダーの詳細は設計上非表示にされています"
    エラーメッセージは、基礎となるモデルプロバイダーが漏洩しないようにサニタイズされています。常にClaudin.ioブランドのOpenAI形式のエラーが表示されます。

### 予算上限に達した場合

現在のウィンドウの支出保護を使い果たすと、リクエストは予算エラー（通常`429`）を返します。ダッシュボードには正確なリセット時間と残りの予算が表示されます。ウィンドウの仕組みについては[プランと制限](plans.md)を参照してください。

## レート制限

Claudin.ioは通常の使用をハードブロックしません。不正なリクエストレートは拒否ではなく*低速化*（透過的なスロットル）されるため、適切に動作するクライアントがペナルティを受けることはありません。実際には何もする必要はありません — 稀な`429`に遭遇したら再試行するだけです。