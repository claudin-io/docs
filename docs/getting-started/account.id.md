# Buat akun Anda

Mendapatkan kunci API yang berfungsi memakan waktu sekitar satu menit.

## 1. Masuk dengan GitHub

Buka **[claudin.io](https://claudin.io)** dan klik **Masuk dengan GitHub**.
Claudin.io menggunakan GitHub untuk login — tidak ada kata sandi terpisah yang perlu dikelola.

Saat pertama kali masuk, akun Anda akan dibuat secara otomatis dengan paket **Gratis**, sehingga Anda dapat mencobanya sebelum membayar.

## 2. Hasilkan kunci API Anda

Setelah Anda berada di [dasbor](https://claudin.io/dashboard):

1. Temukan kartu **Kunci API**.
2. Klik **Hasilkan kunci** (atau **Buat kunci baru**).
3. Salin kunci tersebut — bentuknya seperti `sk-...`.

!!! warning "Perlakukan kunci Anda seperti kata sandi"
    Kunci API Anda menghabiskan kredit paket Anda. Jangan commit ke repositori,
    tempel di obrolan publik, atau membagikannya. Kalau sebuah kunci bocor, cabut
    dari dasbor dan buat yang baru.

## 3. Catat dua nilai yang Anda perlukan

Setiap integrasi membutuhkan dua hal yang sama:

| Nilai | Apa itu |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Model** | `claudinio` |
| **API key** | `sk-...` yang baru saja Anda salin |

Itu saja. Selanjutnya, [lakukan panggilan API mentah](first-call.md) untuk memastikannya berfungsi, atau langsung [menghubungkan alat Anda](../clients/claude-code.md).

---

## Memilih paket

Anda bisa tetap di **Free** untuk mencoba. Saat siap, pilih paket dari dasbor —
dompet kredit yang terisi ulang setiap bulan, mulai $19 — lihat
[Paket & kredit](../plans.md) untuk gambaran lengkapnya.

Peningkatan ditangani melalui Stripe dan berlaku segera.