# OpenCode

[OpenCode](https://opencode.ai) 以兼容 OpenAI 的方式连接到 Claudin.io。最快的方式是使用其内置的身份验证流程。

## 快速设置

1. 运行登录命令：

    ```bash
    opencode auth login
    ```

2. 选择 **Claudinio** 作为提供商。
3. 根据提示粘贴你的 API 密钥——请从你的 [仪表板](https://claudin.io/dashboard) 复制。

然后启动 OpenCode 并选择 **claudinio** 模型。

## 使用环境变量的替代方案

如果你已经 [导出过密钥](../getting-started/set-your-key.md)，OpenCode 会自动读取标准的 OpenAI 变量——无需手动粘贴任何内容：

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 设置项 | 值 |
| --- | --- |
| 基础 URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio` |
| 提供商 | 兼容 OpenAI |

---

遇到问题？请参阅 [常见错误](../api-reference.md#errors) 或 [FAQ](../faq.md)。