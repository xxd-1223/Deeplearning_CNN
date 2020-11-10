# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom_training_data.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import datetime
import json
import os
import re
import matplotlib.pyplot as plt
import torch
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QComboBox, QTableWidget, QCheckBox, QMessageBox, \
    QFileDialog, QApplication
from PyQt5.QtGui import QIcon, QPixmap
import sys
from Deeplearning.copulation import Copulation
from GUI.testmodel_pane import Testmodel


class Customtrain(QWidget):

    directory_path_signal = pyqtSignal(str)
    wnumber = False
    mnumber = 0


    def __init__(self):
        super(Customtrain, self).__init__()

        self.initUI()

    def initUI(self):
        self.t = Testmodel()
        self.setWindowTitle("训练模型")
        #self.setToolTip('你好')  设置提示信息
        self.resize(1081, 834)
        self.setWindowIcon(QIcon('resources/images/LOG.png'))
        self.setStyleSheet("border-image:url(resources/images/background3.jpg)")
        with open("./resources/QSS.qss.txt") as f:
            qss = f.read()
        self.setStyleSheet(qss)
        '''按钮初始化'''
        #开始训练按钮
        self.begin_btn = QPushButton("开始训练", self)
        self.begin_btn.setGeometry(30, 450, 120, 60)
        self.begin_btn.clicked.connect(self.start)
        self.begin_btn.setEnabled(False)
        #上传训练集按钮
        self.uptraindata_btn = QPushButton("上传图片", self)
        self.uptraindata_btn.setGeometry(200, 310, 111, 51)
        self.uptraindata_btn.clicked.connect(self.getdirectorypath)
        self.uptraindata_btn.setEnabled(False)
        #上传权重文件按钮
        # upweightfile_btn = QPushButton("上传权重文件", self)
        # upweightfile_btn.setGeometry(750, 120, 101, 41)
        # upweightfile_btn.clicked.connect(self.getweightfile)
        #upvaliddata_btn.setEnabled(True)
        #验证模型按钮
        # self.testmodel_btn = QPushButton("保存", self)
        # self.testmodel_btn.setGeometry(750, 170, 101, 41)
        # self.testmodel_btn.clicked.connect(self.gettestpictures)
        # self.testmodel_btn.setEnabled(True)
        #确认按钮
        self.verify_btn = QPushButton("确认", self)
        self.verify_btn.setGeometry(30, 410, 93, 28)
        self.verify_btn.setEnabled(False)
        self.verify_btn.clicked.connect(self.writejson)
        #测试按钮
        test_btn = QPushButton("点此测试你的模型", self)
        test_btn.setGeometry(730, 110, 190, 60)
        test_btn.clicked.connect(self.showson)
        #二维码展示按钮
        showQR_btn = QPushButton("", self)
        showQR_btn.setGeometry(40, 609, 200, 200)
        showQR_btn.setEnabled(False)
        showQR_btn.setStyleSheet("border-image:url(resources/images/QR_code.jpg)")
        '''文本框初始化'''
        #输入权重文件名称
        self.weightname_line = QLineEdit(self)
        self.weightname_line.setGeometry(30, 40, 213, 32)
        self.weightname_line.setPlaceholderText("为你的分类项目创建一个name")
        self.weightname_line.setClearButtonEnabled(True)
        self.weightname_line.setMaxLength(10)
        self.weightname_line.editingFinished.connect(self.fix)
        self.weightname_line.setToolTip("系统会将权重文件保存为你输入的名称")

        #输入类名文件名称
        # self.classname_line = QLineEdit(self)
        # self.classname_line.setGeometry(430, 144, 193, 32)
        # self.classname_line.setPlaceholderText("请输入类名文件名称")
        # self.classname_line.setClearButtonEnabled(True)
        # self.classname_line.setMaxLength(10)
        # self.classname_line.editingFinished.connect(self.fix)
        # self.weightname_line.setToolTip("系统会将分类文件保存为你输入的名称")
        '''标签初始化'''
        #上传训练集图片标签
        uptraindata_label = QLabel("上传数据集", self)
        uptraindata_label.setGeometry(220, 270, 120, 16)
        uptraindata_label.setToolTip("请将数据集划分为训练集(train)与测试集(valid)并且每类图片分别保存在不同的文件夹中，文件夹名称设为数字且从1开始")
        #上传测试机集图片标签
        self.showoutput_label = QLabel("", self)
        self.showoutput_label.setGeometry(370, 280, 680, 510)
        self.showoutput_label.setStyleSheet("QLabel{background:white;}"
                      "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.showoutput_label.setScaledContents(True)



        #展示进度条标签
        # bar_label = QLabel("训练进度", self)
        # bar_label.setGeometry(200, 660, 111, 31)

        '''下拉列表初始化'''
        #选择分类数
        self.select_num_combobox = QComboBox(self)
        self.select_num_combobox.setGeometry(30, 110, 140, 22)
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
        self.select_num_combobox.setEnabled(False)
        #选择模型
        self.test_model_combobox = QComboBox(self)
        self.test_model_combobox.setGeometry(200, 110, 140, 22)
        self.test_model_combobox.addItems(["请选择模型", 'resnet18', 'resnet34', 'resnet50', 'resnet101'])
        self.test_model_combobox.setCurrentIndex(0)
        self.test_model_combobox.currentIndexChanged.connect(self.modulenum)
        self.test_model_combobox.setEnabled(False)


        '''表格初始化'''
        #tablewidget初始化
        self.traindata_table = QTableWidget(self)
        self.traindata_table.setGeometry(30, 170, 150, 221)

        '''进度条初始化'''
        #进度条位置150, 700, 211, 51
        # self.show_bar = QProgressBar(self)
        # self.show_bar.setGeometry(150, 700, 211, 51)
        # self.show_bar.setMinimum(50)
        # self.show_bar.setValue(75)
        '''单选按钮初始化'''
        self.gpu_checkbox = QCheckBox("是否使用GPU加速", self)
        self.gpu_checkbox.setGeometry(200, 170, 210, 50)
        self.gpu_checkbox.clicked.connect(self.judgeGPU)
        self.gpu_checkbox.setEnabled(False)


    def fix(self):
        name = self.weightname_line.text()
        fixname = re.sub(r'\.', "", name)
        self.weightname_line.setText(fixname)
        self.weightname = fixname
        self.wnumber = True
        #######
        self.select_num_combobox.setEnabled(True)
        self.test_model_combobox.setEnabled(True)
        self.gpu_checkbox.setEnabled(True)
        self.uptraindata_btn.setEnabled(True)
        print(fixname)

    #判断电脑是否支持GPU加速
    def judgeGPU(self):

        if not torch.cuda.is_available() :
            mb = QMessageBox(QMessageBox.Warning, "GPU", "你的电脑不支持GPU加速训练", QMessageBox.Ok, self)
            mb.exec_()
            self.gpu_checkbox.setChecked(False)


    #结合QCombobox动态生成表格
    def generateform(self, i):

        if not i :
            self.verify_btn.setEnabled(False)

        self.x = i
        print("当前分类数量为", self.x + 1)
        if i == 0 :
            i = -1
        self.traindata_table.setRowCount(i+1)  # 行数
        self.traindata_table.setColumnCount(1)  # 列数
        self.traindata_table.setHorizontalHeaderLabels(['请输入类名'])



    def getdirectorypath(self):

        self.path = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "E:\桌面")
        print(self.path)
        self.directory_path_signal.emit(self.path)
        try:
            if self.x-1 and self.mnumber and self.wnumber :
                self.verify_btn.setEnabled(True)
        except:
            print("输入的东西不全")
        else:
            self.verify_btn.setEnabled(True)


    def gettestpictures(self):
        #path = QFileDialog.getOpenFileNames(self, "选择jpg文件", "E:\桌面", "*.jpg")
        self.projectpath = QFileDialog.getSaveFileName(self, "为你的分类项目创建一个文件夹", "E:\桌面")
        print(self.projectpath)

    def start(self):
        c = Copulation()
        xxxx =self.weightname +".pth"
        self.GPU = self.gpu_checkbox.isChecked()
        if self.x >= 1 and self.mnumber:
            valid_losses, train_losses = c.begin(self.path, xxxx, self.x + 1, self.filenamespath, self.GPU, self.mnumber)
                                                #分别是 数据集路径，权重文件路径，分类数量，类名文件路径
            x = train_losses
            y = valid_losses
            # print("损失值", x)
            # print("损失值", y)
            dt = "LOSS-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
            plt.plot(x, label='train loss')
            plt.plot(y, label='valid loss')
            plt.legend()
            plt.savefig(dt)
            plt.show()
            self.showoutput_label.setPixmap(QPixmap(dt))
        else:
            mb = QMessageBox(QMessageBox.Critical, "错误", "请正确填写所有参数", QMessageBox.Ok, self)
            mb.exec_()

    def writejson(self):
        os.chdir(os.path.dirname(self.path)) #切换当前工作目录到数据集的上一级
        fuckpath = os.path.dirname(self.path) + "/" + self.weightname + "/"

        def mkdir(path):
            if not os.path.isdir(path):
                mkdir(os.path.split(path)[0])
            else:
                return
            os.mkdir(path)
        if not os.path.exists(fuckpath):

            os.mkdir(self.weightname) #根据权重文件的名称创建目录

            print("文件夹已创建")
        else:
            print("文件夹已存在")

        os.chdir(fuckpath)
        #print(fuckpath + "/test/valid/img")
        mkdir(fuckpath + "/test/valid/img")
        self.filenamespath = fuckpath + self.weightname + ".json"   #类名文件的路径
        foopath = fuckpath + "config" + ".json"     #要写入的配置文件的路径
        weightpath = fuckpath + self.weightname + ".pth"
        print(self.filenamespath)

        try:
            y = {}
            for i in range(self.x + 1):
                y[str(i+1)] = self.traindata_table.item(i, 0).text()

            print("y = ", y)

            z = {}
            z["num_classes"] = self.x + 1 #分类数
            z["model"] = self.mnumber #模型
            z["weightpath"] = weightpath#权重文件路径
            z["class_names"] = self.filenamespath #类名文件路径
            z["test"] = fuckpath + "test"
            print("z = ", z)
        except AttributeError:
            mb = QMessageBox(QMessageBox.Critical, "错误", "请正确填写所有参数", QMessageBox.Ok, self)
            mb.exec_()

        else:
            #分类数，模型 classnum = self.x + 1 ,  model = self.mnumber
            with open(foopath, 'w') as fuck:
                fuck.write(json.dumps(z, ensure_ascii=False))

            with open(self.filenamespath, 'w') as f_six:
                f_six.write(json.dumps(y, ensure_ascii=False))
            print("类名写入成功")

            self.begin_btn.setEnabled(True)



    def modulenum(self, i):
        self.mnumber = i
        print("模型号为：", self.mnumber)
        if self.mnumber :
            self.verify_btn.setEnabled(False)

    def showson(self):

        self.t.show()






if __name__=="__main__":
    app=QApplication(sys.argv)
    p=Customtrain()
    #t = Testmodel()
    p.show()
    sys.exit(app.exec_())