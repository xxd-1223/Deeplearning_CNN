#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
------------------------------
@author:99040
@file: copulation.py
------------------------------

@time: 2020/03/08/10:58

------------------------------
"""
import sys

import torch
from torchvision import models


from Deeplearning.preprocess_traindata import Preprocess_traindata
from Deeplearning.training import Train
from Deeplearning import device


class Copulation():

    def __init__(self):
        pass

    def begin(self, path, filename, num_class ,classnamefilepath, train_on_gpu, modelname):
        #数据集路径，
        modelX = {1 : models.resnet18(pretrained=True), 2 : models.resnet34(pretrained=True), 3 : models.resnet50(pretrained=True), 4 : models.resnet101(pretrained=True)}
        #models.resnet50(pretrained=True)

        preprocess = Preprocess_traindata(8, path)#8是batchsize的大小，path是数据集的路径
        try:
            cat_to_name, class_names, dataloaders = preprocess.show_data(classnamefilepath)
            train = Train(train_on_gpu, modelX[modelname], dataloaders, num_class, filename, device)
            #                                                            num_classes
            # 第一次训练
            scheduler, criterion, optimizer_ft, params_to_update, model_ft = train.setOptimizer(1e-2)
        except:
            print("出现未知的错误")
            sys.exit()
        else:

            model, val_acc_history, train_acc_history, valid_losses, train_losses, LRs = train.train_model(10, scheduler, criterion, optimizer_ft, model_ft)


            return valid_losses, train_losses


if __name__ == '__main__':
    pass