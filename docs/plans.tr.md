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

## claudinio vs Claudius

|                      | claudinio 🏆         | claudius ★           |
| -------------------- | -------------------- | -------------------- |
| **Starter**          | ✅                   |                      |
| **Lite**             | ✅                   |                      |
| **Essential**        | ✅                   | ✅                   |
| **Pro**              | ✅                   | ✅                   |
| **Power**            | ✅                   | ✅                   |
| **Ultra**            | ✅                   | ✅                   |

> ** Paranızın karşılığını en iyi veren seçenek.**

### Starter / Lite için: claudinio kullanın

Starter veya Lite kullanıyorsanız, kullanacağınız model claudinio'dur. Ve dürüst olmak gerekirse? Geriye bakmanıza gerek yok. claudinio, öncü modellerle rekabet ederken fiyatının çok küçük bir kısmına mal oluyor — günlük kodlama, öğrenme ve hobi projeleri için mükemmel.

### Essential ve üzeri için: dünya sizin

Essential ve üzeri planlar size hem claudinio hem de claudius'a erişim sağlar. Günlük görevleriniz için claudinio'yu kullanın ve claudius'u ekstra kıvılcıma ihtiyacınız olduğunda saklayın — karmaşık mimari, derin mantıksal akıl yürütme veya zor hata ayıklama oturumları.

### Ama işte altın kural

Hangi planda olursanız olun, claudinio'yu varsayılan modeliniz yapmanızı öneririz. Bu bizim amiral gemimiz ve ona inanıyoruz. Görev gerektirdiğinde her zaman claudius'a geçebilirsiniz.

### Model takma adları

Tüm planlar popüler modeller için takma adları destekler: `claude-sonnet-4`, `gpt-4o`, `gemini-2.5-pro`, `llama-4`, `deepseek-v4`. Tam liste için [API Reference](/api-reference/) sayfamıza bakın.

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
