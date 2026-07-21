# Referensi API

Claudin.io adalah **OpenAI-compatible** API. Jika Anda pernah menggunakan OpenAI API, semuanya di sini sudah familiar — cukup arahkan ke base URL Claudin.io dan gunakan model `claudinio`.

## Base URL

```
https://api.claudin.io
```

Rute bergaya OpenAI berada di bawah `/v1`.

## Autentikasi

Kirimkan kunci API Anda dengan setiap permintaan, sebagai salah satu header berikut:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Model

| ID Model | Jendela konteks |
| --- | --- |
| `claudinio` | 256K token |

Gunakan `claudinio` di mana saja. (Beberapa klien mengharapkan bentuk `provider/model` — untuk itu, gunakan `claudinio/claudinio`.)

## Endpoint

| Metode & jalur | Deskripsi |
| --- | --- |
| `POST /v1/chat/completions` | Penyelesaian chat — endpoint utama |
| `POST /v1/completions` | Penyelesaian teks warisan |
| `POST /v1/messages` | Format Pesan Anthropic |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Embedding teks |
| `GET /v1/models` | Daftar model yang tersedia |

### Penyelesaian chat

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

Parameter OpenAI standar didukung: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (function calling), `response_format`, dan seterusnya.

### `max_tokens` dan penalaran

Model Claudinio bernalar sebelum menjawab, dan **token penalaran diperhitungkan dalam `max_tokens`** — anggaran yang sama mencakup rantai pemikiran internal dan balasan yang terlihat. Oleh karena itu, `max_tokens` yang kecil dapat hampir seluruhnya digunakan untuk penalaran, sehingga jawaban terpotong di tengah kalimat.

Untuk mencegah hal itu, nilai di bawah **4000** secara otomatis dinaikkan menjadi 4000. Nilai yang lebih besar dilewatkan tanpa perubahan, dan menghilangkan parameter selalu diperbolehkan.

Jika Anda mengurai keluaran terstruktur (JSON, XML, format ketat), periksa `finish_reason` sebelum mengurai — `"length"` berarti respons mencapai batas token dan tidak lengkap, sehingga kegagalan penguraian diharapkan daripada masalah model yang salah format:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Streaming

Setel `"stream": true` untuk menerima server-sent events dalam format streaming OpenAI (potongan `data: {...}` yang diakhiri dengan `data: [DONE]`).

### Tool / function calling

`claudinio` mendukung panggilan tool. Kirimkan `tools` dan baca `tool_calls` kembali dari respons, persis seperti pada OpenAI API. Inilah yang membuatnya berfungsi di dalam editor agen seperti Claude Code, Kilo, dan Cursor.

### Input multimodal

`claudinio` adalah model teks, tetapi Claudin.io **secara transparan menangani** blok gambar, audio, dan video: jika Anda mengirimkannya, proxy mengubahnya menjadi deskripsi/transkripsi teks sebelum model melihatnya. Anda tidak perlu melakukan sesuatu yang khusus — kirimkan blok konten OpenAI standar dan semuanya akan berfungsi.

## Error {#errors}

Error mengikuti bentuk error OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Arti | Yang harus dilakukan |
| --- | --- | --- |
| `401` | Kunci API tidak valid atau hilang | Periksa kunci dan header auth |
| `403` | Endpoint tidak diizinkan | Gunakan salah satu jalur `/v1/*` yang didukung |
| `429` | Batas anggaran tercapai atau dibatasi rate | Tunggu reset jendela atau [tingkatkan](plans.md) |
| `400` | Permintaan salah format | Periksa JSON / parameter Anda |
| `5xx` | Gangguan upstream/provider | Coba lagi dengan backoff |

!!! info "Detail penyedia disembunyikan sesuai desain"
    Pesan error dibersihkan agar tidak membocorkan penyedia model yang mendasarinya. Anda akan selalu melihat error bermerek Claudin.io, berbentuk OpenAI.

### Mencapai batas anggaran

Ketika Anda menghabiskan perlindungan pengeluaran jendela saat ini, permintaan akan mengembalikan error anggaran (biasanya `429`). Dasbor Anda menunjukkan waktu reset yang tepat dan sisa anggaran. Lihat [Paket & batasan](plans.md) untuk cara kerja jendela.

## Pembatasan rate

Claudin.io tidak memblokir penggunaan normal secara keras. Tingkat permintaan yang abusive *diperlambat* (throttle transparan) daripada ditolak, sehingga klien yang berperilaku baik tidak pernah dihukum. Dalam praktiknya, Anda tidak perlu melakukan apa pun — cukup coba lagi pada `429` yang jarang terjadi.