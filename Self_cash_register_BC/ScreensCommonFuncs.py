# -*- coding: utf-8 -*-
import sys
import time
import threading
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
from pyzbar.pyzbar import decode
from PyQt5.QtCore import QTimer
import platform
from play_sound import SoundPlayer #階層に注意

# OSがLinuxであれば、ラズパイ上で起動しているとし、カメラを切り替える
if platform.system() == "Linux":
    import picamera
    import picamera.array

#参考・引用
#https://tech-k-labs.xyz/post/pyqt3/

# 商品コードと商品名、金額
def csv2dict(path):
    dict_names, dict_prices = {}, {}
    with open(path) as f:
        data = f.read()
    lines = data.strip().split("\n")
    for line in lines:
        try:
            bc_num, name, price = line.split(",")
            dict_names[bc_num], dict_prices[bc_num] = name, int(price)
        except:
            pass
    return dict_names, dict_prices

def next_screen(screen1, screen2):
    '''
    簡易的な画面遷移
    :param screen1:遷移前の画面
    :param screen2: 遷移後の画面
    :return: なし
    '''
    '''
    position = screen1.pos()  # 遷移前のdlgの座標を取得
    size = screen1.size()  # 遷移前のサイズを取得
    screen2.move(position.x(), position.y())  # 同じ位置へ
    screen2.resize(size)  # 同じサイズへ
    # 画面の位置が完全に重なる
    '''
    screen1.hide()  # 遷移前のダイアログを非表示
    screen2.showFullScreen()  # 遷移後のダイアログを表示

def next_screen_cancel(screen1, screen2):
    '''
    簡易的な画面遷移
    :param screen1:遷移前の画面
    :param screen2: 遷移後の画面
    :return: なし
    '''
    '''
    position = screen1.pos()  # 遷移前のdlgの座標を取得
    size = screen1.size()  # 遷移前のサイズを取得
    screen2.move(position.x(), position.y())  # 同じ位置へ
    screen2.resize(size)  # 同じサイズへ
    # 画面の位置が完全に重なる
    '''
    # SoundPlayer.play('sound/run_away.mp3', stop=True)
    # time.sleep(2)
    screen1.hide()  # 遷移前のダイアログを非表示
    screen2.showFullScreen()  # 遷移後のダイアログを表示

def read_BC(window=None, camera=0):
    if platform.system() == "Linux":
        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as stream:
                # カメラの解像度を960x720にセット
                camera.resolution = (960, 720)
                # カメラのフレームレートを15fpsにセット
                camera.framerate = 15

                # ホワイトバランスをfluorescent(蛍光灯)モードにセット
                # camera.awb_mode = 'auto'
                # camera.awb_mode = 'sunlight'
                # camera.awb_mode = 'cloudy'
                # camera.awb_mode = 'shade'
                # camera.awb_mode = 'tungsten'
                camera.awb_mode = 'fluorescent'
                # camera.awb_mode = 'incandescent'
                # camera.awb_mode = 'flash'
                # camera.awb_mode = 'horizon'

                while True:
                    # stream.arrayにBGRの順で映像データを格納
                    camera.capture(stream, 'bgr', use_video_port=True)
                    frame = stream.array
                    # バーコードの読取り
                    data = decode(frame)

                    if len(data) != 0:
                        # 読み取れたらwhileから抜ける
                        break

                    # キー入力を1ms待って、キーが'q'だったらBreakする
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    # streamをリセット
                    stream.seek(0)
                    stream.truncate()

                cv2.destroyAllWindows()
    else:
        #Mac、Windows上
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

            if len(data) != 0:
                #読み取れたらwhileから抜ける
                break

            # キー入力を1ms待って、キーが'q'だったらBreakする
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        return data

#それぞれの画面に定義したい関数
def register_main(dict_names = None, table_items = None, scan_screen = None, read_result_screen = None):
        '''

        :return:
        '''
        data = read_BC()
        if len(data) == 0:
            print("バーコードが読み取れていない！！！！") # 例外処理について後で考える！
        bc_num = data[0][0].decode('utf-8', 'ignore') if data[0][0].decode('utf-8', 'ignore') in dict_names.keys() else "SOMETHING ELSE" #"その他"よりも任意の英数字の方が良い？
        table_items.append(bc_num)
        #read_result.draw_read_result_func(table_items)
        read_result_screen.showFullScreen()
        scan_screen.hide()

def check_table_items(table_items, self_screen = None, total_screen = None, welcome_screen = None):
    '''
    table_items（お買い物リスト）をチェックして、
    アイテムがあれば、精算画面へ遷移する。
    アイテムがなければ、開始画面へ遷移する。
    :return:
    '''
    if len(tabel_items) != 0:
        total_screen.showFullScreen()
        self_screen.hide()
    else:
        welcome_screen.showFullScreen()
        self_screen.hide()

def draw_read_result(read_result_screen = None, table_items = None, dict_names = None, dict_prices = None):
    '''
    買い物リストを受け取る。
    最後にリストに加えられたものを表示する。
    リスト内の商品名、個数、金額のテーブルを表示する。
    :param table_items: 買い物リスト
    :return:
    '''

    #テスト用

    ## 行数の設定
    read_result_screen.ui.tableWidget.setRowCount(len(table_items))

    for n, t_item in enumerate(table_items):
        # print(t_item[1])
        read_result_screen.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(t_item)))
        read_result_screen.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(t_item)))


def dict_items(table_items):
    dict_items = {}
    for bc_num in table_items:
        if bc_num in dict_items.keys():
            dict_items[bc_num] += 1
        else:
            dict_items[bc_num] = 1
    return dict_items

def update_table(screen, dict_items):
    _str_1, _str_2, _str_3 = "", "", ""
    for items in dict_items.keys():
        _str_1 += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:40pt; color:#fae984;\">" + screen.dict_names[items] + "</span></p>\n"
        _str_2 += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:40pt; color:#fae984;\">" + str(screen.dict_prices[items]*dict_items[items]) + "RWF</span></p>\n"
        _str_3 += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:40pt; color:#31582d;\">" + "×" + str(dict_items[items]) + "</span></p>\n"
    screen.ui.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                            "p, li { white-space: pre-wrap; }\n"
                            "</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:40pt; font-style:normal;\">\n"
                            + _str_1[:-2])
    screen.ui.textEdit_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                            "p, li { white-space: pre-wrap; }\n"
                            "</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:40pt; font-style:normal;\">\n"
                            + _str_2[:-2])
    screen.ui.textEdit_3.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                            "p, li { white-space: pre-wrap; }\n"
                            "</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:40pt; font-style:normal;\">\n"
                            + _str_3[:-2])