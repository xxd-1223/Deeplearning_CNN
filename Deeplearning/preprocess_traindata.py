import json
import os
import matplotlib.pyplot as plt
import numpy as np
import torch
from torchvision import transforms, datasets

from Deeplearning import batch_size

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#读取训练数据和测试数据


class Preprocess_traindata():
    #获取数据路径
    data_dir = 'flower_data/'  #../../

    test_dir = 'E:/桌面/data'

    def __init__(self, batch_size, datapath):

        self.batch_size = batch_size
        self.datapath = datapath

    #对数据的增强方法
    def __data_enhancement(self):
        '''数据增强方法'''
        data_transforms = {
            'train': transforms.Compose([transforms.RandomRotation(45),  # 随机旋转，-45到45度之间随机选
                                         transforms.CenterCrop(224),  # 从中心开始裁剪
                                         transforms.RandomHorizontalFlip(p=0.5),  # 随机水平翻转 选择一个概率概率
                                         transforms.RandomVerticalFlip(p=0.5),  # 随机垂直翻转
                                         transforms.ColorJitter(brightness=0.2, contrast=0.1, saturation=0.1, hue=0.1),
                                         # 参数1为亮度，参数2为对比度，参数3为饱和度，参数4为色相
                                         transforms.RandomGrayscale(p=0.025),  # 概率转换成灰度率，3通道就是R=G=B
                                         transforms.ToTensor(),
                                         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # 均值，标准差
                                         ]),
            'valid': transforms.Compose([transforms.Resize(256),
                                         transforms.CenterCrop(224),
                                         transforms.ToTensor(),
                                         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                         ]),
        }
        return data_transforms


    def preprocess(self):
        '''数据预处理方法'''
        data_transforms = self.__data_enhancement()
        image_datasets = {x: datasets.ImageFolder(os.path.join(self.datapath, x), data_transforms[x]) for x in
                              ['train', 'valid']}
        dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], 8, shuffle=True) for x
                           in ['train', 'valid']}
        dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'valid']}
        class_names = image_datasets['train'].classes

        print("数据集图片数量为： ", dataset_sizes)

        return image_datasets, dataloaders, dataset_sizes, class_names


    def im_convert(self, tensor):
        """ 展示数据"""
        image = tensor.to("cpu").clone().detach()
        image = image.numpy().squeeze()
        image = image.transpose(1, 2, 0)
        image = image * np.array((0.229, 0.224, 0.225)) + np.array((0.485, 0.456, 0.406))
        image = image.clip(0, 1)

        return image
    #展示预处理后的图片
    def show_data(self, classnamefilepath):
        fig=plt.figure(figsize=(20, 12))
        columns = 4
        rows = 2
        image_datasets, dataloaders, dataset_sizes, class_names = self.preprocess()#用到了解包
        dataiter = iter(dataloaders['valid'])
        inputs, classes = dataiter.next()

        #F:/PycharmProjects/Graduation/Deeplearning/cat_to_name.json
        with open(classnamefilepath, 'r') as f:
            cat_to_name = json.load(f)
            print("cat_to_name = ", cat_to_name)
        for idx in range (columns*rows):
            ax = fig.add_subplot(rows, columns, idx+1, xticks=[], yticks=[])
            ax.set_title(cat_to_name[str(int(class_names[classes[idx]]))])
            plt.imshow(self.im_convert(inputs[idx]))
        plt.show()
        return cat_to_name, class_names, dataloaders
    #给子类提供一个接口
    def port(self):

        return self.preprocess()



#Pre = Preprocess_traindata(batch_size, "E:/桌面/data")
#cat_to_name, class_names, dataloaders = Pre.show_data()

# print("cat_to_name = ", cat_to_name)
if __name__ == '__main__' :
    # P = Preprocess_traindata(batch_size)
    # cat_to_name, class_names, _ = P.show_data()
    # Pre = Preprocess_traindata(batch_size, "./flower_data")
    # cat_to_name, class_names, dataloaders = Pre.show_data("F:\PycharmProjects\Graduation\Deeplearning\cat_to_name.json")
    Pre = Preprocess_traindata(batch_size, "E:\桌面\data")
    cat_to_name, class_names, dataloaders = Pre.show_data("E:\桌面\猫狗分类\\猫狗分类.json")
    pass
