# Paket & Batasan

Setiap paket Claudin.io adalah **pemakaian tak terbatas** dengan **batas perlindungan biaya**.
Anda tidak ditagih per token atau per permintaan — Anda membayar harga bulanan tetap dan
menggunakannya secara bebas. Batas ini hanya ada untuk menghentikan agen yang lepas kendali (misalnya, perulangan alat yang tak terbatas) agar tidak menguras paket Anda.

## Paket-paket

| Paket | Harga | Batas perlindungan biaya | Cocok untuk |
| --- | --- | --- | --- |
| **Free** | $0 | $0.45 / hari | Mencoba, penggunaan ringan |
| **Lite** | $5 / bln | $0.60 / jam | Proyek hobi, coding sesekali |
| **Essential** | $10 / bln | $1.50 / jam | Coding harian — pilihan populer |
| **Pro** | $29 / bln | $4.00 / jam | Alur kerja agentik berat |

!!! tip "Kebanyakan orang tidak pernah mencapai batas"
    Batas per jam sudah cukup longgar untuk pekerjaan interaktif normal. Anda biasanya hanya
    mendekatinya jika agen masuk ke dalam perulangan ketat — yang justru saat Anda
    *ingin* ada rem.

## Cara kerja perlindungan biaya

Setiap paket menentukan **jendela** anggaran — periode bergulir dan batas pengeluaran maksimum
di dalamnya:

- **Free** menggunakan jendela **24 jam** (`$0.45/hari`).
- **Lite / Essential / Pro** menggunakan jendela **1 jam**.

Dalam jendela tersebut, pemakaian Anda mengakumulasi biaya internal yang sangat kecil. Ketika
biaya internal tersebut mencapai batas jendela, permintaan dijeda sampai jendela disetel ulang.
Jendela disetel ulang sesuai jadwal tetap (setiap jam tepat, UTC, untuk paket per jam), dan sisa
anggaran Anda ditampilkan **langsung di dasbor Anda**.

Ini adalah *perlindungan biaya*, bukan penagihan terukur — angka dolar adalah plafon perlindungan,
bukan yang Anda bayar. Tagihan Anda sebenarnya hanyalah langganan bulanan tetap.

## Menaikkan & Menurunkan Paket

- **Naikkan** kapan saja dari [dasbor](https://claudin.io/dashboard).
  Pembayaran ditangani melalui Stripe dan batas baru berlaku segera.
- **Turunkan atau batalkan** dari tempat yang sama. Jika Anda membatalkan, Anda tetap mendapat paket
  berbayar hingga akhir periode yang sudah Anda bayar, lalu secara otomatis turun ke **Free** —
  akun dan kunci Anda tetap tersimpan.

## Apa yang termasuk dalam batas

Hanya panggilan model Anda melalui proxy. Setiap permintaan menambah total berjalan jendela saat ini
berdasarkan token yang digunakan. Ketika jendela disetel ulang, totalnya ikut disetel ulang.

Jika Anda mencapai batas dan mendapatkan kesalahan anggaran, Anda memiliki dua opsi:

1. Tunggu hingga jendela disetel ulang (ditampilkan di dasbor Anda).
2. Naikkan ke paket yang lebih tinggi untuk batas yang lebih besar.

Lihat [Kesalahan terkait Paket](api-reference.md#errors) untuk seperti apa tampilan kesalahan anggaran.