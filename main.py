import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt5 import QtWidgets, QtCore
from ui_main import Ui_MainWindow  # pastikan nama file yang dihasilkan sesuai
import crud_operations  # pastikan modul ini ada dan berfungsi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #drakmode
        self.ui.dark_kbox.stateChanged.connect(self.toggle_dark_mode)

        # Setup QLineEdit untuk pencarian
        self.ui.searchInput.setPlaceholderText("Cari kontak...")

        # Set placeholder untuk input fields
        self.ui.nameInput.setPlaceholderText("Masukkan Nama")
        self.ui.phoneInput.setPlaceholderText("Masukkan Nomor Telepon")
        self.ui.emailInput.setPlaceholderText("Masukkan Email")

        # Atur kolom tabel
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Email"])
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSortingEnabled(True)

        # Set header alignment dan mode resize
        header = self.ui.tableWidget.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        # Buat header tabel lebih menonjol
        self.ui.tableWidget.horizontalHeader().setStyleSheet("background-color: #E0E0E0; font-weight: bold;")

        # Load existing contacts
        self.load_contacts()

        # Connect tombol dengan fungsi yang sesuai
        self.ui.pushButton.clicked.connect(self.Add)
        self.ui.pushButton_2.clicked.connect(self.Update)
        self.ui.pushButton_3.clicked.connect(self.Delete)
        self.ui.searchInput.textChanged.connect(self.filter_contacts)

        # Styling tombol
        self.ui.pushButton.setStyleSheet("background-color: #4CAF50; color: white; padding: 5px;")
        self.ui.pushButton_2.setStyleSheet("background-color: #2196F3; color: white; padding: 5px;")
        self.ui.pushButton_3.setStyleSheet("background-color: #f44336; color: white; padding: 5px;")

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
        filter_text = self.ui.searchInput.text()
        self.load_contacts(filter_text)

    def Add(self):
        name = self.ui.nameInput.text()
        phone = self.ui.phoneInput.text()
        email = self.ui.emailInput.text()

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
        name = self.ui.nameInput.text()
        phone = self.ui.phoneInput.text()
        email = self.ui.emailInput.text()

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
            self.ui.nameInput.setText(self.ui.tableWidget.item(selected_row, 1).text())
            self.ui.phoneInput.setText(self.ui.tableWidget.item(selected_row, 2).text())
            self.ui.emailInput.setText(self.ui.tableWidget.item(selected_row, 3).text())

    def clear_inputs(self):
        self.ui.nameInput.clear()
        self.ui.phoneInput.clear()
        self.ui.emailInput.clear()
    
     # Metode untuk mengaktifkan atau menonaktifkan Dark Mode
    def toggle_dark_mode(self):
        if self.ui.dark_kbox.isChecked():
            self.apply_dark_mode()
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
        self.setStyleSheet(dark_style)


# Jalankan aplikasi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
