# OpenCode

[OpenCode](https://opencode.ai) 作为与 OpenAI 兼容的提供商连接到 Claudin.io。最快的方式是其内置的认证流程。

## 快速设置

1. 运行登录命令：

    ```bash
    opencode auth login
    ```

2. 选择 **Claudinio** 作为提供商。
3. 在提示时粘贴您的 API 密钥——从您的 [仪表板](https://claudin.io/dashboard) 复制。

然后启动 OpenCode 并选择 **claudinio** 模型。

## 环境变量替代方案

如果您已经[导出了密钥](../getting-started/set-your-key.md)，OpenCode 会自动获取标准的 OpenAI 环境变量——无需粘贴任何内容：

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| 设置 | 值 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio` |
| 提供商 | 与 OpenAI 兼容 |

---

遇到问题？请查阅[常见错误](../api-reference.md#errors)或[常见问题](../faq.md)。