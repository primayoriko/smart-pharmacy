from PyQt5 import QtWidgets, QtGui, uic
from sqlite3 import Error
import sqlite3
import sys
sys.path.insert(1, '../src/addObat/')
from AddObat import AddObat

def test_addEntry_normal():
    addObatApp = QtWidgets.QApplication(sys.argv)
    testAddObat = AddObat()
    testAddObat.connectDB('TestDB_Obat.db')
    testAddObat.clearDB()
    # (ID, Nama, Jumlah, Deskripsi, Kadaluarsa, Cacat)
    res = testAddObat.addEntry((123, 'haha', 23, '', '1/2/2000', 0), True)
    testAddObat.clearDB()
    assert res == 0

def test_addEntry_jumlahnegatif():
    addObatApp = QtWidgets.QApplication(sys.argv)
    testAddObat = AddObat()
    testAddObat.connectDB('TestDB_Obat.db')
    testAddObat.clearDB()
    # (ID, Nama, Jumlah, Deskripsi, Kadaluarsa, Cacat)
    res = testAddObat.addEntry((123, 'haha', -23, '', '1/2/2000', 0), True)
    testAddObat.clearDB()
    assert res == 1

def test_addEntry_idnegatif():
    addObatApp = QtWidgets.QApplication(sys.argv)
    testAddObat = AddObat()
    testAddObat.connectDB('TestDB_Obat.db')
    testAddObat.clearDB()
    # (ID, Nama, Jumlah, Deskripsi, Kadaluarsa, Cacat)
    res = testAddObat.addEntry((-123, 'haha', 23, '', '1/2/2000', 0), True)
    testAddObat.clearDB()
    assert res == 1

def test_addEntry_radiobuttonbelumdipilih():
    addObatApp = QtWidgets.QApplication(sys.argv)
    testAddObat = AddObat()
    testAddObat.connectDB('TestDB_Obat.db')
    testAddObat.clearDB()
    # (ID, Nama, Jumlah, Deskripsi, Kadaluarsa, Cacat)
    res = testAddObat.addEntry((123, 'haha', 23, '', '1/2/2000', -1), True)
    testAddObat.clearDB()
    assert res == 1



