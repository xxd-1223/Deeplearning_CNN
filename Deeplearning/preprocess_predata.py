import os
#import sys
import datetime

import matplotlib.pyplot as plt
import numpy as np
import torch

from PIL import Image
from torchvision import transforms, datasets

#from Deeplearning import modelX
from Deeplearning.loadmodel import load

from torchvision import models

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#对预测数据进行预处理
class Preprocess_preddata():


    def __init__(self, classnum, weightfilepath, photonum, modelNUM):
        modelX = {1: models.resnet18(pretrained=True), 2: models.resnet34(pretrained=True),
                  3: models.resnet50(pretrained=True), 4: models.resnet101(pretrained=True)}
        self.classnum = classnum
        self.weightpath = weightfilepath
        self.photonum = photonum
        self.modelNUM = modelX[modelNUM]


    def process_image(self, image_path):
        # 读取测试数据
        img = Image.open(image_path)
        # Resize,thumbnail方法只能进行缩小，所以进行了判断
        if img.size[0] > img.size[1]:
            img.thumbnail((10000, 256))
        else:
            img.thumbnail((256, 10000))
        # Crop操作
        left_margin = (img.width - 224) / 2
        bottom_margin = (img.height - 224) / 2
        right_margin = left_margin + 224
        top_margin = bottom_margin + 224
        img = img.crop((left_margin, bottom_margin, right_margin,
                        top_margin))
        # 相同的预处理方法
        img = np.array(img) / 255
        mean = np.array([0.485, 0.456, 0.406])  # provided mean
        std = np.array([0.229, 0.224, 0.225])  # provided std
        img = (img - mean) / std

        # 注意颜色通道应该放在第一个位置
        img = img.transpose((2, 0, 1))

        return img

    def imshow(self,image_path, ax=None, title=None):
        """展示数据"""
        image = self.process_image(image_path)
        if ax is None:
            fig, ax = plt.subplots()

        # 颜色通道还原
        image = np.array(image).transpose((1, 2, 0))

        # 预处理还原
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        image = std * image + mean
        image = np.clip(image, 0, 1)

        ax.imshow(image)
        ax.set_title(title)

        plt.show()
        return ax, image

    def im_convert(self, tensor):
        """ 将处理后的图片还原"""
        image = tensor.to("cpu").clone().detach()
        image = image.numpy().squeeze()
        image = image.transpose(1, 2, 0)
        image = image * np.array((0.229, 0.224, 0.225)) + np.array((0.485, 0.456, 0.406))
        image = image.clip(0, 1)

        return image

    def predictone(self, foo, classname=None, draw = False):
        '''对单张或最多8张图片进行预测'''
        #data_dir = 'one\\'

        data_transforms = {

            'valid': transforms.Compose([transforms.Resize(256),
                                         transforms.CenterCrop(224),
                                         transforms.ToTensor(),
                                         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                         ]),
        }
        try:
            image_datasets = {x: datasets.ImageFolder(os.path.join(foo, x), data_transforms[x]) for x in
                              ['valid']}
            dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], self.photonum, shuffle=False) for x
                           in ['valid']}
        except RuntimeError:
            print("错误，没有图片")
            return None, None, None

        dataiter = iter(dataloaders['valid'])
        images, labels = dataiter.next()

        #图像还原
        '''
        image = images[0].to("cpu").clone().detach()
        image = image.numpy().squeeze()
        image = image.transpose(1, 2, 0)
        image = image * np.array((0.229, 0.224, 0.225)) + np.array((0.485, 0.456, 0.406))
        image = image.clip(0, 1)
        image1 = torch.from_numpy(image)
        plt.imshow(image)
        plt.show()
        #plt.imshow(images[2])
        '''
        #print("标签=", labels)
        #print(self.modelNUM)
        # print(self.weightpath)
        # print(self.classnum)
        #print("模型=", self.modelNUM)
        # print("权重文件路径", self.weightpath)
        # print("分类数", self.classnum)
        model_ft, input_size, best_acc = load.loadmodel(self.modelNUM, self.weightpath, self.classnum, feature_extract=True)
        #model_ft, input_size, best_acc = load.loadmodel(models.resnet18(pretrained=True), "E:/桌面/猫狗分类/猫狗分类.pth", 2, feature_extract= True)

        model_ft.eval()
        train_on_gpu = False
        if train_on_gpu:
            output = model_ft(images.cuda())
        else:
            output = model_ft(images)

        _, preds_tensor = torch.max(output, 1)

        preds = np.squeeze(preds_tensor.numpy()) if not train_on_gpu else np.squeeze(preds_tensor.cpu().numpy())
        #preds 因为preds的值从0开始而真实的值是从1开始，因此需要整体给preds加1
        #preds = preds + 1
        print("Deeplearning-未修正",preds)
        preds += 1
        dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        drawpath = os.path.dirname(self.weightpath) + "\\" + dt
        print(drawpath)

        if draw:
            if self.photonum ==1:
                fig = plt.figure(figsize=(20, 12))
                columns = 1
                rows = 1

                for idx in range (columns*rows):
                    ax = fig.add_subplot(rows, columns, idx+1, xticks=[], yticks=[])
                    ax.set_title(classname[str(preds)], fontdict={'weight':'normal','size': 50})
                    plt.imshow(self.im_convert(images[idx]))
                plt.savefig(drawpath)
            elif self.photonum == 2:
                fig = plt.figure(figsize=(20, 12))
                columns = 2
                rows = 1
                for idx in range(columns * rows):
                    ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
                    ax.set_title(classname[str(preds[idx])], fontdict={'weight': 'normal', 'size': 50})
                    plt.imshow(self.im_convert(images[idx]))
                plt.savefig(drawpath)
            elif self.photonum == 3:
                fig = plt.figure(figsize=(20, 12))
                columns = 3
                rows = 1
                for idx in range(columns * rows):
                    ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
                    ax.set_title(classname[str(preds[idx])], fontdict={'weight': 'normal', 'size': 50})
                    plt.imshow(self.im_convert(images[idx]))
                plt.savefig(drawpath)

            elif self.photonum == 4:
                fig = plt.figure(figsize=(20, 12))
                columns = 2
                rows = 2
                for idx in range(columns * rows):
                    ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
                    ax.set_title(classname[str(preds[idx])], fontdict={'weight': 'normal', 'size': 50})
                    plt.imshow(self.im_convert(images[idx]))
                plt.savefig(drawpath)

            elif self.photonum ==5:
                fig = plt.figure(figsize=(20, 12))
                columns = 4
                rows = 2
                for idx in range(5):
                    ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
                    ax.set_title(classname[str(preds[idx])], fontdict={'weight': 'normal', 'size': 50})
                    plt.imshow(self.im_convert(images[idx]))
                plt.savefig(drawpath)

            elif self.photonum == 6:
                fig = plt.figure(figsize=(20, 12))
                columns = 3
                rows = 2
                for idx in range(columns * rows):
                    ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
                    ax.set_title(classname[str(preds[idx])], fontdict={'weight': 'normal', 'size': 50})
                    plt.imshow(self.im_convert(images[idx]))
                plt.savefig(drawpath)

            elif self.photonum == 7:
                fig = plt.figure(figsize=(20, 12))
                columns = 4
                rows = 2
                for idx in range(7):
                    ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
                    ax.set_title(classname[str(preds[idx])], fontdict={'weight': 'normal', 'size': 50})
                    plt.imshow(self.im_convert(images[idx]))
                plt.savefig(drawpath)

            else :
                fig = plt.figure(figsize=(20, 12))
                columns = 4
                rows = 2
                for idx in range(columns * rows):
                    ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
                    ax.set_title(classname[str(preds[idx])], fontdict={'weight': 'normal', 'size': 50})
                    plt.imshow(self.im_convert(images[idx]))
                plt.savefig(drawpath)


        #展示预测结果
        # fig = plt.figure(figsize=(20, 12))
        # columns = 4
        # rows = 2
        # for idx in range (columns*rows):
        #     ax = fig.add_subplot(rows, columns, idx+1, xticks=[], yticks=[])
        #     ax.set_title(foo[str(preds[idx])], fontdict={'weight':'normal','size': 50})
        #     plt.imshow(self.im_convert(images[idx]))
        # plt.savefig("E:/桌面/猫狗分类/1.jpg")
        # plt.show()

        return preds, best_acc, drawpath

    def __del__(self):

        del self


