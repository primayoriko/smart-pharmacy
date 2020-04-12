# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\data_obat_racik_baru.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(280, 430, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setGeometry(QtCore.QRect(40, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.resepName = QtWidgets.QLabel(Dialog)
        self.resepName.setGeometry(QtCore.QRect(40, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resepName.setFont(font)
        self.resepName.setObjectName("resepName")
        self.headerNamaObat = QtWidgets.QLabel(Dialog)
        self.headerNamaObat.setGeometry(QtCore.QRect(40, 100, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.headerNamaObat.setFont(font)
        self.headerNamaObat.setObjectName("headerNamaObat")
        self.fieldNamaResep = QtWidgets.QLineEdit(Dialog)
        self.fieldNamaResep.setGeometry(QtCore.QRect(150, 70, 431, 20))
        self.fieldNamaResep.setObjectName("fieldNamaResep")
        self.headerJumlah = QtWidgets.QLabel(Dialog)
        self.headerJumlah.setGeometry(QtCore.QRect(330, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.headerJumlah.setFont(font)
        self.headerJumlah.setObjectName("headerJumlah")
        self.headerSatuan = QtWidgets.QLabel(Dialog)
        self.headerSatuan.setGeometry(QtCore.QRect(420, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.headerSatuan.setFont(font)
        self.headerSatuan.setObjectName("headerSatuan")
        self.field_namaObat1 = QtWidgets.QLineEdit(Dialog)
        self.field_namaObat1.setGeometry(QtCore.QRect(40, 130, 281, 20))
        self.field_namaObat1.setObjectName("field_namaObat1")
        self.field_jumlah1 = QtWidgets.QLineEdit(Dialog)
        self.field_jumlah1.setGeometry(QtCore.QRect(330, 130, 81, 20))
        self.field_jumlah1.setObjectName("field_jumlah1")
        self.field_satuan1 = QtWidgets.QComboBox(Dialog)
        self.field_satuan1.setGeometry(QtCore.QRect(420, 130, 161, 22))
        self.field_satuan1.setObjectName("field_satuan1")
        self.addItemsButton = QtWidgets.QPushButton(Dialog)
        self.addItemsButton.setGeometry(QtCore.QRect(40, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addItemsButton.setFont(font)
        self.addItemsButton.setObjectName("addItemsButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleLabel.setText(_translate("Dialog", "Data Obat Racik Baru"))
        self.resepName.setText(_translate("Dialog", "Nama Resep"))
        self.headerNamaObat.setText(_translate("Dialog", "Nama Obat"))
        self.headerJumlah.setText(_translate("Dialog", "Jumlah"))
        self.headerSatuan.setText(_translate("Dialog", "Satuan"))
        self.addItemsButton.setText(_translate("Dialog", "+"))
