from gui.forms.Ui_ProjectArea import Ui_ProjectArea
from PyQt4 import QtCore, QtGui

class ProjectArea(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_ProjectArea()
        self.ui.setupUi(self)
        