# API referansı

Claudin.io, **OpenAI uyumlu** bir API'dir. OpenAI API'yi kullandıysanız
buradaki her şey size tanıdık gelir — tek yapmanız gereken Claudin.io temel
URL'sini işaret etmek ve `claudinio` modelini kullanmak.

## Temel URL

```
https://api.claudin.io
```

OpenAI tarzı yollar `/v1` altında bulunur.

## Kimlik doğrulama

API anahtarınızı her istekte aşağıdaki başlıklardan biri olarak gönderin:

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

Her yerde `claudinio` kullanın. (Bazı istemciler `provider/model` biçimini
bekler — bunlar için `claudinio/claudinio` kullanın.)

## Uç noktalar

| Yöntem ve yol | Açıklama |
| --- | --- |
| `POST /v1/chat/completions` | Sohbet tamamlamaları — birincil uç nokta |
| `POST /v1/completions` | Eski metin tamamlamaları |
| `POST /v1/messages` | Anthropic Messages biçimi |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Metin gömme vektörleri |
| `GET /v1/models` | Kullanılabilir modelleri listele |

### Sohbet tamamlamaları

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],
    "temperature": 0.7
  }'
```

Standart OpenAI parametreleri desteklenir: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (fonksiyon çağrısı),
`response_format` ve diğerleri. Göndermeden önce bilmeye değer sınırları olan iki
parametre vardır: [`max_tokens`](#max_tokens-and-reasoning) bir alt ve bir üst
sınıra sabitlenir, [`n`](#multiple-completions-n) ise `1` olmalıdır.

### `max_tokens` ve akıl yürütme {#max_tokens-and-reasoning}

Claudinio modelleri yanıtlamadan önce akıl yürütür ve **akıl yürütme token'ları
`max_tokens`'tan düşülür** — aynı bütçe iç düşünce zincirini ve görünür yanıtı
kapsar. Bu nedenle küçük bir `max_tokens` neredeyse tamamen akıl yürütmeye
harcanabilir ve yanıt cümlenin ortasında kesilebilir.

Bunu önlemek için **4000**'in altındaki değerler otomatik olarak 4000'e
yükseltilir. Diğer uçta, **393216**'nın üzerindeki değerler 393216'ya —
modellerin kabul ettiği maksimuma — düşürülür; çünkü daha büyük bir sayı "ne
kadar istersen o kadar" olarak değil, doğrudan reddedilir. İkisi arasındaki her
değer olduğu gibi iletilir ve parametreyi atlamak her zaman sorunsuzdur.

`max_tokens` bir rezervasyon değil, bir tavandır: yalnızca gerçekte üretilen
token'lar için faturalandırılırsınız; bu nedenle cömert bir değerin ek maliyeti
yoktur.

Yapılandırılmış çıktıyı (JSON, XML, katı bir biçim) ayrıştırıyorsanız,
ayrıştırmadan önce `finish_reason`'ı kontrol edin — `"length"`, yanıtın token
sınırına ulaştığı ve eksik olduğu anlamına gelir; bu nedenle ayrıştırma hatası
bozuk model sorunu değil, beklenen bir durumdur:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Birden çok tamamlama (`n`) {#multiple-completions-n}

Yalnızca **`n = 1`** desteklenir. `n` değerini 1'den büyük göndermek,
`"code": "unsupported_parameter"` ile `400` döndürür; parametreyi atlamak her
zaman güvenlidir.

Claudinio modelleri yanıtlamadan önce akıl yürütür ve akıl yürütme geçişi tek
bir düşünce hattı üretir — bunu birkaç bağımsız adaya dallandırmanın ucuz bir
yolu yoktur, bu yüzden yukarı akış sağlayıcıları da böyle bir seçenek sunmaz.
Birden fazla aday istiyorsanız, isteği birden çok kez gönderin (daha yüksek bir
`temperature` size çeşitlilik sağlar) ve her birinin ayrıca faturalandırıldığını
unutmayın.

`n > 1` değerini sessizce tek bir seçenek döndürmek yerine reddederiz: dört
isteyen ve bir alan bir istemci genellikle daha sonra kendi kodunun içinde,
nedenini açıklayan bizden bir hata olmadan başarısız olur.

### Akış

OpenAI akış biçiminde sunucu tarafından gönderilen olayları almak için
`"stream": true` olarak ayarlayın (`data: {...}` parçaları `data: [DONE]` ile
sonlandırılır).

### Araç / fonksiyon çağrısı

`claudinio` araç çağrılarını destekler. Tıpkı OpenAI API'de olduğu gibi `tools`
parametresini iletin ve yanıttan `tool_calls` değerini okuyun. Claude Code, Kilo
ve Cursor gibi ajan tabanlı editörlerin içinde çalışmasını sağlayan şey budur.

### Çok modlu girdi

`claudinio` bir metin modelidir, ancak Claudin.io görsel, ses ve video
bloklarını **şeffaf bir şekilde işler**: bunları gönderirseniz, proxy bunları
model görmeden önce metin açıklamalarına/yazıya dökümlerine dönüştürür. Özel bir
şey yapmanıza gerek yok — standart OpenAI içerik blokları gönderin ve her şey
çalışır.

## Hatalar {#errors}

Hatalar OpenAI hata biçimini izler:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Durum | Anlam | Ne yapmalı |
| --- | --- | --- |
| `401` | Geçersiz veya eksik API anahtarı | Anahtarı ve kimlik doğrulama başlığını kontrol edin |
| `403` | Uç noktaya izin verilmiyor | Desteklenen `/v1/*` yollarından birini kullanın |
| `402` | Etkin abonelik yok | [Abone olun](https://claudin.io/dashboard) — yeniden denemek işe yaramaz |
| `429` | Bütçe sınırına ulaşıldı veya hız sınırlaması uygulandı | Pencere sıfırlanmasını bekleyin (`Retry-After` başlığına bakın) veya [yükseltin](plans.md) |
| `400` | Hatalı istek | JSON / parametrelerinizi kontrol edin — [`max_tokens`](#max_tokens-and-reasoning) ve [`n`](#multiple-completions-n) bölümlerine bakın |
| `5xx` | Yukarı akış/sağlayıcı aksaması | Geri çekilme (backoff) ile yeniden deneyin |

!!! info "Sağlayıcı ayrıntıları tasarım gereği gizlidir"
    Hata mesajları, altta yatan model sağlayıcısını sızdırmamak için temizlenir.
    Her zaman Claudin.io markalı, OpenAI biçimli hatalar görürsünüz.

### Bütçe sınırına ulaşma

Geçerli pencerenin harcama korumasını tükettiğinizde, istekler pencere
sıfırlanana kadarki saniyeleri veren bir `Retry-After` başlığıyla `429`
döndürür. Panonuz tam sıfırlanma zamanını ve kalan bütçeyi gösterir. Hemen
yeniden denemek yerine bu başlığa göre bekleyin. Pencerelerin nasıl çalıştığı
için [Planlar ve limitler](plans.md) bölümüne bakın.

## Hız sınırlama

Claudin.io normal kullanımı kesin olarak engellemez. Kötüye kullanılan istek
hızları reddedilmek yerine *yavaşlatılır* (şeffaf bir kısma mekanizması),
böylece düzgün davranan istemciler asla cezalandırılmaz. Pratikte hiçbir şey
yapmanıza gerek yok — nadir görülen `429` durumunda yalnızca yeniden deneyin.
