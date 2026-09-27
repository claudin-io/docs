# Planlar ve krediler

Her Claudin.io planı, her ay dolan bir **kredi cüzdanıdır**. Bir istek,
kullandığı token kadar kredi harcar — `claudinio` üzerinde tipik bir kodlama
isteği yaklaşık **bir kredi**. **Planınızın kredileri her ay yenilenir — o
ayın hakkıdır ve birikmez. Yükleme olarak satın aldığınız krediler asla sona
ermez. Saatlik bir sınır yoktur.**

## Planlar

| Plan | Fiyat | Kredi / ay | Kimin için |
| --- | --- | --- | --- |
| **Start** | $19 / ay | 3.000 | Denemek, hafif günlük kullanım |
| **Solo** ★ | $39 / ay | 7.000 | Tek geliştirici, her gün |
| **Pro** | $99 / ay | 18.000 | Yoğun ajan iş akışları |
| **Studio** | $199 / ay | 36.000 | Birden fazla ajan, tüm gün |
| **Max** | $399 / ay | 72.000 | Üretim, ekipler, botlar |

Her kredi planı her modeli içerir: `claudinio`, `claudius` ve tüm
[katalog](#catalogue). Planlar yalnızca her ay kaç kredi geldiğiyle ayrılır —
ve plan büyüdükçe her kredi ucuzlar. Saatlik sınırlı eski planlar `claudinio`
kullanır — bkz. [Eski planlar](#legacy-plans).

!!! tip "Hangi plan ayınıza sığar"
    `claudinio` üzerinde tipik bir istek yaklaşık bir kredidir; binlerce gerçek
    istek üzerinde ölçüldü. Ajanınızın dolu bir günde gönderdiği istekleri
    sayın, 22 iş günüyle çarpın ve onu içine alan basamağı seçin. İki basamak
    arasındaysanız küçüğünü alın — ara sıra gelen yoğun ayı bir yükleme
    karşılar.

### Yüklemeler {#top-ups}

Bir sonraki ay gelmeden daha fazlasına mı ihtiyacınız var? Bir **yükleme**,
aynı cüzdana anında kredi ekler, her planda:

| Yükleme | Kredi |
| --- | --- |
| $10 | 1.200 |
| $25 | 3.000 |
| $50 | 6.000 |

Yükleme kredileri plan kredilerinizle aynı cüzdana girer ve her model onları
harcar. İstekler önce o ayın plan kredilerini harcar; satın aldığınız yükleme
kredileri korunur ve asla sona ermez.

## Neden krediler (ve neden saatlik sınır yok)

Planlarımız, **saatlik bir harcama tavanı** olan sabit bir fiyattı — döngüye
takılmış bir ajana karşı bir fren, diyorduk. Bir şeyi değiştirmeden önce bunu
üç günlük gerçek trafikte ölçtük: **Pro'daki her 10 aktif saatten 1'i**
(%11,1) tavanın bir geliştiriciyi görevinin ortasında kesmesiyle bitiyordu ve
Essential'da 13'te 1'i. Bunlar sonsuz döngüler değildi. Çalışan insanlardı.

İhtiyacınız olduğunda kullanamayacağınız kapasiteyi satan bir plan yanlış
biçimdedir. Bu yüzden tavan kalktı. Bir plan, aylık bir kredi sayısıdır; yoğun
bir saati sakin saatler öder; yoğun bir ay, bir bekleme yerine bir yükleme
uzağındadır. Ajanınızı durduran tek şey boş bir cüzdandır ve panel bakiyeyi
her zaman gösterir.

## Bir kredi ne alır

Bir kredi her eksende aynı değerdedir. `claudinio` üzerinde:

| | 1M token başına kredi |
| --- | --- |
| Girdi (önbellek ıskası) | 40 |
| Girdi (önbellek isabeti) | 6 |
| Çıktı | 80 |

Bir ajanın tokenlarının neredeyse tamamı istem tokenlarıdır ve bir çalışma
oturumunda neredeyse tamamı önbellekten gelir — bu yüzden tipik bir istek bir
krediye yakın düşer ve bu yüzden uzun oturumlar istek başına kısalardan
ucuzdur.

## Hangi model? `claudinio`, `claudius` ve katalog

| Model | Nedir | Kredi maliyeti | Dahil olduğu planlar |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Kod için ayarladığımız, ölçtüğümüz ve önbelleğe aldığımız model | 1× — istek başına yaklaşık bir kredi | Her plan |
| **claudius** ★ | Derin akıl yürütme için premium seçeneğimiz | claudinio kredilerinin 6x katına kadar (3× girdi, 4× çıktı, 6× önbellek okuma) | Her kredi planı (Start, Solo, Pro, Studio, Max) |

**Önerimiz `claudinio`.** Her planın etrafında kurulduğu model: istemi onun
için ayarlıyoruz, her değerlendirme onu puanladı ve bir kredi onunla en uzağa
gider. Gördüğümüz en etkili yapılandırma, **`claudius` ile planlamak,
`claudinio` ile uygulamak** — akıl yürütme, premium modelin katını hak ettiği
yer; uygulama döngüsü ise hacmin olduğu yer.

### Katalog: bir modeli adıyla seçin {#catalogue}

Üçüncü taraf bir modeli adıyla da isteyebilirsiniz. Bir katalog modeli
**ham** sunulur — sağlayıcının modeli, kendi istemcinizin sistem istemi,
Claudinio ayarı yok — ve her eksende `claudinio` kredilerinin sabit bir tam
sayı katına mal olur, böylece fiyat tek bir sayı olarak okunur:

| Model kimliği | Model | Sağlayıcı | `claudinio`'ya göre kredi |
| --- | --- | --- | --- |
| `deepseek-v4.1-flash` | DeepSeek V4.1 Flash | DeepSeek | 2× |
| `mimo-v2.6-pro` | MiMo V2.6 Pro | Xiaomi | 2× |
| `gpt-6-luna` | GPT-6 Luna | OpenAI | 2× |
| `glm-5.3-flash` | GLM 5.3 Flash | Z.ai | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `gemini-3.8-flash` | Gemini 3.8 Flash | Google | 9× |
| `glm-5.3` | GLM 5.3 | Z.ai | 20× |
| `gpt-6-sol` | GPT-6 Sol | OpenAI | 23× |
| `grok-4.7` | Grok 4.7 | xAI | 29× |
| `kimi-k3` | Kimi K3 | Moonshot | 33× |
| `opus-5.5` | Claude Opus 5.5 | Anthropic | 36× |

İstemcinizde `model=kimi-k3` (veya yukarıdaki herhangi bir kimlik) ayarlayın;
yalnızca o istek katı öder — oturumun geri kalanı `claudinio` tarifesinden
devam eder. Her katalog modeli her planda kullanılabilir.

!!! note "Neden hâlâ `claudinio` öneriyoruz"
    Katalog, seçmek isteyen geliştirici için vardır; herhangi bir girdi kodda
    daha iyi ölçüldüğü için değil. `claudinio`, değerlendirmelerimizin
    karşılaştırma modeli, istem önbelleğinin etrafında kurulduğu model ve —
    istek başına 2× ile 36× daha ucuz olarak — kredilerinizin en uzağa gittiği
    modeldir. Bir katalog modeline bilinçli olarak, ona ihtiyaç duyan görev
    için başvurun.

> 💡 İpucu: `claudinio`, kodlama ajanlarının varsayılan olarak gönderdiği
> takma adları da çözer — `claude-sonnet-4`, `gpt-4o`, `o3-mini` ve onlarcası —
> bu yüzden onu kullanmak için ajanınızın yapılandırmasını değiştirmeniz
> gerekmez.

## Cüzdan boşaldığında

İstekler `402` ve `insufficient_credits` koduyla yanıt verir (bkz.
[Hatalar](api-reference.md#errors)). Hiçbir şey kuyruğa alınmaz ve hiçbir şey
ücretlendirilmez. İki seçeneğiniz var, ikisi de anında:

1. [Panelden](https://claudin.io/dashboard) **bir yükleme satın alın**.
2. **Daha büyük bir plana geçin** — yeni ayın kredileri faturayla gelir.

Panel bakiyenizi, günün harcamasını ve oraya varmadan önce düşük bakiye
uyarısını gösterir; bakiye düştüğünde size bir kez e-posta göndeririz.

## Eski planlar (saatlik sınırlı Essential, Pro, Ultra) {#legacy-plans}

Yukarıdaki kredi planları yeni hesapların abone olduğu planlardır. Önceki
planlardan birine (Essential, Pro, Ultra) zaten
aboneyseniz, planınız **tam olarak eskisi gibi kalır: aynı fiyat, aynı saatlik
sınır ve normal şekilde yenilenmeye devam eder**.
[Panelden](https://claudin.io/dashboard) Essential, Pro ve Ultra arasında hâlâ
geçiş yapabilirsiniz, API anahtarınız değişmez ve [yüklemeler](#top-ups) her
zamanki gibi saatlik sınırın ötesindeki kullanımı karşılar.

Saatlik sınırlı eski planlar `claudinio` kullanır. `claudius` ve
[katalog](#catalogue) kredi planlarıyla gelir: saatlik sınırlı bir planda,
bunlardan birini adlandıran bir istek `claudinio` tarafından karşılanır —
reddedilmez ve hata döndürmez.
