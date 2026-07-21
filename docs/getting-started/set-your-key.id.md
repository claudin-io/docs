# Atur kunci API Anda

Atur kunci Claudin.io Anda **sekali** sebagai variabel lingkungan dan setiap alat dalam panduan ini dapat menggunakannya kembali — tidak perlu menempelkannya ke setiap klien secara manual.

Ambil kunci `sk-...` Anda dari [dasbor](https://claudin.io/dashboard) (lihat [Buat akun Anda](account.md)), lalu tambahkan ke profil shell Anda agar tersedia di setiap terminal baru.

## macOS / Linux

=== "zsh (default di macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Ganti `sk-...` dengan kunci asli Anda. Tidak yakin shell yang Anda gunakan? Jalankan `echo $SHELL`.

## Verifikasi

```bash
echo $CLAUDINIO_API_KEY
```

Anda akan melihat kunci Anda tercetak kembali. Jika kosong, buka terminal baru atau jalankan ulang perintah `source` di atas.

## Mengapa ini membantu

Setiap skrip **Pengaturan cepat** di bagian [Hubungkan alat Anda](../clients/opencode.md) membaca `$CLAUDINIO_API_KEY`, jadi setelah diekspor Anda dapat menjalankan salah satunya apa adanya — tidak ada `YOUR_API_KEY` yang perlu diganti. Alat yang membaca variabel lingkungan secara langsung (`env_key` milik Codex, CLI yang kompatibel dengan OpenAI) juga akan mengambilnya secara otomatis.

!!! warning "Perlakukan kunci Anda seperti kata sandi"
    Siapa pun yang memiliki kunci ini dapat menghabiskan anggaran paket Anda. Jangan commit `~/.zshrc` / `~/.bashrc` Anda ke repositori publik. Jika kunci bocor, cabut di dasbor dan ekspor yang baru.

---

Kunci sudah diekspor? Sekarang [lakukan panggilan pertama Anda](first-call.md) atau langsung ke [menghubungkan alat Anda](../clients/opencode.md).