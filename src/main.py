# Main Program
from PyQt5 import QtWidgets, QtGui
from designer.UpdateJumlahObat import Ui_MainWindow
import sqlite3
from sqlite3 import Error

class AppWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.mainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainWindow)
        self.mainWindow.setWindowTitle('Update Jumlah Obat')
        self.mainWindow.setWindowIcon(QtGui.QIcon('../assets/img/icon.png'))

        self.buttonOk.clicked.connect(lambda: self.confirm(self.inputID.text(), self.inputJumlah.text()))
        self.buttonCancel.clicked.connect(self.closeWindow)

        self.connectDB('Obat.db')

    def connectDB(self, DBName):
        try:
            self.con = sqlite3.connect(DBName)
            return self.con
        except Error as e:
            self.showError(str(e))
    
    def isInteger(x):
        for char in x:
            if ('0' <= char <= '9' or char == '-'):
                continue
            return False
        return True

    def confirm(self, idobat, jumlah):
        if (not AppWindow.isInteger(idobat) or not AppWindow.isInteger(jumlah)): 
            self.showError('idobat dan perubahan jumlah obat harus integer!')
            return
        if (idobat == "" or jumlah == ""):
            self.showError('idobat dan perubahan jumlah obat harus berisi!')
            return
        print("IDObat : " + idobat + ", Jumlah : " + jumlah)
        # TODO
        if (self.changeObatCount(int(idobat), int(jumlah))):
            self.closeWindow()

    def changeObatCount(self, id, jumlah):
        if (id < 0):
            self.showError('idobat harus bernilai positif!')
            return False
        cursorDB = self.con.cursor()
        check = cursorDB.execute("SELECT Jumlah FROM Obat WHERE ID = " + str(id))
        count = 0
        cur_jumlah = 0
        for temp in check:
            count += 1
            cur_jumlah = temp[0]
        if (count > 0 and (cur_jumlah + jumlah) >= 0):
            cursorDB.execute("UPDATE Obat set Jumlah = " + str(cur_jumlah + jumlah) + " WHERE ID = " + str(id))
            self.con.commit()
            return True
        elif (count == 0):
            self.showError('tidak ada obat ber-ID: ' + str(id) + '!')
        else:
            self.showError('jumlah obat tidak boleh menjadi minus!')
        return False

    def showError(self, msg):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(msg)
        error_dialog.exec_()

    def closeWindow(self):
        self.mainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AppWindow()
    ui.mainWindow.show()
    sys.exit(app.exec_())