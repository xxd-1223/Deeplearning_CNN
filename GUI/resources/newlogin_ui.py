# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newlogin.ui'
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
        self.link_btn = QtWidgets.QPushButton(self.login_bottom)
        self.link_btn.setObjectName("link_btn")
        self.horizontalLayout_2.addWidget(self.link_btn, 0, QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.login_bottom)
        self.widget_3.setMinimumSize(QtCore.QSize(320, 304))
        self.widget_3.setMaximumSize(QtCore.QSize(320, 304))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
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
        self.login_btn_2 = QtWidgets.QPushButton(self.widget_3)
        self.login_btn_2.setGeometry(QtCore.QRect(60, 80, 200, 50))
        self.login_btn_2.setMinimumSize(QtCore.QSize(200, 50))
        self.login_btn_2.setMaximumSize(QtCore.QSize(200, 50))
        self.login_btn_2.setStyleSheet("QPushButton{\n"
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
        self.login_btn_2.setIcon(icon)
        self.login_btn_2.setIconSize(QtCore.QSize(30, 30))
        self.login_btn_2.setObjectName("login_btn_2")
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
        self.login_btn_2.clicked.connect(Login.show_preset_pane)
        self.pushButton_4.clicked.connect(Login.open_cnn_link)
        self.login_btn.clicked.connect(Login.show_train_pane)
        self.link_btn.clicked.connect(Login.open_link)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.link_btn.setText(_translate("Login", "进入网页版"))
        self.login_btn.setText(_translate("Login", "训练模型"))
        self.pushButton_4.setText(_translate("Login", "Convolutional Neural Network"))
        self.login_btn_2.setText(_translate("Login", "进入花卉识别"))
import images_res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
