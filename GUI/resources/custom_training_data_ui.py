# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom_training_data.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
#
#
# class Custominputdata(QtWidgets):
#
#     def __init__(self, parent=None):
#         super(Custominputdata, self).__init__(parent)
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("自定义训练模型")
#         self.resize(1081, 834)
#         layout = QHBoxLayout()
#         tablewidget = QTableWidget()
#         #设置表格的行数
#         tablewidget.setRowCount(6)
#         #设置表格的列数
#         tablewidget.setColumnCount(3)
#
#         layout.addWidget(tablewidget)
#
#         tablewidget.setHorizontalHeaderLabels(['类名', '上传图片'])
#         nameItem = QTableWidget("小明")
#         tablewidget.setItem(0, 0, nameItem)
#
#         pictureItem = QTableWidget("图片")
#         tablewidget.setItem(0, 0, pictureItem)
#
#         self.setLayout(layout)
#         pass
#     # def setupUi(self, Form):
#     #     Form.setObjectName("Form")
#     #     Form.resize(1081, 834)
#     #     self.pushButton = QtWidgets.QPushButton(Form)
#     #     self.pushButton.setGeometry(QtCore.QRect(460, 740, 121, 61))
#     #     self.pushButton.setObjectName("pushButton")
#     #     self.tableWidget = QtWidgets.QTableWidget(Form)
#     #     self.tableWidget.setGeometry(QtCore.QRect(310, 110, 431, 501))
#     #     self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
#     #     self.tableWidget.setObjectName("tableWidget")
#     #     self.tableWidget.setColumnCount(2)
#     #     self.tableWidget.setRowCount(6)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setVerticalHeaderItem(0, item)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setVerticalHeaderItem(1, item)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setVerticalHeaderItem(2, item)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setVerticalHeaderItem(3, item)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setVerticalHeaderItem(4, item)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setVerticalHeaderItem(5, item)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setHorizontalHeaderItem(0, item)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setHorizontalHeaderItem(1, item)
#     #     item = QtWidgets.QTableWidgetItem()
#     #     self.tableWidget.setItem(0, 0, item)
#     #     self.tableWidget.horizontalHeader().setVisible(True)
#     #     self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
#     #     self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
#     #     self.tableWidget.horizontalHeader().setMinimumSectionSize(33)
#     #     self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
#     #     self.tableWidget.horizontalHeader().setStretchLastSection(True)
#     #     self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
#     #     self.tableWidget.verticalHeader().setSortIndicatorShown(False)
#     #     self.tableWidget.verticalHeader().setStretchLastSection(True)
#     #
#     #     self.retranslateUi(Form)
#     #     QtCore.QMetaObject.connectSlotsByName(Form)
#     #
#     # def retranslateUi(self, Form):
#     #     _translate = QtCore.QCoreApplication.translate
#     #     Form.setWindowTitle(_translate("Form", "Form"))
#     #     self.pushButton.setText(_translate("Form", "开始训练"))
#     #     self.tableWidget.setWhatsThis(_translate("Form", "<html><head/><body><p>ewqeq</p></body></html>"))
#     #     item = self.tableWidget.verticalHeaderItem(0)
#     #     item.setText(_translate("Form", "编号"))
#     #     item = self.tableWidget.verticalHeaderItem(1)
#     #     item.setText(_translate("Form", "1"))
#     #     item = self.tableWidget.verticalHeaderItem(2)
#     #     item.setText(_translate("Form", "2"))
#     #     item = self.tableWidget.verticalHeaderItem(3)
#     #     item.setText(_translate("Form", "3"))
#     #     item = self.tableWidget.verticalHeaderItem(4)
#     #     item.setText(_translate("Form", "4"))
#     #     item = self.tableWidget.verticalHeaderItem(5)
#     #     item.setText(_translate("Form", "5"))
#     #     item = self.tableWidget.horizontalHeaderItem(0)
#     #     item.setText(_translate("Form", "类名"))
#     #     item = self.tableWidget.horizontalHeaderItem(1)
#     #     item.setText(_translate("Form", "上传图片"))
#     #     __sortingEnabled = self.tableWidget.isSortingEnabled()
#     #     self.tableWidget.setSortingEnabled(False)
#     #     self.tableWidget.setSortingEnabled(__sortingEnabled)
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#
#     ui = Custominputdata()
#     ui.show()
#     sys.exit(app.exec_())
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

