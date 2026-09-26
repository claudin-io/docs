# SSS

## Claudin.io tam olarak nedir?

Yapay zekâ kodlama ajanları için bir API proxy'si. Aylık bir plan ödersiniz,
her ay dolan bir kredi cüzdanı ve Claude Code, Kilo, Zed, Codex, Cursor veya
herhangi bir OpenAI istemcisinde kullanabileceğiniz OpenAI/Anthropic uyumlu
bir API anahtarı alırsınız. Tipik bir kodlama isteği yaklaşık bir kredidir.
Token başına fatura yok, saatlik sınır yok.

## Bir sınır var mı?

Yalnızca cüzdanınız. Saatlik sınır, oturum sınırı veya haftalık kota yok —
ajanınızı durduran tek şey boş bir bakiyedir ve bir yükleme bunu anında çözer.
Kullanmadığınız krediler cüzdanda kalır ve asla sona ermez. Bkz.
[Planlar ve krediler](plans.md).

## Neden sabit fiyat yerine krediler?

Çünkü sabit fiyatlı planların saatlik sınırını gerçek trafikte ölçtük ve
Pro'daki her 10 aktif saatten 1'ini kesiyordu — görevinin ortasındaki
insanları, kontrolden çıkmış döngüleri değil. İhtiyacınız olduğunda
kullanamayacağınız kapasiteyi satan bir plan yanlış biçimdedir. Krediler
gördüğünüz bir sayıdır, sakin saatlerin ödediği yoğun bir saattir ve bir
bekleme yerine bir yükleme uzağındaki yoğun bir aydır.

## Kodlama dışı işler için kullanabilir miyim?

API OpenAI uyumludur, dolayısıyla teknik olarak her istek çalışır. Ama hizmet
**yapay zekâ ile programlama** için kurulmuştur: yönlendirme, istemler ve
önbellek kodlama ajanları için ayarlanmıştır. Programlamayla ilgisi olmayan
etkinlik — genel sohbet botları, kodsuz otomasyon — özel yönlendirme alabilir
ve kodlama trafiğinden farklı bir model veya katmanla sunulabilir.

## Hangi modeli kullanıyorum?

Varsayılan olarak **`claudinio`** (`sağlayıcı/model` biçimini isteyen
istemciler için `claudinio/claudinio`). Temel URL `https://api.claudin.io`.
Kod için ayarladığımız, ölçtüğümüz ve önbelleğe aldığımız modeldir ve
kredilerinizin en uzağa gittiği modeldir.

## Başka bir model seçebilir miyim?

Evet, adıyla. `claudius` premium seçeneğimizdir, 6× krediye kadar.
[Katalog](plans.md#catalogue) sekiz üçüncü taraf model ekler — Claude Sonnet
5 ve Haiku 4.5, Gemini 3.1 Pro, Kimi K3, GLM 5.3, MiniMax M3, Qwen3 Coder —
her biri `claudinio` kredilerinin sabit bir katı olarak fiyatlanır, 3× ile
22× arası. Kimliği istemcinizde ayarlayın; yalnızca o istek katı öder. Her
model her plandadır; hâlâ `claudinio` öneriyoruz.

## `Authorization` ile mi yoksa `x-api-key` ile mi kimlik doğrularım?

İkisi de çalışır. `Authorization: Bearer YOUR_API_KEY` veya
`x-api-key: YOUR_API_KEY`.

## Listede olmayan bir araçla kullanabilir miyim?

Evet — özel bir OpenAI temel URL'si ayarlamaya izin veren her araç çalışır.
[Genel OpenAI kurulumunu](clients/openai-compatible.md) kullanın.

## Araç / fonksiyon çağrısını destekliyor mu?

Evet. Ajan tabanlı editörlerde bu yüzden çalışır. OpenAI API'sinde olduğu gibi
`tools` geçirin ve `tool_calls` okuyun.

## Görsel, ses veya video işleyebilir mi?

Evet, şeffaf biçimde. Standart OpenAI içerik blokları gönderin; proxy,
görsel/ses/videoyu model görmeden önce metin açıklamalarına veya
transkripsiyonlara dönüştürür. Yapılandırılacak özel bir şey yok.

## Bağlam penceresi ne kadar?

256K token.

## Nasıl yükseltir veya iptal ederim?

[Panelinizden](https://claudin.io/dashboard). Yükseltmeler anında uygulanır
(Stripe üzerinden). İptal ederseniz ödenmiş planınızı ödenmiş dönemin sonuna
kadar korursunuz. Cüzdanda zaten olan krediler sizindir ve plan bittikten
sonra da çalışmaya devam eder.

## Geri ödeme alabilir miyim?

**İlk ödemenizden itibaren 48 saat içinde** evet — hesabınızın e-postasından
[support@claudin.io](mailto:support@claudin.io) adresine yazın. Abonelik
hemen sona erer ve ödediğiniz tutarı, hesabınızın o süredeki model kullanım
maliyetini karşılayan bir kullanım ve işlem ücreti düşülerek (asla
ödediğinizden fazla değil) geri alırsınız. Bir gün denediniz ve size göre
değil miydi? Neredeyse tamamını geri alırsınız. Tüm ayın kredilerini iki günde
mi harcadınız? Az ya da hiç beklemeyin. 48 saatten sonra geri ödeme yoktur;
iptal, planınızı ödenmiş dönemin sonuna kadar korur. Tam metin
[Koşullarda](https://claudin.io/terms).

## `402 insufficient_credits` aldım. Şimdi ne olacak?

Cüzdanınız boş. Panelden bir [yükleme](plans.md#top-ups) satın alın veya daha
büyük bir plana geçin — ikisi de anında uygulanır. Hiçbir şey kuyruğa alınmadı
ve başarısız istek için hiçbir şey ücretlendirilmedi.

## Eski Essential / Pro / Ultra planıma ne olur?

Tam olarak eskisi gibi çalışmaya devam eder: aynı fiyat, aynı saatlik sınır ve
normal şekilde yenilenir. Panelden Essential, Pro ve Ultra arasında hâlâ geçiş
yapabilirsiniz ve API anahtarınız değişmez. Saatlik sınırlı planlar `claudinio`
kullanır; `claudius` ve model kataloğu kredi planlarıyla gelir, bu yüzden
saatlik sınırlı bir planda bunları adlandıran bir istek `claudinio` tarafından
karşılanır. Bkz. [Eski planlar](plans.md#legacy-plans).

## Bir istek 401 ile başarısız oldu.

Anahtarınız eksik veya yanlış. Panelden yeniden kopyalayın ve fazladan boşluk
olmadığından ve kimlik doğrulama başlığının ayarlandığından emin olun.

## Anahtarım sızdı. Ne yapmalıyım?

Panelden iptal edin ve hemen yenisini oluşturun. Anahtarlara parola gibi
davranın — asla commit etmeyin ve herkese açık paylaşmayın.

## Nereden yardım alabilirim?

[Panelinizdeki](https://claudin.io/dashboard) **Destek** kartından bir bilet
açın veya desteğe e-posta gönderin. Size geri döneriz.
