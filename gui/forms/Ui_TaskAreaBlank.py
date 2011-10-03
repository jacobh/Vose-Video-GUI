# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaskAreaBlank.ui'
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

class Ui_TaskAreaBlank(object):
    def setupUi(self, TaskAreaBlank):
        TaskAreaBlank.setObjectName(_fromUtf8("TaskAreaBlank"))
        TaskAreaBlank.resize(267, 421)
        self.verticalLayout = QtGui.QVBoxLayout(TaskAreaBlank)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(TaskAreaBlank)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(TaskAreaBlank)
        QtCore.QMetaObject.connectSlotsByName(TaskAreaBlank)

    def retranslateUi(self, TaskAreaBlank):
        TaskAreaBlank.setWindowTitle(QtGui.QApplication.translate("TaskAreaBlank", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TaskAreaBlank", "No Task Selected", None, QtGui.QApplication.UnicodeUTF8))

