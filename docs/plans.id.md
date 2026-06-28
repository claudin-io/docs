# Paket dan batasan

Setiap paket Claudin.io adalah **penggunaan tak terbatas** dengan **batas perlindungan pengeluaran**.
Anda tidak ditagih per token atau per permintaan — Anda membayar harga bulanan tetap dan
menggunakannya secara bebas. Batas ini hanya ada untuk menghentikan agen yang tak terkendali
(misalnya, lingkaran alat tak terbatas) dari menghabiskan paket Anda.

## Paket-paket

| Paket | Harga | Perlindungan pengeluaran | Terbaik untuk |
| --- | --- | --- | --- |
| **Pemula** | $5 / bln | $0.50 / jam | Mencoba — komitmen rendah |
| **Ringan** | $9 / bln | $1.00 / jam | Proyek hobi, coding sesekali |
| **Esensial** | $19 / bln atau $189 / thn | $2.00 / jam | Coding harian — pilihan populer |
| **Pro** ★ | $39 / bln atau $389 / thn | $4.00 / jam | Alur kerja agen berat |
| **Kuat** | $59 / bln atau $589 / thn | $6.00 / jam | Tim, banyak proyek |
| **Ultra** | $99 / bln atau $989 / thn | $10.00 / jam | Kekuatan maksimal, tim & produksi |

!!! tip "Kebanyakan orang tidak pernah mencapai batas"
    Batas per jam cukup besar untuk pekerjaan interaktif normal. Anda biasanya hanya
    menyentuhnya jika agen masuk ke lingkaran ketat — persis saat Anda *ingin* rem.

## claudinio vs Claudius

|                      | claudinio 🏆         | claudius ★           |
| -------------------- | -------------------- | -------------------- |
| **Starter**          | ✅                   |                      |
| **Lite**             | ✅                   |                      |
| **Essential**        | ✅                   | ✅                   |
| **Pro**              | ✅                   | ✅                   |
| **Power**            | ✅                   | ✅                   |
| **Ultra**            | ✅                   | ✅                   |

> **Nilai terbaik untuk uang Anda.**

### Untuk Starter / Lite: gunakan claudinio

Jika Anda menggunakan Starter atau Lite, claudinio adalah model yang akan Anda gunakan. Dan jujur? Anda tidak perlu melihat ke belakang. claudinio mampu bersaing dengan model-model frontier sementara harganya hanya sebagian kecil — menjadikannya sempurna untuk coding sehari-hari, belajar, dan proyek hobi.

### Untuk Essential ke atas: dunia adalah milik Anda

Essential ke atas memberi Anda akses ke claudinio dan claudius. Gunakan claudinio untuk tugas sehari-hari dan simpan claudius untuk saat Anda membutuhkan percikan ekstra — arsitektur kompleks, penalaran mendalam, atau sesi debugging yang sulit.

### Tapi ingat, aturan emasnya

Terlepas dari paket Anda, kami merekomendasikan menjadikan claudinio sebagai model default Anda. Ini adalah model unggulan kami, dan kami percaya padanya. Anda selalu dapat beralih ke claudius ketika tugas membutuhkannya.

### Alias Model

Semua paket mendukung alias model untuk model populer seperti: `claude-sonnet-4`, `gpt-4o`, `gemini-2.5-pro`, `llama-4`, `deepseek-v4`. Lihat [API Reference](/api-reference/) kami untuk daftar lengkap.

## Bagaimana cara kerja perlindungan pengeluaran

Setiap paket mendefinisikan **jendela** anggaran — periode bergulir dan pengeluaran maksimum di dalamnya:

- **Pemula**, **Ringan**, **Esensial**, **Pro**, **Kuat**, dan **Ultra** menggunakan jendela **1 jam**.

Di dalam jendela, penggunaan Anda mengakumulasi biaya internal kecil. Ketika biaya
internal itu mencapai batas jendela, permintaan berhenti sampai jendela direset.

Hanya panggilan model Anda melalui proxy. Setiap permintaan menambah total berjalan
jendela saat ini berdasarkan token yang digunakan. Ketika jendela direset,
totalnya juga direset.

Jika Anda mencapai batas dan mendapatkan error anggaran, Anda memiliki dua opsi:

1. Tunggu jendela direset (ditunjukkan di dasbor Anda).
2. Upgrade ke paket yang lebih tinggi untuk batas yang lebih besar.

Lihat [Error terkait paket](api-reference.md#errors) untuk melihat seperti apa error anggaran.
