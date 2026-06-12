[Hermes Agent](https://github.com/NousResearch/hermes-agent) adalah agen
terminal open-source buatan Nous Research. Ia mendukung endpoint apa pun yang
kompatibel dengan OpenAI, sehingga cocok untuk Claudin.io.

## Mulai cepat dengan wizard

Keluar dari sesi Hermes aktif (`Ctrl + C` atau `/quit`), lalu jalankan:

```bash
hermes model
```

Pilih **Custom endpoint** dari menu dan isi:

| Field | Nilai |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | kunci `sk-...` Anda |
| Model name | `claudinio` |

Hermes menyimpan konfigurasi secara otomatis ke `~/.hermes/config.yaml`.

Coba:

```bash
hermes
```

## Konfigurasi manual

Edit `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-kunci-anda"
  default: "claudinio"
```

Atau atur nilai secara langsung:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Verifikasi:

```bash
hermes config check
hermes config show
```

> **Tip:** Untuk tugas kompleks dengan pemanggilan alat, pastikan Hermes Agent
> Anda menggunakan model dengan setidaknya 64K token konteks (Claudinio mendukung ini).

## Pemecahan masalah

| Masalah | Solusi |
| --- | --- |
| Galat autentikasi | Periksa kunci API dengan `hermes doctor` |
| Model tidak ditemukan | Pastikan nama model tepat `claudinio` |
| Koneksi ditolak | Verifikasi `https://api.claudin.io/v1` dapat dijangkau |

## Perintah berguna

| Perintah | Deskripsi |
| --- | --- |
| `hermes config show` | Lihat konfigurasi saat ini |
| `hermes config edit` | Edit secara interaktif |
| `hermes doctor` | Diagnostik masalah |
| `hermes model` | Ganti penyedia |
