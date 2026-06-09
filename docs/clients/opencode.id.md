# OpenCode

[OpenCode](https://opencode.ai) terhubung ke Claudin.io sebagai penyedia yang kompatibel dengan OpenAI. Jalur tercepat adalah alur autentikasi bawaannya.

## Pengaturan Cepat

1. Jalankan perintah login:

    ```bash
    opencode auth login
    ```

2. Pilih **Claudinio** sebagai penyedia.
3. Tempel kunci API Anda saat diminta — salin dari [dasbor](https://claudin.io/dashboard) Anda.

Kemudian mulai OpenCode dan pilih model **claudinio**.

## Alternatif Variabel Lingkungan

Jika Anda sudah [mengekspor kunci Anda](../getting-started/set-your-key.md), OpenCode akan mengambil variabel OpenAI standar — tidak perlu menempelkan apa pun:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Pengaturan | Nilai |
| --- | --- |
| URL Dasar | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| Penyedia | Kompatibel dengan OpenAI |

---

Ada masalah? Lihat [kesalahan umum](../api-reference.md#errors) atau [FAQ](../faq.md).