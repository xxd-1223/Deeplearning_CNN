# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom_training_data.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Customtrain(object):
    def setupUi(self, Customtrain):
        Customtrain.setObjectName("Customtrain")
        Customtrain.resize(1081, 834)
        self.begin_btn = QtWidgets.QPushButton(Customtrain)
        self.begin_btn.setGeometry(QtCore.QRect(190, 520, 121, 61))
        self.begin_btn.setObjectName("begin_btn")
        self.test_label = QtWidgets.QLabel(Customtrain)
        self.test_label.setGeometry(QtCore.QRect(740, 70, 131, 41))
        self.test_label.setObjectName("test_label")
        self.test_model_cb = QtWidgets.QComboBox(Customtrain)
        self.test_model_cb.setGeometry(QtCore.QRect(736, 120, 121, 22))
        self.test_model_cb.setObjectName("test_model_cb")
        self.output_label = QtWidgets.QLabel(Customtrain)
        self.output_label.setGeometry(QtCore.QRect(770, 240, 91, 20))
        self.output_label.setObjectName("output_label")
        self.traindata_table = QtWidgets.QTableView(Customtrain)
        self.traindata_table.setGeometry(QtCore.QRect(110, 130, 281, 221))
        self.traindata_table.setObjectName("traindata_table")
        self.select_num_cb = QtWidgets.QComboBox(Customtrain)
        self.select_num_cb.setGeometry(QtCore.QRect(110, 70, 131, 22))
        self.select_num_cb.setObjectName("select_num_cb")
        self.select_num_cb.addItem("")
        self.pushButton = QtWidgets.QPushButton(Customtrain)
        self.pushButton.setGeometry(QtCore.QRect(110, 420, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Customtrain)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 420, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Customtrain)
        self.label.setGeometry(QtCore.QRect(130, 390, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Customtrain)
        self.label_2.setGeometry(QtCore.QRect(300, 390, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Customtrain)
        self.label_3.setGeometry(QtCore.QRect(740, 280, 141, 51))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Customtrain)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 170, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(Customtrain)
        self.progressBar.setGeometry(QtCore.QRect(150, 700, 211, 51))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(Customtrain)
        self.label_4.setGeometry(QtCore.QRect(200, 660, 111, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Customtrain)
        QtCore.QMetaObject.connectSlotsByName(Customtrain)

    def retranslateUi(self, Customtrain):
        _translate = QtCore.QCoreApplication.translate
        Customtrain.setWindowTitle(_translate("Customtrain", "Form"))
        self.begin_btn.setText(_translate("Customtrain", "开始训练"))
        self.test_label.setText(_translate("Customtrain", "测试自定义模型"))
        self.output_label.setText(_translate("Customtrain", "预测结果"))
        self.select_num_cb.setItemText(0, _translate("Customtrain", "选择分类数量"))
        self.pushButton.setText(_translate("Customtrain", "PushButton"))
        self.pushButton_2.setText(_translate("Customtrain", "PushButton"))
        self.label.setText(_translate("Customtrain", "训练集图片"))
        self.label_2.setText(_translate("Customtrain", "测试集图片"))
        self.label_3.setText(_translate("Customtrain", "TextLabel"))
        self.pushButton_3.setText(_translate("Customtrain", "上传图片"))
        self.label_4.setText(_translate("Customtrain", "训练进度"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Customtrain = QtWidgets.QWidget()
    ui = Ui_Customtrain()
    ui.setupUi(Customtrain)
    Customtrain.show()
    sys.exit(app.exec_())
