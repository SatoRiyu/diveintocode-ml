import numpy as np
import sys
import cv2
from pyzbar.pyzbar import decode
from PIL import Image

from BC_video_copy import read_BC

def add_main():

    data = read_BC()
    # 読み取り結果を出力
    result = data[0][0].decode('utf-8', 'ignore')
    while True:
        print("result :", result)
        name = input("商品名を入力してください。:")
        price = input("商品の値段（税抜）を入力してください。:")

        while True:
            inp = input("これで良ければ'Y'、ダメならば'N'を入力してください。:")
            if inp in ['y','Y','n','N']:break #正しいキーが入力されるまで繰り返す
            print('正しいキーを入力してください')
        # キー入力を無制限に待って、キーが'q'だったらBreakする
        if inp in ['y','Y']:
            break
        elif inp in ['n','N']:
            continue
    with open('names_prices/BC_names.txt', mode="a") as f:
        f.write("{}, {}\n".format(result, name))
    with open('names_prices/BC_prices.txt', mode="a") as f:
        f.write("{}, {}\n".format(result, price))

if __name__ == "__main__":
    add_main()
