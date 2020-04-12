"""Main program loader

Menjalankan menu data_obat_racik_baru
"""
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QFileDialog, QMessageBox
from PyQt5 import QtGui, QtCore, QtWidgets
from designer.data_obat_racik_baru import Ui_Dialog
import sqlite3

satuanList = ["Gram", "Miligram", "Tablet", "Kapsul", "Sachet"]

class AppWindow(QDialog):
    """AppWindow class

    Taking layout information from Ui_Dialog class and adding logic
    """
    def __init__(self):
        super().__init__()
        self.count = 1
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.addItemsButton.clicked.connect(self.add_item_list)
        self.ui.vNamaObat.setAlignment(QtCore.Qt.AlignTop)
        self.ui.vJumlah.setAlignment(QtCore.Qt.AlignTop)
        self.ui.vSatuan.setAlignment(QtCore.Qt.AlignTop)
        self.ui.field_satuan1.insertItems(0, satuanList)
    
    def add_item_list(self):
        field_namaObat2 = QtWidgets.QLineEdit(self)
        field_namaObat2.setObjectName("field_namaObat" + str(self.count + 1))
        self.ui.vNamaObat.addWidget(field_namaObat2)
        field_jumlah2 = QtWidgets.QLineEdit(self)
        field_jumlah2.setObjectName("field_jumlah" + str(self.count + 1))
        self.ui.vJumlah.addWidget(field_jumlah2)
        field_satuan2 = QtWidgets.QComboBox(self)
        field_satuan2.setObjectName("field_satuan" + str(self.count + 1))
        field_satuan2.insertItems(0, satuanList)
        self.ui.vSatuan.addWidget(field_satuan2)
        if self.count < 9:
            self.ui.addItemsButton.setGeometry(40, 160 + self.count * 30, 31, 31)
        self.count += 1
        # print(self.ui.field_namaObat2)
        # print(self.ui.field_namaObat1)
    def show_alert_box(self, msg):
        alert = QMessageBox()
        alert.setText(msg)
        alert.setWindowTitle("Error")
        alert.setIcon(QMessageBox.Critical)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()

def get_dialog_data(parent, count):
    retval = []
    for i in range (1, count+1) :
        tupl = (parent.findChild(QtWidgets.QLineEdit, "field_namaObat" + str(i)).text(),
                parent.findChild(QtWidgets.QLineEdit, "field_jumlah" + str(i)).text(),
                parent.findChild(QtWidgets.QComboBox, "field_satuan" + str(i)).currentText())
        retval.append(tupl)
    return { "nama" : parent.ui.fieldNamaResep.text(), "data" : retval }

def run():
    app = QApplication([])
    w = AppWindow()
    w.show()
    app.exec_()
    print(get_dialog_data(w, w.count))

if __name__ == "__main__":
    run()