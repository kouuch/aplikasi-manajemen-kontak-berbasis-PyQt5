from db_connection import create_connection

def get_contacts():
    connection = create_connection()
    if connection is None:
        print("Koneksi ke database gagal.")
        return []
    cursor = connection.cursor()
    query = "SELECT * FROM contacts"
    cursor.execute(query)
    contacts = cursor.fetchall()
    connection.close()
    return contacts

def add_contact(name, phone, email):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, phone, email))
        connection.commit()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")  # Log kesalahan atau tampilkan pesan ke pengguna
    finally:
        connection.close()

def update_contact(contact_id, name, phone, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE contacts SET name = %s, phone = %s, email = %s WHERE id = %s"
    cursor.execute(query, (name, phone, email, contact_id))
    connection.commit()
    connection.close()

def delete_contact(contact_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM contacts WHERE id = %s"
    cursor.execute(query, (contact_id,))
    connection.commit()
    connection.close()