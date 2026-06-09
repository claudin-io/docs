# API anahtarınızı ayarlayın

Claudin.io anahtarınızı **bir kez** ortam değişkeni olarak ayarlayın; bu kılavuzdaki her araç onu yeniden kullanabilir — her istemciye elle yapıştırmanıza gerek kalmaz.

`sk-...` anahtarınızı [panodan](https://claudin.io/dashboard) alın (bkz. [Hesap oluşturma](account.md)), ardından her yeni terminalde kullanılabilir olması için kabuk profilinize ekleyin.

## macOS / Linux

=== "zsh (macOS varsayılanı)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

`sk-...` ifadesini gerçek anahtarınızla değiştirin. Hangi kabuğu kullandığınızdan emin değil misiniz? `echo $SHELL` komutunu çalıştırın.

## Doğrulama

```bash
echo $CLAUDINIO_API_KEY
```

Anahtarınızın geri yazdırıldığını görmelisiniz. Boşsa, yeni bir terminal açın veya yukarıdaki `source` komutunu yeniden çalıştırın.

## Neden yardımcı olur

[Aracınızı bağlayın](../clients/opencode.md) bölümündeki her **Hızlı kurulum** betiği `$CLAUDINIO_API_KEY` değişkenini okur, bu nedenle dışa aktarıldığında herhangi birini olduğu gibi çalıştırabilirsiniz — değiştirilecek `YOUR_API_KEY` yoktur. Ortam değişkenlerini doğrudan okuyan araçlar (Codex'in `env_key` değişkeni, OpenAI uyumlu herhangi bir CLI) da otomatik olarak algılar.

!!! warning "Anahtarınıza şifre gibi davranın"
    Bu anahtara sahip olan herkes planınızın bütçesini harcayabilir. `~/.zshrc` / `~/.bashrc` dosyalarınızı herkese açık bir depoya göndermeyin. Anahtar sızarsa, panoda iptal edin ve yeni bir tane dışa aktarın.

---

Anahtar dışa aktarıldı mı? Şimdi [ilk çağrınızı yapın](first-call.md) veya doğrudan [aracınızı bağlamaya](../clients/opencode.md) atlayın.