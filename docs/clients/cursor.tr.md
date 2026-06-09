# Cursor

[Cursor](https://cursor.com), ayarları aracılığıyla OpenAI uyumlu bir model eklemenize olanak tanır. Claudin.io, OpenAI temel URL geçersiz kılma yoluyla bağlanır.

## Kurulum

1. **Cursor → Ayarlar → Modeller** (veya **Cursor Ayarlar → AI**) öğesini açın.
2. **OpenAI API Key**'e gidin ve **Override OpenAI Base URL** seçeneğini genişletin.
3. Ayarlayın:

    | Alan | Değer |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. **Modeller** altında, **`claudinio`** adında özel bir model ekleyin ve etkinleştirin.
5. Cursor'ın yalnızca Claudin.io kullanmasını istiyorsanız diğer varsayılan modelleri devre dışı bırakın.

!!! note "Cursor'ın kendi özellikleri"
    Cursor'ın aracısal özellikleri, OpenAI uyumlu bir sohbet modeliyle en iyi şekilde çalışır.
    `claudinio`, araç çağrılarını destekler, bu nedenle Composer/Agent akışları çalışır. Bazı
    Cursor'a özel özellikler (Sekme otomatik tamamlama, vb.) Cursor'ın kendi modellerinde çalışır
    ve sağlayıcı geçersiz kılma işleminiz üzerinden yönlendirilmez.

## Doğrulama

Cursor'da bir sohbet açın, **claudinio**'yu seçin ve bir mesaj gönderin. Yanıt alırsanız, hazırsınız.
Almazsanız, temel URL'nin `/v1` ile bittiğini ve anahtarın fazladan boşluk olmadan yapıştırıldığını
tekrar kontrol edin.

| Ayar | Değer |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |