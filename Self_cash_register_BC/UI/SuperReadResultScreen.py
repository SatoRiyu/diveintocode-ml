# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperReadResultScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperReadResultScreen(object):
    def setupUi(self, SuperReadResultScreen):
        SuperReadResultScreen.setObjectName("SuperReadResultScreen")
        SuperReadResultScreen.resize(1440, 813)
        SuperReadResultScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperReadResultScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperReadResultScreen.setFont(font)
        SuperReadResultScreen.setToolTipDuration(-2)
        SuperReadResultScreen.setStyleSheet("background:rgb(5, 165, 250)")
        self.centralwidget = QtWidgets.QWidget(SuperReadResultScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(200)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 140))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(150)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_2.addWidget(self.textEdit_3, 0, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 0, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(420, 100))
        self.pushButton_4.setMaximumSize(QtCore.QSize(420, 100))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background:url(:/newPrefix/continue.png)")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(420, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(420, 100))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:url(:/newPrefix/finish.png)\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(420, 100))
        self.pushButton_3.setMaximumSize(QtCore.QSize(420, 100))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(60)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background:url(:/newPrefix/cansel.png)")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 2, 1, 1, 1)
        SuperReadResultScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperReadResultScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperReadResultScreen)

    def retranslateUi(self, SuperReadResultScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperReadResultScreen.setWindowTitle(_translate("SuperReadResultScreen", "ReadResultScreen"))
        self.label.setText(_translate("SuperReadResultScreen", "<html><head/><body><p align=\"center\"><span style=\" color:#fae984;\">COFFEE</span></p></body></html>"))
        self.label_2.setText(_translate("SuperReadResultScreen", "<html><head/><body><p align=\"center\"><span style=\" color:#31582d;\">150RWF</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("SuperReadResultScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#31582d;\">×2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#31582d;\">×1</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("SuperReadResultScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#fae984;\">250RWF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#fae984;\">300RWF</span></p></body></html>"))
        self.textEdit.setHtml(_translate("SuperReadResultScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#fae984;\">MINERAL WATER</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#fae984;\">COFFEE</span></p></body></html>"))

import teamdragon_System_NAVI_rc
