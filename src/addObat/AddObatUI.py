from PyQt5 import QtWidgets, uic
import sys

class AddObatUI(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(AddObatUI, self).__init__(*args, **kwargs)
        # layout = QtWidgets.QVBoxLayout()
        uic.loadUi('addObatWindow.ui', self)
        self.AddButton.clicked.connect(self.sendRequest)
        self.CancelButton.clicked.connect(self.cancelRequest)
        self.show()

    def sendRequest(self):
        try:
            if(int(self.JumlahObat.toPlainText())<1):
                raise Exception('Jumlah obat harus lebih dari nol!')
            print("hello kitty")
        # Something to do with db
        except Exception as e:
            self.showError(str(e))
        # Something

    def cancelRequest(self):
        self.close()

    def showError(self, msg):
        # print(msg)
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(msg)
        error_dialog.exec_()

