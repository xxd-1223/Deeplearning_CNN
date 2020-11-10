#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
------------------------------
@author:99040
@file: preset_pane.py
------------------------------

@time: 2020/03/18/22:38

------------------------------
"""
import os
import shutil
import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFileDialog, QApplication

from Deeplearning.predictoutput import Pred_output
from Deeplearning.preprocess_predata import Preprocess_preddata


class Presetpane(QWidget):


    def __init__(self):
        super(Presetpane, self).__init__()
        self.initUI()


    def initUI(self):

        self.setWindowTitle("花卉识别")
        self.setToolTip('你好')  # 设置提示信息
        self.resize(940, 780)
        self.setWindowIcon(QIcon('resources/images/LOG.png'))
        with open("./resources/QSS.qss.txt") as f:
            qss = f.read()
        self.setStyleSheet(qss)

        '''按钮控件'''
        #
        refresh_btn = QPushButton("刷新", self)
        refresh_btn.setGeometry(90, 70, 151, 41)
        refresh_btn.clicked.connect(self.refresh)
        #
        upphoto_btn = QPushButton("上传图片", self)
        upphoto_btn.setGeometry(250, 70, 151, 41)
        upphoto_btn.clicked.connect(self.getphoto)
        #
        self.btn = QPushButton("确认", self)
        self.btn.setGeometry(400, 70, 151, 41)
        self.btn.clicked.connect(self.predict)
        self.btn.setEnabled(False)
        '''标签控件'''
        #用于结果图片
        self.show_label = QLabel("", self)
        self.show_label.setGeometry(40, 150, 850, 570)
        self.show_label.setStyleSheet("QLabel{background:white;}"
                                      "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.show_label.setScaledContents(True)
        pass

    def refresh(self):
        os.chdir("F:/PycharmProjects/Graduation/Deeplearning")
        P = Pred_output()
        images, labels = P.get_testdata()
        print(type(labels))
        preds, best_acc = P.predict(images, 10)
        # print("labels = ", labels)
        # print("preds = ", preds)
        print("预测的概率为：{:.2%}".format(best_acc))
        # P.show(images, labels, preds)
        path = P.show(images, labels, preds)

        self.show_label.setPixmap(QPixmap(path))

    #上传图片
    def getphoto(self):
        self.path = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "E:\桌面")

        if self.path != '':
            self.jpgnum = self.foo(self.path)
            print("jpg文件数量为：", self.jpgnum)
            if self.jpgnum != 0:
                self.btn.setEnabled(True)
                pass
            else:
                print("没有图片")
                sys.exit()

    #将上传的图片复制到指定目录
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
                print("组合后的jpg文件路径为：", newpath)
                shutil.copy(newpath, "F:\\PycharmProjects\\Graduation\\Deeplearning\\one\\valid\\test")

        else:
            print("图片数量过多！！！")
        print("所有的jpg文件名为：", needfile)
        print("当前的工作路径为：", os.getcwd())
        return num

    def predict(self):
        y = {"3": "风铃草", "1": "月见草", "7": "蝴蝶兰", "10": "驴欺口", "6": "卷丹", "9": "乌头", "4": "香豌豆", "2": "硬叶兜兰", "5": "金盏花",
         "8": "鹤望兰"}
        os.chdir("F:/PycharmProjects/Graduation/Deeplearning")
        x = 0
        print("x=", x)
        x += 1
        # 参数的意思分别是分类数，权重文件路径，上传了几张图片（最大为8），使用的模型
        p = Preprocess_preddata(10, "F:\\PycharmProjects\\Graduation\\Deeplearning\\checkpoint.pth", self.jpgnum, 3)
        preds, best_acc, picturepath = p.predictone("one/", y, True)


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
            self.clear("one/valid/test")
            print("完成！！！！")
            #del p
            self.btn.setEnabled(False)

            return True


    #清空
    def clear(self, path):
        print(path)
        shutil.rmtree(path)
        os.mkdir(path)
        print("已清空")


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Presetpane()
    window.show()

    sys.exit(app.exec_())

