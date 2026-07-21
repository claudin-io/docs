# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent), Nous Research tarafından geliştirilen açık kaynaklı bir terminal AI ajanıdır. Herhangi bir OpenAI uyumlu uç noktayı destekler ve Claudin.io için mükemmel bir uyum sağlar.

## Sihirbazla hızlı başlangıç

Aktif bir Hermes oturumundan çıkın (`Ctrl + C` veya `/quit`), ardından çalıştırın:

```bash
hermes model
```

Menüden **Özel uç nokta** seçin ve aşağıdakileri doldurun:

| Alan | Değer |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | `sk-...` anahtarınız |
| Model adı | `claudinio` |

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
  api_key: "sk-sua-chave-aqui"
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

> **İpucu:** Araç çağrısı içeren karmaşık görevler için Hermes Agent'ınızın en az 64K token bağlamına sahip bir model kullandığından emin olun (Claudinio bunu destekler).

## Sorun Giderme

| Sorun | Çözüm |
| --- | --- |
| Kimlik doğrulama hatası | `hermes doctor` ile API anahtarınızı tekrar kontrol edin |
| Model bulunamadı | Model adının tam olarak `claudinio` olduğundan emin olun |
| Bağlantı reddedildi | `https://api.claudin.io/v1` adresine ağınızdan erişilebildiğini doğrulayın |