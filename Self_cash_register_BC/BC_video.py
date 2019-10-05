import sys
import cv2
from pyzbar.pyzbar import decode
from PIL import Image

# 商品コードと商品名、金額
dict_name = {"1234ABXDGEAEDA56788": "a", ".H068$": "b", "4912345678904": "c",
             "4901777018686": "Natural_Mineral_Water", "4902705001879": "SAVAS"}
dict_prices = {"1234ABXDGEAEDA56788": 120, ".H068$": 150,
               "4912345678904": 100, "4901777018686": 108, "4902705001879": 260}

# VideoCaptureのインスタンスを作成する。
# 引数でカメラを選べれる。
cap = cv2.VideoCapture(0)

if cap.isOpened() is False:
    print("can not open camera")
    sys.exit()

prices = 0

while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    # バーコードの読取り
    data = decode(frame)

    cv2.imshow('frame', frame)
    if len(data) != 0:

        # コード内容を出力
        print(dict_name[data[0][0].decode('utf-8', 'ignore')],
              ":", dict_prices[data[0][0].decode('utf-8', 'ignore')])
        #print(data[0][0].decode('utf-8', 'ignore'))

        # 料金を加算
        prices += dict_prices[data[0][0].decode('utf-8', 'ignore')]

        print("prices =", prices)
        #読み取れたらwhileから抜ける
        break

    # キー入力を1ms待って、キーが'q'だったらBreakする
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
