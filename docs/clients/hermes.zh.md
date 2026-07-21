# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) 是一个由 Nous Research 开发的开源终端 AI 代理。它支持任何兼容 OpenAI 的端点，因此非常适合 Claudin.io。

## 快速开始向导

退出任何活动的 Hermes 会话（按 `Ctrl + C` 或输入 `/quit`），然后运行：

```bash
hermes model
```

在菜单中选择 **自定义端点**，然后填写：

| 字段 | 值 |
| --- | --- |
| 基础 URL | `https://api.claudin.io/v1` |
| API 密钥 | 你的 `sk-...` 密钥 |
| 模型名称 | `claudinio` |

Hermes 会将配置自动保存到 `~/.hermes/config.yaml`。

试用：

```bash
hermes
```

## 手动配置

编辑 `~/.hermes/config.yaml`：

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

或直接设置值：

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

验证：

```bash
hermes config check
hermes config show
```

> **提示：** 对于涉及工具调用的复杂任务，请确保你的 Hermes Agent 使用至少 64K token 上下文的模型（Claudinio 支持此功能）。

## 故障排除

| 问题 | 解决方案 |
| --- | --- |
| 认证错误 | 使用 `hermes doctor` 仔细检查你的 API 密钥 |
| 未找到模型 | 确保模型名称精确为 `claudinio` |
| 连接被拒绝 | 确认从你的网络可以访问 `https://api.claudin.io/v1` |