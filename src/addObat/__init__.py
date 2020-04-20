import sys
from PyQt5 import QtWidgets, uic
from AddObat import AddObat

if __name__ == '__main__':
    addObatApp = QtWidgets.QApplication(sys.argv)
    addObatWindow = AddObat()
    addObatWindow.connectDB('../../db/Obat.db')
    addObatWindow.show()
    sys.exit(addObatApp.exec_())
