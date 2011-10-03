# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectArea.ui'
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

class Ui_ProjectArea(object):
    def setupUi(self, ProjectArea):
        ProjectArea.setObjectName(_fromUtf8("ProjectArea"))
        ProjectArea.resize(749, 475)
        self.verticalLayout = QtGui.QVBoxLayout(ProjectArea)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ProjectArea)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(ProjectArea)
        QtCore.QMetaObject.connectSlotsByName(ProjectArea)

    def retranslateUi(self, ProjectArea):
        ProjectArea.setWindowTitle(QtGui.QApplication.translate("ProjectArea", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjectArea", "No Project Selected", None, QtGui.QApplication.UnicodeUTF8))

