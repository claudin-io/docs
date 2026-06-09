# 设置你的 API 密钥

将你的 Claudin.io 密钥**一次性**设置为环境变量，本指南中的每个工具都可以重复使用它——无需手动将其粘贴到每个客户端中。

从[仪表盘](https://claudin.io/dashboard)获取你的 `sk-...` 密钥（参阅[创建账户](account.md)），然后将其添加到你的 shell 配置文件中，这样每个新终端都可以使用它。

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

将 `sk-...` 替换为你的真实密钥。不确定你正在使用哪个 shell？运行 `echo $SHELL`。

## 验证

```bash
echo $CLAUDINIO_API_KEY
```

你应该会看到你的密钥被打印出来。如果为空，请打开新终端或重新运行上面的 `source` 命令。

## 为何这很有帮助

[连接你的工具](../clients/opencode.md)一节中的每个**快速设置**脚本都会读取 `$CLAUDINIO_API_KEY`，因此一旦导出该变量，你可以按原样运行其中任何一个脚本——无需替换 `YOUR_API_KEY`。直接读取环境变量的工具（Codex 的 `env_key`、任何兼容 OpenAI 的 CLI）也会自动获取它。

!!! warning "像对待密码一样对待你的密钥"
    任何拥有此密钥的人都可以消耗你计划的预算。请勿将你的 `~/.zshrc` / `~/.bashrc` 提交到公共仓库。如果密钥泄露，请在仪表盘中撤消它并导出一个新的密钥。

---

密钥已导出？现在[进行首次调用](first-call.md)或直接跳转到[连接你的工具](../clients/opencode.md)。