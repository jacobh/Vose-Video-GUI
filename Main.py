#!/usr/bin/python
import sys

from PyQt4 import QtCore, QtGui
from gui.MainWindow import MainWindow
from gui.ProjectList import ProjectList
from gui.TaskAreaBlank import TaskAreaBlank



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    projectList = ProjectList()
    taskAreaBlank = TaskAreaBlank()
    
    window.ui.projectListDock.setWidget(projectList)
    window.ui.taskAreaDock.setWidget(taskAreaBlank)
    
    window.show()
    projectList.show()
    
    sys.exit(app.exec_())