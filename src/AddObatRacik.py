"""Main program loader

Menjalankan menu data_obat_racik_baru
"""
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QFileDialog, QMessageBox
from PyQt5 import QtGui, QtCore, QtWidgets
from designer.data_obat_racik_baru import Ui_Dialog
import sqlite3
import uuid
import os

default_path = os.path.join(os.path.dirname(__file__), "../Obat.db")

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

def storeDialogDataInDb(data, dbPath):
    dbHandler = sqlite3.connect(dbPath)
    # check if ObatRacikExists
    dbCursor = dbHandler.cursor()
    dbCursor.execute(("SELECT nama FROM ObatRacik WHERE nama='" + data["nama"] + "';"))
    if (len(dbCursor.fetchall()) == 0) :
        new_obat_racik_query = """
            INSERT INTO ObatRacik(IDObatRacik, nama) VALUES(""" + str(uuid.uuid4().int%10000000000) + """ ,'""" + data["nama"] + """');
        """
        dbCursor.execute(new_obat_racik_query)
        dbCursor.execute("SELECT IDObatRacik FROM ObatRacik WHERE nama='" + data["nama"] + "';")
        racik = dbCursor.fetchone()
        print(racik[0])
        # if not exist, add new
        for item in data["data"] :
            queryString = """
                INSERT INTO BahanObatRacik(IDObatRacik, IDObat, jumlah, satuan)
                VALUES(""" + str(racik[0]) + """, """ + str(item[0]) + """, 
                """ + str(item[1]) + """, '""" + str(item[2]) + """');
            """
            # print(item)

def create_obat_racik_table(dbPath):
    if check_if_table_exist(dbPath, 'ObatRacik'):
        return "Already exist!"
    dbHandler = sqlite3.connect(dbPath)
    dbCursor = dbHandler.cursor()
    obat_racik_query = """
    CREATE TABLE ObatRacik (
        IDObatRacik int(10) unique not null,
        nama varchar(30) not null,
        deskripsi varchar(300),
        PRIMARY KEY (IDObatRacik)
    );
    """
    dbCursor.execute(obat_racik_query)
    if check_if_table_exist(dbPath, 'ObatRacik'):
        dbHandler.close()
        return "Create Failed!"
    dbHandler.close()
    return "Create Success!"

def create_bahan_obat_racik_table(dbPath):
    if check_if_table_exist(dbPath, 'BahanObatRacik'):
        return "Already exist!"
    dbHandler = sqlite3.connect(dbPath)
    dbCursor = dbHandler.cursor()
    obat_racik_query = """
    CREATE TABLE BahanObatRacik (
        IDObatRacik int(10) not null,
        nama text not null,
        jumlah decimal(7,3) not null,
        satuan text not null,
        PRIMARY KEY (IDObatRacik, nama)
    );
    """
    dbCursor.execute(obat_racik_query)
    if check_if_table_exist(dbPath, 'BahanObatRacik'):
        dbHandler.close()
        return "Create Failed!"
    dbHandler.close()
    return "Create Success!"

def check_if_table_exist(db_path, table_name):
    dbHandler = sqlite3.connect(db_path)
    dbCursor = dbHandler.cursor()
    check_table_query = """
    SELECT name FROM sqlite_master WHERE name='""" + table_name + """'
    AND type='table';
    """
    dbCursor.execute(check_table_query)
    if len(dbCursor.fetchall()) > 0:
        dbHandler.close()
        return True
    dbHandler.close()
    return False

def run():
    app = QApplication([])
    w = AppWindow()
    w.show()
    app.exec_()
    print(create_obat_racik_table(default_path))
    print(create_bahan_obat_racik_table(default_path))
    storeDialogDataInDb(get_dialog_data(w, w.count), default_path)

if __name__ == "__main__":
    run()