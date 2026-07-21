# 设置你的 API 密钥

将你的 Claudin.io 密钥**一次性**设置为环境变量后，本指南中的每个工具都可以重复使用 —— 无需再手动粘贴到每个客户端中。

从[控制台](https://claudin.io/dashboard)获取你的 `sk-...` 密钥（请参阅[创建你的账户](account.md)），然后将其添加到你的 shell 配置文件中，以便在每个新终端中都可以使用。

## macOS / Linux

=== "zsh（macOS 默认）"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

将 `sk-...` 替换为你的真实密钥。不确定你当前使用的 shell？运行 `echo $SHELL` 即可查看。

## 验证

```bash
echo $CLAUDINIO_API_KEY
```

你应该会看到打印出的密钥。如果为空，请打开一个新的终端或重新运行上面的 `source` 命令。

## 为何这样做有帮助

[连接你的工具](../clients/opencode.md)章节中的每个**快速配置**脚本都会读取 `$CLAUDINIO_API_KEY`，因此一旦导出，你就可以直接运行其中的任何一个 —— 无需替换 `YOUR_API_KEY`。直接读取环境变量的工具（Codex 的 `env_key`、任何兼容 OpenAI 的 CLI）也会自动获取到它。

!!! warning "像对待密码一样保管你的密钥"
    拥有此密钥的任何人都可以使用你计划的额度。请勿将你的 `~/.zshrc` / `~/.bashrc` 提交到公共仓库。如果密钥泄露，请在控制台中撤销它并导出一个新的密钥。

---

密钥已导出？现在[发起你的首次调用](first-call.md)或直接跳转到[连接你的工具](../clients/opencode.md)。