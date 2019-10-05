from pyzbar.pyzbar import decode
from PIL import Image

# 画像ファイルの指定
images = ("code39.jpg", "code41.jpg", "code40.png", "IMG_3024.JPG", "IMG_3025.JPG")
dict_name = {"1234ABXDGEAEDA56788" : "a", ".H068$" : "b", "4912345678904" : "c", "4901777018686" : "Natural_Mineral_Water", "4902705001879" : "SAVAS"}
dict_prices = {"1234ABXDGEAEDA56788" : 120, ".H068$" : 150, "4912345678904" : 100, "4901777018686" : 108, "4902705001879" : 260}

prices = 0
for img in images:
    # バーコードの読取り
    data = decode(Image.open(img))

    # コード内容を出力
    print(dict_name[data[0][0].decode('utf-8', 'ignore')], ":", dict_prices[data[0][0].decode('utf-8', 'ignore')])
    #print(data[0][0].decode('utf-8', 'ignore'))

    # 料金を加算
    prices += dict_prices[data[0][0].decode('utf-8', 'ignore')]

print("prices =", prices)