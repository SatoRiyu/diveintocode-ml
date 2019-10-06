# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from UI.ui_prot0 import Ui_Dialog

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

#pilイメージオブジェクトをQtで表示できるよう変換する関数
#https://qiita.com/odaman68000/items/c8c4093c784bff43d319
#ライブラリにあるかもしれないので、見つけられたら消す
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

def create_QPixmap(image):
  qimage = QtGui.QImage(image.data, image.shape[1], image.shape[0], image.shape[1] * 4, QtGui.QImage.Format_ARGB32_Premultiplied)
  pixmap = QtGui.QPixmap.fromImage(qimage)
  return pixmap

class Test(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.btn_stat_0 = None
        self.btn_stat_2 = None
        self.btn_stat_3 = None
        self.btn_stat_4 = None
        # クリックされたらbuttonClickedの呼び出し
        self.ui.pushButton_3.clicked.connect(self.buttonClicked3)
        self.ui.pushButton_4.clicked.connect(self.buttonClicked4)
    def slot1(self): #イベント処理の関数
        self.ui.label.setText('Hello World!')

    def buttonClicked3(self):
        global inp
        inp = "Y"
        return "Y"

    def buttonClicked4(self):
        global inp
        inp = "N"
        return "N"

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
        cv2.imshow('frame', frame)
        if len(data) != 0:
            #読み取れたらwhileから抜ける
            break

        # キー入力を1ms待って、キーが'q'だったらBreakする
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return data


def register_main(window=None):
    #金額の初期化
    prices = 0
    table_items = []
    while True:

        data = read_BC(window)
        if len(data)==0:
            break #例外処理について後で考える！
        SoundPlayer.play('sound/critical.mp3')
        # コード内容を出力
        #print(dict_name[data[0][0].decode('utf-8', 'ignore')],
        #      ":", dict_prices[data[0][0].decode('utf-8', 'ignore')])
        #print(data[0][0].decode('utf-8', 'ignore'))
        if data[0][0].decode('utf-8', 'ignore') in dict_name.keys():
            table_items.append([dict_name[data[0][0].decode('utf-8', 'ignore')], dict_prices[data[0][0].decode('utf-8', 'ignore')]])
        else:
            table_items.append(["その他", 0])

        ## テーブルの初期化 列名までクリアされてしまう！
        #window.ui.tableWidget.clear()

        ## 行数の設定
        window.ui.tableWidget.setRowCount(len(table_items))

        for n, t_item in enumerate(table_items):
            #print(t_item[1])
            window.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(t_item[0]))
            window.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(t_item[1])))

        # 料金を加算
        #prices += dict_prices[data[0][0].decode('utf-8', 'ignore')]
        prices += table_items[-1][1]
        #print("小計 =", prices)
        window.ui.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem(str(prices)))

        inp = None
        while True:
            window.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                ">続けるなら'Y'キー、終了するなら'N'キーを押してください。</p></body></html>")
            window.ui.pushButton_3.setText("次の商品(Y)")
            window.ui.pushButton_4.setText("終了(N)")
            inp = input("続けるなら'Y'キー、終了するなら'N'キーを押してください。:")

            if inp in ['y','Y','N','n'] : break #正しいキーが入力されるまで繰り返す
            print('正しいキーを入力してください')

        # キー入力を無制限に待って、キーが'q'だったらBreakする
        if inp in ['y','Y']:
            continue
        elif inp in ['n','N']:
            break

        # キー入力を1ms待って、キーが'q'だったらBreakする
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    prices = int(np.ceil(prices*1.1))
    #画面が更新される前に閉じられている可能性有り→updata()すればOK
    window.ui.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem(str(prices)))
    window.ui.tableWidget_2.update()
    if prices >= 300:
        SoundPlayer.play('sound/levelup.mp3', stop=True)
    else:
        SoundPlayer.play('sound/fin.mp3', stop=True)
    #window.ui.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem(str(prices)))
    print("合計 =", prices)
    sleep(3)



if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Test()
  window.show()
  # ここから手続き始まり
  SoundPlayer.play('sound/thema.mp3')
  inp = None
  while True:
      window.ui.textBrowser.setHtml(
          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
          "p, li { white-space: pre-wrap; }\n"
          "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
          ">会計を始めるなら'Y'キー、終了するなら'N'キーを押してください。</p></body></html>")
      window.ui.pushButton_3.setText("会計開始(Y)")
      window.ui.pushButton_4.setText("終了(N)")
      inp = input("会計を始めるなら'Y'キー、終了するなら'N'キーを押してください。:")
      if inp in ['y', 'Y', 'n', 'N']: break  # 正しいキーが入力されるまで繰り返す
      print('正しいキーを入力してください')
  if inp in ['y', 'Y']:
      SoundPlayer.play('sound/zoma.mp3', stop=True)
      register_main(window)
  elif inp in ['n', 'N']:
      SoundPlayer.play('sound/run_away.mp3', stop=True)
      sleep(3)

  #sys.exit(app.exec_())




