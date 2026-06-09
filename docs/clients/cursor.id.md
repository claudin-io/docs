# Cursor

[Cursor](https://cursor.com) memungkinkan Anda menambahkan model yang kompatibel dengan OpenAI melalui pengaturannya. Claudin.io terhubung melalui override URL dasar OpenAI.

## Pengaturan

1. Buka **Cursor → Settings → Models** (atau **Cursor Settings → AI**).
2. Gulir ke **OpenAI API Key** dan perluas opsi **Override OpenAI Base URL**.
3. Atur:

    | Bidang | Nilai |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Di bawah **Models**, tambahkan model kustom bernama **`claudinio`** dan aktifkan.
5. Nonaktifkan model default lainnya jika Anda ingin Cursor hanya menggunakan Claudin.io.

!!! note "Fitur milik Cursor"
    Fitur agen Cursor bekerja paling baik dengan model obrolan yang kompatibel dengan OpenAI.
    `claudinio` mendukung panggilan alat, sehingga alur Composer/Agent berfungsi. Beberapa
    fitur milik Cursor (Tab autocomplete, dll.) berjalan di model Cursor sendiri
    dan tidak dialihkan melalui override penyedia Anda.

## Verifikasi

Buka obrolan di Cursor, pilih **claudinio**, dan kirim pesan. Jika Anda mendapatkan balasan, Anda siap. Jika tidak, periksa kembali apakah URL dasar diakhiri dengan `/v1` dan kunci ditempelkan tanpa spasi tambahan.

| Pengaturan | Nilai |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |