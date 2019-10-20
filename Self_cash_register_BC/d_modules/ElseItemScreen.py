# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperElseItemScreen import *
from ScreensCommonFuncs import *

class ElseItemScreen(QtWidgets.QMainWindow):
    '''

    '''
    def __init__(self, parent = None, dict_names = None, dict_prices = None):
        '''

        :param parent:
        :param dict_names:
        :param dict_prices:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperElseItemScreen()
        self.ui.setupUi(self)
