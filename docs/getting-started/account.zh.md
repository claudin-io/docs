# 创建你的账户

获取一个可用的 API key 大约需要一分钟。

## 1. 使用 GitHub 登录

前往 **[claudin.io](https://claudin.io)** 并点击 **Sign in with GitHub**。
Claudin.io 使用 GitHub 进行登录——无需单独管理密码。

首次登录时，你的账户会自动在 **Free** 计划下创建，这样你可以在付费前先试用。

## 2. 生成你的 API key

进入[仪表板](https://claudin.io/dashboard)后：

1. 找到 **API Keys** 卡片。
2. 点击 **Generate key**（或 **Create new key**）。
3. 复制密钥——它看起来像 `sk-...`。

!!! warning "请像对待密码一样对待你的密钥"
    你的 API key 可以访问你计划的预算。不要将其提交到仓库、粘贴到公共聊天或分享。如果密钥泄露，请从仪表板撤销并生成一个新的。

## 3. 记下你将需要的两个值

每个集成都需要相同的两个东西：

| 值 | 说明 |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **模型** | `claudinio` |
| **API key** | 你刚复制的 `sk-...` |

就是这样。接下来，要么[进行原始 API 调用](first-call.md)以确认其正常工作，要么直接跳到[连接你的工具](../clients/claude-code.md)。

---

## 选择套餐

你可以留在 **Free** 计划上试用。准备好后，从仪表板升级——查看[套餐与限制](../plans.md)了解完整详情。

升级通过 Stripe 处理，并立即生效。