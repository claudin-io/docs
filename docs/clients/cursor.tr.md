# Cursor

[Cursor](https://cursor.com), ayarları aracılığıyla OpenAI uyumlu bir model eklemenizi sağlar. Claudin.io, OpenAI temel URL'sini geçersiz kılma yoluyla bağlanır.

## Kurulum

1. **Cursor → Ayarlar → Modeller**'i (veya **Cursor Ayarları → AI**'yı) açın.
2. **OpenAI API Anahtarı**'na ilerleyin ve **OpenAI Temel URL'sini Geçersiz Kıl** seçeneğini genişletin.
3. Aşağıdaki gibi ayarlayın:

    | Alan | Değer |
    | --- | --- |
    | OpenAI API Anahtarı | `YOUR_API_KEY` |
    | Temel URL | `https://api.claudin.io/v1` |

4. **Modeller** altında, **`claudinio`** adında özel bir model ekleyin ve etkinleştirin.
5. Cursor'un yalnızca Claudin.io kullanmasını istiyorsanız diğer varsayılan modelleri devre dışı bırakın.

!!! note "Cursor'ın kendi özellikleri"
    Cursor'ın aracı özellikleri, OpenAI uyumlu bir sohbet modeliyle en iyi şekilde çalışır.
    `claudinio`, araç çağrılarını destekler, bu nedenle Composer/Agent akışları çalışır.
    Bazı Cursor'a özel özellikler (Sekme otomatik tamamlama, vb.) Cursor'ın kendi modellerinde çalışır ve sağlayıcı geçersiz kılmanız üzerinden yönlendirilmez.

## Doğrulama

Cursor'da bir sohbet açın, **claudinio**'yu seçin ve bir mesaj gönderin. Bir yanıt alırsanız, hazırsınız. Almazsanız, temel URL'nin `/v1` ile bittiğini ve anahtarın fazladan boşluk olmadan yapıştırıldığını iki kez kontrol edin.

| Ayar | Değer |
| --- | --- |
| Temel URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |