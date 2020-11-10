import torch
from torch import nn
from torchvision import models



from Deeplearning import model_name


class Loadmodel:

    def __init__(self):
        pass
    #设置是否改变Resnet神经网络模型的其他层
    def __set_parameter_requires_grad(self, model, feature_extract):  # 保留除最后一层以外其他层的weights不变
        if feature_extract:
            for param in model.parameters():
                param.requires_grad = False

    # 初始化模型
    def initialize_model(self, modelnum, num_classes, feature_extract):
        # 选择合适的模型，不同模型的初始化方法稍微有点区别
        input_size = 0

        if model_name == "resnet":
            """ Resnet152
            """
            model_ft = modelnum #models.resnet18(pretrained = True)
            #print("web:", model_ft)
            self.__set_parameter_requires_grad(model_ft, feature_extract)
            num_ftrs = model_ft.fc.in_features
            model_ft.fc = nn.Sequential(nn.Linear(num_ftrs, num_classes),
                                        nn.LogSoftmax(dim = 1))
            input_size = 224

            #print("layer层模型为：", model_ft)
        else:
            print("Invalid model name, exiting...")
            exit()

        return model_ft, input_size

    def loadmodel(self,modelX, weightpath, num_classes, feature_extract):#分类数10，使用训练好的权重True

        model_ft, input_size = self.initialize_model(modelX, num_classes, feature_extract)

        checkpoint = torch.load(weightpath)

        best_acc = checkpoint['best_acc']

        model_ft.load_state_dict(checkpoint['state_dict'])

        return model_ft, input_size, best_acc



load = Loadmodel()


if __name__ == '__main__' :
    pass

