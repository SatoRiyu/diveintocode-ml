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
        read_result.setStyleSheet("background:rgb(44, 147, 209)")
        self.label = QtWidgets.QLabel(read_result)
        self.label.setGeometry(QtCore.QRect(20, 40, 971, 171))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(223)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(read_result)
        self.label_2.setGeometry(QtCore.QRect(290, 220, 411, 121))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(160)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(read_result)
        self.pushButton.setGeometry(QtCore.QRect(100, 470, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(read_result)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 540, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(read_result)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 640, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(read_result)
        self.tableWidget.setGeometry(QtCore.QRect(450, 400, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(read_result)
        QtCore.QMetaObject.connectSlotsByName(read_result)

    def retranslateUi(self, read_result):
        _translate = QtCore.QCoreApplication.translate
        read_result.setWindowTitle(_translate("read_result", "Form"))
        self.label.setText(_translate("read_result", "<html><head/><body><p><span style=\" color:#ffe677;\">Mineral water</span></p></body></html>"))
        self.label_2.setText(_translate("read_result", "<html><head/><body><p><span style=\" color:#fee776;\">200RWF</span></p></body></html>"))
        self.pushButton.setText(_translate("read_result", "PushButton"))
        self.pushButton_2.setText(_translate("read_result", "PushButton"))
        self.pushButton_3.setText(_translate("read_result", "PushButton"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("read_result", "商品名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("read_result", "金額"))

