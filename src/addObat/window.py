from PyQt5 import QtWidgets, uic
from AddObatUI import *
import sys

if __name__ == '__main__':
    # print("hello world")
    addObatApp = QtWidgets.QApplication(sys.argv)
    addObatWindow = AddObatUI()
    addObatApp.exec_()
