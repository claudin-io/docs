# Cursor

[Cursor](https://cursor.com)は設定からOpenAI互換モデルを追加できます。
Claudin.ioはOpenAIベースURLのオーバーライドを介して接続します。

## セットアップ

1. **Cursor → Settings → Models**（または**Cursor Settings → AI**）を開きます。
2. **OpenAI API Key**までスクロールし、**Override OpenAI Base URL**オプションを展開します。
3. 設定：

    | フィールド | 値 |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. **Models**で、**`claudinio`**という名前のカスタムモデルを追加し、有効にします。
5. CursorがClaudin.ioのみを使用するようにしたい場合は、他のデフォルトモデルを無効にします。

!!! note "Cursor独自の機能"
    Cursorのエージェント機能はOpenAI互換のチャットモデルで最適に動作します。
    `claudinio`はツール呼び出しをサポートしているため、Composer/Agentフローが機能します。
    Cursor独自の機能（Tab補完など）はCursor自身のモデルで実行され、プロバイダーのオーバーライドを通じてルーティングされません。

## 確認

Cursorでチャットを開き、**claudinio**を選択してメッセージを送信します。返信があれば設定完了です。ない場合は、ベースURLが`/v1`で終わっていることと、キーに余分なスペースがないことを再確認してください。

| 設定 | 値 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |