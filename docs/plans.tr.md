# Planlar ve limitler

Her Claudin.io planı, **harcama koruma sınırı** olan **sınırsız kullanımdır**.
Token veya istek başına faturalandırılmazsınız — sabit bir aylık ücret öder ve
özgürce kullanırsınız. Sınır, yalnızca kontrolden çıkmış bir aracın (örneğin sonsuz
bir araç döngüsü) planınızı tüketmesini durdurmak için vardır.

## Planlar

| Plan | Fiyat | Harcama koruması | En iyi için |
| --- | --- | --- | --- |
| **Başlangıç** | $5 / ay | $0.50 / saat | Denemek — düşük taahhüt |
| **Hafif** | $9 / ay | $1.00 / saat | Hobi projeleri, ara sıra kodlama |
| **Temel** | $19 / ay veya $189 / yıl | $2.00 / saat | Günlük kodlama — popüler seçim |
| **Pro** ★ | $39 / ay veya $389 / yıl | $4.00 / saat | Ağır ajan iş akışları |
| **Güçlü** | $59 / ay veya $589 / yıl | $6.00 / saat | Ekipler, çoklu projeler |
| **Ultra** | $99 / ay veya $989 / yıl | $10.00 / saat | Maksimum güç, ekipler ve üretim |

!!! ipucu "Çoğu insan asla sınıra ulaşmaz"
    Saatlik sınır normal etkileşimli çalışma için cömerttir. Genellikle yalnızca bir
    ajan dar bir döngüye girdiğinde takılırsınız — tam da bir fren *istediğiniz* zaman.

## Harcama koruması nasıl çalışır

Her plan bir bütçe **penceresi** tanımlar — kayan bir süre ve içinde maksimum harcama:

- **Başlangıç**, **Hafif**, **Temel**, **Pro**, **Güçlü** ve **Ultra** bir **1 saatlik** pencere kullanır.

Pencere içinde, kullanımınız küçük bir iç maliyet biriktirir. Bu iç maliyet pencerenin
sınırına ulaştığında, pencere sıfırlanana kadar istekler duraklatılır.

Yalnızca model çağrılarınız proxy üzerinden geçer. Her istek, kullanılan tokenlara
dayanarak mevcut pencerenin toplamına eklenir. Pencere sıfırlandığında, toplam da sıfırlanır.

Sınıra ulaşıp bütçe hatası alırsanız, iki seçeneğiniz vardır:

1. Pencerenin sıfırlanmasını bekleyin (panelinizde gösterilir).
2. Daha büyük bir sınır için üst plana yükseltin.

Bütçe hatasının nasıl göründüğü için [Planla ilgili hatalar](api-reference.md#errors) bölümüne bakın.
