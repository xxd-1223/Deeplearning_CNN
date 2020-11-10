# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(599, 507)
        self.gridLayout = QtWidgets.QGridLayout(Login)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.login_bottom = QtWidgets.QWidget(Login)
        self.login_bottom.setStyleSheet("")
        self.login_bottom.setObjectName("login_bottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.login_bottom)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.login_bottom)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.login_bottom)
        self.widget_3.setMinimumSize(QtCore.QSize(320, 304))
        self.widget_3.setMaximumSize(QtCore.QSize(320, 304))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.account_cb = QtWidgets.QComboBox(self.widget_3)
        self.account_cb.setGeometry(QtCore.QRect(10, 30, 298, 40))
        self.account_cb.setMinimumSize(QtCore.QSize(298, 40))
        self.account_cb.setMaximumSize(QtCore.QSize(298, 40))
        self.account_cb.setStyleSheet("QComboBox {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom:1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QComboBox:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"QComboBox::drop-down {\n"
"    border-color: transparent;\n"
"    width: 60px;\n"
"    height:40px;\n"
"}\n"
"QComboBox:down-arrow {\n"
"    image: url(:/login/images/login_down_icon.png);\n"
"    width: 60px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    min-height: 60px;\n"
"}\n"
"QComboBox QAbstractItemView:item {\n"
"    color: lightblue;\n"
"}")
        self.account_cb.setEditable(True)
        self.account_cb.setObjectName("account_cb")
        self.account_cb.addItem("")
        self.account_cb.addItem("")
        self.pwd_line = QtWidgets.QLineEdit(self.widget_3)
        self.pwd_line.setGeometry(QtCore.QRect(10, 100, 298, 35))
        self.pwd_line.setMinimumSize(QtCore.QSize(298, 35))
        self.pwd_line.setMaximumSize(QtCore.QSize(298, 35))
        self.pwd_line.setStyleSheet("QLineEdit{\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"\n"
"")
        self.pwd_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_line.setClearButtonEnabled(True)
        self.pwd_line.setObjectName("pwd_line")
        self.login_btn = QtWidgets.QPushButton(self.widget_3)
        self.login_btn.setGeometry(QtCore.QRect(60, 200, 200, 50))
        self.login_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.login_btn.setMaximumSize(QtCore.QSize(200, 50))
        self.login_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    spacing: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 250);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/images/login_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon)
        self.login_btn.setIconSize(QtCore.QSize(30, 30))
        self.login_btn.setObjectName("login_btn")
        self.auto_login_cb = QtWidgets.QCheckBox(self.widget_3)
        self.auto_login_cb.setGeometry(QtCore.QRect(210, 160, 87, 19))
        self.auto_login_cb.setMinimumSize(QtCore.QSize(87, 19))
        self.auto_login_cb.setMaximumSize(QtCore.QSize(87, 19))
        self.auto_login_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.auto_login_cb.setObjectName("auto_login_cb")
        self.remember_pwd_cb = QtWidgets.QCheckBox(self.widget_3)
        self.remember_pwd_cb.setGeometry(QtCore.QRect(20, 160, 87, 19))
        self.remember_pwd_cb.setMinimumSize(QtCore.QSize(87, 19))
        self.remember_pwd_cb.setMaximumSize(QtCore.QSize(87, 19))
        self.remember_pwd_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remember_pwd_cb.setObjectName("remember_pwd_cb")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 270, 301, 30))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.login_bottom)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QtCore.QSize(120, 120))
        self.pushButton_2.setStyleSheet("border-image: url(:/login/images/QR_code.jpg);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.login_bottom, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setStyleSheet("border-image: url(:/login/images/CNN.jpeg);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Login)
        self.pushButton.clicked.connect(Login.show_register_pane)
        self.pushButton_4.clicked.connect(Login.open_cnn_link)
        self.account_cb.editTextChanged['QString'].connect(Login.enable_login_btn)
        self.pwd_line.textChanged['QString'].connect(Login.enable_login_btn)
        self.login_btn.clicked.connect(Login.check_login)
        self.remember_pwd_cb.clicked['bool'].connect(Login.auto_login)
        self.auto_login_cb.clicked['bool'].connect(Login.remember_pwd)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.pushButton.setText(_translate("Login", "注册账号"))
        self.account_cb.setItemText(0, _translate("Login", "990409144"))
        self.account_cb.setItemText(1, _translate("Login", "1600923552"))
        self.login_btn.setText(_translate("Login", "安全登录"))
        self.auto_login_cb.setText(_translate("Login", "自动登录"))
        self.remember_pwd_cb.setText(_translate("Login", "记住密码"))
        self.pushButton_4.setText(_translate("Login", "Convolutional Neural Network"))
import images_res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
