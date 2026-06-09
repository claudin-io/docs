# Planlar ve sınırlar

Her Claudin.io planı, **harcama koruma sınırı** ile **sınırsız kullanım** sunar. Token başına veya istek başına fatura edilmezsiniz — sabit bir aylık ücret öder ve özgürce kullanırsınız. Sınır yalnızca kontrolden çıkmış bir aracının (örneğin sonsuz araç döngüsü) planınızı tüketmesini durdurmak için vardır.

## Planlar

| Plan | Fiyat | Harcama koruması | En uygun |
| --- | --- | --- | --- |
| **Ücretsiz** | $0 | $0.45 / gün | Denemek, hafif kullanım |
| **Hafif** | $5 / ay | $0.60 / saat | Hobi projeleri, ara sıra kodlama |
| **Temel** | $10 / ay | $1.50 / saat | Günlük kodlama — popüler seçim |
| **Pro** | $29 / ay | $4.00 / saat | Yoğun aracılı iş akışları |

!!! tip "Çoğu kişi sınıra asla ulaşmaz"
    Saatlik sınır, normal etkileşimli çalışma için cömerttir. Genellikle yalnızca bir aracı sıkı bir döngüye girdiğinde buna yaklaşırsınız — ki bu tam da bir fren istediğiniz andır.

## Harcama koruması nasıl çalışır

Her plan, bir bütçe **penceresi** tanımlar — hareketli bir dönem ve içinde maksimum harcama:

- **Ücretsiz** bir **24 saatlik** pencere kullanır (`$0.45/gün`).
- **Hafif / Temel / Pro** bir **1 saatlik** pencere kullanır.

Pencere içinde, kullanımınız küçük bir dahili maliyet biriktirir. Bu dahili maliyet pencerenin sınırına ulaştığında, pencere sıfırlanana kadar istekler durdurulur. Pencere sabit bir programla sıfırlanır (saatlik planlar için her saatin başında UTC) ve kalan bütçeniz **panonuzda canlı olarak** gösterilir.

Bu *harcama koruması*dır, ölçülen fatura değil — dolar rakamları koruma tavanıdır, ödediğiniz şey değil. Gerçek faturanız yalnızca sabit aylık aboneliktir.

## Yükseltme ve düşürme

- [Panodan](https://claudin.io/dashboard) istediğiniz zaman **yükseltebilirsiniz**. Ödeme Stripe üzerinden yapılır ve yeni limitler hemen uygulanır.
- Aynı yerden **düşürebilir veya iptal edebilirsiniz**. İptal ederseniz, önceden ödediğiniz dönemin sonuna kadar ücretli planınızı korur, ardından otomatik olarak **Ücretsiz**'e düşersiniz — hesabınız ve anahtarlarınız korunur.

## Sınırı ne etkiler?

Yalnızca proxy aracılığıyla yaptığınız model çağrıları. Her istek, kullandığı token'lara göre mevcut pencerenin devam eden toplamına eklenir. Pencere sıfırlandığında, toplam da onunla birlikte sıfırlanır.

Sınıra ulaşır ve bir bütçe hatası alırsanız, iki seçeneğiniz vardır:

1. Pencerenin sıfırlanmasını bekleyin (panonuzda gösterilir).
2. Daha büyük bir sınır için daha yüksek bir plana yükseltin.

Bütçe hatasının nasıl göründüğü için [Planlarla ilgili hatalar](api-reference.md#errors) bölümüne bakın.