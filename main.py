import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit, QVBoxLayout, QWidget
from PyQt5 import QtWidgets, QtCore
from ui_main import Ui_MainWindow
import crud_operations

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # QLineEdit untuk pencarian
        self.searchInput = QLineEdit(self)
        self.searchInput.setPlaceholderText("Cari kontak...")  # Teks placeholder
        
        # Tambahkan searchInput ke posisi atas layout grid
        # Misalnya, tambahkan ke baris 0, kolom 0, dan span untuk mencakup beberapa kolom
        self.ui.gridLayout.addWidget(self.searchInput, 0, 0, 1, 4)

        # Atur kolom tabel
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Email"])
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Set header alignment dan mode resize
        header = self.ui.tableWidget.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        # Buat header tabel lebih menonjol dengan background dan font tebal
        self.ui.tableWidget.horizontalHeader().setStyleSheet("background-color: #E0E0E0; font-weight: bold;")

        # Load existing contacts
        self.load_contacts()

        # Connect buttons to functions
        self.ui.pushButton.setStyleSheet("background-color: #4CAF50; color: white; padding: 5px;")
        self.ui.pushButton_2.setStyleSheet("background-color: #2196F3; color: white; padding: 5px;")
        self.ui.pushButton_3.setStyleSheet("background-color: #f44336; color: white; padding: 5px;")

        # Connect search input to filter function
        self.searchInput.textChanged.connect(self.filter_contacts)

    def load_contacts(self, filter_text=""):
        contacts = crud_operations.get_contacts()
        if filter_text:
            contacts = [contact for contact in contacts if filter_text.lower() in contact[1].lower()]
        
        self.ui.tableWidget.setRowCount(len(contacts))
        for row_num, contact in enumerate(contacts):
            self.ui.tableWidget.setItem(row_num, 0, QTableWidgetItem(str(contact[0])))  # ID
            self.ui.tableWidget.setItem(row_num, 1, QTableWidgetItem(contact[1]))  # Name
            self.ui.tableWidget.setItem(row_num, 2, QTableWidgetItem(contact[2]))  # Phone
            self.ui.tableWidget.setItem(row_num, 3, QTableWidgetItem(contact[3]))  # Email

        self.ui.tableWidget.resizeColumnsToContents()

    def filter_contacts(self):
        filter_text = self.searchInput.text()
        self.load_contacts(filter_text)

    def Add(self):
        name = self.ui.lineEdit.text()
        phone = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()

        if not name or not phone or not email:
            QMessageBox.warning(self, "Kesalahan Input", "Semua field harus diisi.")
            return 

        crud_operations.add_contact(name, phone, email)
        QMessageBox.information(self, "Sukses", "Kontak berhasil ditambahkan!")
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
