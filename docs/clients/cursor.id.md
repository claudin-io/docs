# Cursor

[Cursor](https://cursor.com) memungkinkan Anda menambahkan model yang kompatibel dengan OpenAI melalui pengaturannya. Claudin.io terhubung melalui penggantian OpenAI base URL.

## Setup

1. Buka **Cursor → Settings → Models** (atau **Cursor Settings → AI**).
2. Gulir ke **OpenAI API Key** dan perluas opsi **Override OpenAI Base URL**.
3. Atur:

    | Bidang | Nilai |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Di bawah **Models**, tambahkan model kustom bernama **`claudinio`** dan aktifkan.
5. Nonaktifkan model default lainnya jika Anda ingin Cursor menggunakan Claudin.io secara eksklusif.

!!! note "Fitur bawaan Cursor"
    Fitur agen Cursor bekerja paling baik dengan model obrolan yang kompatibel dengan OpenAI.
    `claudinio` mendukung pemanggilan alat, sehingga alur Composer/Agent berfungsi. Beberapa
    fitur milik Cursor (Tab autocomplete, dll.) berjalan pada model Cursor sendiri dan tidak
    dirutekan melalui penggantian penyedia Anda.

## Verify

Buka obrolan di Cursor, pilih **claudinio**, dan kirim pesan. Jika Anda mendapatkan balasan, Anda siap. Jika tidak, periksa kembali apakah base URL diakhiri dengan `/v1` dan kunci ditempel tanpa spasi ekstra.

| Pengaturan | Nilai |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |