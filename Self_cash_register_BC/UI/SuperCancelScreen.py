# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperCancelScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperCanselScreen(object):
    def setupUi(self, SuperCanselScreen):
        SuperCanselScreen.setObjectName("SuperCanselScreen")
        SuperCanselScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperCanselScreen.sizePolicy().hasHeightForWidth())
        SuperCanselScreen.setSizePolicy(sizePolicy)
        SuperCanselScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperCanselScreen.setMaximumSize(QtCore.QSize(16777207, 16777215))
        SuperCanselScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperCanselScreen.setFont(font)
        SuperCanselScreen.setToolTipDuration(-2)
        SuperCanselScreen.setStyleSheet("background:rgb(5, 165, 250)")
        self.centralwidget = QtWidgets.QWidget(SuperCanselScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_yes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_yes.setMinimumSize(QtCore.QSize(420, 120))
        self.pushButton_yes.setMaximumSize(QtCore.QSize(420, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(80)
        self.pushButton_yes.setFont(font)
        self.pushButton_yes.setStyleSheet("background:rgb(250, 233, 132);\n"
"color:rgb(49, 88, 45)")
        self.pushButton_yes.setObjectName("pushButton_yes")
        self.horizontalLayout.addWidget(self.pushButton_yes)
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_no = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_no.sizePolicy().hasHeightForWidth())
        self.pushButton_no.setSizePolicy(sizePolicy)
        self.pushButton_no.setMinimumSize(QtCore.QSize(420, 120))
        self.pushButton_no.setMaximumSize(QtCore.QSize(420, 120))
        self.pushButton_no.setStyleSheet("background:rgb(250, 233, 132);\n"
"color:rgb(49, 88, 45);\n"
"font: 80pt \"DIN Condensed\";")
        self.pushButton_no.setObjectName("pushButton_no")
        self.horizontalLayout.addWidget(self.pushButton_no)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        SuperCanselScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperCanselScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperCanselScreen)

    def retranslateUi(self, SuperCanselScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperCanselScreen.setWindowTitle(_translate("SuperCanselScreen", "CanselScreen"))
        self.label_3.setText(_translate("SuperCanselScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#fae984;\">CANCEL?</span></p></body></html>"))
        self.pushButton_yes.setText(_translate("SuperCanselScreen", "YES"))
        self.pushButton_no.setText(_translate("SuperCanselScreen", "NO"))

import teamdragon_System_NAVI_rc
