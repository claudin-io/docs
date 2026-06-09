# OpenCode

[OpenCode](https://opencode.ai), Claudin.io'ya OpenAI uyumlu bir sağlayıcı olarak bağlanır. En hızlı yol, yerleşik kimlik doğrulama akışıdır.

## Hızlı kurulum

1. Oturum açma komutunu çalıştırın:

    ```bash
    opencode auth login
    ```

2. Sağlayıcı olarak **Claudinio**'yu seçin.
3. İstendiğinde API anahtarınızı yapıştırın — bunu [kontrol panelinizden](https://claudin.io/dashboard) kopyalayın.

Ardından OpenCode'u başlatın ve **claudinio** modelini seçin.

## Ortam değişkeni alternatifi

Eğer anahtarınızı zaten [dışa aktardıysanız](../getting-started/set-your-key.md), OpenCode standart OpenAI değişkenlerini alır — hiçbir şey yapıştırmanıza gerek yoktur:

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

Sorun mu var? [Yaygın hatalara](../api-reference.md#errors) veya [FAQ](../faq.md)'ye bakın.