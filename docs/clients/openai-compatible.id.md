# Klien yang kompatibel dengan OpenAI

Claudin.io mengimplementasikan permukaan API OpenAI, sehingga **setiap** alat, SDK, atau pustaka yang memungkinkan Anda mengatur base URL kustom akan berfungsi. Jika editor Anda tidak tercantum di bagian ini, gunakan pengaturan generik ini.

## Tiga nilai

| Pengaturan | Nilai |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| API key | kunci `sk-...` Anda |

Kebanyakan alat menyebut bidang base URL sebagai salah satu dari: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint*, atau *Custom provider URL*. Selalu sertakan akhiran `/v1`.

## Variabel lingkungan

Banyak CLI dan SDK membaca variabel OpenAI standar — atur ini dan selesai. Jika Anda telah [mengekspor kunci Anda](../getting-started/set-your-key.md), gunakan kembali `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Titik akhir yang didukung

Claudin.io merutekan jalur gaya OpenAI ini:

| Titik Akhir | Tujuan |
| --- | --- |
| `POST /v1/chat/completions` | Penyelesaian obrolan (yang utama) |
| `POST /v1/completions` | Penyelesaian teks lama |
| `POST /v1/messages` | Format Pesan Anthropic |
| `POST /v1/responses` | API Responses (digunakan oleh Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Daftar model yang tersedia |

## Autentikasi

Kirim kunci Anda sebagai **salah satu** dari:

```http
Authorization: Bearer YOUR_API_KEY
```

atau

```http
x-api-key: YOUR_API_KEY
```

Keduanya diterima — pilih mana yang dikeluarkan klien Anda.

---

Lihat [referensi API](../api-reference.md) lengkap untuk detail permintaan/respons dan penanganan kesalahan.