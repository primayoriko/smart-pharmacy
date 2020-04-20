import sqlite3
from sqlite3 import Error
from PyQt5 import QtWidgets, QtGui, uic

class AddObat(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(AddObat, self).__init__(*args, **kwargs)
        uic.loadUi('addObatWindow.ui', self)
        self.setWindowTitle('Tambah Obat')
        self.setWindowIcon(QtGui.QIcon('../../assets/img/icon.png'))  
        self.AddButton.clicked.connect(self.sendRequest)
        self.CancelButton.clicked.connect(self.cancelRequest)

    def connectDB(self, DBName):
        try:
            self.con = sqlite3.connect(DBName)
            return self.con
        except Error as e:
            self.showError(str(e))

    def addEntry(self, entry, testMode):
        try:
            if(entry[0] < 1):
                raise Exception('ID obat harus bilangan bulat positif!')
            if(entry[2] < 1):
                raise Exception('Jumlah obat harus lebih dari nol!')
            if(entry[5] == -1):
                raise Exception('Kondisi cacat atau tidak harus dirinci!')

            cursorDB = self.con.cursor()
            cursorDB.execute('''INSERT INTO Obat(ID, Nama, Jumlah, Deskripsi, Kadaluarsa, Cacat) VALUES (?, ?, ?, ?, ?, ?)''', entry)
            self.con.commit()
            if(not testMode):
                QtWidgets.QMessageBox.information(self, 'Sukses', 'Data obat berhasil ditambahkan ke database!')
            return 0

        except Exception as e:
            if(not testMode):
                self.showError(str(e))
            return 1


    def sendRequest(self):
        try:
            cacatOpt = -1
            if(self.Yes.isChecked()):
                cacatOpt = 1
            elif(self.No.isChecked()):
                cacatOpt = 0
            entry = (int(self.IDObat.toPlainText()), self.NamaObat.toPlainText(), int(self.JumlahObat.toPlainText()), self.DescObat.toPlainText(), self.KadaluarsaObat.date().toString("dd/MM/yyyy"), cacatOpt)
            self.addEntry(entry, False)            
            return 0
        except Exception as e:
            self.showError(str(e))
            return 1

    def cancelRequest(self):
        self.close()

    def showError(self, msg):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.setWindowTitle('ERROR')
        error_dialog.setWindowIcon(QtGui.QIcon('../../assets/img/icon.png'))  
        error_dialog.showMessage(msg)
        error_dialog.exec_()

    def clearDB(self):
        cursorDB = self.con.cursor()
        cursorDB.execute('DELETE FROM Obat')
        self.con.commit()

# dialog = QtWidgets.QDialog()    
# succ_dialog = SuccessMessage(dialog)
# succ_dialog.setupUi(dialog)
# dialog.show()
# dialog.exec_()
