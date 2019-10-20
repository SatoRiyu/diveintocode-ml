# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperTotalScreen import *
from ScreensCommonFuncs import *

class TotalScreen(QtWidgets.QMainWindow):
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperTotalScreen()
        self.ui.setupUi(self)

    def showEvent(self, _):
        total = 0
        for item in self.table_items:
            total += self.dict_prices[item]
        self.ui.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:150pt; color:#fae984;\">" + str(total) + "RWF" + "</span></p></body></html>")
        
        update_table(self, dict_items(self.table_items))
