# Referensi API

Claudin.io adalah **API yang kompatibel dengan OpenAI**. Jika Anda pernah menggunakan API OpenAI, semuanya di sini terasa familier — cukup arahkan ke URL dasar Claudin.io dan gunakan model `claudinio`.

## URL dasar

```
https://api.claudin.io
```

Rute bergaya OpenAI tersedia di bawah `/v1`.

## Autentikasi

Kirim kunci API Anda dengan setiap permintaan, sebagai salah satu header berikut:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Model

| ID model | Jendela konteks |
| --- | --- |
| `claudinio` | 256K token |

Gunakan `claudinio` di mana saja. (Beberapa klien mengharapkan bentuk `provider/model` — untuk itu, gunakan `claudinio/claudinio`.)

## Endpoint

| Metode & path | Deskripsi |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions — endpoint utama |
| `POST /v1/completions` | Completions teks lawas |
| `POST /v1/messages` | Format Anthropic Messages |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Embedding teks |
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

Parameter OpenAI standar didukung: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (function calling), `response_format`, dan seterusnya. Dua di antaranya memiliki batas yang perlu Anda ketahui sebelum mengirimnya: [`max_tokens`](#max_tokens-and-reasoning) dibatasi antara nilai minimum dan maksimum, dan [`n`](#multiple-completions-n) harus `1`.

### `max_tokens` dan penalaran {#max_tokens-and-reasoning}

Model Claudinio bernalar sebelum menjawab, dan **token penalaran diperhitungkan dalam `max_tokens`** — anggaran yang sama mencakup rantai pemikiran internal dan balasan yang terlihat. Oleh karena itu, `max_tokens` yang kecil bisa habis hampir seluruhnya untuk penalaran, sehingga jawaban terpotong di tengah kalimat.

Untuk mencegah hal itu, nilai di bawah **4000** otomatis dinaikkan menjadi 4000. Di sisi lain, nilai di atas **393216** diturunkan menjadi 393216 — maksimum yang dapat diterima model — karena angka yang lebih besar ditolak mentah-mentah, bukan dianggap sebagai "sebanyak yang Anda mau". Nilai apa pun di antara keduanya diteruskan tanpa perubahan, dan tidak menyertakan parameter ini selalu aman.

`max_tokens` adalah batas atas, bukan reservasi: Anda ditagih untuk token yang benar-benar dihasilkan, jadi nilai yang besar tidak memerlukan biaya tambahan.

Jika Anda mengurai output terstruktur (JSON, XML, format ketat), periksa `finish_reason` sebelum mengurai — `"length"` berarti respons mencapai batas token dan tidak lengkap, sehingga kegagalan penguraian adalah hal yang wajar, bukan masalah model yang rusak:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Beberapa completions (`n`) {#multiple-completions-n}

Hanya **`n = 1`** yang didukung. Mengirim `n` lebih besar dari 1 akan mengembalikan `400` dengan `"code": "unsupported_parameter"`; tidak menyertakan parameter ini selalu aman.

Model Claudinio bernalar sebelum menjawab, dan proses penalaran menghasilkan satu alur pemikiran — tidak ada cara murah untuk mencabangnya menjadi beberapa kandidat independen, sehingga penyedia hulu tidak menyediakannya. Jika Anda menginginkan lebih dari satu kandidat, kirim permintaan lebih dari sekali (`temperature` yang lebih tinggi memberi Anda variasi), dan perlu diingat bahwa masing-masing ditagih secara terpisah.

Kami menolak `n > 1` alih-alih diam-diam mengembalikan satu pilihan: klien yang meminta empat dan menerima satu biasanya akan gagal di kemudian hari, di dalam kodenya sendiri, tanpa ada error dari kami yang menjelaskan alasannya.

### Streaming

Setel `"stream": true` untuk menerima server-sent events dalam format streaming OpenAI (potongan `data: {...}` yang diakhiri dengan `data: [DONE]`).

### Tool / function calling

`claudinio` mendukung tool calls. Kirim `tools` dan baca kembali `tool_calls` dari respons, persis seperti pada API OpenAI. Inilah yang membuatnya berfungsi di dalam editor agentik seperti Claude Code, Kilo, dan Cursor.

### Input multimodal

`claudinio` adalah model teks, tetapi Claudin.io **menangani secara transparan** blok gambar, audio, dan video: jika Anda mengirimnya, proxy mengubahnya menjadi deskripsi/transkripsi teks sebelum model melihatnya. Anda tidak perlu melakukan hal khusus apa pun — kirim blok konten OpenAI standar dan semuanya berfungsi.

## Error {#errors}

Error mengikuti bentuk error OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Makna | Yang harus dilakukan |
| --- | --- | --- |
| `401` | Kunci API tidak valid atau tidak ada | Periksa kunci dan header autentikasi |
| `403` | Endpoint tidak diizinkan | Gunakan salah satu jalur `/v1/*` yang didukung |
| `402` | Tidak ada langganan aktif | [Berlangganan](https://claudin.io/dashboard) — mencoba lagi tidak akan membantu |
| `429` | Batas anggaran tercapai atau terkena rate limit | Tunggu reset jendela (lihat header `Retry-After`) atau [tingkatkan paket](plans.md) |
| `400` | Permintaan rusak | Periksa JSON / parameter Anda — lihat [`max_tokens`](#max_tokens-and-reasoning) dan [`n`](#multiple-completions-n) |
| `5xx` | Gangguan upstream/provider | Coba lagi dengan backoff |

!!! info "Detail provider sengaja disembunyikan"
    Pesan error disanitasi sehingga tidak membocorkan penyedia model yang
    mendasarinya. Anda akan selalu melihat error bermerek Claudin.io
    berbentuk OpenAI.

### Mencapai batas anggaran

Saat Anda menghabiskan perlindungan pengeluaran pada jendela saat ini, permintaan akan mengembalikan `429` dengan header `Retry-After` yang menunjukkan detik hingga jendela direset. Dasbor Anda menampilkan waktu reset yang tepat dan sisa anggaran. Tunggulah sesuai header tersebut alih-alih mencoba lagi segera. Lihat [Paket & batasan](plans.md) untuk mengetahui cara kerja jendela tersebut.

### Sebuah pesan alih-alih `429` {#cap-alternative-response}

Pada sejumlah kecil akun kami sedang mencoba jawaban berbeda untuk situasi yang
sama. Alih-alih galat, permintaan diselesaikan dan balasannya sendiri
menjelaskan bahwa batas sudah tercapai dan kapan batas itu disetel ulang. Kami
mengukur apakah dengan cara ini informasinya sampai ke orangnya lebih andal
daripada galat yang ditelan diam-diam oleh agen mereka — dan apakah, kalau
dikatakan terus terang, mereka lebih memilih pindah ke paket yang pas.

**Kalau kamu membangun otomasi, jangan membaca `2xx` sebagai "pekerjaan
selesai".** Perlakukan balasan yang menyatakan batas tercapai sebagai batas yang
memang tercapai, dan tunggu sampai jendelanya disetel ulang. `429` di atas tetap
perilaku bawaan dan itulah yang diterima hampir semua akun.

## Rate limiting

Claudin.io tidak memblokir total penggunaan normal. Laju permintaan yang abusif *diperlambat* (throttle yang transparan) alih-alih ditolak, sehingga klien yang berperilaku baik tidak akan pernah dirugikan. Dalam praktiknya, Anda tidak perlu melakukan apa pun — cukup coba lagi pada `429` yang jarang terjadi.
