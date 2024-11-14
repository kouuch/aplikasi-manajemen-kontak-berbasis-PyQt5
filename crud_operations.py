from db_connection import create_connection  # Impor fungsi untuk membuat koneksi ke database

def get_contacts():
    connection = create_connection()  # Membuat koneksi ke database
    if connection is None:  # Mengecek apakah koneksi gagal
        print("Koneksi ke database gagal.")  # Menampilkan pesan jika koneksi gagal
        return []  # Mengembalikan daftar kosong jika koneksi gagal
    cursor = connection.cursor()  # Membuat cursor untuk mengeksekusi query
    query = "SELECT * FROM contacts"  # Query untuk mengambil semua data kontak
    cursor.execute(query)  # Menjalankan query
    contacts = cursor.fetchall()  # Mengambil semua hasil query
    connection.close()  # Menutup koneksi ke database setelah selesai
    return contacts  # Mengembalikan daftar kontak

def add_contact(name, phone, email):
    try:
        connection = create_connection()  # Membuat koneksi ke database
        cursor = connection.cursor()  # Membuat cursor untuk mengeksekusi query
        query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"  # Query untuk menambahkan kontak baru
        cursor.execute(query, (name, phone, email))  # Menjalankan query dengan parameter yang diberikan
        connection.commit()  # Menyimpan perubahan ke database
    except Exception as e:  # Menangani error jika terjadi kesalahan saat eksekusi
        print(f"Terjadi kesalahan: {e}")  # Menampilkan pesan error jika terjadi masalah
    finally:
        connection.close()  # Menutup koneksi ke database setelah operasi selesai

def update_contact(contact_id, name, phone, email):
    connection = create_connection()  # Membuat koneksi ke database
    cursor = connection.cursor()  # Membuat cursor untuk mengeksekusi query
    query = "UPDATE contacts SET name = %s, phone = %s, email = %s WHERE id = %s"  # Query untuk memperbarui data kontak
    cursor.execute(query, (name, phone, email, contact_id))  # Menjalankan query untuk update data berdasarkan ID
    connection.commit()  # Menyimpan perubahan ke database
    connection.close()  # Menutup koneksi ke database setelah operasi selesai

def delete_contact(contact_id):
    connection = create_connection()  # Membuat koneksi ke database
    cursor = connection.cursor()  # Membuat cursor untuk mengeksekusi query
    query = "DELETE FROM contacts WHERE id = %s"  # Query untuk menghapus kontak berdasarkan ID
    cursor.execute(query, (contact_id,))  # Menjalankan query untuk menghapus data berdasarkan ID
    connection.commit()  # Menyimpan perubahan ke database
    connection.close()  # Menutup koneksi ke database setelah operasi selesai
