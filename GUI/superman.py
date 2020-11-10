#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
------------------------------
@author:99040
@file: superman.py
------------------------------

@time: 2020/03/18/21:30

------------------------------
"""
import sys

from PyQt5.QtCore import Qt, QUrl, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QDesktopServices, QIcon
from resources.newlogin_ui import Ui_Login
class Entrance(QWidget, Ui_Login):

    show_preset_pane_signal = pyqtSignal()
    show_train_pane_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowIcon(QIcon('resources/images/LOG.png'))
        self.setWindowTitle("CNN-ResNet")

    def show_preset_pane(self):
        #print("弹出注册界面")
        self.show_preset_pane_signal.emit()

    def open_cnn_link(self):
        #print("神经网络")
        link = "https://baike.baidu.com/item/%E5%8D%B7%E7%A7%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C"
        QDesktopServices.openUrl(QUrl(link))

    def show_train_pane(self):

        self.show_train_pane_signal.emit()
    def open_link(self):
        link = "http://127.0.0.1:8000/app/imagefield"
        QDesktopServices.openUrl(QUrl(link))
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Entrance()
    window.show()
    sys.exit(app.exec_())
    pass