if __name__=="__main__":
    Num = 1
    class_names = { "3": "风铃草",  "1": "月见草",  "7": "蝴蝶兰",  "10": "驴欺口", "6": "卷丹",  "9": "乌头",   "4": "香豌豆", "2": "硬叶兜兰",  "5": "金盏花",   "8": "鹤望兰"}
    P = Preprocess_preddata(10, "F:\PycharmProjects\Graduation\Deeplearning\checkpoint.pth", Num, 3)
    #参数的意思分别是分类数，权重文件路径，上传了几张图片（最大为8），使用的模型
    preds, best_acc, _ = P.predictone('one\\', class_names, draw=False)
    print("修正后", preds)
    print("正确率为：{:.2%}".format(best_acc))
    if Num > 1:
        for i in preds:
            print("预测的结果分别为", class_names[str(i)])
    else:
       print("预测的结果分别为", class_names[str(preds.tolist())])

    # class_names = {'1': '狗', '2': '猫'}
    # P = Preprocess_preddata(2, "E:/桌面/猫狗分类/猫狗分类.pth", Num, 1)
    # # 参数的意思分别是分类数，权重文件路径，上传了几张图片（最大为8），使用的模型
    # preds, best_acc = P.predictone('one\\')
    # print("preds = ", preds)
    # print("正确率为：{:.2%}".format(best_acc))
    # if Num > 1:
    #     for i in preds:
    #         print("预测的结果分别为", class_names[str(i)])
    # else:
    #    print("预测的结果分别为", class_names[str(preds.tolist())])
    pass



