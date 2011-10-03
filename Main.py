#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui
from gui.Ui_MainWindow import Ui_MainWindow

# We start a new class here
# derived from QMainWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the pushButton to a message method.
        #self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),message)

def message():
    print "Hello, world !\n"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())