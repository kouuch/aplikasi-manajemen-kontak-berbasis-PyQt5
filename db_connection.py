import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Sesuaikan dengan konfigurasi MySQL Anda
            user="root",       # Ganti dengan username MySQL Anda
            password="",       # Ganti dengan password MySQL Anda
            database="crud_db" # Ganti dengan nama database Anda
        )
        if connection.is_connected():
            print("Koneksi ke database berhasil.")
        return connection
    except Error as e:
        print(f"Error: '{e}' terjadi saat menghubungkan ke database.")
        return None

# Tambahkan kode berikut untuk menguji koneksi saat file dijalankan
if __name__ == "__main__":
    create_connection()