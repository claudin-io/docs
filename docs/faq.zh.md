# 常见问题

## Claudin.io 到底是什么？

一个面向AI编程代理的API代理。你支付固定的月订阅费，就能获得一个兼容OpenAI/Anthropic的API密钥，可用于Claude Code、Kilo、Zed、Codex、Cursor或任何OpenAI客户端。没有按token计费。

## 真的是无限的吗？

使用是无限的——没有请求计数器或token计量器。唯一的限制是每个时间窗口内的**消费保护上限**，用于防止失控的代理耗尽你的套餐。在正常的交互式工作中，你很少会触及这个上限。详见[套餐与限制](plans.md)。

## 我应该使用什么模型？

始终使用 **`claudinio`**（对于需要`provider/model`形式的客户端，可以使用`claudinio/claudinio`）。基础URL是`https://api.claudin.io`。

## 我使用`Authorization`还是`x-api-key`进行身份验证？

两种方式都可以。`Authorization: Bearer YOUR_API_KEY` 或 `x-api-key: YOUR_API_KEY`。

## 能否将其与未列出的工具一起使用？

可以——任何允许你设置自定义OpenAI基础URL的工具都可以使用。请参考[通用OpenAI设置](clients/openai-compatible.md)。

## 是否支持工具/函数调用？

支持。这正是它能在代理编辑器中工作的原因。像使用OpenAI API一样传递`tools`并读取`tool_calls`。

## 能否处理图片、音频或视频？

可以，完全透明。发送标准的OpenAI内容块；代理会在模型看到之前将图片/音频/视频转换为文本描述或转录。无需特殊配置。

## 上下文窗口是多少？

256K token。

## 如何升级或取消？

从你的[仪表盘](https://claudin.io/dashboard)操作。升级立即生效（通过Stripe）。如果取消，你将继续使用已付费的套餐直到当前周期结束，然后自动降级为Free。

## 遇到了预算错误，该怎么办？

你已达到当前窗口的消费保护上限。要么等待窗口重置（你的仪表盘会显示重置时间），要么[升级](plans.md)以获得更高的上限。

## 请求失败并返回401。

你的密钥缺失或错误。从仪表盘重新复制，确保没有多余的空格，并且正确设置了认证头。

## 我的密钥泄漏了，该怎么办？

立即从仪表盘吊销并生成新密钥。请将密钥视为密码——切勿提交或公开分享。

## 如何获得帮助？

从你的[仪表盘](https://claudin.io/dashboard)中的**支持**卡片打开工单，或发送邮件至支持邮箱。我们会尽快回复你。