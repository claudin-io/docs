---
hide:
  - navigation
  - toc
---

<div class="cl-hero" markdown>

# 請求書の不安がないコーディング。上限ではなくクレジット。

Claudin.ioはAIコーディングエージェント向けのAPIプロキシです。**月額プラン**を選ぶと、毎月補充されるクレジットのウォレットが手に入り、リクエストあたり約1クレジットで使えます — トークン単位の請求なし、時間あたりの上限なし。プランのクレジットは毎月更新されます — その月の割り当てであり、繰り越されません。トップアップで購入したクレジットは決して失効しません。

</div>

[はじめる :material-arrow-right:](getting-started/account.md){ .md-button .md-button--primary }
[プランを見る](plans.md){ .md-button }

---

## Claudin.ioを選ぶ理由

<div class="grid cards" markdown>

-   :material-wallet:{ .lg .middle } __メーターではなくクレジット__

    ---

    プランは月あたりのクレジット数で、典型的なリクエストは約1クレジット。
    時間あたりの上限もセッションの上限もありません — 唯一の上限はウォレットで、
    トップアップで即座に補充できます。

-   :material-power-plug:{ .lg .middle } __お使いのツールで動く__

    ---

    OpenAIおよびAnthropic互換のエンドポイント。OpenCode、Claude Code、Kilo Code、
    Zed、Codex、Cursor、または任意のOpenAIクライアントに数分で組み込めます。

-   :material-cash-multiple:{ .lg .middle } __予測できるコスト__

    ---

    決まった数のクレジットに対する固定の月額料金。月末の請求書に驚きはありません。
    プランのクレジットは請求ごとに更新され、繰り越されません。トップアップで
    購入したクレジットは決して失効しません。

-   :material-format-list-bulleted:{ .lg .middle } __チューニング済みのモデル、選びたいときのカタログ__

    ---

    `claudinio` がデフォルトであり私たちのおすすめです — クレジットが最も
    遠くまで行くモデル。名前付きの8モデルは設定1つで使え、それぞれ `claudinio`
    クレジットの固定倍率です。

</div>

## 4ステップではじめる

1. **[アカウントを作成](getting-started/account.md)**し、APIキーをコピーします。
2. **[APIキーを設定](getting-started/set-your-key.md)** — シェルで一度だけ。
3. **[ツールを接続](clients/opencode.md)** — エディタまたはエージェントを選びます。
4. **[最初の呼び出し](getting-started/first-call.md)**をして、開発を始めましょう。

!!! tip "モデル名は `claudinio` です"
    どのクライアントを使っても、指定するモデルIDは **`claudinio`** です — 特定の
    モデルが欲しいときは[カタログID](plans.md#catalogue)を。ベースURLは
    **`https://api.claudin.io`** です。

---

<small>お困りですか？ [FAQ](faq.md)を確認するか、[ダッシュボード](https://claudin.io/dashboard)の
サポートカードからご連絡ください。</small>
