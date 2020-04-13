from PyQt5 import QtWidgets, uic
from AddObat import AddObat
import sys

if __name__ == '__main__':
    addObatApp = QtWidgets.QApplication(sys.argv)
    addObatWindow = AddObat()
    addObatWindow.show()
    sys.exit(addObatApp.exec_())
