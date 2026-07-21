# FAQ

## Claudin.io 到底是什么？

针对AI编程代理的API代理。您按月支付固定订阅费用，获得一个兼容OpenAI/Anthropic的API密钥，可以用于Claude Code、Kilo、Zed、Codex、Cursor或任何OpenAI客户端。无按token计费。

## 真的是无限使用吗？

用量是无限的——没有请求计数或token计量。唯一的限制是每个时间窗口内的**消费保护上限**，用于防止失控的代理耗尽您的套餐。在正常的交互式工作中，您很少会达到这个上限。请参见[套餐与限制](plans.md)。

## 我应该使用哪个模型？

始终使用**`claudinio`**（对于需要`provider/model`形式的客户端，使用`claudinio/claudinio`）。基础URL是`https://api.claudin.io`。

## 我应该用`Authorization`还是`x-api-key`进行身份验证？

两者都可以。`Authorization: Bearer YOUR_API_KEY`或`x-api-key: YOUR_API_KEY`。

## 我可以将其用于未列出的工具吗？

是的——任何允许您设置自定义OpenAI基础URL的工具都可以使用。请参见[通用OpenAI设置](clients/openai-compatible.md)。

## 它支持工具/函数调用吗？

是的。这就是它能在代理编辑器中工作的原因。传递`tools`并像使用OpenAI API一样读取`tool_calls`。

## 它能处理图像、音频或视频吗？

是的，透明地处理。发送标准的OpenAI内容块；代理会将图像/音频/视频转换为文本描述或转录，然后再让模型处理。无需特殊配置。

## 上下文窗口大小是多少？

256K tokens。

## 如何升级或取消？

从您的[仪表板](https://claudin.io/dashboard)操作。升级立即生效（通过Stripe）。如果您取消，您将保留已付费的套餐直到当前付费周期结束，然后自动降级为免费套餐。

## 我遇到了预算错误。现在怎么办？

您已达到当前窗口的消费保护上限。要么等待窗口重置（您的仪表板会显示重置时间），要么[升级](plans.md)以获得更高的上限。

## 请求返回401错误。

您的密钥缺失或错误。请从仪表板重新复制，确保没有多余的空格，并且设置了认证头部。

## 我的密钥泄露了。我该怎么办？

立即从仪表板撤销并生成新密钥。像对待密码一样对待密钥——切勿提交到代码仓库或公开分享。

## 我如何获得帮助？

从您的[仪表板](https://claudin.io/dashboard)中的**支持**卡片提交工单，或发送电子邮件至支持邮箱。我们会回复您。