# Dokumentasi GUI Tools

Repositori ini berisi tiga alat antarmuka pengguna grafis (GUI) untuk bekerja dengan teknik kriptografi dan steganografi. Alat-alat ini dirancang agar mudah digunakan dan menyediakan fungsionalitas untuk enkripsi, dekripsi, serta steganografi.

## Daftar Isi
- [Cipher GUI](#cipher-gui)
- [DES GUI](#des-gui)
- [Steganography GUI](#steganography-gui)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

---

## Cipher GUI

Alat Cipher GUI menyediakan antarmuka sederhana untuk melakukan enkripsi dan dekripsi menggunakan cipher dasar seperti Caesar cipher atau substitution cipher.

### Fitur
- Mengenkripsi pesan menggunakan cipher dasar.
- Mendekripsi pesan dengan kunci yang sesuai.
- Antarmuka input dan output yang ramah pengguna.

### Contoh Penggunaan
1. Masukkan pesan plaintext.
2. Pilih metode cipher dan kunci.
3. Klik tombol "Encrypt" untuk mendapatkan pesan terenkripsi.
4. Gunakan tombol "Decrypt" dengan kunci yang sama untuk mendapatkan kembali pesan asli.

---

## DES GUI

Alat DES GUI mengimplementasikan algoritma Data Encryption Standard (DES), memungkinkan pengguna untuk mengenkripsi dan mendekripsi teks secara aman menggunakan kunci sepanjang 8 karakter.

### Fitur
- Mengenkripsi plaintext dengan DES.
- Mendekripsi ciphertext kembali ke plaintext.
- Validasi panjang kunci (harus 8 karakter).

### Contoh Penggunaan
1. Masukkan pesan plaintext.
2. Masukkan kunci sepanjang 8 karakter.
3. Klik tombol "Encrypt" untuk menghasilkan pesan terenkripsi.
4. Gunakan tombol "Decrypt" dengan kunci yang sama untuk mendapatkan kembali plaintext.

---

## Steganography GUI

Alat Steganography GUI memungkinkan pengguna untuk menyembunyikan pesan rahasia di dalam gambar dan mengambilnya kembali jika diperlukan.

### Fitur
- Menyisipkan pesan rahasia ke dalam gambar.
- Mengekstrak pesan tersembunyi dari gambar.
- Mendukung format gambar `.png` dan `.jpg`.

### Contoh Penggunaan
1. Pilih file gambar.
2. Masukkan pesan rahasia untuk disembunyikan.
3. Klik tombol "Hide Message" untuk menyisipkan pesan.
4. Gunakan tombol "Show Message" untuk mengekstrak pesan tersembunyi dari gambar.

---

## Instalasi

### Prasyarat
- Python 3.x
- Library yang diperlukan: `tkinter`, `pycryptodome`

### Langkah-langkah
1. Clone repositori:
   ```bash
   git clone https://github.com/your-username/gui-tools.git
   ```
2. Navigasikan ke direktori proyek:
   ```bash
   cd gui-tools
   ```
3. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan salah satu alat:
   ```bash
   python des_gui.py  # Untuk DES GUI
   python cipher_gui.py  # Untuk Cipher GUI
   python steganography_gui.py  # Untuk Steganography GUI
   ```

---

## Penggunaan

Setiap alat memiliki antarmuka grafis yang mudah digunakan. Ikuti petunjuk di GUI untuk melakukan operasi seperti enkripsi, dekripsi, atau steganografi.

---

## Kontribusi

Kontribusi sangat diterima! Silakan fork repositori ini, buat branch fitur baru, dan kirimkan pull request.

---

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
