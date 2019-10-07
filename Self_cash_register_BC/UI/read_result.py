# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_result.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_read_result(object):
    def setupUi(self, read_result):
        read_result.setObjectName("read_result")
        read_result.resize(1024, 768)
        self.label = QtWidgets.QLabel(read_result)
        self.label.setGeometry(QtCore.QRect(30, 70, 971, 171))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(223)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(read_result)
        self.label_2.setGeometry(QtCore.QRect(320, 310, 411, 121))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(160)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(read_result)
        self.label_3.setGeometry(QtCore.QRect(120, 560, 271, 111))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(read_result)
        self.label_4.setGeometry(QtCore.QRect(670, 570, 221, 91))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(read_result)
        QtCore.QMetaObject.connectSlotsByName(read_result)

    def retranslateUi(self, read_result):
        _translate = QtCore.QCoreApplication.translate
        read_result.setWindowTitle(_translate("read_result", "Form"))
        self.label.setText(_translate("read_result", "Mineral water\n"
""))
        self.label_2.setText(_translate("read_result", "200RWF"))
        self.label_3.setText(_translate("read_result", "FInish?\n"
" Press space key"))
        self.label_4.setText(_translate("read_result", "continue?\n"
" Press Enter key"))

