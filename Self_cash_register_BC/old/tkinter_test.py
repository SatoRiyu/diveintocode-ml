#-*- coding: utf8 -*-
import sys
import tkinter as tk
from time import sleep
import matplotlib

import matplotlib
matplotlib.use('tkagg')

root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Entryを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('400x300')

# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()

# Entryを出現させる
Entry1 = tk.Entry()
Entry1.insert(tk.END, u'挿入する文字列')        # 最初から文字を入れておく
Entry1.pack()

#sleep(30)
root.mainloop()