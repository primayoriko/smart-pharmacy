"""Main program loader

Menjalankan menu data_obat_racik_baru
"""
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QFileDialog, QMessageBox
from PyQt5 import QtGui, QtCore, QtWidgets
from designer.data_obat_racik_baru import Ui_Dialog

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.addItemsButton.clicked.connect(self.add_item_list)
        self.show()
    
    def add_item_list(self):
        self.ui.field_namaObat1 = QtWidgets.QLineEdit(self)
        self.ui.field_namaObat1.setGeometry(QtCore.QRect(40, 160, 281, 20))
        self.ui.field_namaObat1.setObjectName("field_namaObat2")
        self.ui.field_jumlah1 = QtWidgets.QLineEdit(self)
        self.ui.field_jumlah1.setGeometry(QtCore.QRect(330, 160, 81, 20))
        self.ui.field_jumlah1.setObjectName("field_jumlah2")
        self.ui.field_satuan1 = QtWidgets.QComboBox(self)
        self.ui.field_satuan1.setGeometry(QtCore.QRect(420, 160, 161, 22))
        self.ui.field_satuan1.setObjectName("field_satuan2")
        self.ui.addItemsButton = QtWidgets.QPushButton(self)
        self.ui.addItemsButton.setGeometry(QtCore.QRect(40, 190, 31, 31))

app = QApplication([])
w = AppWindow()
w.show()
app.exec_()