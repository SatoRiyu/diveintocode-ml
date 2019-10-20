# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperNoItemsScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperNoItemsScreen(object):
    def setupUi(self, SuperNoItemsScreen):
        SuperNoItemsScreen.setObjectName("SuperNoItemsScreen")
        SuperNoItemsScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperNoItemsScreen.sizePolicy().hasHeightForWidth())
        SuperNoItemsScreen.setSizePolicy(sizePolicy)
        SuperNoItemsScreen.setMinimumSize(QtCore.QSize(1400, 800))
        SuperNoItemsScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperNoItemsScreen.setFont(font)
        SuperNoItemsScreen.setToolTipDuration(-2)
        SuperNoItemsScreen.setStyleSheet("background:rgb(5, 165, 250)")
        self.centralwidget = QtWidgets.QWidget(SuperNoItemsScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        SuperNoItemsScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperNoItemsScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperNoItemsScreen)

    def retranslateUi(self, SuperNoItemsScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperNoItemsScreen.setWindowTitle(_translate("SuperNoItemsScreen", "NoItemsScreen"))
        self.label_2.setText(_translate("SuperNoItemsScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#fae984;\">BARCODE</span></p></body></html>"))
        self.label_3.setText(_translate("SuperNoItemsScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#fae984;\">NOT FOUND</span></p></body></html>"))
        self.pushButton_EXIT.setText(_translate("SuperNoItemsScreen", "EXIT"))

import teamdragon_System_NAVI_rc
