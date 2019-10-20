import numpy as np
import sys
from pyzbar.pyzbar import decode
from PIL import Image
import picamera
import picamera.array
import cv2

# 商品コードと商品名、金額
dict_name = {"1234ABXDGEAEDA56788": "a", ".H068$": "b", "4912345678904": "c",
             "4901777018686": "Natural_Mineral_Water", "4902705001879": "SAVAS"}
dict_prices = {"1234ABXDGEAEDA56788": 120, ".H068$": 150,
               "4912345678904": 100, "4901777018686": 108, "4902705001879": 260}



def read_BC(camera=0):
    # VideoCaptureのインスタンスを作成する。
    # 引数でカメラを選べれる。
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as stream:
            # カメラの解像度を320x240にセット
            camera.resolution = (320, 240)
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

                # system.arrayをウインドウに表示
                cv2.imshow('frame', stream.array)

                # 'q'を入力でアプリケーション終了
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                # streamをリセット
                stream.seek(0)
                stream.truncate()

            cv2.destroyAllWindows()
    return data


def register_main():

    #金額の初期化
    prices = 0
    while True:

        data = read_BC()
        if len(data)==0:
            break #例外処理について後で考える！

        # コード内容を出力
        print(dict_name[data[0][0].decode('utf-8', 'ignore')],
              ":", dict_prices[data[0][0].decode('utf-8', 'ignore')])
        #print(data[0][0].decode('utf-8', 'ignore'))

        # 料金を加算
        prices += dict_prices[data[0][0].decode('utf-8', 'ignore')]
        print("小計 =", prices)

        while True:
            inp=input("続けるなら'C'キー、終了するなら'Q'キーを押してください。：")
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
    print("合計 =", prices)

register_main()

