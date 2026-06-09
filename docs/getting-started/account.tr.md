# Hesabınızı oluşturun

Çalışan bir API anahtarı almak yaklaşık bir dakika sürer.

## 1. GitHub ile oturum açın

**[claudin.io](https://claudin.io)** adresine gidin ve **GitHub ile oturum aç** seçeneğine tıklayın.
Claudin.io, giriş için GitHub'ı kullanır — ayrı bir şifre yönetmeniz gerekmez.

İlk kez oturum açtığınızda, hesabınız otomatik olarak **Ücretsiz** planda oluşturulur,
böylece herhangi bir ödeme yapmadan deneyebilirsiniz.

## 2. API anahtarınızı oluşturun

[Panele](https://claudin.io/dashboard) giriş yaptıktan sonra:

1. **API Anahtarları** kartını bulun.
2. **Anahtar oluştur** (veya **Yeni anahtar oluştur**) seçeneğine tıklayın.
3. Anahtarı kopyalayın — `sk-...` şeklinde görünecektir.

!!! warning "Anahtarınızı bir parola gibi koruyun"
    API anahtarınız, planınızın bütçesine erişim sağlar. Bunu bir depoya göndermeyin,
    halka açık bir sohbette yapıştırmayın veya paylaşmayın. Bir anahtar sızarsa,
    panel üzerinden iptal edin ve yeni bir tane oluşturun.

## 3. İhtiyacınız olacak iki değeri not edin

Her entegrasyon aynı iki şeye ihtiyaç duyar:

| Değer | Açıklama |
| --- | --- |
| **Temel URL** | `https://api.claudin.io` |
| **Model** | `claudinio` |
| **API anahtarı** | az önce kopyaladığınız `sk-...` |

Bu kadar. Ardından, çalıştığını doğrulamak için [ham bir API çağrısı yapabilir](first-call.md)
veya doğrudan [aracınızı bağlamaya](../clients/claude-code.md) geçebilirsiniz.

---

## Plan seçme

Denemek için **Ücretsiz** planda kalabilirsiniz. Daha fazla alana hazır
olduğunuzda, panel üzerinden yükseltme yapın — ayrıntılı döküm için [Planlar & limitler](../plans.md)
sayfasına bakın.

Yükseltmeler Stripe üzerinden gerçekleştirilir ve anında etkili olur.