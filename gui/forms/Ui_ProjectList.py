# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectList.ui'
#
# Created: Thu Oct  6 10:07:34 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProjectList(object):
    def setupUi(self, ProjectList):
        ProjectList.setObjectName(_fromUtf8("ProjectList"))
        ProjectList.resize(248, 427)
        self.verticalLayout = QtGui.QVBoxLayout(ProjectList)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(ProjectList)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton = QtGui.QToolButton(ProjectList)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(ProjectList)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ProjectList)
        QtCore.QMetaObject.connectSlotsByName(ProjectList)

    def retranslateUi(self, ProjectList):
        ProjectList.setWindowTitle(QtGui.QApplication.translate("ProjectList", "Form", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("ProjectList", "EM301", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(1).setText(QtGui.QApplication.translate("ProjectList", "TH101v", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(2).setText(QtGui.QApplication.translate("ProjectList", "VoseConference2011", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton.setText(QtGui.QApplication.translate("ProjectList", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("ProjectList", "Delete", None, QtGui.QApplication.UnicodeUTF8))