#------------------------------------------------
# class tableview(QWidget):
#     def __init__(self):
#         super(tableview, self).__init__()
#         self.setWindowTitle("QTableView表格视图控件演示")
#         self.resize(600,500)
#
#         self.model=QStandardItemModel(5,3) #创建一个标准的数据源model
#         self.model.setHorizontalHeaderLabels(["id","姓名","年龄"])  #设置表格的表头名称
#
#         self.tableview=QTableView()
#         #关联model和tableview控件
#         self.tableview.setModel(self.model)
#
#         #添加数据
#         #首先定义字符类数据
#         item11=QStandardItem("10")
#         item12=QStandardItem("雷神")
#         item13=QStandardItem("2000")
#         #其次将定义好的的数据添加到数据源model中
#         self.model.setItem(0,0,item11)
#         self.model.setItem(0,1,item12)
#         self.model.setItem(0,2,item13)
#
#         layout=QVBoxLayout()
#         layout.addWidget(self.tableview)
#         self.setLayout(layout)
#------------------------------------------------
class Customtrain(QWidget):

    def __init__(self):
        super(Customtrain, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableView表格视图控件演示")
        #self.setToolTip('你好')  设置提示信息
        self.resize(1081, 834)
        self.setWindowIcon(QIcon('resources/images/LOG.png'))#GUI/resources/images

        '''按钮初始化'''
        #开始训练按钮
        begin_btn = QPushButton("开始训练", self)
        begin_btn.setGeometry(190, 520, 121, 61)
        #上传训练集按钮
        uptraindata_btn = QPushButton("上传图片", self)
        uptraindata_btn.setGeometry(110, 420, 111, 51)
        uptraindata_btn.clicked.connect(self.getdirectorypath)
        #上传验证集按钮
        upvaliddata_btn = QPushButton("上传图片", self)
        upvaliddata_btn.setGeometry(290, 420, 111, 51)
        upvaliddata_btn.clicked.connect(self.getdirectorypath)
        #验证模型按钮
        testmodel_btn = QPushButton("上传图片", self)
        testmodel_btn.setGeometry(750, 170, 101, 41)
        testmodel_btn.clicked.connect(self.getdirectorypath)

        '''标签初始化'''
        #上传训练集图片标签
        uptraindata_label = QLabel("上传训练集图片", self)
        uptraindata_label.setGeometry(120, 390, 120, 16)
        #上传测试机集图片标签
        upvaliddata_label = QLabel("上传测试集图片", self)
        upvaliddata_label.setGeometry(300, 390, 120, 16)
        #测试模型标签
        testmodel_label = QLabel("测试自定义模型", self)
        testmodel_label.setGeometry(740, 280, 141, 51)
        #标记结果位置标签
        output_label = QLabel("预测结果", self)
        output_label.setGeometry(770, 240, 91, 20)
        #输出结果标签
        showoutput_label = QLabel(self)
        showoutput_label.setGeometry(740, 280, 141, 51)
        #展示进度条标签
        bar_label = QLabel("训练进度", self)
        bar_label.setGeometry(200, 660, 111, 31)

        '''下拉列表初始化'''
        #combobox初始化（下拉列表）
        self.select_num_combobox = QComboBox(self)
        self.select_num_combobox.setGeometry(110, 70, 140, 22)
        self.select_num_combobox.addItems(["请输入分类数量", '2', '3', '4' ,'5'])
        self.select_num_combobox.setCurrentIndex(0)
        self.select_num_combobox.currentIndexChanged.connect(self.generateform)
        self.select_num_combobox.setStyleSheet('''QComboBox {
	color:rgb(81,72,65);
	background: #ffffff;
}
QComboBox:editable {
	background: #ffffff;
	color: rgb(81,72,65);
	selection-color:rgb(81,72,65);
	selection-background-color: #ffffff;
}
QComboBox QAbstractItemView {
	color:rgb(81,72,65);	
	background: #ffffff;
	selection-color: #ffffff;
	selection-background-color: rgb(246, 134, 86);
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
	color:  #1e1d23;	
	background: #ffffff;
}''')
        self.test_model_combobox = QComboBox(self)
        self.test_model_combobox.setGeometry(736, 120, 140, 22)
        self.test_model_combobox.addItems(["请输入分类数量", '2', '3', '4', '5'])
        self.test_model_combobox.setCurrentIndex(0)
        #self.test_model_combobox.currentIndexChanged.connect(self.generateform)


        '''表格初始化'''
        #tablewidget初始化
        self.traindata_table = QTableWidget(self)
        self.traindata_table.setGeometry(110, 130, 280, 221)

        '''进度条初始化'''
        #进度条位置150, 700, 211, 51
        self.show_bar = QProgressBar(self)
        self.show_bar.setGeometry(150, 700, 211, 51)
        self.show_bar.setMinimum(50)
        self.show_bar.setValue(75)
        #
        # self.traindata_table.setRowCount(5)#行数
        # self.traindata_table.setColumnCount(2)#列数
        # self.traindata_table.setHorizontalHeaderLabels(['类名', '图片'])
        #self.btn1 = QPushButton("上传图片")
    #结合QCombobox动态生成表格
    def generateform(self, i):
        if i == 0:
            i = -1
        self.traindata_table.setRowCount(i+1)  # 行数
        self.traindata_table.setColumnCount(2)  # 列数
        self.traindata_table.setHorizontalHeaderLabels(['请输入类名', '上传图片'])

        btn1 = QPushButton("上传图片", self)
        btn2 = QPushButton("上传图片", self)
        btn3 = QPushButton("上传图片", self)
        btn4 = QPushButton("上传图片", self)
        btn5 = QPushButton("上传图片", self)

        #将单元格内容设为button
        self.traindata_table.setCellWidget(0, 1, btn1)
        self.traindata_table.setCellWidget(1, 1, btn2)
        self.traindata_table.setCellWidget(2, 1, btn3)
        self.traindata_table.setCellWidget(3, 1, btn4)
        self.traindata_table.setCellWidget(4, 1, btn5)

        btn1.clicked.connect(self.getdirectorypath)
        btn2.clicked.connect(self.getdirectorypath)
        btn3.clicked.connect(self.getdirectorypath)
        btn4.clicked.connect(self.getdirectorypath)
        btn5.clicked.connect(self.getdirectorypath)


    def getdirectorypath(self):

        path = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "../")
        print(path)
        return path


if __name__=="__main__":
    app=QApplication(sys.argv)
    p=Customtrain()
    p.show()
    sys.exit(app.exec_())