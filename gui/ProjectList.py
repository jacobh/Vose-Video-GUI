from gui.forms.Ui_ProjectList import Ui_ProjectList
from PyQt4 import QtCore, QtGui

class ProjectList(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_ProjectList()
        self.ui.setupUi(self)
        