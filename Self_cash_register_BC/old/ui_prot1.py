from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


def main():
    app = QApplication(sys.argv)
    table = QTableWidget()
    tableItem = QTableWidgetItem()

    # initiate table
    table.setWindowTitle("QTableWidget Example")
    table.setRowCount(4)
    table.setColumnCount(2)

    horzHeaders = QStringList();
    horzHeaders << "Name" << "Age";
    table.setHorizontalHeaderLabels(horzHeaders);

    # set data
    table.setItem(0, 0, QTableWidgetItem("Tom"))
    table.setItem(0, 1, QTableWidgetItem("15"))
    table.setItem(1, 0, QTableWidgetItem("Ken"))
    table.setItem(1, 1, QTableWidgetItem("40"))
    table.setItem(2, 0, QTableWidgetItem("Susie"))
    table.setItem(2, 1, QTableWidgetItem("22"))
    table.setItem(3, 0, QTableWidgetItem("Kevin"))
    table.setItem(3, 1, QTableWidgetItem("65"))

    # show table
    table.show()
    return app.exec_()


if __name__ == '__main__':
    main()