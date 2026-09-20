# Paket & kredit

Setiap paket Claudin.io adalah **dompet kredit** yang terisi ulang setiap bulan.
Sebuah permintaan menghabiskan kredit sebanyak token yang dipakainya — sekitar
**satu kredit** untuk permintaan coding biasa di `claudinio` — dan yang tidak
Anda pakai tetap ada di dompet. **Kredit tidak pernah kedaluwarsa, dan tidak ada
batas per jam.**

## Paket

| Paket | Harga | Kredit / bulan | Untuk siapa |
| --- | --- | --- | --- |
| **Start** | $19 / bulan | 3,000 | Mencoba, pemakaian harian ringan |
| **Solo** ★ | $39 / bulan | 7,000 | Satu developer, setiap hari |
| **Pro** | $99 / bulan | 18,000 | Alur kerja agentik berat |
| **Studio** | $199 / bulan | 36,000 | Beberapa agen, sepanjang hari |
| **Max** | $399 / bulan | 72,000 | Produksi, tim, bot |

Setiap paket menyertakan setiap model: `claudinio`, `claudius` dan seluruh
[katalog](#catalogue). Paket hanya berbeda pada jumlah kredit yang datang tiap
bulan — dan makin besar paketnya, makin murah tiap kreditnya.

!!! tip "Paket mana yang cukup untuk bulan Anda"
    Permintaan biasa di `claudinio` menghabiskan sekitar satu kredit, diukur
    dari ribuan permintaan nyata. Hitung permintaan agen Anda dalam satu hari
    penuh, kalikan 22 hari kerja, dan pilih anak tangga yang menampungnya.
    Kalau berada di antara dua paket, ambil yang lebih kecil — bulan berat
    sesekali cukup ditutup dengan satu top-up.

### Top-up {#top-ups}

Butuh lebih sebelum bulan berikutnya tiba? Sebuah **top-up** menambahkan kredit
ke dompet yang sama seketika, di paket mana pun:

| Top-up | Kredit |
| --- | --- |
| $10 | 1,200 |
| $25 | 3,000 |
| $50 | 6,000 |

Kredit top-up dan kredit paket adalah kredit yang sama: keduanya bertambah,
tidak pernah kedaluwarsa, dan dipakai oleh setiap model.

## Mengapa kredit (dan tidak ada lagi batas per jam)

Paket kami dulunya harga tetap dengan **batas pengeluaran per jam** — rem
terhadap agen yang terjebak dalam loop, kata kami. Sebelum mengubah apa pun,
kami mengukurnya pada tiga hari lalu lintas nyata: **1 dari setiap 10 jam
aktif di Pro** (11.1%) berakhir dengan batas memutus seorang developer di
tengah pekerjaan, dan 1 dari 13 di Essential. Itu bukan loop tak berujung.
Itu orang-orang yang sedang bekerja.

Paket yang menjual kapasitas yang tidak bisa dipakai saat dibutuhkan salah
bentuknya. Maka batas itu dihapus. Sebuah paket adalah sejumlah kredit per
bulan; jam yang berat dibayar oleh jam-jam yang tenang; bulan yang berat
tinggal satu top-up, bukan menunggu. Satu-satunya yang menghentikan agen Anda
adalah dompet kosong, dan dasbor selalu menampilkan saldonya.

## Apa yang didapat dari satu kredit

Satu kredit bernilai sama di setiap sumbu. Di `claudinio`:

| | Kredit per 1M token |
| --- | --- |
| Input (cache miss) | 40 |
| Input (cache hit) | 6 |
| Output | 80 |

Hampir semua token agen adalah token prompt, dan dalam sesi kerja hampir
semuanya datang dari cache — karena itu permintaan biasa berada di sekitar
satu kredit, dan karena itu sesi panjang lebih murah per permintaan daripada
sesi pendek.

## Model mana? `claudinio`, `claudius` dan katalog

| Model | Apa itu | Biaya kredit | Termasuk di |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Model yang kami tala, ukur, dan cache untuk kode | 1× — sekitar satu kredit per permintaan | Setiap paket |
| **claudius** ★ | Opsi premium kami untuk penalaran mendalam | hingga 6x kredit claudinio (3× input, 4× output, 6× pembacaan cache) | Setiap paket (Start, Solo, Pro, Studio, Max) |

**Rekomendasi kami adalah `claudinio`.** Itulah model yang menjadi dasar setiap
paket: yang kami tala prompt-nya, yang dinilai setiap evaluasi, dan tempat satu
kredit berjalan paling jauh. Pengaturan paling efektif yang kami lihat adalah
**merencanakan dengan `claudius`, mengeksekusi dengan `claudinio`** — penalaran
adalah tempat model premium membayar pengalinya, dan loop eksekusi adalah
tempat volumenya.

### Katalog: pilih model berdasarkan nama {#catalogue}

Anda juga bisa meminta model pihak ketiga berdasarkan nama. Model katalog
disajikan **mentah** — model penyedia, system prompt dari klien Anda sendiri,
tanpa penalaan Claudinio — dan menghabiskan kelipatan bulat tetap dari kredit
`claudinio` di setiap sumbu, sehingga harganya terbaca sebagai satu angka:

| ID model | Model | Penyedia | Kredit vs `claudinio` |
| --- | --- | --- | --- |
| `qwen3-coder-flash` | Qwen3 Coder Flash | Qwen | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `qwen3-coder-plus` | Qwen3 Coder Plus | Qwen | 10× |
| `haiku-4.5` | Claude Haiku 4.5 | Anthropic | 11× |
| `glm-5.3` | GLM 5.3 | Z.ai | 13× |
| `kimi-k3` | Kimi K3 | Moonshot | 18× |
| `sonnet-5` | Claude Sonnet 5 | Anthropic | 21× |
| `gemini-3.1-pro` | Gemini 3.1 Pro | Google | 22× |

Setel `model=sonnet-5` (atau ID mana pun di atas) di klien Anda, dan hanya
permintaan itu yang membayar pengalinya — sisa sesi Anda tetap berjalan dengan
tarif `claudinio`. Setiap model katalog tersedia di setiap paket.

!!! note "Mengapa kami tetap merekomendasikan `claudinio`"
    Katalog ada untuk developer yang ingin memilih, bukan karena ada entri yang
    terukur lebih baik untuk kode. `claudinio` adalah model yang kami evaluasi,
    yang menjadi dasar cache prompt, dan — dengan 3× hingga 22× lebih murah per
    permintaan — tempat kredit Anda berjalan paling jauh. Gunakan model katalog
    dengan sengaja, untuk tugas yang memang membutuhkannya.

> 💡 Tips: `claudinio` juga menyelesaikan alias yang dikirim agen coding secara
> default — `claude-sonnet-4`, `gpt-4o`, `o3-mini` dan puluhan lainnya — jadi
> Anda tidak perlu mengubah konfigurasi agen untuk memakainya.

## Saat dompet kosong

Permintaan dijawab dengan `402` dan kode `insufficient_credits` (lihat
[Error](api-reference.md#errors)). Tidak ada yang mengantre, tidak ada yang
ditagih. Anda punya dua jalan, keduanya seketika:

1. **Beli top-up** dari [dasbor](https://claudin.io/dashboard).
2. **Naik ke paket lebih besar** — kredit bulan baru datang bersama faktur.

Dasbor menampilkan saldo Anda, pengeluaran hari ini, dan peringatan saldo
rendah sebelum Anda sampai di sana, dan kami mengirim satu email saat saldo
menipis.

## Paket lama (Essential, Pro, Ultra dengan batas per jam) {#legacy-plans}

Kalau Anda berada di salah satu paket sebelumnya, paket itu **terus berjalan
persis seperti sebelumnya, dengan batas per jamnya, sampai akhir periode yang
sudah dibayar**. Setelah itu tidak diperpanjang. Pelanggan bulanan menerima
kredit kehormatan untuk mencoba sistem baru sebelum memilih paket — dua bulan
pada harga paket lama; pelanggan tahunan menyimpan seluruh tahunnya dan
berpindah ke kredit saat itu berakhir. Kunci API Anda tidak berubah.
