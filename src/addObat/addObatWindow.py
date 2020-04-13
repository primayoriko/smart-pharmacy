# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addObatWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(435, 451)
        self.CancelButton = QtWidgets.QPushButton(Form)
        self.CancelButton.setGeometry(QtCore.QRect(330, 400, 93, 28))
        self.CancelButton.setObjectName("CancelButton")
        self.KadaluarsaObat = QtWidgets.QDateEdit(Form)
        self.KadaluarsaObat.setGeometry(QtCore.QRect(100, 230, 110, 22))
        self.KadaluarsaObat.setObjectName("KadaluarsaObat")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 55, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(100, 280, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.CacatOptObat = QtWidgets.QButtonGroup(Form)
        self.CacatOptObat.setObjectName("CacatOptObat")
        self.CacatOptObat.addButton(self.radioButton)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.label.setObjectName("label")
        self.DescObat = QtWidgets.QPlainTextEdit(Form)
        self.DescObat.setGeometry(QtCore.QRect(100, 110, 251, 71))
        self.DescObat.setObjectName("DescObat")
        self.NamaObat = QtWidgets.QPlainTextEdit(Form)
        self.NamaObat.setGeometry(QtCore.QRect(100, 60, 251, 31))
        self.NamaObat.setObjectName("NamaObat")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 310, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.CacatOptObat.addButton(self.radioButton_2)
        self.AddButton = QtWidgets.QPushButton(Form)
        self.AddButton.setGeometry(QtCore.QRect(220, 400, 93, 28))
        self.AddButton.setObjectName("AddButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 55, 16))
        self.label_3.setObjectName("label_3")
        self.JumlahObat = QtWidgets.QPlainTextEdit(Form)
        self.JumlahObat.setGeometry(QtCore.QRect(100, 190, 251, 31))
        self.JumlahObat.setObjectName("JumlahObat")
        self.IDObat = QtWidgets.QPlainTextEdit(Form)
        self.IDObat.setGeometry(QtCore.QRect(100, 20, 251, 31))
        self.IDObat.setObjectName("IDObat")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CancelButton.setText(_translate("Form", "Cancel"))
        self.label_7.setText(_translate("Form", "Cacat"))
        self.label_6.setText(_translate("Form", "Kadaluarsa"))
        self.label_4.setText(_translate("Form", "Deskripsi"))
        self.radioButton.setText(_translate("Form", "Ya"))
        self.label.setText(_translate("Form", "Nama Obat"))
        self.radioButton_2.setText(_translate("Form", "Tidak"))
        self.AddButton.setText(_translate("Form", "Add"))
        self.label_5.setText(_translate("Form", "Jumlah"))
        self.label_3.setText(_translate("Form", "ID Obat"))
