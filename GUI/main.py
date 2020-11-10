#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
------------------------------
@author:99040
@file: main.py
------------------------------

@time: 2020/03/18/22:21

------------------------------
"""


import sys

from PyQt5.QtWidgets import QApplication

from GUI.custom_pane import Customtrain
from GUI.preset_pane import Presetpane
from GUI.superman import Entrance

if __name__ == '__main__':

    def showTrain():
        c.show()

    def showPreset():
        p.show()

    app = QApplication(sys.argv)
    p = Presetpane()#预训练好的模型面板
    e = Entrance() #程序入口面板
    e.show_preset_pane_signal.connect(showPreset)
    e.show_train_pane_signal.connect(showTrain)
    c = Customtrain()
    e.show()
    sys.exit(app.exec_())
