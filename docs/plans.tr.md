# Planlar ve limitler

Her Claudin.io planı, **harcama koruma limiti** ile birlikte **sınırsız kullanım** sunar.
Token veya istek başına faturalandırılmazsınız — sabit bir aylık ücret öder ve
özgürce kullanırsınız. Limit yalnızca kontrolden çıkmış bir ajanın (örneğin sonsuz araç döngüsü)
planınızı tüketmesini önlemek için vardır.

## Planlar

| Plan | Fiyat | Harcama koruması | En uygun |
| --- | --- | --- | --- |
| **Starter** | $5 / ay | $0.50 / saat | Deneme amaçlı — düşük taahhüt |
| **Lite** | $9 / ay | $1.00 / saat | Hobi projeleri, ara sıra kodlama |
| **Essential** | $19 / ay veya $189 / yıl | $2.00 / saat | Günlük kullanım için kaliteli |
| **Pro** ★ | $39 / ay veya $389 / yıl | $4.00 / saat | Yoğun ajan iş akışları |
| **Power** | $59 / ay veya $589 / yıl | $6.00 / saat | Ekipler, birden çok proje |
| **Ultra** | $99 / ay veya $989 / yıl | $10.00 / saat | Maksimum güç, ekipler ve üretim |

!!! tip "Çoğu kişi asla limite ulaşmaz"
    Saatlik limit, normal etkileşimli çalışma için cömerttir. Genellikle yalnızca
    bir ajan sıkı bir döngüye girdiğinde buna yaklaşırsınız — ki bu tam da bir
    fren istediğiniz andır.

## Hangi modeli seçmelisiniz? Claudinio vs Claudius

Kodlama ajanınız için iki ana model sunuyoruz:

| Model | Arka uç | Kullanım alanı | Önerilen |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Hızlı, dengeli, uygun maliyetli | Günlük kodlama, hobi projeleri, genel kod | **Tüm planlar** (Starter'dan Ultra'ya) |
| **claudius** ★ | Premium, derin muhakeme | Karmaşık görevler, derin muhakeme, yoğun ajan iş akışları | Essential+ (Pro, Power, Ultra) |

### Açık konuşma

Eğer **Starter** ($5) veya **Lite** ($9) planındaysanız — **`claudinio` kullanın ve arkanıza bakmayın.** 🎯

İşte gerçek: `claudinio`, günlük kodlama için Claude Sonnet'e benzer kaliteyi **iç maliyetin çok daha azıyla** sunar. Lite planında, `claudinio` ile **saatte yüzlerce istek** alabilirsiniz — oysa `claudius` saatlik bütçenizi çok daha hızlı tüketir.

| Metrik | claudinio | claudius |
| --- | --- | --- |
| Saatlik bütçeye etkisi | Düşük — çok daha uzun süre dayanır | Yüksek — daha hızlı tüketir |
| Kullanım alanı | Günlük kodlama, kişisel projeler | Yoğun muhakeme, karmaşık ajanlar |

**Altın kural:** Ajanınızı (Claude Code, Cursor, Continue, vb.) varsayılan model olarak `claudinio` ile yapılandırın. Yalnızca daha fazla muhakeme gücüne açıkça ihtiyacınız olduğunda — ve planınız buna izin veriyorsa (Essential+) — `claudius`'a geçin. Hobi projeleri için `claudinio` **ihtiyacınız olan her şey** ve muhtemelen **beklediğinizden fazlasıdır**.

> 💡 İpucu: Her iki model de tüm büyük kodlama ajanlarıyla çalışır. Ajan yapılandırmanızda `model=claudinio` veya `model=claudius` ayarını yapmanız yeterlidir. `claudinio` ayrıca `claude-sonnet-4`, `gpt-4o`, `o3-mini` ve düzinelerce takma adı otomatik olarak çözümler — ajan yapılandırmanızı değiştirmenize gerek yoktur.

## Harcama koruması nasıl çalışır

Her plan bir bütçe **penceresi** tanımlar — kayan bir dönem ve bu dönem içindeki maksimum harcama:

- **Starter**, **Lite**, **Essential**, **Pro**, **Power** ve **Ultra** **1 saatlik** bir pencere kullanır.

Pencere içinde kullanımınız küçük bir iç maliyet biriktirir. Bu iç maliyet pencerenin limitine ulaştığında, pencere sıfırlanana kadar istekler duraklatılır.

Proxy üzerinden yalnızca model çağrılarınız yapılır. Her istek, kullandığı tokenlara göre mevcut pencerenin devam eden toplamına eklenir. Pencere sıfırlandığında, toplam da onunla birlikte sıfırlanır.

Limite ulaşıp bir bütçe hatası alırsanız, iki seçeneğiniz vardır:

1. Pencerenin sıfırlanmasını bekleyin (panonuzda gösterilir).
2. Daha büyük bir limit için daha yüksek bir plana yükseltin.

Bütçe hatasının nasıl göründüğü için [Planlarla ilgili hatalar](api-reference.md#errors) bölümüne bakın.