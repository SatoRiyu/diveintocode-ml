import numpy as np
import sys
import cv2
from play_sound import SoundPlayer #階層に注意
from time import sleep
from pyzbar.pyzbar import decode
from PIL import Image
from PyQt5 import QtWidgets
from UI import ui_prot0


# 商品コードと商品名、金額
dict_name = {"1234ABXDGEAEDA56788": "a", ".H068$": "b", "4912345678904": "c",
             "4901777018686": "Natural_Mineral_Water", "4902705001879": "SAVAS"}
dict_prices = {"1234ABXDGEAEDA56788": 120, ".H068$": 150,
               "4912345678904": 100, "4901777018686": 108, "4902705001879": 260}



def read_BC(camera=0):
    # VideoCaptureのインスタンスを作成する。
    # 引数でカメラを選べれる。
    cap = cv2.VideoCapture(camera)

    if cap.isOpened() is False:
        print("can not open camera")
        sys.exit()

    while True:
        # VideoCaptureから1フレーム読み込む
        ret, frame = cap.read()

        # バーコードの読取り
        data = decode(frame)

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

def register_main():

    #金額の初期化
    prices = 0
    while True:

        data = read_BC()
        if len(data)==0:
            break #例外処理について後で考える！
        SoundPlayer.play('sound/critical.mp3')
        # コード内容を出力
        print(dict_name[data[0][0].decode('utf-8', 'ignore')],
              ":", dict_prices[data[0][0].decode('utf-8', 'ignore')])
        #print(data[0][0].decode('utf-8', 'ignore'))

        # 料金を加算
        prices += dict_prices[data[0][0].decode('utf-8', 'ignore')]
        print("小計 =", prices)

        while True:
            inp=input("続けるなら'C'キー、終了するなら'Q'キーを押してください。:")
            if inp in ['c','C','q','Q']:break #正しいキーが入力されるまで繰り返す
            print('正しいキーを入力してください')

        # キー入力を無制限に待って、キーが'q'だったらBreakする
        if inp in ['c','C']:
            continue
        elif inp in ['q','Q']:
            break

        # キー入力を1ms待って、キーが'q'だったらBreakする
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    prices = int(np.ceil(prices*1.1))
    if prices >= 300:
        SoundPlayer.play('sound/levelup.mp3', stop=True)
    else:
        SoundPlayer.play('sound/fin.mp3', stop=True)
    print("合計 =", prices)
    sleep(3)

#ここから手続き始まり
SoundPlayer.play('sound/thema.mp3',stop=True)
while True:
    inp=input("会計を始めるなら'S'キー、終了するなら'Q'キーを押してください。:")
    if inp in ['s','S','q','Q']:break #正しいキーが入力されるまで繰り返す
    print('正しいキーを入力してください')
if inp in ['s','S']:
    SoundPlayer.play('sound/zoma.mp3', stop=True)
    register_main()
elif inp in ['q','Q']:
    SoundPlayer.play('sound/run_away.mp3', stop=True)
    sleep(3)
