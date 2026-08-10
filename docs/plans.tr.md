# Planlar ve limitler

Her Claudin.io planı, **harcama koruma limiti** ile birlikte **sınırsız kullanım** sunar.
Token veya istek başına faturalandırılmazsınız — sabit bir aylık ücret öder ve
özgürce kullanırsınız. Limit yalnızca kontrolden çıkmış bir ajanın (örneğin sonsuz araç döngüsü)
planınızı tüketmesini önlemek için vardır.

## Planlar

| Plan | Fiyat | Harcama koruması | En uygun |
| --- | --- | --- | --- |
| **Lite** | $9 / ay | $1.00 / saat | Hobi projeleri, ara sıra kodlama |
| **Essential** | $19 / ay veya $189 / yıl | $2.00 / saat | Günlük kullanım için kaliteli |
| **Pro** ★ | $39 / ay veya $389 / yıl | $4.00 / saat | Yoğun ajan iş akışları |
| **Ultra** | $99 / ay veya $989 / yıl | $10.00 / saat | Maksimum güç, ekipler ve üretim |

!!! tip "Çoğu kişi asla limite ulaşmaz"
    Saatlik limit, normal etkileşimli çalışma için cömerttir. Genellikle yalnızca
    bir ajan sıkı bir döngüye girdiğinde buna yaklaşırsınız — ki bu tam da bir
    fren istediğiniz andır.

## Hangi modeli seçmelisiniz? Claudinio vs Claudius

Kodlama ajanınız için iki ana model sunuyoruz:

| Model | Arka uç | Kullanım alanı | Önerilen |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Hızlı, dengeli, uygun maliyetli | Günlük kodlama, hobi projeleri, genel kod | **Tüm planlar** (Lite'dan Ultra'ya) |
| **claudius** ★ | Premium, derin muhakeme | Karmaşık görevler, derin muhakeme, yoğun ajan iş akışları | **Pro ve Ultra** |
!!! warning "`claudius`, Pro ve Ultra'ya dahildir"
    **Lite** ve **Essential**'da `claudius` adını taşıyan bir istek reddedilmez — `claudinio` tarafından karşılanır ve `claudinio` tarifesinden faturalandırılır. Ajanınız çalışmaya devam eder ve premium tarife, onu içermeyen bir planda size asla yansıtılmaz.

    **Pro** ve **Ultra**'da şunu unutmayın: limit **istek sayısıyla değil, dolarla** ölçülür; aynı iş `claudius` üzerinde yaklaşık altı katını harcar. Pro'da (4 $/saat) bu, saat dolmadan yaklaşık 70 premium istek demektir; Ultra'da (10 $/saat) yaklaşık 175. Varsayılanı `claudinio` bırakın ve gerçekten akıl yürütme gerektiğinde `claudius`'a geçin.

### Açık konuşma

Eğer **Lite** ($9) planındaysanız — **`claudinio` kullanın ve arkanıza bakmayın.** 🎯

İşte gerçek: `claudinio`, günlük kodlamada Claude Sonnet ile karşılaştırılabilir kaliteyi **iç maliyetin çok küçük bir kısmına** sunar. Lite planında onunla **saatte yüzlerce istek** yapabilirsiniz — her planın etrafında kurulduğu model bu yüzden odur.

| Metrik | claudinio | claudius |
| --- | --- | --- |
| Saatlik bütçeye etkisi | Düşük — çok daha uzun süre dayanır | Yüksek — istek başına 6x |
| Kullanım alanı | Günlük kodlama, kişisel projeler | Yoğun muhakeme, karmaşık ajanlar |

**Altın kural:** Ajanınızı (Claude Code, Cursor, Continue, vb.) varsayılan model olarak `claudinio` ile yapılandırın. Yalnızca daha fazla muhakeme gücüne açıkça ihtiyacınız olduğunda  `claudius`'a geçin. Hobi projeleri için `claudinio` **ihtiyacınız olan her şey** ve muhtemelen **beklediğinizden fazlasıdır**.

> 💡 İpucu: Her iki model de tüm büyük kodlama ajanlarıyla çalışır. Ajan yapılandırmanızda `model=claudinio` ayarlayın — Pro ya da Ultra'daysanız `model=claudius`. `claudinio` ayrıca `claude-sonnet-4`, `gpt-4o`, `o3-mini` gibi onlarca takma adı otomatik çözer — ajanınızın yapılandırmasını değiştirmenize gerek yok.

## Harcama koruması nasıl çalışır

Her plan bir bütçe **penceresi** tanımlar — kayan bir dönem ve bu dönem içindeki maksimum harcama:

- **Lite**, **Essential**, **Pro** ve **Ultra** **1 saatlik** bir pencere kullanır.

Pencere içinde kullanımınız küçük bir iç maliyet biriktirir. Bu iç maliyet pencerenin limitine ulaştığında, pencere sıfırlanana kadar istekler duraklatılır.

Proxy üzerinden yalnızca model çağrılarınız yapılır. Her istek, kullandığı tokenlara göre mevcut pencerenin devam eden toplamına eklenir. Pencere sıfırlandığında, toplam da onunla birlikte sıfırlanır.

Limite ulaşıp bir bütçe hatası alırsanız, iki seçeneğiniz vardır:

1. Pencerenin sıfırlanmasını bekleyin (panonuzda gösterilir).
2. Daha büyük bir limit için daha yüksek bir plana yükseltin.

Bütçe hatasının nasıl göründüğü için [Planlarla ilgili hatalar](api-reference.md#errors) bölümüne bakın.