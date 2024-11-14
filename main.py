import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import QtWidgets, QtCore  # Tambahkan impor yang mungkin diperlukan
from ui_main import Ui_MainWindow  # pastikan nama file sesuai
import crud_operations  # modul CRUD Anda

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set up table widget
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Email"])
        
        # Agar tabel tidak bisa diedit langsung
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Set header alignment dan mode resize
        header = self.ui.tableWidget.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)  # Resize otomatis

        # Set kolom terakhir untuk stretch (hanya jika perlu)
        header.setStretchLastSection(True)

        # Load existing contacts
        self.load_contacts()

        # Connect buttons to functions
        self.ui.pushButton.clicked.connect(self.Add)
        self.ui.pushButton_2.clicked.connect(self.Update)
        self.ui.pushButton_3.clicked.connect(self.Delete)

    def load_contacts(self):
        contacts = crud_operations.get_contacts()
        self.ui.tableWidget.setRowCount(len(contacts))
        for row_num, contact in enumerate(contacts):
            self.ui.tableWidget.setItem(row_num, 0, QTableWidgetItem(str(contact[0])))  # ID
            self.ui.tableWidget.setItem(row_num, 1, QTableWidgetItem(contact[1]))  # Name
            self.ui.tableWidget.setItem(row_num, 2, QTableWidgetItem(contact[2]))  # Phone
            self.ui.tableWidget.setItem(row_num, 3, QTableWidgetItem(contact[3]))  # Email

        # Sesuaikan lebar kolom setelah data dimuat
        self.ui.tableWidget.resizeColumnsToContents()

    def Add(self):
        print("Tombol Add diklik")  # Debug untuk memastikan tombol diklik
        name = self.ui.lineEdit.text()  # Nama
        phone = self.ui.lineEdit_2.text()  # Phone
        email = self.ui.lineEdit_3.text()  # Email

        # Validasi input
        if not name or not phone or not email:
            QMessageBox.warning(self, "Kesalahan Input", "Semua field harus diisi.")
            return 

        # Menambah kontak ke database
        crud_operations.add_contact(name, phone, email)

        # Umpan balik setelah sukses menambahkan
        QMessageBox.information(self, "Sukses", "Kontak berhasil ditambahkan!")

        # Memuat ulang kontak untuk memperbarui tampilan
        self.load_contacts()
        self.clear_inputs()

    def Update(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Select Contact", "Please select a contact to update.")
            return

        contact_id = int(self.ui.tableWidget.item(selected_row, 0).text())
        name = self.ui.lineEdit.text()
        phone = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()

        crud_operations.update_contact(contact_id, name, phone, email)
        self.load_contacts()
        self.clear_inputs()

    def Delete(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Select Contact", "Please select a contact to delete.")
            return

        contact_id = int(self.ui.tableWidget.item(selected_row, 0).text())
        crud_operations.delete_contact(contact_id)
        self.load_contacts()
        self.clear_inputs()

    def populate_selected_contact(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            self.ui.lineEdit.setText(self.ui.tableWidget.item(selected_row, 1).text())
            self.ui.lineEdit_2.setText(self.ui.tableWidget.item(selected_row, 2).text())
            self.ui.lineEdit_3.setText(self.ui.tableWidget.item(selected_row, 3).text())

    def clear_inputs(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

# Jalankan aplikasi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
