# API referansı

Claudin.io **OpenAI ile uyumlu** bir API'dir. OpenAI API'sini kullandıysanız,
buradaki her şey tanıdık gelecektir — sadece Claudin.io temel URL'sini işaret edin ve
`claudinio` modelini kullanın.

## Temel URL

```
https://api.claudin.io
```

OpenAI tarzı rotalar `/v1` altında bulunur.

## Kimlik Doğrulama

API anahtarınızı her istekte, başlık olarak gönderin:

```http
Authorization: Bearer API_ANAHTARINIZ
```

```http
x-api-key: API_ANAHTARINIZ
```

## Model

| Model kimliği | Bağlam penceresi |
| --- | --- |
| `claudinio` | 256K token |

Her yerde `claudinio` kullanın. (Bazı istemciler `sağlayıcı/model` formatını bekler — onlar
için `claudinio/claudinio` kullanın.)

## Uç Noktalar

| Metod & yol | Açıklama |
| --- | --- |
| `POST /v1/chat/completions` | Sohbet tamamlama — birincil uç nokta |
| `POST /v1/completions` | Eski metin tamamlama |
| `POST /v1/messages` | Anthropic Mesaj formatı |
| `POST /v1/responses` | Yanıtlar API (Codex) |
| `POST /v1/embeddings` | Metin gömmeleri |
| `GET /v1/models` | Mevcut modelleri listele |

### Sohbet tamamlama

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer API_ANAHTARINIZ" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "Yardımcı bir asistansınız."},
      {"role": "user", "content": "Proxy'ler hakkında bir haiku yaz."}
    ],
    "temperature": 0.7
  }'
```

Standart OpenAI parametreleri desteklenir: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (fonksiyon çağrısı),
`response_format` vb.

### Akış

Sunucu tarafından gönderilen olayları OpenAI akış formatında almak için
`"stream": true` olarak ayarlayın (`data: {...}` parçaları `data: [DONE]` ile sonlandırılır).

### Araç / fonksiyon çağrısı

`claudinio`, araç çağrılarını destekler. OpenAI API'sinde olduğu gibi `tools` parametresini
iletin ve yanıttan `tool_calls` değerini okuyun. Bu, onu Claude Code, Kilo ve Cursor gibi
aracı editörlerin içinde çalıştıran şeydir.

### Çoklu ortam girdisi

`claudinio` bir metin modelidir, ancak Claudin.io, görüntü, ses ve video bloklarını
**şeffaf bir şekilde işler**: bunları gönderirseniz, proxy model bunları görmeden önce
bunları metin açıklamalarına/transkripsiyonlarına dönüştürür. Özel bir şey yapmanıza gerek
yok — standart OpenAI içerik blokları gönderin ve çalışsın.

## Hatalar {#errors}

Hatalar, OpenAI hata yapısını izler:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Durum | Anlamı | Ne yapmalı |
| --- | --- | --- |
| `401` | Geçersiz veya eksik API anahtarı | Anahtarı ve kimlik doğrulama başlığını kontrol edin |
| `403` | Uç noktaya izin verilmiyor | Desteklenen `/v1/*` yollarından birini kullanın |
| `429` | Bütçe sınırına ulaşıldı veya hız sınırlaması | Pencere sıfırlanmasını bekleyin veya [yükseltme](plans.md) yapın |
| `400` | Hatalı istek | JSON / parametrelerinizi kontrol edin |
| `5xx` | Yukarı akış/sağlayıcı aksaklığı | Geri çekilme ile yeniden deneyin |

!!! info "Sağlayıcı detayları tasarım gereği gizlidir"
    Hata mesajları, altta yatan model sağlayıcısını sızdırmamak için temizlenir.
    Her zaman Claudin.io markalı, OpenAI şeklinde hatalar göreceksiniz.

### Bütçe sınırına ulaşma

Geçerli pencerenin harcama korumasını tükettiğinizde, istekler bir bütçe hatası
döndürür (genellikle `429`). Paneliniz tam sıfırlanma süresini ve kalan bütçeyi
gösterir. Pencerelerin nasıl çalıştığı hakkında [Planlar ve limitler](plans.md) bölümüne bakın.

## Hız sınırlaması

Claudin.io, normal kullanımı engellemez. Kötüye kullanım amaçlı istek oranları reddedilmek
yerine *yavaşlatılır* (şeffaf bir kısıtlama), bu nedenle iyi davranan istemciler asla
cezalandırılmaz. Pratikte hiçbir şey yapmanıza gerek yok — nadir görülen `429`
durumunda sadece yeniden deneyin.