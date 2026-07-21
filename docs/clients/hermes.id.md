# Agen Hermes

[Agen Hermes](https://github.com/NousResearch/hermes-agent) adalah agen AI terminal sumber terbuka oleh Nous Research. Ini mendukung endpoint apa pun yang kompatibel dengan OpenAI, menjadikannya sangat cocok untuk Claudin.io.

## Mulai cepat dengan wizard

Keluar dari sesi Hermes yang aktif (`Ctrl + C` atau `/quit`), lalu jalankan:

```bash
hermes model
```

Pilih **Endpoint Kustom** dari menu dan isi:

| URL Dasar | `https://api.claudin.io/v1` |
| Kunci API | kunci `sk-...` Anda |
| Nama Model | `claudinio` |

Hermes menyimpan konfigurasi secara otomatis ke `~/.hermes/config.yaml`.

Cobalah:

```bash
hermes
```

## Konfigurasi manual

Edit `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
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

> **Tip:** Untuk tugas kompleks dengan pemanggilan alat, pastikan Agen Hermes Anda menggunakan model dengan setidaknya konteks 64K token (Claudinio mendukung ini).

## Pemecahan masalah

| Masalah | Perbaikan |
| --- | --- |
| Kesalahan autentikasi | Periksa ulang kunci API Anda dengan `hermes doctor` |
| Model tidak ditemukan | Pastikan nama model tepat `claudinio` |
| Koneksi ditolak | Verifikasi `https://api.claudin.io/v1` dapat dijangkau dari jaringan Anda |