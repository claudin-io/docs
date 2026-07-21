# OpenCode

[OpenCode](https://opencode.ai), Claudin.io'ya OpenAI uyumlu bir sağlayıcı olarak bağlanır. En hızlı yol, yerleşik kimlik doğrulama akışıdır.

## Hızlı kurulum

1. Giriş komutunu çalıştırın:

    ```bash
    opencode auth login
    ```

2. Sağlayıcı olarak **Claudinio**'yu seçin.
3. İstendiğinde API anahtarınızı yapıştırın — [panonuzdan](https://claudin.io/dashboard) kopyalayın.

Ardından OpenCode'u başlatın ve **claudinio** modelini seçin.

## Ortam değişkeni alternatifi

Anahtarınızı zaten [dışa aktardıysanız](../getting-started/set-your-key.md), OpenCode standart OpenAI değişkenlerini alır — herhangi bir şey yapıştırmanız gerekmez:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Ayar | Değer |
| --- | --- |
| Temel URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| Sağlayıcı | OpenAI uyumlu |

---

Sorun mu var? [Yaygın hatalara](../api-reference.md#errors) veya [FAQ](../faq.md)'e bakın.