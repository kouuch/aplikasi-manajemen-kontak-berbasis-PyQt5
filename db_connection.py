import mysql.connector  # Impor library untuk koneksi ke MySQL
from mysql.connector import Error  # Impor kelas Error untuk menangani kesalahan koneksi

def create_connection():
    try:
        # Mencoba untuk membuat koneksi ke database MySQL
        connection = mysql.connector.connect(
            host="localhost",  # Sesuaikan dengan konfigurasi host MySQL Anda
            user="root",       # Ganti dengan username MySQL Anda
            password="",       # Ganti dengan password MySQL Anda
            database="crud_db" # Ganti dengan nama database Anda
        )
        # Mengecek apakah koneksi berhasil
        if connection.is_connected():
            print("Koneksi ke database berhasil.")  # Menampilkan pesan jika koneksi berhasil
        return connection  # Mengembalikan objek koneksi jika berhasil
    except Error as e:  # Menangani kesalahan koneksi
        print(f"Error: '{e}' terjadi saat menghubungkan ke database.")  # Menampilkan pesan error jika terjadi kesalahan
        return None  # Mengembalikan None jika koneksi gagal

# Tambahkan kode berikut untuk menguji koneksi saat file dijalankan
if __name__ == "__main__":  # Memastikan kode ini hanya dijalankan ketika file dijalankan langsung
    create_connection()  # Memanggil fungsi create_connection untuk menguji koneksi
