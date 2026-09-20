# Hesabınızı oluşturun

Çalışan bir API anahtarı almak yaklaşık bir dakika sürer.

## 1. GitHub ile oturum açın

**[claudin.io](https://claudin.io)** adresine gidin ve **GitHub ile oturum açın**'a tıklayın.
Claudin.io, giriş için GitHub'ı kullanır — ayrı bir parola yönetmeniz gerekmez.

İlk kez oturum açtığınızda, hesabınız otomatik olarak **Ücretsiz** planda oluşturulur, böylece hiçbir şey ödemeden deneyebilirsiniz.

## 2. API anahtarınızı oluşturun

[Dashboard](https://claudin.io/dashboard) sayfasına girdikten sonra:

1. **API Anahtarları** kartını bulun.
2. **Anahtar oluştur** (veya **Yeni anahtar oluştur**) seçeneğine tıklayın.
3. Anahtarı kopyalayın — `sk-...` şeklinde görünür.

!!! warning "Anahtarınıza bir parola gibi davranın"
    API anahtarınız planınızın kredilerini harcar. Bir depoya commit etmeyin,
    herkese açık bir sohbete yapıştırmayın ve paylaşmayın. Bir anahtar sızarsa
    panelden iptal edin ve yenisini oluşturun.

## 3. İhtiyacınız olacak iki değeri not edin

Her entegrasyon aynı iki şeye ihtiyaç duyar:

| Değer | Ne olduğu |
| --- | --- |
| **Temel URL** | `https://api.claudin.io` |
| **Model** | `claudinio` |
| **API anahtarı** | az önce kopyaladığınız `sk-...` |

Bu kadar. Şimdi, çalıştığını doğrulamak için [ham bir API çağrısı yapın](first-call.md) veya doğrudan [aracınızı bağlama](../clients/claude-code.md) bölümüne geçin.

---

## Bir plan seçme

Denemek için **Free**'de kalabilirsiniz. Hazır olduğunuzda panelden bir plan
seçin — her ay dolan bir kredi cüzdanı, $19'dan başlayan — tam resim için bkz.
[Planlar ve krediler](../plans.md).

Yükseltmeler Stripe üzerinden yapılır ve hemen etkili olur.