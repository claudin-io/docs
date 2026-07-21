# OpenAI uyumlu herhangi bir istemci

Claudin.io, OpenAI API yüzeyini uygular, bu nedenle özel bir temel URL ayarlamanıza izin veren **herhangi bir** araç, SDK veya kitaplık çalışır. Editörünüz bu bölümde listelenmemişse, bu genel ayarları kullanın.

## Üç değer

| Ayar | Değer |
| --- | --- |
| Temel URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| API anahtarı | `sk-...` anahtarınız |

Çoğu araç, temel URL alanını şunlardan biri olarak adlandırır: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint* veya *Custom provider URL*. Her zaman `/v1` sonekini ekleyin.

## Ortam değişkenleri

Birçok CLI ve SDK, standart OpenAI değişkenlerini okur — bunları ayarlayın ve işiniz biter. [Anahtarınızı dışa aktardıysanız](../getting-started/set-your-key.md), `$CLAUDINIO_API_KEY`'i yeniden kullanın:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Desteklenen uç noktalar

Claudin.io, bu OpenAI tarzı yolları yönlendirir:

| Uç nokta | Amaç |
| --- | --- |
| `POST /v1/chat/completions` | Sohbet tamamlama (ana olan) |
| `POST /v1/completions` | Eski metin tamamlama |
| `POST /v1/messages` | Anthropic Messages formatı |
| `POST /v1/responses` | Responses API (Codex tarafından kullanılır) |
| `POST /v1/embeddings` | Gömme |
| `GET /v1/models` | Mevcut modelleri listele |

## Kimlik Doğrulama

Anahtarınızı **aşağıdakilerden biri** olarak gönderin:

```http
Authorization: Bearer YOUR_API_KEY
```

veya

```http
x-api-key: YOUR_API_KEY
```

Her ikisi de kabul edilir — istemcinizin gönderdiğini seçin.

---

İstek/yanıt ayrıntıları ve hata yönetimi için tam [API referansına](../api-reference.md) bakın.