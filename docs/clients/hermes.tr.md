[Hermes Agent](https://github.com/NousResearch/hermes-agent), Nous Research
tarafından geliştirilmiş açık kaynak bir terminal ajanıdır. OpenAI uyumlu tüm
uç noktaları destekler, bu da onu Claudin.io için mükemmel bir seçenek yapar.

## Sihirbazla hızlı başlangıç

Aktif bir Hermes oturumundan çıkın (`Ctrl + C` veya `/quit`), ardından çalıştırın:

```bash
hermes model
```

Menüden **Custom endpoint** seçin ve doldurun:

| Alan | Değer |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | `sk-...` anahtarınız |
| Model name | `claudinio` |

Hermes yapılandırmayı otomatik olarak `~/.hermes/config.yaml` dosyasına kaydeder.

Deneyin:

```bash
hermes
```

## Manuel yapılandırma

`~/.hermes/config.yaml` dosyasını düzenleyin:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-anahtariniz"
  default: "claudinio"
```

Veya değerleri doğrudan ayarlayın:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Doğrulayın:

```bash
hermes config check
hermes config show
```

> **İpucu:** Karmaşık araç çağrısı görevleri için Hermes Agent'ınızın en az
> 64K token bağlamlı bir model kullandığından emin olun (Claudinio bunu destekler).

## Sorun giderme

| Sorun | Çözüm |
| --- | --- |
| Kimlik doğrulama hatası | `hermes doctor` ile API anahtarını kontrol edin |
| Model bulunamadı | Model adının tam olarak `claudinio` olduğundan emin olun |
| Bağlantı reddedildi | `https://api.claudin.io/v1` adresine erişilebildiğini doğrulayın |

## Kullanışlı komutlar

| Komut | Açıklama |
| --- | --- |
| `hermes config show` | Mevcut yapılandırmayı görüntüle |
| `hermes config edit` | Etkileşimli düzenleme |
| `hermes doctor` | Sorunları teşhis et |
| `hermes model` | Sağlayıcı değiştir |
