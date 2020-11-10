#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
------------------------------
@author:99040
@file: register_pane.py
------------------------------
@time: 2020/03/04/22:33

Change Activity: 2020/3/4
------------------------------
"""
from PyQt5.Qt import *
from resources.register_ui import Ui_Register
class RegisterPane(QWidget, Ui_Register):

    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.animation_targets = [self.about_menue_btn, self.reset_menue_btn, self.exit_menue_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]


    def show_hide_menue(self, checked):
        print(checked)
        animation_group = QSequentialAnimationGroup(self)

        for idx, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            #if not checked:
            animation.setStartValue(self.main_menue_btn.pos())
            animation.setEndValue(self.animation_targets_pos[idx])
            # else:
            #     animation.setEndValue(self.main_menue_btn.pos())
            #     animation.setStartValue(self.animation_targets_pos[idx])
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.OutBounce)
            animation_group.addAnimation(animation)
        if not checked:
            animation_group.setDirection(QAbstractAnimation.Forward)
        else:
            animation_group.setDirection(QAbstractAnimation.Backward)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)


        pass
    #退出按钮点击事件
    def exit_ui(self):
        self.exit_signal.emit()
        pass
    def about_cnn(self):
        print("关于")
        pass
    def resnet_data(self):
        print("重置")
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_pwd_le.clear()
        pass

    def check_register(self):
        '''注册按钮的信号'''
        print("注册")

        account_text = self.account_le.text()
        password_txt = self.password_le.text()
        self.register_account_pwd_signal.emit(account_text, password_txt)

    def enable_register_btn(self):
        '''判定'''
        print("判定")
        account_text = self.account_le.text()
        password_txt = self.password_le.text()
        cp_txt = self.confirm_pwd_le.text()
        #判定密码格式
        if len(account_text) > 0 and len(password_txt) > 0 and len(cp_txt) > 0 and password_txt == cp_txt:
            print("正确")
        else:
            print("错误")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_signal.connect(lambda :print("退出"))
    window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()
    sys.exit(app.exec_())
