# Pertanyaan yang sering diajukan

## Apa sebenarnya Claudin.io?

Proxy API untuk agen coding AI. Anda membayar paket bulanan, mendapat dompet
kredit yang terisi ulang setiap bulan dan kunci API yang kompatibel dengan
OpenAI/Anthropic untuk dipakai di Claude Code, Kilo, Zed, Codex, Cursor atau
klien OpenAI mana pun. Permintaan coding biasa menghabiskan sekitar satu
kredit. Tidak ada tagihan per token, tidak ada batas per jam.

## Apakah ada batasnya?

Hanya dompet Anda. Tidak ada batas per jam, batas sesi, atau kuota mingguan —
satu-satunya yang menghentikan agen Anda adalah saldo kosong, dan satu top-up
langsung memperbaikinya. Kredit paket Anda diperbarui setiap bulan dan tidak
menumpuk; kredit yang Anda beli lewat top-up tidak pernah kedaluwarsa. Lihat [Paket & kredit](plans.md).

## Mengapa kredit, bukan harga tetap?

Karena kami mengukur batas per jam dari paket harga tetap pada lalu lintas nyata
dan batas itu memutus 1 dari setiap 10 jam aktif di Pro — orang-orang di tengah
pekerjaan, bukan loop yang lepas kendali. Paket yang menjual kapasitas yang
tidak bisa dipakai saat dibutuhkan salah bentuknya. Kredit adalah angka yang
Anda lihat, jam berat yang dibayar oleh jam-jam tenang, dan bulan berat yang
tinggal satu top-up, bukan menunggu.

## Bisakah dipakai untuk selain coding?

API-nya kompatibel dengan OpenAI, jadi secara teknis permintaan apa pun bekerja.
Namun layanan ini dibangun untuk **pemrograman AI**: routing, prompt, dan
caching ditala untuk agen coding. Aktivitas non-pemrograman — chatbot umum,
otomasi tanpa kode — bisa mendapat routing khusus dan dilayani oleh model atau
tier yang berbeda dari lalu lintas coding.

## Model apa yang saya pakai?

Secara default **`claudinio`** (atau `claudinio/claudinio` untuk klien yang
menuntut bentuk `provider/model`). Base URL-nya `https://api.claudin.io`. Itu
model yang kami tala, ukur, dan cache untuk kode, dan tempat kredit Anda
berjalan paling jauh.

## Bisakah saya memilih model lain?

Ya, berdasarkan nama. `claudius` adalah opsi premium kami, hingga 6× kredit.
[Katalog](plans.md#catalogue) menambahkan dua belas model pihak ketiga —
DeepSeek V4.1 Flash, MiMo V2.6 Pro, GPT-6 Luna dan Sol, GLM 5.3 dan 5.3 Flash,
MiniMax M3, Gemini 3.8 Flash, Grok 4.7, Kimi K3, Claude Sonnet 5.5,
Claude Opus 5.5 — masing-masing dihargai sebagai kelipatan tetap dari kredit
`claudinio`, dari 2× hingga 36×. Setel ID-nya di klien Anda dan hanya permintaan
itu yang membayar pengalinya. Setiap model ada di setiap paket; kami tetap
merekomendasikan `claudinio`.

## Autentikasi dengan `Authorization` atau `x-api-key`?

Keduanya bekerja. `Authorization: Bearer YOUR_API_KEY` atau
`x-api-key: YOUR_API_KEY`.

## Bisakah dipakai dengan alat yang tidak ada di daftar?

Ya — alat apa pun yang mengizinkan base URL OpenAI kustom akan bekerja. Gunakan
[pengaturan OpenAI generik](clients/openai-compatible.md).

## Apakah mendukung tool / function calling?

Ya. Itulah sebabnya ia bekerja di editor agentik. Kirim `tools` dan baca
`tool_calls` seperti di API OpenAI.

## Bisakah menangani gambar, audio, atau video?

Ya, secara transparan. Kirim blok konten OpenAI standar; proxy mengubah
gambar/audio/video menjadi deskripsi teks atau transkripsi sebelum model
melihatnya. Tidak ada yang perlu dikonfigurasi khusus.

## Berapa jendela konteksnya?

256K token.

## Bagaimana cara upgrade atau membatalkan?

Dari [dasbor](https://claudin.io/dashboard) Anda. Upgrade berlaku seketika
(melalui Stripe). Jika membatalkan, paket berbayar Anda tetap berlaku sampai
akhir periode yang sudah dibayar. Kredit paket Anda berakhir bersama periode
itu; kredit yang Anda beli lewat top-up tetap di dompet dan terus bekerja
setelah paket berakhir.

## Bisakah saya mendapat pengembalian dana?

**Dalam 48 jam sejak pembayaran pertama**, ya — tulis ke
[support@claudin.io](mailto:support@claudin.io) dari email akun Anda.
Langganan berakhir seketika dan Anda menerima kembali apa yang dibayar,
dikurangi biaya pemakaian dan pemrosesan yang menutup biaya pemakaian model
akun Anda dalam periode itu (tidak pernah lebih dari yang Anda bayar). Mencoba
sehari dan bukan untuk Anda? Anda mendapat hampir semuanya kembali.
Menghabiskan kredit sebulan penuh dalam dua hari? Bersiaplah menerima sedikit
atau tidak sama sekali. Setelah 48 jam tidak ada pengembalian; pembatalan
mempertahankan paket Anda sampai akhir periode yang dibayar. Teks lengkapnya
ada di [Ketentuan](https://claudin.io/terms).

## Saya mendapat `402 insufficient_credits`. Sekarang apa?

Dompet Anda kosong. Beli [top-up](plans.md#top-ups) dari dasbor atau naik ke
paket lebih besar — keduanya berlaku seketika. Tidak ada yang mengantre, dan
tidak ada yang ditagih untuk permintaan yang gagal.

## Apa yang terjadi dengan paket Essential / Pro / Ultra lama saya?

Terus berjalan persis seperti sebelumnya: harga yang sama, batas per jam yang
sama, dan terus diperpanjang seperti biasa. Anda masih bisa berpindah antara
Essential, Pro dan Ultra dari dasbor, dan kunci API Anda tidak berubah. Paket
dengan batas per jam memakai `claudinio`; `claudius` dan katalog model
disertakan dalam paket kredit, jadi pada paket dengan batas per jam permintaan
yang menyebutnya dilayani oleh `claudinio`. Lihat [Paket lama](plans.md#legacy-plans).

## Sebuah permintaan gagal dengan 401.

Kunci Anda hilang atau salah. Salin lagi dari dasbor dan pastikan tidak ada
spasi tambahan dan header auth sudah disetel.

## Kunci saya bocor. Apa yang harus dilakukan?

Cabut dari dasbor dan buat yang baru seketika. Perlakukan kunci seperti kata
sandi — jangan pernah commit atau membagikannya secara publik.

## Di mana saya bisa mendapat bantuan?

Buka tiket dari kartu **Dukungan** di [dasbor](https://claudin.io/dashboard)
Anda, atau kirim email ke dukungan. Kami akan menghubungi Anda.
