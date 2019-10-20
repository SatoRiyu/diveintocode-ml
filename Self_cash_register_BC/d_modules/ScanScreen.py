# -*- coding: utf-8 -*-
import sys
import time
# import picamera
# import picamera.array
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperScanScreen import *
from ScreensCommonFuncs import *
from play_sound import SoundPlayer #階層に注意

class ScanScreen(QtWidgets.QMainWindow):
    repeatTime = 100 # ms
    search_time = 10 # s
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperScanScreen()
        self.ui.setupUi(self)
        self.table_items, self.dict_names, self.dict_prices = [], [], []
        self.read_result_screen = None

    def showEvent(self, _):
        '''
        :param _: 使わない
        :return:
        '''
        self.capture_display()
        # self.capture_display_raspi()

    def keyPressEvent(self, e):
        self.capture.release()
        self.timer.stop()
        # エスケープキーを押すと画面が閉じる
        if e.key() == Qt.Key_F:
            self.hide()
            self.no_items_screen.showFullScreen()
        elif e.key() == Qt.Key_G:
            self.hide()
            self.else_item_screen.showFullScreen()
        elif e.key() == Qt.Key_H:
            for item in ["4901777018686", "4902705001879", "4902102113625", "4902102113625", "4902102113625", "4897036690055", "4902705001879"]:
                self.table_items.append(item)
            self.hide()
            self.read_result_screen.showFullScreen()

    def capture_display(self):
        self.CAMERA_MODE = 0
        self.v_width, self.v_height= 960, 720

        #camera setup
        self.capture = cv2.VideoCapture(self.CAMERA_MODE)

        if self.capture.isOpened() is False:
            raise Exception("IO Error")

        size = (self.v_width, self.v_height)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH ,self.v_width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,self.v_height)

        self.start_time = time.time()
        self._set()
        #update timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._set)
        self.timer.start(self.repeatTime)

    def _set(self):
        #camera capture
        ret, cv_img = self.capture.read()
        # バーコードの読取り
        data = decode(cv_img)
        self._check_BC(data)
        if ret == False:
            return
        cv_img = cv2.flip(cv2.cvtColor(cv_img,cv2.COLOR_BGR2RGB), 1)
        height, width, dim = cv_img.shape
        bytesPerLine = dim * width
        self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.ui.label_2.setPixmap(QPixmap.fromImage(self.image))
        self._check_time()
    
    def _check_BC(self, data):
        if len(data) != 0:
            self.capture.release()
            self.timer.stop()
            # SoundPlayer.play('sound/critical.mp3')
            # 読み取れたらwhileから抜ける
            bc_num = data[0][0].decode('utf-8', 'ignore') if data[0][0].decode('utf-8', 'ignore') in self.dict_names.keys() else "somethingelse"
            if bc_num != "somethingelse":
                self.table_items.append(bc_num)
                self.hide()
                self.read_result_screen.showFullScreen()
            else:
                self.hide()
                self.else_item_screen.showFullScreen()

    def _check_time(self):
        current_time = time.time()
        if current_time - self.start_time > self.search_time:
            self.capture.release()
            self.timer.stop()
            self.hide()
            self.no_items_screen.showFullScreen()

    def cancel_scanning(self, welcome_screen, read_result_screen):
        # self.capture.release()
        self.timer.stop()
        if self.table_items == []:
            self.hide()
            welcome_screen.showFullScreen()
        else:
            self.hide()
            read_result_screen.showFullScreen()

    

    def capture_display_raspi(self):
        self.CAMERA_MODE = 0
        self.v_width, self.v_height= 960, 720 # カメラの解像度を self.v_width × self.v_height にセット
        # VideoCaptureのインスタンスを作成する。
        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as stream:
                self.camera, self.stream = camera, stream
                self.camera.resolution = (self.v_width, self.v_height)
                self.camera.framerate = 15 # カメラのフレームレートを15fpsにセット
                # ホワイトバランスをfluorescent(蛍光灯)モードにセット
                self.camera.awb_mode = 'fluorescent'

                self.start_time = time.time()
                self._set_raspi()
                #update timer
                self.timer = QTimer(self)
                self.timer.timeout.connect(self._set_raspi)
                self.timer.start(self.repeatTime)
        return data

    def _set_raspi(self):
        # stream.arrayにBGRの順で映像データを格納
        self.camera.capture(stream, 'bgr', use_video_port=True)
        frame = self.stream.array
        # バーコードの読取り
        data = decode(frame)
        # system.arrayをウインドウに表示
        # cv2.imshow('frame', stream.array)
        # streamをリセット
        self.stream.seek(0)
        self.stream.truncate()
        self._check_BC_raspi(data)

        cv_img = cv2.flip(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB), 1)
        height, width, dim = cv_img.shape
        bytesPerLine = dim * width
        self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.ui.label_2.setPixmap(QPixmap.fromImage(self.image))
        self._check_time_raspi()

    def _check_BC_raspi(self, data):
        if len(data) != 0:
            self.timer.stop()
            # SoundPlayer.play('sound/critical.mp3')
            # 読み取れたらwhileから抜ける
            bc_num = data[0][0].decode('utf-8', 'ignore') if data[0][0].decode('utf-8', 'ignore') in self.dict_names.keys() else "somethingelse"
            if bc_num != "somethingelse":
                self.table_items.append(bc_num)
                self.hide()
                self.read_result_screen.showFullScreen()
            else:
                self.hide()
                self.else_item_screen.showFullScreen()

    def _check_time_raspi(self):
        current_time = time.time()
        if current_time - self.start_time > self.search_time:
            self.timer.stop()
            self.hide()
            self.no_items_screen.showFullScreen()