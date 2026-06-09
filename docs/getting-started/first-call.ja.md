# 初めてのコール

エディタを接続する前に、キーが正常に動作することを1回のリクエストで確認する価値があります。Claudin.ioは**OpenAI Chat Completions**形式（およびAnthropic Messages形式も）をサポートしています。

これらの例は`$CLAUDINIO_API_KEY`からキーを読み取ります。[キーをエクスポート](set-your-key.md)して一度設定してください。（SDKスニペットでは、`YOUR_API_KEY`を[ダッシュボード](account.md)のキーに置き換えるか、同じ環境変数から読み取ってください。）

## cURLを使用する

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLAUDINIO_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "user", "content": "Say hello in one short sentence."}
    ]
  }'
```

通常のOpenAIスタイルのJSONレスポンスが`choices`配列とともに返ってくるはずです。

!!! tip "`x-api-key`も使用可能"
    Claudin.ioは、キーを`Authorization: Bearer YOUR_API_KEY`として受け付けるか、**または**`x-api-key: YOUR_API_KEY`ヘッダーとして受け付けます。クライアントが送信する方を使用してください。

## OpenAI Python SDKを使用する

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.claudin.io/v1",
    api_key="YOUR_API_KEY",
)

resp = client.chat.completions.create(
    model="claudinio",
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)

print(resp.choices[0].message.content)
```

## OpenAI Node SDKを使用する

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.claudin.io/v1",
  apiKey: "YOUR_API_KEY",
});

const resp = await client.chat.completions.create({
  model: "claudinio",
  messages: [{ role: "user", content: "Say hello in one short sentence." }],
});

console.log(resp.choices[0].message.content);
```

## ストリーミング

`stream: true`を設定し、サーバー送信イベントを読み取ります。OpenAI APIとまったく同じです。

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Authorization: Bearer $CLAUDINIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claudinio",
    "stream": true,
    "messages": [{"role": "user", "content": "Count to five."}]
  }'
```

---

有効なレスポンスが返ってきましたか？素晴らしい—次に[お気に入りのツールを接続](../clients/claude-code.md)しましょう。失敗した場合は、[APIリファレンス](../api-reference.md#errors)で一般的なエラーを確認してください。