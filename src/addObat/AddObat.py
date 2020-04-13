from SuccessMessage import SuccessMessage
from PyQt5 import QtWidgets, QtGui, uic
import sys
import sqlite3
from sqlite3 import Error

class AddObat(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(AddObat, self).__init__(*args, **kwargs)
        uic.loadUi('addObatWindow.ui', self)
        self.setWindowTitle('Tambah Obat')
        self.setWindowIcon(QtGui.QIcon('../../assets/img/icon.png'))  
        self.AddButton.clicked.connect(self.sendRequest)
        self.CancelButton.clicked.connect(self.cancelRequest)
        self.connectDB('../Obat.db')

    def connectDB(self, DBName):
        try:
            self.con = sqlite3.connect(DBName)
            return self.con
        except Error as e:
            self.showError(str(e))

    def addEntry(self, entry):
        cursorDB = self.con.cursor()
        cursorDB.execute('''INSERT INTO Obat(ID, Nama, Jumlah, Deskripsi, Kadaluarsa, Cacat) VALUES (?, ?, ?, ?, ?, ?)''', entry)
        self.con.commit()

    def sendRequest(self):
        try:
            # Something to do with db
            if(int(self.JumlahObat.toPlainText())<1):
                raise Exception('Jumlah obat harus lebih dari nol!')
            if(not self.Yes.isChecked() and not self.No.isChecked()):
                raise Exception('Kondisi cacat atau tidak harus dirinci!')
            cacatOpt = 0
            if(self.Yes.isChecked()):
                cacatOpt = 1
            entry = (int(self.IDObat.toPlainText()), self.NamaObat.toPlainText(), int(self.JumlahObat.toPlainText()), self.DescObat.toPlainText(), self.KadaluarsaObat.date().toString("dd/MM/yyyy"), cacatOpt)
            self.addEntry(entry)
            QtWidgets.QMessageBox.information(self, 'Sukses', 'Data obat berhasil ditambahkan ke database!')
            # dialog = QtWidgets.QDialog()    
            # succ_dialog = SuccessMessage(dialog)
            # succ_dialog.setupUi(dialog)
            # dialog.show()
            # dialog.exec_()
        except Exception as e:
            self.showError(str(e))

    def cancelRequest(self):
        self.close()

    def showError(self, msg):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.setWindowTitle('ERROR')
        error_dialog.setWindowIcon(QtGui.QIcon('../../assets/img/icon.png'))  
        error_dialog.showMessage(msg)
        error_dialog.exec_()

