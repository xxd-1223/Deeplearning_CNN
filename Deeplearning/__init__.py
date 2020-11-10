import torch
from torchvision import models


batch_size = 8

feature_extract = True #是否用训练好的权重

model_name = 'resnet' #使用resnet模型

model_ft = models.resnet50()  #使用resnet迁移学习

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") #判断电脑是否支持GPU加速

filename= 'checkpoint.pth'  # 保存文件的名字

num_classes = 10 #分10类

modelX = {1 : models.resnet18(pretrained=True), 2 : models.resnet34(pretrained=True), 3 : models.resnet50(pretrained=True), 4 : models.resnet101(pretrained=True)}

