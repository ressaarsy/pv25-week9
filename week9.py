import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QInputDialog,
    QHBoxLayout, QVBoxLayout, QLabel
)
from PyQt5.QtCore import Qt

class DemoInput(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.setGeometry(100, 100, 600, 250)

        self.lay_utama = QVBoxLayout()
        self.lay_utama.setAlignment(Qt.AlignCenter)

        baris1 = QHBoxLayout()
        self.tbl_list = QPushButton("Choose from list")
        self.teks_list = QLineEdit()
        self.teks_list.setMinimumWidth(300)
        baris1.addWidget(self.tbl_list)
        baris1.addSpacing(20)
        baris1.addWidget(self.teks_list)
        baris1.setAlignment(Qt.AlignCenter)

        baris2 = QHBoxLayout()
        self.tbl_nama = QPushButton("get name")
        self.teks_nama = QLineEdit()
        self.teks_nama.setMinimumWidth(300)
        baris2.addWidget(self.tbl_nama)
        baris2.addSpacing(20)
        baris2.addWidget(self.teks_nama)
        baris2.setAlignment(Qt.AlignCenter)

        baris3 = QHBoxLayout()
        self.tbl_int = QPushButton("Enter an integer")
        self.teks_int = QLineEdit()
        self.teks_int.setMinimumWidth(300)
        baris3.addWidget(self.tbl_int)
        baris3.addSpacing(20)
        baris3.addWidget(self.teks_int)
        baris3.setAlignment(Qt.AlignCenter)

        self.label_identitas = QLabel("Nama: Muh. Ressa | NIM: F1D022137")
        self.label_identitas.setAlignment(Qt.AlignCenter)

        self.lay_utama.addLayout(baris1)
        self.lay_utama.addLayout(baris2)
        self.lay_utama.addLayout(baris3)
        self.lay_utama.addSpacing(20)
        self.lay_utama.addWidget(self.label_identitas)

        self.setLayout(self.lay_utama)

        self.tbl_list.clicked.connect(self.pilih_item)
        self.tbl_nama.clicked.connect(self.masuk_nama)
        self.tbl_int.clicked.connect(self.masuk_angka)

    def pilih_item(self):
        daftar = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog", 
                                        "list of languages", daftar, 0, False)
        if ok and item:
            self.teks_list.setText(item)

    def masuk_nama(self):
        nama, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and nama:
            self.teks_nama.setText(nama)

    def masuk_angka(self):
        angka, ok = QInputDialog.getInt(self, "integer input dialog", "enter a number")
        if ok:
            self.teks_int.setText(str(angka))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    jdl = DemoInput()
    jdl.show()
    sys.exit(app.exec_())
