# API anahtarınızı ayarlayın

Claudin.io anahtarınızı **bir kez** ortam değişkeni olarak ayarlayın ve bu kılavuzdaki her araç onu yeniden kullanabilsin — her istemciye elle yapıştırmanız gerekmez.

`sk-...` anahtarınızı [panodan](https://claudin.io/dashboard) alın ([Hesap oluşturma](account.md) bölümüne bakın), ardından her yeni terminalde kullanılabilir olması için kabuk profilinize ekleyin.

## macOS / Linux

=== "zsh (macOS'ta varsayılan)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

`sk-...` kısmını gerçek anahtarınızla değiştirin. Hangi kabuğu kullandığınızdan emin değil misiniz? `echo $SHELL` komutunu çalıştırın.

## Doğrulama

```bash
echo $CLAUDINIO_API_KEY
```

Anahtarınızı geri yazdırıldığını görmelisiniz. Boşsa, yeni bir terminal açın veya yukarıdaki `source` komutunu yeniden çalıştırın.

## Bunun faydası

[Aracınızı bağlama](../clients/opencode.md) bölümündeki her **Hızlı kurulum** komut dosyası `$CLAUDINIO_API_KEY` değerini okur, böylece dışa aktarıldıktan sonra herhangi birini olduğu gibi çalıştırabilirsiniz — değiştirmeniz gereken `YOUR_API_KEY` yoktur. Ortam değişkenlerini doğrudan okuyan araçlar (Codex'in `env_key`'i, OpenAI uyumlu herhangi bir CLI) da onu otomatik olarak alır.

!!! warning "Anahtarınızı şifre gibi koruyun"
    Bu anahtara sahip herkes kredilerinizi harcayabilir. `~/.zshrc` / `~/.bashrc`
    dosyanızı herkese açık bir depoya commit etmeyin. Anahtar sızarsa panelden
    iptal edin ve yenisini dışa aktarın.

---

Anahtar dışa aktarıldı mı? Şimdi [ilk çağrınızı yapın](first-call.md) veya doğrudan [aracınızı bağlama](../clients/opencode.md) bölümüne geçin.