# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Oct  3 14:49:40 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(905, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.projectAreaFrame = QtGui.QWidget(self.centralwidget)
        self.projectAreaFrame.setObjectName(_fromUtf8("projectAreaFrame"))
        self.verticalLayout_2.addWidget(self.projectAreaFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.projectListDock = QtGui.QDockWidget(MainWindow)
        self.projectListDock.setMinimumSize(QtCore.QSize(150, 323))
        self.projectListDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.projectListDock.setObjectName(_fromUtf8("projectListDock"))
        self.projectListLayout = QtGui.QWidget()
        self.projectListLayout.setObjectName(_fromUtf8("projectListLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.projectListLayout)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.projectListDock.setWidget(self.projectListLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.projectListDock)
        self.taskAreaDock = QtGui.QDockWidget(MainWindow)
        self.taskAreaDock.setMinimumSize(QtCore.QSize(200, 46))
        self.taskAreaDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.taskAreaDock.setObjectName(_fromUtf8("taskAreaDock"))
        self.taskAreaLayout = QtGui.QWidget()
        self.taskAreaLayout.setObjectName(_fromUtf8("taskAreaLayout"))
        self.verticalLayout = QtGui.QVBoxLayout(self.taskAreaLayout)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.taskAreaDock.setWidget(self.taskAreaLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.taskAreaDock)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.projectListDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Project List", None, QtGui.QApplication.UnicodeUTF8))
        self.taskAreaDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Task Area", None, QtGui.QApplication.UnicodeUTF8))

