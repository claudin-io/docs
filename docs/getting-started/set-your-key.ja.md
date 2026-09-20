# APIキーを設定する

Claudin.ioのキーを**一度だけ**環境変数に設定すれば、このガイドのすべてのツールで再利用できます — 各クライアントに手動で貼り付ける必要はありません。

[ダッシュボード](https://claudin.io/dashboard)から`sk-...`キーを取得し（[アカウントを作成する](account.md)を参照）、それをシェルプロファイルに追加して、新しいターミナルごとに利用できるようにします。

## macOS / Linux

=== "zsh（macOSのデフォルト）"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

`sk-...`を実際のキーに置き換えてください。使用しているシェルがわからない場合は、`echo $SHELL`を実行してください。

## 確認

```bash
echo $CLAUDINIO_API_KEY
```

キーが表示されるはずです。空の場合は、新しいターミナルを開くか、上記の`source`コマンドを再実行してください。

## これが役立つ理由

[ツールを接続する](../clients/opencode.md)セクションの**クイックセットアップ**スクリプトはすべて`$CLAUDINIO_API_KEY`を読み取るため、一度エクスポートすれば、そのままどれでも実行できます — 置き換えるべき`YOUR_API_KEY`はありません。環境変数を直接読み取るツール（Codexの`env_key`、OpenAI互換のCLIなど）も自動的に取得します。

!!! warning "キーはパスワードと同じように扱ってください"
    このキーを持つ人は誰でもあなたのクレジットを使えます。`~/.zshrc` / `~/.bashrc` を
    公開リポジトリにコミットしないでください。キーが漏洩したら、ダッシュボードで
    失効させて新しいキーをエクスポートしてください。

---

キーをエクスポートしましたか？次は[最初の呼び出しを行い](first-call.md)、または[ツールの接続](../clients/opencode.md)に直接進んでください。