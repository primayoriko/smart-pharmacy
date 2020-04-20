
import sqlite3
from sqlite3 import Error
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QListWidget
from PyQt5.QtCore import Qt, QAbstractTableModel
from designer.ShowListObat import Ui_MainWindow


class TableModel(QAbstractTableModel):

    header_labels = ['ID', 'Nama', 'Jumlah', 'Deskripsi', 'Kadaluarsa', 'Cacat']

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class TableModel2(QAbstractTableModel):

    header_labels = ['IDObatRacik', 'Nama Resep', 'DaftarObat']

    def __init__(self, data):
        super(TableModel2, self).__init__()
        self._data = data

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class AppWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.mainWindow = QMainWindow()
        self.mainWindow.setWindowTitle('Data Obat dan Obat Racik')
        self.mainWindow.setWindowIcon(QtGui.QIcon('../assets/img/icon.png'))
        self.setupUi(self.mainWindow)
        self.fetchObat()
        self.fetchObatRacik()

    def connectDB(self, DBName):
        try:
            self.con = sqlite3.connect(DBName)
            return self.con
        except Error as e:
            self.showError(str(e))

    def clicked(self, qmodelindex):
        item = self.tableView.currentItem()
        print(item.text())
    
    def connectDB(self, database):
        try:
            con = sqlite3.connect(database)
            return con
        except Error as e:
            self.showError(str(e))

    def fetchObat(self):
        #get data obat from database obat
        con = self.connectDB('Obat.db')
        cursorDB = con.cursor()
        check = cursorDB.execute("SELECT * FROM Obat")
        data = check.fetchall()

        self.model = TableModel(data)
        self.tableView.setModel(self.model)

    def fetchObatRacik(self):
        #get data from database obat racik

        #dummy data from a list
        data = [
            ['paracetamol', 'yoriko', 100],
            ['anti covid 19', 'lol', 100000],
            ['auto grandmaster', 'cf', 1],
        ]

        self.model_2 = TableModel2(data)
        self.tableView_2.setModel(self.model_2)

    def closeWindow(self):
        self.mainWindow.close()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = AppWindow()
    ui.mainWindow.show()
    sys.exit(app.exec_())
