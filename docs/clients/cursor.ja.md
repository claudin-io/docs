# Cursor

[Cursor](https://cursor.com) を使用すると、設定からOpenAI互換のモデルを追加できます。Claudin.ioは、OpenAIベースURLのオーバーライドを介して接続します。

## セットアップ

1. **Cursor → 設定 → モデル**（または **Cursor 設定 → AI**）を開きます。
2. **OpenAI APIキー**までスクロールし、**OpenAIベースURLのオーバーライド** オプションを展開します。
3. 設定:

    | 項目 | 値 |
    | --- | --- |
    | OpenAI APIキー | `YOUR_API_KEY` |
    | ベースURL | `https://api.claudin.io/v1` |

4. **モデル**で、**`claudinio`** という名前のカスタムモデルを追加し、有効にします。
5. CursorがClaudin.ioのみを使用するようにする場合は、他のデフォルトモデルを無効にします。

!!! note "Cursor独自の機能"
    Cursorのエージェント機能は、OpenAI互換のチャットモデルで最適に動作します。
    `claudinio`はツールコールをサポートしているため、Composer/Agentフローが機能します。一部のCursor独自の機能（Tab補完など）はCursor自身のモデルで動作し、プロバイダオーバーライドを経由しません。

## 確認

Cursorでチャットを開き、**claudinio**を選択してメッセージを送信します。返信が返ってくれば設定完了です。返信がない場合は、ベースURLが`/v1`で終わっていること、APIキーに余分なスペースが含まれていないことを再確認してください。

| 設定 | 値 |
| --- | --- |
| ベースURL | `https://api.claudin.io/v1` |
| モデル | `claudinio` |