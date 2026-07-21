# API referansı

Claudin.io, **OpenAI uyumlu** bir API'dir. OpenAI API'sini kullandıysanız, buradaki her şey tanıdık gelecektir — sadece Claudin.io temel URL'sini işaret edin ve `claudinio` modelini kullanın.

## Temel URL

```
https://api.claudin.io
```

OpenCI tarzı yollar `/v1` altında bulunur.

## Kimlik Doğrulama

API anahtarınızı her istekte, aşağıdaki başlıklardan biri olarak gönderin:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Model

| Model kimliği | Bağlam penceresi |
| --- | --- |
| `claudinio` | 256K token |

`claudinio`'yu her yerde kullanın. (Bazı istemciler `provider/model` biçimini bekler — onlar için `claudinio/claudinio` kullanın.)

## Uç Noktalar

| Yöntem ve yol | Açıklama |
| --- | --- |
| `POST /v1/chat/completions` | Sohbet tamamlama — birincil uç nokta |
| `POST /v1/completions` | Eski metin tamamlama |
| `POST /v1/messages` | Anthropic Messages biçimi |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Metin yerleştirme (embedding) |
| `GET /v1/models` | Mevcut modelleri listele |

### Sohbet tamamlama

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "Yardımcı bir asistan."},
      {"role": "user", "content": "Proxy'ler hakkında bir haiku yaz."}
    ],
    "temperature": 0.7
  }'
```

Standart OpenAI parametreleri desteklenir: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (fonksiyon çağrısı), `response_format` vb.

### `max_tokens` ve akıl yürütme

Claudinio modelleri yanıtlamadan önce akıl yürütür ve **akıl yürütme token'ları `max_tokens` limitine dahildir** — aynı bütçe, iç düşünce zincirini ve görünür yanıtı kapsar. Bu nedenle küçük bir `max_tokens` değeri neredeyse tamamen akıl yürütmeye harcanabilir ve yanıt cümle ortasında kesilebilir.

Bunu önlemek için **4000**'in altındaki değerler otomatik olarak 4000'e yükseltilir. Daha büyük değerler olduğu gibi iletilir ve parametreyi atlamak her zaman sorunsuzdur.

Yapılandırılmış çıktı (JSON, XML, katı bir biçim) ayrıştırıyorsanız, ayrıştırmadan önce `finish_reason`'u kontrol edin. `"length"` değeri, yanıtın token sınırına ulaştığı ve tamamlanmadığı anlamına gelir, bu nedenle ayrıştırma hatası beklenir — model sorunu değildir:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # kesildi — daha büyük bir max_tokens ile yeniden dene
data = json.loads(choice.message.content)
```

### Akış (Streaming)

`"stream": true` olarak ayarlayarak, OpenAI akış biçiminde (`data: {...}` blokları ve sonunda `data: [DONE]`) sunucu tarafından gönderilen olayları alın.

### Araç / fonksiyon çağrısı

`claudinio` araç çağrılarını destekler. `tools` parametresini iletin ve yanıttan `tool_calls`'u okuyun — tıpkı OpenAI API'sinde olduğu gibi. Bu sayede Claude Code, Kilo Code ve Cursor gibi ajan editörlerde çalışır.

### Çok modlu girdi

`claudinio` bir metin modelidir, ancak Claudin.io **görüntü, ses ve video bloklarını şeffaf bir şekilde işler**: bunları gönderirseniz, proxy bunları model görmeden önce metin açıklamalarına/transkripsiyonlarına dönüştürür. Özel bir şey yapmanız gerekmez — standart OpenAI içerik bloklarını gönderin ve çalışsın.

## Hatalar {#errors}

Hatalar, OpenAI hata yapısını izler:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Durum | Anlamı | Ne yapmalı |
| --- | --- | --- |
| `401` | Geçersiz veya eksik API anahtarı | Anahtarı ve auth başlığını kontrol edin |
| `403` | Uç noktaya izin verilmiyor | Desteklenen `/v1/*` yollarından birini kullanın |
| `429` | Bütçe sınırına ulaşıldı veya hız sınırı | Pencere sıfırlanmasını bekleyin veya [yükseltme yapın](plans.md) |
| `400` | Hatalı istek | JSON / parametrelerinizi kontrol edin |
| `5xx` | Yukarı akış/sağlayıcı sorunu | Geri çekilmeli (backoff) tekrar deneyin |

!!! info "Sağlayıcı detayları tasarım gereği gizlidir"
    Hata mesajları, altta yatan model sağlayıcısını sızdırmamak için temizlenir. Her zaman Claudin.io markalı, OpenAI şeklinde hatalar görürsünüz.

### Bütçe sınırına ulaşma

Mevcut pencerenin harcama korumasını tükettiğinizde, istekler bir bütçe hatası döndürür (genellikle `429`). Panonuz, tam sıfırlanma zamanını ve kalan bütçeyi gösterir. Pencerelerin nasıl çalıştığı hakkında [Planlar ve limitler](plans.md) bölümüne bakın.

## Hız sınırlama

Claudin.io normal kullanımı sert bir şekilde engellemez. Kötüye kullanım amaçlı istek hızları, reddedilmek yerine *yavaşlatılır* (şeffaf bir kısıtlama), böylece iyi davranan istemciler asla cezalandırılmaz. Pratikte herhangi bir şey yapmanız gerekmez — nadir görülen `429` durumunda sadece tekrar deneyin.