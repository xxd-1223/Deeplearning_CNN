import datetime

import matplotlib.pyplot as plt
import numpy as np
import torch

#显示汉字
from torchvision import models

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

from Deeplearning.loadmodel import load
from Deeplearning.preprocess_traindata import Preprocess_traindata


cat_to_name = { "3": "风铃草",  "1": "月见草",  "7": "蝴蝶兰",  "10": "驴欺口", "6": "卷丹",  "9": "乌头",   "4": "香豌豆","2": "硬叶兜兰",  "5": "金盏花",   "8": "鹤望兰"}

class Pred_output(Preprocess_traindata):

    def __init__(self):
        self.p = Preprocess_traindata(8, "F:\\PycharmProjects\\Graduation\\Deeplearning\\flower_data")
        pass

    def get_testdata(self):

        image_datasets, dataloaders, *_ = self.p.preprocess()
        dataiter = iter(dataloaders['valid'])
        images, labels = dataiter.next()

        return images, labels


    def predict(self, images, num_classes):


        model_ft, input_size, best_acc = load.loadmodel(models.resnet50(pretrained=True), "checkpoint.pth", num_classes, feature_extract= True)

        model_ft.eval()

        train_on_gpu = False

        if train_on_gpu:
            output = model_ft(images.cuda())
        else:
            output = model_ft(images)

        _, preds_tensor = torch.max(output, 1)

        preds = np.squeeze(preds_tensor.numpy()) if not train_on_gpu else np.squeeze(preds_tensor.cpu().numpy())
        #preds 依次得到预测的结果的序号
        #preds = preds + 1  #修正值

        for index, value in enumerate(preds):
            if preds[index] == 0:
                preds[index] += 1
            # else:
            #     preds[index] += 1

        return preds, best_acc

    def show(self, images, labels, preds):
        dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        path = "image/"+ dt

        labelsx = labels.numpy().tolist()
        for index, value in enumerate(labelsx):
            if labelsx[index] == 0:
                labelsx[index] += 1

        fig = plt.figure(figsize=(20, 20))
        columns = 4
        rows = 2

        for idx in range(columns * rows):
            ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
            plt.imshow(self.p.im_convert(images[idx]))
            ax.set_title(
                "{} ({})".format(cat_to_name[str(preds[idx])], cat_to_name[str(labelsx[idx])]),
                color=("green" if cat_to_name[str(preds[idx])] == cat_to_name[str(labelsx[idx])] else "red"), fontdict={'weight': 'normal', 'size': 25})
        plt.savefig(path)
        #plt.show()
        return path


if __name__ == '__main__' :
    P = Pred_output()
    images, labels = P.get_testdata()
    print(type(labels))
    preds, best_acc = P.predict(images, 10)
    # print("labels = ", labels)
    # print("preds = ", preds)
    print("预测的概率为：{:.2%}".format(best_acc))
    for i in preds:
        print("预测的结果分别为",cat_to_name[str(i)])
    P.show(images, labels, preds)


    print('------------------------------------------------')



