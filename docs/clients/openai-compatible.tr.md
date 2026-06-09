# Herhangi bir OpenAI uyumlu istemci

Claudin.io, OpenAI API yüzeyini uygular, bu nedenle özel bir temel URL ayarlamanıza izin veren **herhangi** bir araç, SDK veya kütüphane çalışır. Eğer editörünüz bu bölümde listelenmemişse, bu genel ayarları kullanın.

## Üç değer

| Ayar | Değer |
| --- | --- |
| Temel URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| API anahtarı | sizin `sk-...` anahtarınız |

Çoğu araç temel URL alanını şunlardan biri olarak adlandırır: *Temel URL*, *API Tabanı*, *OpenAI Temel URL'si*, *Uç Nokta* veya *Özel sağlayıcı URL'si*. Her zaman `/v1` son ekini ekleyin.

## Ortam değişkenleri

Birçok CLI ve SDK standart OpenAI değişkenlerini okur — bunları ayarlayın ve işiniz biter. Eğer [anahtarınızı dışa aktardıysanız](../getting-started/set-your-key.md), `$CLAUDINIO_API_KEY`'i yeniden kullanın:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Desteklenen uç noktalar

Claudin.io şu OpenAI tarzı yolları yönlendirir:

| Uç Nokta | Amaç |
| --- | --- |
| `POST /v1/chat/completions` | Sohbet tamamlama (ana olan) |
| `POST /v1/completions` | Eski metin tamamlama |
| `POST /v1/messages` | Anthropic Mesaj formatı |
| `POST /v1/responses` | Yanıtlar API'si (Codex tarafından kullanılır) |
| `POST /v1/embeddings` | Gömmeler |
| `GET /v1/models` | Mevcut modelleri listele |

## Kimlik doğrulama

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

İstek/yanıt detayları ve hata işleme için tam [API referansına](../api-reference.md) bakın.