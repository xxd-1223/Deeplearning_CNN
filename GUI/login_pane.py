#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
------------------------------
@author:99040
@file: login_pane.py
------------------------------

@time: 2020/03/05/15:36

------------------------------
"""

#!usr/bin/env python
#-*- coding:utf-8 _*-

from PyQt5.Qt import *
from resources.login_ui import Ui_Login
class LoginPane(QWidget, Ui_Login):

    show_register_pane_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def show_register_pane(self):
        print("弹出注册界面")
        self.show_register_pane_signal.emit()

    def open_cnn_link(self):
        print("神经网络")
        link = "https://baike.baidu.com/item/%E5%8D%B7%E7%A7%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C"
        QDesktopServices.openUrl(QUrl(link))

    def enable_login_btn(self):

        account = self.account_cb.currentText()
        pwd = self.pwd_line.text()
        print(account, pwd)
        if len(account) > 0 and len(pwd) >0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def check_login(self):

        account = self.account_cb.currentText()
        pwd = self.pwd_line.text()
        self.check_login_signal.emit(account, pwd)

    def auto_login(self, checked):
        print("自动登录", checked)
        if checked:
            print("设置记住密码")
            self.remember_pwd_cb.setChecked(True)


    def remember_pwd(self, checked):
        print("记住密码", checked)

        if not checked:
            print("设置自动登录")
            self.auto_login_cb.setChecked(False)

    #错误动画效果
    def show_error_animation(self):

        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)
        animation.setPropertyName(b"pos")

        animation.setKeyValueAt(0, self.login_bottom.pos())
        animation.setKeyValueAt(0.2, self.login_bottom.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.login_bottom.pos())
        animation.setKeyValueAt(0.7, self.login_bottom.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.login_bottom.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)







if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())
