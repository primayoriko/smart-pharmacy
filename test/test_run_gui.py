"""GUI runner test

This module is to test the main.py, checking the return value
"""
import sys
import sqlite3
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtCore
sys.path.insert(1, "../src")

import main

def not_test_main(qtbot):
    wt = main.AppWindow()
    qtbot.keyClicks(wt.ui.fieldNamaResep, "Pramanix")
    qtbot.keyClicks(wt.findChild(QtWidgets.QLineEdit, "field_namaObat1"), "Paracetamol")
    qtbot.keyClicks(wt.findChild(QtWidgets.QLineEdit, "field_jumlah1"), "500")
    assert main.get_dialog_data(wt, wt.count) == {
        'nama' : 'Pramanix',
        'data' : [
            ('Paracetamol', '500', 'Gram')
        ]
    }
    qtbot.mouseClick(wt.ui.addItemsButton, QtCore.Qt.LeftButton)
    assert wt.count == 2
    assert main.get_dialog_data(wt, wt.count) == {
        'nama' : 'Pramanix',
        'data' : [
            ('Paracetamol', '500', 'Gram'), ('','', 'Gram')
        ]
    }
    qtbot.keyClicks(wt.findChild(QtWidgets.QLineEdit, "field_namaObat2"), "Ibuprofen")
    qtbot.keyClicks(wt.findChild(QtWidgets.QLineEdit, "field_jumlah2"), "100")
    assert main.get_dialog_data(wt, wt.count) == {
        'nama' : 'Pramanix',
        'data' : [
            ('Paracetamol', '500', 'Gram'), ('Ibuprofen','100', 'Gram')
        ]
    }
    qtbot.keyClicks(wt.ui.fieldNamaResep, "\b\b\b\b\b\b\b")
    qtbot.keyClicks(wt.ui.fieldNamaResep, "aramex")
    assert main.get_dialog_data(wt, wt.count) == {
        'nama' : 'Paramex',
        'data' : [
            ('Paracetamol', '500', 'Gram'), ('Ibuprofen','100', 'Gram')
        ]
    }
    app = QApplication([])
