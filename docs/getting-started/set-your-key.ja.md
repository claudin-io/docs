# APIキーを設定する

Claudin.ioのキーを**一度だけ**環境変数として設定すれば、このガイドのすべてのツールで再利用できます。各クライアントに手作業で貼り付ける必要はありません。

[dashboard](https://claudin.io/dashboard)から`sk-...`キーを取得し（[Create your account](account.md)を参照）、シェルプロファイルに追加して、新しいターミナルすべてで利用できるようにします。

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

`sk-...`を実際のキーに置き換えてください。どのシェルを使用しているかわからない場合は、`echo $SHELL`を実行してください。

## 確認

```bash
echo $CLAUDINIO_API_KEY
```

キーが表示されるはずです。空の場合は、新しいターミナルを開くか、上記の`source`コマンドを再実行してください。

## これが役立つ理由

[Connect your tool](../clients/opencode.md)セクションの**クイックセットアップ**スクリプトはすべて`$CLAUDINIO_API_KEY`を読み取るため、エクスポートさえすれば、そのまま実行できます。`YOUR_API_KEY`を置き換える必要はありません。環境変数を直接読み取るツール（Codexの`env_key`、OpenAI互換CLIなど）も自動的に認識します。

!!! warning "キーをパスワードのように扱ってください"
    このキーを持っている人は誰でもあなたのプランの予算を使うことができます。`~/.zshrc` / `~/.bashrc`を公開リポジトリにコミットしないでください。キーが漏洩した場合は、ダッシュボードで失効させ、新しいキーをエクスポートしてください。

---

キーをエクスポートしましたか？では、[最初の呼び出しを行う](first-call.md)か、[ツールを接続する](../clients/opencode.md)に直接進んでください。