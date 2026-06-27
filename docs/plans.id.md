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

## Cara kerja perlindungan pengeluaran

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
