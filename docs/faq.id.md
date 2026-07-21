# FAQ

## Apa itu Claudin.io, sebenarnya?

Proksi API untuk agen coding AI. Anda membayar langganan bulanan tetap dan mendapatkan kunci API yang kompatibel dengan OpenAI/Anthropic yang dapat Anda gunakan di Claude Code, Kilo, Zed, Codex, Cursor, atau klien OpenAI mana pun. Tanpa tagihan per-token.

## Apakah benar-benar tidak terbatas?

Penggunaan tidak terbatas — tidak ada penghitung permintaan atau meter token. Satu-satunya batasan adalah **batas perlindungan pengeluaran** per periode waktu yang menghentikan agen yang lepas kendali agar tidak menghabiskan paket Anda. Dalam pekerjaan interaktif normal, Anda jarang mencapainya. Lihat [Paket & batasan](plans.md).

## Model apa yang saya gunakan?

Selalu **`claudinio`** (atau `claudinio/claudinio` untuk klien yang menginginkan format `provider/model`). URL dasarnya adalah `https://api.claudin.io`.

## Apakah saya melakukan autentikasi dengan `Authorization` atau `x-api-key`?

Keduanya berfungsi. `Authorization: Bearer YOUR_API_KEY` atau `x-api-key: YOUR_API_KEY`.

## Bisakah saya menggunakannya dengan alat yang tidak tercantum?

Ya — alat apa pun yang memungkinkan Anda mengatur URL dasar OpenAI kustom akan berfungsi. Gunakan [pengaturan OpenAI generik](clients/openai-compatible.md).

## Apakah mendukung pemanggilan alat / fungsi?

Ya. Itulah mengapa ia berfungsi di dalam editor agentik. Berikan `tools` dan baca `tool_calls` seperti pada OpenAI API.

## Bisakah menangani gambar, audio, atau video?

Ya, secara transparan. Kirim blok konten OpenAI standar; proksi mengonversi gambar/audio/video menjadi deskripsi teks atau transkripsi sebelum model melihatnya. Tidak perlu mengonfigurasi apa pun.

## Berapa ukuran jendela konteks?

256K token.

## Bagaimana cara meningkatkan atau membatalkan?

Dari [dasbor](https://claudin.io/dashboard) Anda. Peningkatan berlaku segera (melalui Stripe). Jika Anda membatalkan, Anda tetap mendapatkan paket berbayar hingga akhir periode yang sudah Anda bayar, kemudian turun ke Gratis secara otomatis.

## Saya mendapatkan error anggaran. Apa yang harus dilakukan?

Anda telah mencapai batas perlindungan pengeluaran untuk periode saat ini. Tunggu hingga periode direset (dasbor Anda menunjukkan kapan) atau [tingkatkan](plans.md) untuk batas yang lebih besar.

## Permintaan gagal dengan 401.

Kunci Anda hilang atau salah. Salin ulang dari dasbor dan pastikan tidak ada spasi tambahan, serta header auth sudah diatur.

## Kunci saya bocor. Apa yang harus saya lakukan?

Cabut dari dasbor dan buat yang baru segera. Perlakukan kunci seperti kata sandi — jangan pernah melakukan commit atau membagikannya secara publik.

## Di mana saya bisa mendapatkan bantuan?

Buka tiket dari kartu **Dukungan** di [dasbor](https://claudin.io/dashboard) Anda, atau email dukungan. Kami akan menghubungi Anda kembali.