# Cursor

[Cursor](https://cursor.com) 让你可以通过其设置添加一个 OpenAI 兼容的模型。Claudin.io 通过 OpenAI 基础 URL 覆盖进行接入。

## 设置

1. 打开 **Cursor → Settings → Models**（或 **Cursor Settings → AI**）。
2. 滚动到 **OpenAI API Key** 并展开 **Override OpenAI Base URL** 选项。
3. 设置：

    | 字段 | 值 |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. 在 **Models** 下，添加一个名为 **`claudinio`** 的自定义模型并启用它。
5. 如果你希望 Cursor 独占使用 Claudin.io，则禁用其他默认模型。

!!! note "Cursor 的自身特性"
    Cursor 的智能代理功能与 OpenAI 兼容的聊天模型配合最佳。`claudinio` 支持工具调用，因此 Composer/Agent 流程能够正常工作。部分 Cursor 专有功能（Tab 自动补全等）运行在 Cursor 自身的模型上，不会通过你的提供商覆盖进行路由。

## 验证

在 Cursor 中打开聊天，选择 **claudinio**，然后发送一条消息。如果你收到回复，说明配置成功。如果没有，请仔细检查 Base URL 是否以 `/v1` 结尾，以及 API 密钥是否粘贴且没有多余空格。

| 设置 | 值 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |