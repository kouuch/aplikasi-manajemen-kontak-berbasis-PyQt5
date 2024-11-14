# Aplikasi Manajemen Kontak dengan PyQt5

Aplikasi manajemen kontak berbasis desktop menggunakan **PyQt5** untuk antarmuka pengguna dan **MySQL** untuk penyimpanan data. Aplikasi ini memungkinkan pengguna untuk menambah, memperbarui, menghapus, dan mencari kontak dengan dukungan untuk mode terang dan gelap.

## Fitur
- **Mode Gelap**: Dapat mengaktifkan atau menonaktifkan mode gelap untuk antarmuka pengguna.
- **Operasi CRUD**:
  - **Tambah Kontak**: Menambahkan kontak baru dengan nama, nomor telepon, dan email.
  - **Perbarui Kontak**: Memperbarui informasi kontak yang sudah ada.
  - **Hapus Kontak**: Menghapus kontak yang dipilih dari daftar.
  - **Cari Kontak**: Memfilter kontak berdasarkan nama menggunakan input pencarian.
- **Tabel Kontak**: Menampilkan daftar kontak dalam bentuk tabel dengan ID, Nama, Telepon, dan Email.

## Instalasi

1. **Clone repository** ini ke lokal komputer Anda:
    ```bash
    https://github.com/kouuch/aplikasi-manajemen-kontak-berbasis-PyQt5.git
    ```
2. **Install dependencies**:
    Pastikan Anda memiliki Python 3.x terinstal. Anda juga perlu menginstal dependensi yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```
3. **Install MySQL**:
    Aplikasi ini menggunakan **MySQL** sebagai database backend. Pastikan MySQL terinstal dan jalankan database berikut:
    - Buat database baru dengan nama `crud_db`.
    - Buat tabel `contacts` dengan skema berikut:
    ```sql
    CREATE TABLE contacts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(15) NOT NULL,
        email VARCHAR(255) NOT NULL
    );
    ```
    - Anda dapat mengonfigurasi kredensial MySQL di dalam kode, tepatnya pada bagian `create_connection()` di `crud_operations.py`.

## Tampilan Proyek
![1](https://github.com/user-attachments/assets/2401bb0b-aad8-4cd4-9eda-ea26eff95670)
