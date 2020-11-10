#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
------------------------------
@author:99040
@file: testmodel_pane.py
------------------------------

@time: 2020/03/12/17:31

------------------------------
"""
import json
import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFileDialog, QApplication

import os
import shutil

from Deeplearning.preprocess_predata import Preprocess_preddata


class Testmodel(QWidget):

    def __init__(self):
        super(Testmodel, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("测试模型")
        self.setToolTip('你好')  #设置提示信息
        self.resize(940, 780)
        self.setWindowIcon(QIcon('resources/images/LOG.png'))
        with open("./resources/QSS.qss.txt") as f:
            qss = f.read()
        self.setStyleSheet(qss)
        #self.setStyleSheet()
        '''按钮初始化'''
        #上传权重文件按钮
        upweightfile_btn = QPushButton("上传config文件", self)
        upweightfile_btn.setGeometry(90, 70, 151, 41)
        upweightfile_btn.clicked.connect(self.getconfigfile)
        #上传图片按钮
        self.testmodel_btn = QPushButton("上传图片", self)
        self.testmodel_btn.setGeometry(260, 70, 101, 41)
        self.testmodel_btn.clicked.connect(self.gettestpictures)
        self.testmodel_btn.setEnabled(False)

        #开始测试模型按钮
        self.begin_btn = QPushButton("开始", self)
        self.begin_btn.setGeometry(390, 70, 101, 41)
        self.testmodel_btn.clicked.connect(self.begaintest)
        self.begin_btn.setEnabled(False)
        #展示结果
        self.show_label = QLabel("", self)
        self.show_label.setGeometry(40, 150, 790, 570)
        self.show_label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.show_label.setScaledContents(True)

    def getconfigfile(self):
        path = QFileDialog.getOpenFileName(self, "选择一个配置文件", "E:\桌面", "config.json")
        print(path)
        if path[0] != '':
            with open(path[0], 'r') as f:
                cat_to_name = json.load(f)

            print("配置文件读取到的字典为：", cat_to_name)
            self.num_classes, self.model, self.weightpath, self.class_names, self.trainpath= self.damn(cat_to_name)
            self.testmodel_btn.setEnabled(True)


    def gettestpictures(self):
        self.path = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "E:\桌面")

        if self.path != '' :
            self.jpgnum = self.foo(self.path)
            print("jpg文件数量为：", self.jpgnum)
            if self.jpgnum != 0:
                self.begin_btn.setEnabled(True)
            else:
                print("没有图片")
                sys.exit()

    def foo(self, path):
        l = os.listdir(path)
        print("图片集的路径为 = ", path)
        num = 0
        needfile = []
        for filename in l:
            if os.path.splitext(filename)[1] == '.jpg':
                num+=1
                needfile.append(filename)
        if num <= 8 :
            for love in needfile:
                newpath = os.path.abspath(os.path.join(path, love))
                #print("组合后的jpg文件路径为：", newpath)
                shutil.copy(newpath, self.trainpath + "/valid/img")

        else:
            print("图片数量过多！！！")
        #print("所有的jpg文件名为：", needfile)
        #print("当前的工作路径为：", os.getcwd())
        return num


    def clear(self, path):
        print(path)
        shutil.rmtree(path)
        os.mkdir(path)
        #print("已清空")


    def damn(self, cat_to_name):
        num_classes = cat_to_name['num_classes']
        model = cat_to_name['model']
        weightpath = cat_to_name['weightpath']
        class_names = cat_to_name['class_names']
        trainpath = cat_to_name['test']
        return num_classes, model, weightpath, class_names, trainpath

    def begaintest(self):
        #{'num_classes': 2, 'model': 1, 'weightpath': 'E:/桌面/猫狗分类/猫狗分类.pth', 'class_names': 'E:/桌面/猫狗分类/猫狗分类.json'}
        #依次是分类数，模型，权重文件路径，类名文件路径
        # self.num_classes = self.cat_to_name['num_classes']
        # self.model = self.cat_to_name['model']
        # self.weightpath = self.cat_to_name['weightpath']
        # self.class_names = self.cat_to_name['class_names']
        # self.trainpath = self.cat_to_name['test']
        os.chdir(os.path.dirname(self.weightpath))
        print("num_classes=", self.num_classes)
        print("model=",self.model)
        print("weightpath=",self.weightpath)
        print("class_names=",self.class_names)
        #把类名文件读入字典y中
        #y = {}
        with open(self.class_names, 'r') as f:
            y = json.load(f)

        print("y=" , y)
        # 参数的意思分别是分类数，权重文件路径，上传了几张图片（最大为8），使用的模型
        p = Preprocess_preddata(self.num_classes, self.weightpath, self.jpgnum, self.model)
        preds, best_acc, picturepath = p.predictone(self.trainpath, y, True)


        try:
            print("修正以后的预测值为：", preds)
            print("正确率为：{:.2%}".format(best_acc))
            #结果分别为
            if self.jpgnum > 1:
                for i in preds:
                    print("预测的结果分别为", y[str(i)])
            else:
                print("预测的结果分别为", y[str(preds.tolist())])
        except KeyError:
            print("值错误")
        except AttributeError:
            print("没有上传图片")

        else:
            self.show_label.setPixmap(QPixmap(picturepath))
            self.clear(self.trainpath + "/valid/img")
            print("完成！！！！")
        #finally:






if __name__ == '__main__':

    app = QApplication(sys.argv)
    p = Testmodel()
    p.show()
    sys.exit(app.exec_())
    pass