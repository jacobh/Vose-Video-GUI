#!/usr/bin/python
import sys

from PyQt4 import QtCore, QtGui
from gui.MainWindow import MainWindow
#from gui.forms.Ui_ProjectArea import Ui_ProjectArea
from gui.ProjectList import ProjectList



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())