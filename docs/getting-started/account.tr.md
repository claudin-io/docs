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

!!! uyarı "Anahtarınıza bir parola gibi davranın"
    API anahtarınız, planınızın bütçesine erişim sağlar. Bunu bir depoya eklemeyin, herkese açık bir sohbette yapıştırmayın veya paylaşmayın. Bir anahtar sızarsa, kontrol panelinden iptal edin ve yeni bir tane oluşturun.

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

Denemek için **Ücretsiz** planda kalabilirsiniz. Daha fazla alana hazır olduğunuzda, kontrol panelinden yükseltme yapın — tam döküm için [Planlar ve limitler](../plans.md) bölümüne bakın.

Yükseltmeler Stripe üzerinden yapılır ve hemen etkili olur.