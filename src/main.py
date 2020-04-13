# Main Program
from PyQt5 import QtWidgets
from designer.UpdateJumlahObat import Ui_MainWindow

class AppWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.mainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainWindow)

        self.buttonOk.clicked.connect(lambda: self.confirm(self.inputID.text(), self.inputJumlah.text()))
        self.buttonCancel.clicked.connect(self.closeWindow)
    
    def isInteger(x):
        for char in x:
            if ('0' <= char <= '9' or char == '-'):
                continue
            return False
        return True

    def confirm(self, idobat, jumlah):
        if (not AppWindow.isInteger(idobat) or not AppWindow.isInteger(jumlah)): 
            return
        if (idobat == "" or jumlah == ""):
            return
        print("IDObat : " + idobat + ", Jumlah : " + jumlah)
        # TODO
        # addObat()
        self.closeWindow()

    def closeWindow(self):
        self.mainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AppWindow()
    ui.mainWindow.show()
    sys.exit(app.exec_())