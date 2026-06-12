[Hermes Agent](https://github.com/NousResearch/hermes-agent) 是由 Nous Research
开发的开源终端代理。它支持任何兼容 OpenAI 的端点，非常适合与 Claudin.io 配合使用。

## 使用向导快速开始

退出任何活跃的 Hermes 会话（`Ctrl + C` 或 `/quit`），然后运行：

```bash
hermes model
```

从菜单中选择 **Custom endpoint** 并填写：

| 字段 | 值 |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | 你的 `sk-...` 密钥 |
| Model name | `claudinio` |

Hermes 会自动将配置保存到 `~/.hermes/config.yaml`。

试试看：

```bash
hermes
```

## 手动配置

编辑 `~/.hermes/config.yaml`：

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-ni-de-mi-yao"
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

> **提示：** 对于涉及工具调用的复杂任务，请确保你的 Hermes Agent 使用
> 至少 64K token 上下文的模型（Claudinio 支持）。

## 故障排除

| 问题 | 解决方法 |
| --- | --- |
| 认证错误 | 使用 `hermes doctor` 检查 API 密钥 |
| 找不到模型 | 确保模型名称精确为 `claudinio` |
| 连接被拒绝 | 验证 `https://api.claudin.io/v1` 是否可访问 |

## 实用命令

| 命令 | 描述 |
| --- | --- |
| `hermes config show` | 查看当前配置 |
| `hermes config edit` | 交互式编辑 |
| `hermes doctor` | 诊断问题 |
| `hermes model` | 切换提供商 |
