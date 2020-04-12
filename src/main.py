from PyQt5.QtWidgets import QMainWindow, QListWidget
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5 import QtGui, QtCore, QtWidgets
from designer.ShowListObat import Ui_MainWindow
from PyQt5.QtGui import *

class TableModel(QAbstractTableModel):

    header_labels = ['IDObat', 'Nama Obat', 'Deskripsi', 'Harga']

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
        self.setupUi(self.mainWindow)
        self.fetchObat()
        self.fetchObatRacik()
    
    def clicked(self, qmodelindex):
        item = self.tableView.currentItem()
        print(item.text())
    
    def fetchObat(self):
        #get data obat from database obat
        data = [
            ['paracetamol', 'yoriko', 100, 'kaplet'],
            ['anti covid 19', 'lol', 100000, 'dus'],
            ['auto grandmaster', 'cf', 1, 'buah'],
        ]
        self.model = TableModel(data)
        self.tableView.setModel(self.model)
    
    def fetchObatRacik(self):
        #get data from database obat racik
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
