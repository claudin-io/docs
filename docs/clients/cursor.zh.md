# Cursor

[Cursor](https://cursor.com) 允许你通过其设置添加兼容 OpenAI 的模型。Claudin.io 通过 OpenAI 基础 URL 覆盖接入。

## 设置

1. 打开 **Cursor → 设置 → 模型**（或 **Cursor 设置 → AI**）。
2. 滚动到 **OpenAI API 密钥**，展开 **覆盖 OpenAI 基础 URL** 选项。
3. 设置：

    | 字段 | 值 |
    | --- | --- |
    | OpenAI API 密钥 | `YOUR_API_KEY` |
    | 基础 URL | `https://api.claudin.io/v1` |

4. 在**模型**下，添加一个名为 **`claudinio`** 的自定义模型并启用它。
5. 如果你希望 Cursor 独占使用 Claudin.io，请禁用其他默认模型。

!!! note "Cursor 自己的功能"
    Cursor 的智能体功能与兼容 OpenAI 的聊天模型配合最佳。`claudinio` 支持工具调用，因此 Composer/Agent 流程可以正常工作。某些 Cursor 专有功能（Tab 自动补全等）运行在 Cursor 自己的模型上，不会通过你的提供商覆盖进行路由。

## 验证

在 Cursor 中打开聊天，选择 **claudinio**，然后发送一条消息。如果收到回复，则配置成功。如果没有，请检查基础 URL 是否以 `/v1` 结尾，并且密钥粘贴时没有多余空格。

| 设置项 | 值 |
| --- | --- |
| 基础 URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio` |