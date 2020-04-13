# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\successMessage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class SuccessMessage(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(SuccessMessage, self).__init__(*args, **kwargs)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(257, 114) 
        self.dialog = Dialog
        self.OKButton = QtWidgets.QPushButton(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(80, 70, 93, 28))
        self.OKButton.setObjectName("OKButton")
        self.OKButton.clicked.connect(self.closeWindow)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 211, 51))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sukses"))
        Dialog.setWindowIcon(QtGui.QIcon('../../assets/img/icon.png')) 
        self.OKButton.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "Data obat berhasil ditambahkan ke database!"))

    def closeWindow(self):
        self.dialog.close()