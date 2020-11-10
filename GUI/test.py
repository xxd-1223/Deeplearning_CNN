#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
------------------------------
@author:99040
@file: test.py
------------------------------

@time: 2020/03/05/16:50

------------------------------
"""
from PyQt5.Qt import *
from custom_pane import Customtrain
from login_pane import LoginPane
from register_pane import RegisterPane
import os

import sys



app = QApplication(sys.argv)
#控件面板的创建
login_pane = LoginPane()
#register_pane = RegisterPane(login_pane)
register_pane = RegisterPane()
#register_pane.move(0, 0)
#register_pane.show()
custom_pane = Customtrain()
# custom_Pane.show()




#槽函数
def exit_register_pane():#注册界面退出按钮的槽函数
    # animation = QPropertyAnimation(register_pane)
    # animation.setTargetObject(register_pane)
    # animation.setPropertyName(b"pos")
    # animation.setStartValue(QPoint(0, 0))
    # animation.setEndValue(QPoint(login_pane.width(), 0))
    # animation.setDuration(200)
    # animation.setEasingCurve(QEasingCurve.InBounce)
    # animation.start(QAbstractAnimation.DeleteWhenStopped)
    register_pane.close()

def show_register_pane():#登录界面注册账号按钮的槽函数
    print("展示注册界面")
    register_pane.show()
    animation = QPropertyAnimation(register_pane)
    animation.setTargetObject(register_pane)
    animation.setPropertyName(b"pos")
    #animation.setStartValue(QPoint(0, login_pane.height()))
    animation.setStartValue(QPoint(300, 500))
    animation.setEndValue(QPoint(0, 0))
    animation.setDuration(200)
    animation.setEasingCurve(QEasingCurve.OutBounce)
    animation.start(QAbstractAnimation.DeleteWhenStopped)

def check_login(account, pwd):
    if account == "990409144" and pwd == "1":
        print("登录成功")
        path = "E:\\桌面\\test\\" + account

        if not os.path.isdir(path):
            os.mkdir(path)

        custom_pane.fatherpath = path
        custom_pane.show()
        login_pane.hide()  #隐藏登录面板

    else:
        login_pane.show_error_animation()

#获得路径
def checkpath(path):


    print("main中=", path)
    return path

register_pane.exit_signal.connect(exit_register_pane)#连接main里面定义的接收函数
login_pane.show_register_pane_signal.connect(show_register_pane)
login_pane.check_login_signal.connect(check_login)
#custom_pane.directory_path_signal.connect(checkpath)


login_pane.show()


sys.exit(app.exec_())

if __name__=="__main__":
    pass
