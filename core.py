#-*- coding: UTF-8 -*-

import cv2
import numpy as np
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QImage, QPixmap
import time

class videolar(QObject):

    yolla = pyqtSignal(np.ndarray)

    def __init__(self, yontem):
        super().__init__()
        self.yontem = yontem
        self._runnable = True

    @pyqtSlot()
    def veriakimi(self):
        cap = cv2.VideoCapture(self.yontem)

        while self._runnable:

            ret, frame = cap.read()

            if ret:
                self.yolla.emit(frame)
                time.sleep(0.05)

            else: break

    def stop(self):
        self._runnable = False

class fotograflar(QObject):

    yolla = pyqtSignal(np.ndarray)

    def __init__(self, dosya):
        super().__init__()
        self.dosya = dosya
        self._runnable = True

    def fotoveri(self):
        while self._runnable:
            image = cv2.imread(self.dosya)
            self.yolla.emit(image)
            time.sleep(0.05)

    def stop(self):
        self._runnable = False