#!/usr/bin/python
import sys

from PyQt4 import QtCore, QtGui
from gui.forms.Ui_MainWindow import Ui_MainWindow
from gui.forms.Ui_ProjectArea import Ui_ProjectArea
from gui.forms.Ui_ProjectList import Ui_ProjectList
from gui.forms.Ui_TaskAreaBlank import Ui_TaskAreaBlank

# We start a new class here
# derived from QMainWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        taskArea = Ui_TaskAreaBlank()
        dock = self.ui.taskAreaDock
        layout = self.ui.verticalLayout
        taskArea.setupUi(self)
        #layout.addWidget(taskArea)
        
        dockWidgetContents = QtGui.QWidget()
        dockWidgetContents.setObjectName(("dockWidgetContents"))
        verticalLayout_3 = QtGui.QVBoxLayout(dockWidgetContents)
        verticalLayout_3.setObjectName(("verticalLayout_3"))
        projectListFrame = QtGui.QWidget(dockWidgetContents)
        projectListFrame.setObjectName(("projectListFrame"))
        verticalLayout_3.addWidget(projectListFrame)
        dock.setWidget(dockWidgetContents)
        
        
        # Connect the pushButton to a message method.
        #self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),message)

def message():
    print "Hello, world !\n"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())