# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from UI.start import Ui_MainWindow
from UI.view1 import Ui_Form as view1
from UI.read_result import Ui_read_result

import numpy as np
import cv2
from play_sound import SoundPlayer #階層に注意
from time import sleep
from pyzbar.pyzbar import decode
from PIL import Image

# 商品コードと商品名、金額
dict_name = {"1234ABXDGEAEDA56788": "a", ".H068$": "b", "4912345678904": "c",
             "4901777018686": "Natural_Mineral_Water", "4902705001879": "SAVAS"}
dict_prices = {"1234ABXDGEAEDA56788": 120, ".H068$": 150,
               "4912345678904": 100, "4901777018686": 108, "4902705001879": 260}

class StartWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(StartWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def keyPressEvent(self, e):
        # Enterを押すとバーコード読み取り画面が現れる
        #print(e)
        #print(e.key())
        if e.key() == 16777220:
            view_1.show()
            self.hide()
        elif e.key() == Qt.Key_Escape:
            self.close()

class View1(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(View1, self).__init__(parent)
        self.ui = view1()
        self.ui.setupUi(self)
        self.table_items =[]
    def keyPressEvent(self, e):
        # エスケープキーを押すと画面が閉じる
        if e.key() == 16777220:
            self.register_main()
        elif e.key() == Qt.Key_Escape:
            self.close()

    def register_main(self):
        data = read_BC()
        if len(data) == 0:
            print("バーコードが読み取れていない！！！！") # 例外処理について後で考える！
        if data[0][0].decode('utf-8', 'ignore') in dict_name.keys():
            self.table_items.append([dict_name[data[0][0].decode('utf-8', 'ignore')],
                                dict_prices[data[0][0].decode('utf-8', 'ignore')]])
        else:
            self.table_items.append(["その他", 0])
        print(self.table_items[-1][0], self.table_items[-1][1])
        read_result.draw_result(self.table_items[-1][0], self.table_items[-1][1])
        read_result.show()
        self.hide()




class ReadResult(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(ReadResult, self).__init__(parent)
        self.ui = Ui_read_result()
        self.ui.setupUi(self)
    def keyPressEvent(self, e):
        # Enterを押すとバーコード読み取り画面が現れる
        if e.key() == 16777220:
            view_1.show()
            self.hide()

    def draw_result(self, name, price):
        self.ui.label.setText(name)
        self.ui.label_2.setText(str(price)+"RWF")



def read_BC(window=None, camera=0):
    # VideoCaptureのインスタンスを作成する。
    # 引数でカメラを選べれる。
    cap = cv2.VideoCapture(camera)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 50)  # カメラ画像の横幅を250に設定
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 50)  # カメラ画像の縦幅を250に設定

    if cap.isOpened() is False:
        print("can not open camera")
        sys.exit()

    while True:
        # VideoCaptureから1フレーム読み込む
        ret, frame = cap.read()

        # バーコードの読取り
        data = decode(frame)

        #ウィンドウの中でカメラの映像を表示したい
        #img_res = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #img_res = cv2.resize(img_res, (250, 250))
        #qt_img = create_QPixmap(img_res)
        #window.ui.label_setPix.setPixmap(qt_img)
        #cv2.imshow('frame', frame)
        if len(data) != 0:
            #読み取れたらwhileから抜ける
            break

        # キー入力を1ms待って、キーが'q'だったらBreakする
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return data



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    start_window = StartWindow()
    view_1 = View1()
    read_result = ReadResult()
    start_window.show()
    sys.exit(app.exec_())
