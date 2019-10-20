# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperElseItemScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperElseItemScreen(object):
    def setupUi(self, SuperElseItemScreen):
        SuperElseItemScreen.setObjectName("SuperElseItemScreen")
        SuperElseItemScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperElseItemScreen.sizePolicy().hasHeightForWidth())
        SuperElseItemScreen.setSizePolicy(sizePolicy)
        SuperElseItemScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperElseItemScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperElseItemScreen.setFont(font)
        SuperElseItemScreen.setToolTipDuration(-2)
        SuperElseItemScreen.setStyleSheet("background:rgb(5, 165, 250)")
        self.centralwidget = QtWidgets.QWidget(SuperElseItemScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EXIT.setMinimumSize(QtCore.QSize(420, 120))
        self.pushButton_EXIT.setMaximumSize(QtCore.QSize(420, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(80)
        self.pushButton_EXIT.setFont(font)
        self.pushButton_EXIT.setStyleSheet("background:rgb(250, 233, 132);\n"
"color:rgb(49, 88, 45)")
        self.pushButton_EXIT.setObjectName("pushButton_EXIT")
        self.horizontalLayout.addWidget(self.pushButton_EXIT)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        SuperElseItemScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperElseItemScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperElseItemScreen)

    def retranslateUi(self, SuperElseItemScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperElseItemScreen.setWindowTitle(_translate("SuperElseItemScreen", "ElseItemScreen"))
        self.label_2.setText(_translate("SuperElseItemScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#fae984;\">THIS ITEM IS</span></p></body></html>"))
        self.label_3.setText(_translate("SuperElseItemScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#fae984;\">NOT REGISTERD</span></p></body></html>"))
        self.pushButton_EXIT.setText(_translate("SuperElseItemScreen", "EXIT"))

import teamdragon_System_NAVI_rc
