import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt5 import QtWidgets, QtCore
from ui_main import Ui_MainWindow  # pastikan nama file yang dihasilkan sesuai
import crud_operations  # pastikan modul ini ada dan berfungsi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  # Inisialisasi antarmuka pengguna yang dihasilkan oleh PyQt5 designer
        self.ui.setupUi(self)  # Setup UI untuk main window

        # Dark Mode Switch
        self.ui.dark_kbox.stateChanged.connect(self.toggle_dark_mode)  # Menghubungkan state checkbox untuk dark mode dengan fungsi toggle_dark_mode

        # Setup QLineEdit untuk pencarian
        self.ui.searchInput.setPlaceholderText("Cari kontak...")  # Set placeholder untuk input pencarian

        # Set placeholder untuk input fields
        self.ui.nameInput.setPlaceholderText("Masukkan Nama")
        self.ui.phoneInput.setPlaceholderText("Masukkan Nomor Telepon")
        self.ui.emailInput.setPlaceholderText("Masukkan Email")

        # Atur kolom tabel
        self.ui.tableWidget.setColumnCount(4)  # Tentukan jumlah kolom pada tabel
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Email"])  # Label untuk setiap kolom
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Menonaktifkan editing pada tabel
        self.ui.tableWidget.setSortingEnabled(True)  # Mengaktifkan sorting pada tabel

        # Set header alignment dan mode resize
        header = self.ui.tableWidget.horizontalHeader()  # Mendapatkan header tabel
        header.setDefaultAlignment(QtCore.Qt.AlignHCenter)  # Mengatur alignment teks header ke tengah
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)  # Resize otomatis sesuai dengan konten
        header.setStretchLastSection(True)  # Menyebarkan lebar kolom terakhir

        # Buat header tabel lebih menonjol
        self.ui.tableWidget.horizontalHeader().setStyleSheet("background-color: #E0E0E0; font-weight: bold;")  # Styling untuk header tabel

        # Load existing contacts
        self.load_contacts()  # Memuat data kontak yang sudah ada ke dalam tabel

        # Connect tombol dengan fungsi yang sesuai
        self.ui.pushButton.clicked.connect(self.Add)  # Tombol untuk menambahkan kontak
        self.ui.pushButton_2.clicked.connect(self.Update)  # Tombol untuk memperbarui kontak
        self.ui.pushButton_3.clicked.connect(self.Delete)  # Tombol untuk menghapus kontak
        self.ui.searchInput.textChanged.connect(self.filter_contacts)  # Tombol pencarian kontak

        # Styling tombol
        self.ui.pushButton.setStyleSheet("background-color: #4CAF50; color: white; padding: 5px;")  # Styling tombol tambah
        self.ui.pushButton_2.setStyleSheet("background-color: #2196F3; color: white; padding: 5px;")  # Styling tombol update
        self.ui.pushButton_3.setStyleSheet("background-color: #f44336; color: white; padding: 5px;")  # Styling tombol delete

    def load_contacts(self, filter_text=""):
        contacts = crud_operations.get_contacts()  # Mengambil daftar kontak dari modul crud_operations
        if filter_text:  # Jika ada filter pencarian
            contacts = [contact for contact in contacts if filter_text.lower() in contact[1].lower()]  # Filter kontak berdasarkan nama

        self.ui.tableWidget.setRowCount(len(contacts))  # Menentukan jumlah baris pada tabel
        for row_num, contact in enumerate(contacts):  # Menambahkan data kontak ke tabel
            self.ui.tableWidget.setItem(row_num, 0, QTableWidgetItem(str(contact[0])))  # ID
            self.ui.tableWidget.setItem(row_num, 1, QTableWidgetItem(contact[1]))  # Name
            self.ui.tableWidget.setItem(row_num, 2, QTableWidgetItem(contact[2]))  # Phone
            self.ui.tableWidget.setItem(row_num, 3, QTableWidgetItem(contact[3]))  # Email

        self.ui.tableWidget.resizeColumnsToContents()  # Menyesuaikan ukuran kolom agar sesuai dengan konten

    def filter_contacts(self):
        filter_text = self.ui.searchInput.text()  # Mengambil teks filter dari input pencarian
        self.load_contacts(filter_text)  # Memanggil fungsi untuk memuat kontak yang sudah difilter

    def Add(self):
        name = self.ui.nameInput.text()  # Mendapatkan input nama
        phone = self.ui.phoneInput.text()  # Mendapatkan input nomor telepon
        email = self.ui.emailInput.text()  # Mendapatkan input email

        if not name or not phone or not email:  # Mengecek apakah ada input yang kosong
            QMessageBox.warning(self, "Kesalahan Input", "Semua field harus diisi.")  # Menampilkan pesan jika ada input kosong
            return 

        crud_operations.add_contact(name, phone, email)  # Menambahkan kontak baru
        QMessageBox.information(self, "Sukses", "Kontak berhasil ditambahkan!")  # Menampilkan pesan sukses
        self.load_contacts()  # Memuat kembali kontak yang ada
        self.clear_inputs()  # Mengosongkan input fields

    def Update(self):
        selected_row = self.ui.tableWidget.currentRow()  # Mendapatkan baris yang dipilih pada tabel
        if selected_row == -1:  # Jika tidak ada baris yang dipilih
            QMessageBox.warning(self, "Select Contact", "Please select a contact to update.")  # Menampilkan pesan jika tidak ada kontak yang dipilih
            return

        contact_id = int(self.ui.tableWidget.item(selected_row, 0).text())  # Mengambil ID kontak yang dipilih
        name = self.ui.nameInput.text()  # Mengambil input nama
        phone = self.ui.phoneInput.text()  # Mengambil input nomor telepon
        email = self.ui.emailInput.text()  # Mengambil input email

        crud_operations.update_contact(contact_id, name, phone, email)  # Memperbarui data kontak
        self.load_contacts()  # Memuat kembali kontak yang ada
        self.clear_inputs()  # Mengosongkan input fields

    def Delete(self):
        selected_row = self.ui.tableWidget.currentRow()  # Mendapatkan baris yang dipilih pada tabel
        if selected_row == -1:  # Jika tidak ada baris yang dipilih
            QMessageBox.warning(self, "Select Contact", "Please select a contact to delete.")  # Menampilkan pesan jika tidak ada kontak yang dipilih
            return

        contact_id = int(self.ui.tableWidget.item(selected_row, 0).text())  # Mengambil ID kontak yang dipilih
        crud_operations.delete_contact(contact_id)  # Menghapus kontak yang dipilih
        self.load_contacts()  # Memuat kembali kontak yang ada
        self.clear_inputs()  # Mengosongkan input fields

    def populate_selected_contact(self):
        selected_row = self.ui.tableWidget.currentRow()  # Mendapatkan baris yang dipilih
        if selected_row != -1:  # Jika ada baris yang dipilih
            # Mengisi input fields dengan data kontak yang dipilih
            self.ui.nameInput.setText(self.ui.tableWidget.item(selected_row, 1).text())
            self.ui.phoneInput.setText(self.ui.tableWidget.item(selected_row, 2).text())
            self.ui.emailInput.setText(self.ui.tableWidget.item(selected_row, 3).text())

    def clear_inputs(self):
        # Mengosongkan semua input fields
        self.ui.nameInput.clear()
        self.ui.phoneInput.clear()
        self.ui.emailInput.clear()
    
    # Metode untuk mengaktifkan atau menonaktifkan Dark Mode
    def toggle_dark_mode(self):
        if self.ui.dark_kbox.isChecked():  # Mengecek apakah checkbox dark mode aktif
            self.apply_dark_mode()  # Aktifkan dark mode
        else:
            self.setStyleSheet("")  # Kembali ke mode terang

    def apply_dark_mode(self):
        dark_style = """
        QMainWindow {
            background-color: #2e2e2e;
            color: #ffffff;
        }
        QLabel, QLineEdit, QTableWidget, QTableWidgetItem {
            color: #ffffff;
        }
        QPushButton {
            background-color: #444444;
            color: white;
            border: none;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #666666;
        }
        QLineEdit {
            background-color: #3c3c3c;
            border: 1px solid #5a5a5a;
            color: white;
        }
        QTableWidget {
            background-color: #3c3c3c;
            alternate-background-color: #444444;
            gridline-color: #5a5a5a;
        }
        QHeaderView::section {
            background-color: #5a5a5a;
            color: white;
            padding: 4px;
        }
        """
        self.setStyleSheet(dark_style)  # Menerapkan stylesheet untuk mode gelap ke seluruh aplikasi

# Jalankan aplikasi
if __name__ == "__main__":  # Pastikan kode ini hanya dijalankan saat file dijalankan langsung
    app = QApplication(sys.argv)  # Membuat instance aplikasi Qt
    window = MainWindow()  # Membuat instance dari jendela utama aplikasi
    window.show()  # Menampilkan jendela utama
    sys.exit(app.exec_())  # Menjalankan event loop aplikasi Qt dan keluar saat aplikasi ditutup
