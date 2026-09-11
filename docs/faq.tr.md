# FAQ

## Claudin.io tam olarak nedir?

AI kodlama ajanları için bir API proxy'si. Sabit bir aylık abonelik ödersiniz ve Claude Code, Kilo, Zed, Codex, Cursor veya herhangi bir OpenAI istemcisine ekleyebileceğiniz OpenAI/Anthropic uyumlu bir API anahtarı alırsınız. Token başına ücretlendirme yok.

## Gerçekten sınırsız mı?

Kullanım sınırsızdır — istek sayacı veya token ölçer yoktur. Tek sınır, kontrolden çıkan bir ajanın planınızı tüketmesini önleyen zaman dilimi başına bir **harcama koruma limitidir**. Normal etkileşimli çalışmada nadiren bu limite ulaşırsınız. Bkz. [Planlar ve limitler](plans.md).

## Kodlama dışındaki işler için kullanabilir miyim?

API, OpenAI uyumludur; teknik olarak her istek çalışır. Ancak hizmet **yapay
zekâ ile programlama** için üretilmiştir: yönlendirme, prompt'lar ve önbellek
kodlama ajanlarına göre ayarlanmıştır. Programlamayla ilgili olmayan etkinlikler
— genel sohbet botları, kodlama dışı otomasyon — özel yönlendirme alabilir ve
kodlama trafiğinden farklı bir model veya katmanla sunulabilir.

## Hangi modeli kullanmalıyım?

Her zaman **`claudinio`** (veya `provider/model` formunu isteyen istemciler için `claudinio/claudinio`). Temel URL `https://api.claudin.io` şeklindedir.

## `Authorization` veya `x-api-key` ile mi kimlik doğrulaması yapıyorum?

Her ikisi de çalışır. `Authorization: Bearer API_ANAHTARINIZ` veya `x-api-key: API_ANAHTARINIZ`.

## Listede olmayan bir araçla kullanabilir miyim?

Evet — özel bir OpenAI temel URL'si ayarlamanıza izin veren herhangi bir araç çalışır. [Genel OpenAI kurulumunu](clients/openai-compatible.md) kullanın.

## Araç / fonksiyon çağrısını destekliyor mu?

Evet. Bu nedenle ajan editörlerin içinde çalışır. OpenAI API'sinde olduğu gibi `tools` parametresini geçirin ve `tool_calls` okuyun.

## Görselleri, sesi veya videoyu işleyebilir mi?

Evet, şeffaf bir şekilde. Standart OpenAI içerik blokları gönderin; proxy, model bunları görmeden önce görselleri/sesi/videoyu metin açıklamalarına veya transkripsiyonlara dönüştürür. Yapılandırmanız gereken özel bir şey yok.

## Bağlam penceresi nedir?

256K token.

## Nasıl yükseltebilir veya iptal edebilirim?

[Panelinizden](https://claudin.io/dashboard). Yükseltmeler (Stripe üzerinden) anında uygulanır. İptal ederseniz, zaten ödediğiniz dönemin sonuna kadar ücretli planınızda kalırsınız, ardından otomatik olarak Ücretsiz plana düşersiniz.

## İade alabilir miyim?

**İlk ödemenizden itibaren 48 saat içinde**, evet — hesabınızın e-posta
adresinden [support@claudin.io](mailto:support@claudin.io) adresine yazın.
Abonelik derhal sona erer ve ödediğiniz tutarı, bu süre içinde hesabınızın
yaptığı model kullanımının maliyetini karşılayan bir kullanım ve işlem ücreti
düşülerek geri alırsınız (asla ödediğinizden fazla değil). Bir gün denediniz ve
size göre değil miydi? Neredeyse tamamını geri alırsınız. İki gün boyunca saatlik
tavanda mı çalıştırdınız? Az ya da hiç bekleyin. 48 saat sonra iade yoktur; iptal
etmek planınızı ödenmiş dönemin sonuna kadar korur. Tam metin
[Şartlar](https://claudin.io/terms) sayfasında.

## Bir bütçe hatasıyla karşılaştım. Şimdi ne yapmalıyım?

Mevcut zaman diliminin harcama koruma limitine ulaştınız. Dilimin sıfırlanmasını bekleyin (paneliniz ne zaman sıfırlanacağını gösterir) veya daha büyük bir limit için [yükseltin](plans.md).

## Bir istek 401 hatasıyla başarısız oldu.

Anahtarınız eksik veya yanlış. Panelden yeniden kopyalayın ve fazladan boşluk olmadığından ve kimlik doğrulama başlığının ayarlandığından emin olun.

## Anahtarım sızdı. Ne yapmalıyım?

Panelden iptal edin ve hemen yeni bir tane oluşturun. Anahtarlara şifreler gibi davranın — asla depoya göndermeyin veya herkese açık olarak paylaşmayın.

## Nereden yardım alabilirim?

[Panelinizdeki](https://claudin.io/dashboard) **Destek** kartından bir talep açın veya desteğe e-posta gönderin. Size geri döneceğiz.