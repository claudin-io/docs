# Referensi API

Claudin.io adalah **OpenAI-compatible** API. Jika Anda pernah menggunakan OpenAI API, semuanya di sini sudah familiar — cukup arahkan ke base URL Claudin.io dan gunakan model `claudinio`.

## Base URL

```
https://api.claudin.io
```

Rute bergaya OpenAI berada di bawah `/v1`.

## Autentikasi

Kirim kunci API Anda dengan setiap permintaan, sebagai salah satu header:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Model

| Model id | Jendela konteks |
| --- | --- |
| `claudinio` | 256K token |

Gunakan `claudinio` di mana saja. (Beberapa klien mengharapkan bentuk `provider/model` — untuk itu, gunakan `claudinio/claudinio`.)

## Endpoints

| Metode & jalur | Deskripsi |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions — titik akhir utama |
| `POST /v1/completions` | Teks completions lawas |
| `POST /v1/messages` | Format pesan Anthropic |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Teks embeddings |
| `GET /v1/models` | Daftar model yang tersedia |

### Chat completions

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],
    "temperature": 0.7
  }'
```

Parameter OpenAI standar didukung: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (pemanggilan fungsi), `response_format`, dan seterusnya.

### Streaming

Atur `"stream": true` untuk menerima kejadian yang dikirim server dalam format streaming OpenAI (`data: {...}` potongan yang diakhiri dengan `data: [DONE]`).

### Tool / function calling

`claudinio` mendukung panggilan alat. Kirim `tools` dan baca `tool_calls` kembali dari respons, persis seperti dengan OpenAI API. Inilah yang membuatnya berfungsi di dalam editor agen seperti Claude Code, Kilo, dan Cursor.

### Input multimodal

`claudinio` adalah model teks, tetapi Claudin.io **secara transparan menangani** blok gambar, audio, dan video: jika Anda mengirimnya, proxy mengubahnya menjadi deskripsi/transkripsi teks sebelum model melihatnya. Anda tidak perlu melakukan sesuatu yang khusus — kirim blok konten OpenAI standar dan semuanya berfungsi.

## Kesalahan {#errors}

Kesalahan mengikuti bentuk kesalahan OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Arti | Apa yang harus dilakukan |
| --- | --- | --- |
| `401` | Kunci API tidak valid atau hilang | Periksa kunci dan header auth |
| `403` | Endpoint tidak diizinkan | Gunakan salah satu jalur `/v1/*` yang didukung |
| `429` | Batas anggaran tercapai atau dibatasi kecepatan | Tunggu reset jendela atau [tingkatkan](plans.md) |
| `400` | Permintaan salah bentuk | Periksa JSON / parameter Anda |
| `5xx` | Gangguan upstream/penyedia | Coba lagi dengan backoff |

!!! info "Detail penyedia disembunyikan secara desain"
    Pesan kesalahan dibersihkan sehingga tidak membocorkan penyedia model yang mendasarinya. Anda akan selalu melihat kesalahan bermerek Claudin.io, berbentuk OpenAI.

### Mengenai batas anggaran

Saat Anda menghabiskan perlindungan pengeluaran jendela saat ini, permintaan akan mengembalikan kesalahan anggaran (biasanya `429`). Dasbor Anda menunjukkan waktu reset yang tepat dan sisa anggaran. Lihat [Paket & batasan](plans.md) untuk cara kerja jendela.

## Pembatasan laju

Claudin.io tidak memblokir penggunaan normal secara keras. Tingkat permintaan yang kasar akan *diperlambat* (throttle transparan) daripada ditolak, sehingga klien yang berperilaku baik tidak pernah dihukum. Dalam praktiknya Anda tidak perlu melakukan apa pun — cukup coba lagi pada `429` yang jarang terjadi.