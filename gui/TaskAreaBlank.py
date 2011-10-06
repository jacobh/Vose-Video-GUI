from gui.forms.Ui_TaskAreaBlank import Ui_TaskAreaBlank
from PyQt4 import QtCore, QtGui

class TaskAreaBlank(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_TaskAreaBlank()
        self.ui.setupUi(self)
        