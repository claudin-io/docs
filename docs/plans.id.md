# Rencana & batasan

Setiap paket Claudin.io adalah **penggunaan tanpa batas** dengan **batas perlindungan pengeluaran**.
Anda tidak ditagih per token atau per permintaan — Anda membayar harga bulanan tetap dan
menggunakannya secara bebas. Batas tersebut hanya ada untuk menghentikan agen yang lepas kendali (misalnya, perulangan alat tak terbatas) agar tidak menguras paket Anda.

## Paket yang tersedia

| Paket | Harga | Perlindungan pengeluaran | Terbaik untuk |
| --- | --- | --- | --- |
| **Starter** | $5 / bln | $0,50 / jam | Mencoba — komitmen rendah |
| **Lite** | $9 / bln | $1,00 / jam | Proyek hobi, coding sesekali |
| **Essential** | $19 / bln atau $189 / thn | $2,00 / jam | Kualitas untuk penggunaan sehari-hari |
| **Pro** ★ | $39 / bln atau $389 / thn | $4,00 / jam | Alur kerja agentic berat |
| **Power** | $59 / bln atau $589 / thn | $6,00 / jam | Tim, banyak proyek |
| **Ultra** | $99 / bln atau $989 / thn | $10,00 / jam | Kekuatan maksimal, tim & produksi |

!!! tip "Kebanyakan orang tidak pernah mencapai batas"
    Batas per jam cukup longgar untuk pekerjaan interaktif normal. Anda biasanya hanya
    mendekati batas jika agen masuk ke dalam perulangan ketat — yang justru saat Anda
    *ingin* rem.

## Model mana yang harus Anda pilih? Claudinio vs Claudius

Kami menawarkan dua model utama untuk agen coding Anda:

| Model | Backend | Kasus penggunaan | Direkomendasikan untuk |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Cepat, seimbang, hemat biaya | Coding sehari-hari, proyek hobi, kode umum | **Semua paket** (Starter hingga Ultra) |
| **claudius** ★ | Premium, penalaran mendalam | Tugas kompleks, penalaran mendalam, alur kerja agentic berat | Essential+ (Pro, Power, Ultra) |

### Bicara terus terang

Jika Anda di **Starter** ($5) atau **Lite** ($9) — **gunakan `claudinio` dan jangan berpikir dua kali.** 🎯

Inilah kenyataannya: `claudinio` memberikan kualitas yang sebanding dengan Claude Sonnet untuk coding sehari-hari dengan **sebagian kecil dari biaya internal**. Pada paket Lite, Anda bisa mendapatkan **ratusan permintaan per jam** dengan `claudinio` — sementara `claudius` akan menghabiskan anggaran per jam Anda jauh lebih cepat.

| Metrik | claudinio | claudius |
| --- | --- | --- |
| Dampak pada anggaran per jam | Rendah — bertahan lebih lama | Tinggi — habis lebih cepat |
| Kasus penggunaan | Coding harian, proyek pribadi | Penalaran berat, agen kompleks |

**Aturan emas:** Konfigurasikan agen Anda (Claude Code, Cursor, Continue, dll.) dengan `claudinio` sebagai model default. Hanya beralih ke `claudius` saat Anda benar-benar membutuhkan lebih banyak daya penalaran — dan jika paket Anda mengizinkannya (Essential+). Untuk proyek hobi, `claudinio` **adalah semua yang Anda butuhkan** dan kemungkinan **lebih dari yang Anda harapkan**.

> 💡 Tips: Kedua model bekerja dengan semua agen coding utama. Cukup atur `model=claudinio` atau `model=claudius` di konfigurasi agen Anda. `claudinio` juga secara otomatis menyelesaikan alias seperti `claude-sonnet-4`, `gpt-4o`, `o3-mini` dan puluhan lainnya — tidak perlu mengubah konfigurasi agen Anda.

## Cara kerja perlindungan pengeluaran

Setiap paket menentukan **jendela** anggaran — periode bergulir dan pengeluaran maksimum
di dalamnya:

- **Starter**, **Lite**, **Essential**, **Pro**, **Power**, dan **Ultra** menggunakan jendela **1 jam**.

Dalam jendela tersebut, penggunaan Anda mengakumulasi biaya internal yang sangat kecil. Ketika
biaya internal itu mencapai batas jendela, permintaan berhenti hingga jendela direset.

Hanya panggilan model Anda melalui proxy. Setiap permintaan menambah total berjalan
jendela saat ini berdasarkan token yang digunakan. Saat jendela direset,
totalnya juga ikut direset.

Jika Anda mencapai batas dan mendapatkan kesalahan anggaran, Anda memiliki dua opsi:

1. Tunggu hingga jendela direset (ditampilkan di dasbor Anda).
2. Tingkatkan ke paket yang lebih tinggi untuk batas yang lebih besar.

Lihat [Kesalahan terkait rencana](api-reference.md#errors) untuk seperti apa tampilan kesalahan anggaran.