# Rencana & batasan

Setiap paket Claudin.io adalah **penggunaan tanpa batas** dengan **batas perlindungan pengeluaran**.
Anda tidak ditagih per token atau per permintaan — Anda membayar harga bulanan tetap dan
menggunakannya secara bebas. Batas tersebut hanya ada untuk menghentikan agen yang lepas kendali (misalnya, perulangan alat tak terbatas) agar tidak menguras paket Anda.

## Paket yang tersedia

| Paket | Harga | Perlindungan pengeluaran | Terbaik untuk |
| --- | --- | --- | --- |
| **Essential** | $19 / bln atau $189 / thn | $2,00 / jam | Kualitas untuk penggunaan sehari-hari |
| **Pro** ★ | $39 / bln atau $389 / thn | $4,00 / jam | Alur kerja agentic berat |
| **Ultra** | $99 / bln atau $989 / thn | $10,00 / jam | Kekuatan maksimal, tim & produksi |

!!! tip "Kebanyakan orang tidak pernah mencapai batas"
    Batas per jam cukup longgar untuk pekerjaan interaktif normal. Anda biasanya hanya
    mendekati batas jika agen masuk ke dalam perulangan ketat — yang justru saat Anda
    *ingin* rem.

## Model mana yang harus Anda pilih? Claudinio vs Claudius

Kami menawarkan dua model utama untuk agen coding Anda:

| Model | Backend | Kasus penggunaan | Direkomendasikan untuk |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Cepat, seimbang, hemat biaya | Coding sehari-hari, proyek hobi, kode umum | **Semua paket** (Essential hingga Ultra) |
| **claudius** ★ | Premium, penalaran mendalam | Tugas kompleks, penalaran mendalam, alur kerja agentic berat | **Pro dan Ultra** |
!!! warning "`claudius` termasuk dalam Pro dan Ultra"
    Di **Essential**, permintaan yang menyebut `claudius` tidak ditolak — permintaan itu dilayani oleh `claudinio` dan ditagih dengan tarif `claudinio`. Agen Anda tetap berjalan, dan tarif premium tidak pernah dikenakan pada paket yang tidak memuatnya.

    Di **Pro** dan **Ultra**, ingat bahwa batasnya dihitung **dalam dolar, bukan jumlah permintaan**: pekerjaan yang sama di `claudius` memakai sekitar enam kali lipat. Di Pro ($4/jam) itu sekitar 70 permintaan premium sebelum jamnya habis; di Ultra ($10/jam), sekitar 175. Biarkan `claudinio` sebagai default dan pakai `claudius` saat Anda memang butuh penalarannya.

### Bicara terus terang

Inilah kenyataannya: `claudinio` memberikan kualitas yang sebanding dengan Claude Sonnet untuk coding sehari-hari dengan **sebagian kecil dari biaya internal**. Pada paket Essential, Anda bisa mendapatkan **ratusan permintaan per jam** dengannya — itulah sebabnya setiap paket dibangun di sekitar model ini.

| Metrik | claudinio | claudius |
| --- | --- | --- |
| Dampak pada anggaran per jam | Rendah — bertahan lebih lama | Tinggi — 6x per permintaan |
| Kasus penggunaan | Coding harian, proyek pribadi | Penalaran berat, agen kompleks |

**Aturan emas:** Konfigurasikan agen Anda (Claude Code, Cursor, Continue, dll.) dengan `claudinio` sebagai model default. Hanya beralih ke `claudius` saat Anda benar-benar membutuhkan lebih banyak daya penalaran. Untuk proyek hobi, `claudinio` **adalah semua yang Anda butuhkan** dan kemungkinan **lebih dari yang Anda harapkan**.

> 💡 Tips: Kedua model bekerja dengan semua agen coding utama. Setel `model=claudinio` di konfigurasi agen Anda — atau `model=claudius` jika Anda di Pro atau Ultra. `claudinio` juga otomatis menyelesaikan alias seperti `claude-sonnet-4`, `gpt-4o`, `o3-mini` dan puluhan lainnya — tidak perlu mengubah konfigurasi agen Anda.

## Cara kerja perlindungan pengeluaran

Setiap paket menentukan **jendela** anggaran — periode bergulir dan pengeluaran maksimum
di dalamnya:

- **Essential**, **Pro**, dan **Ultra** menggunakan jendela **1 jam**.

Dalam jendela tersebut, penggunaan Anda mengakumulasi biaya internal yang sangat kecil. Ketika
biaya internal itu mencapai batas jendela, permintaan berhenti hingga jendela direset.

Hanya panggilan model Anda melalui proxy. Setiap permintaan menambah total berjalan
jendela saat ini berdasarkan token yang digunakan. Saat jendela direset,
totalnya juga ikut direset.

Jika Anda mencapai batas dan mendapatkan kesalahan anggaran, Anda memiliki dua opsi:

1. Tunggu hingga jendela direset (ditampilkan di dasbor Anda).
2. Tingkatkan ke paket yang lebih tinggi untuk batas yang lebih besar.

Lihat [Kesalahan terkait rencana](api-reference.md#errors) untuk seperti apa tampilan kesalahan anggaran.