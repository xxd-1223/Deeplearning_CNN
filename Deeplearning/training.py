import copy
import time

import matplotlib.pyplot as plt
import torch
import torch.optim as optim
from torch import nn

from Deeplearning import feature_extract
from Deeplearning.loadmodel import load



class Train():

    # 用户可以自定义：权重文件，resnet模型的层数，预训练的数据，分类数量
    def __init__(self, train_on_gpu, model_ft, dataloaders, num_classes, filename, device):

        self.train_on_gpu = train_on_gpu #是否使用GPU加速
        self.model_ft = model_ft         #迁移学习的模型
        self.dataloaders = dataloaders   #进行数据增强后的数据集
        self.num_classes = num_classes   #分类数量
        self.filename = filename         #权重文件的路径
        self.device = device             #使用的设备 CPU/GPU




    def setlayer(self):

        model_ft, input_size = load.initialize_model(self.model_ft, self.num_classes, feature_extract)  # use_pretrained使用预训练模型


        # GPU计算
        model_ft = model_ft.to(self.device)

        # 是否训练所有层
        params_to_update = model_ft.parameters()
        print("Params to learn:")
        if feature_extract:
            params_to_update = []
            for name, param in model_ft.named_parameters():
                if param.requires_grad == True:
                    params_to_update.append(param)
                    print("\t", name)
        else:
            for name, param in model_ft.named_parameters():
                if param.requires_grad == True:
                    print("\t", name)
        self.params_to_update =params_to_update
        return params_to_update, model_ft


    def setOptimizer(self, lr):

        params_to_update, model_ft = self.setlayer()  #设置层

        optimizer_ft = optim.Adam(params_to_update, lr)
        scheduler = optim.lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)  # 学习率每7个epoch衰减成原来的1/10
        # 最后一层已经LogSoftmax()了，所以不能nn.CrossEntropyLoss()来计算了，nn.CrossEntropyLoss()相当于logSoftmax()和nn.NLLLoss()整合
        criterion = nn.NLLLoss()

        return scheduler, criterion, optimizer_ft, params_to_update, model_ft


    #进行训练
    def train_model(self, num_epochs, scheduler, criterion, optimizer, model, is_inception=False):
        since = time.time()
        best_acc = 0

        #scheduler, criterion, optimizer, params_to_update, model = self.setOptimizer(1e-2)

        val_acc_history = []
        train_acc_history = []
        train_losses = []
        valid_losses = []
        LRs = [optimizer.param_groups[0]['lr']]

        best_model_wts = copy.deepcopy(model.state_dict())

        for epoch in range(num_epochs):
            print('Epoch {}/{}'.format(epoch, num_epochs - 1))
            print('-' * 10)

            # 训练和验证
            for phase in ['train', 'valid']:
                if phase == 'train':
                    model.train()  # 训练
                else:
                    model.eval()  # 验证

                running_loss = 0.0
                running_corrects = 0

                # 把数据都取个遍
                for inputs, labels in self.dataloaders[phase]:
                    inputs = inputs.to(self.device)
                    labels = labels.to(self.device)

                    # 清零
                    optimizer.zero_grad()
                    # 只有训练的时候计算和更新梯度
                    with torch.set_grad_enabled(phase == 'train'):
                        if is_inception and phase == 'train':
                            outputs, aux_outputs = model(inputs)
                            loss1 = criterion(outputs, labels)
                            loss2 = criterion(aux_outputs, labels)
                            loss = loss1 + 0.4 * loss2
                        else:  # resnet执行的是这里
                            outputs = model(inputs)
                            loss = criterion(outputs, labels)

                        _, preds = torch.max(outputs, 1)

                        # 训练阶段更新权重
                        if phase == 'train':
                            loss.backward()
                            optimizer.step()

                    # 计算损失
                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)

                epoch_loss = running_loss / len(self.dataloaders[phase].dataset)
                epoch_acc = running_corrects.double() / len(self.dataloaders[phase].dataset)

                time_elapsed = time.time() - since
                print('Time elapsed {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
                print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

                # 得到最好那次的模型
                if phase == 'valid' and epoch_acc > best_acc:
                    best_acc = epoch_acc
                    best_model_wts = copy.deepcopy(model.state_dict())
                    state = {
                        'state_dict': model.state_dict(),
                        'best_acc': best_acc,
                        'optimizer': optimizer.state_dict(),
                    }
                    torch.save(state, self.filename)
                if phase == 'valid':
                    val_acc_history.append(epoch_acc)
                    valid_losses.append(epoch_loss)
                    scheduler.step(epoch_loss)
                if phase == 'train':
                    train_acc_history.append(epoch_acc)
                    train_losses.append(epoch_loss)

            print('Optimizer learning rate : {:.7f}'.format(optimizer.param_groups[0]['lr']))
            LRs.append(optimizer.param_groups[0]['lr'])
            print()

        time_elapsed = time.time() - since
        print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
        print('Best val Acc: {:4f}'.format(best_acc))

        # 训练完后用最好的一次当做模型最终的结果
        model.load_state_dict(best_model_wts)
        return model, val_acc_history, train_acc_history, valid_losses, train_losses, LRs




        checkpoint = torch.load(self.filename)
        best_acc = checkpoint['best_acc']
        model_ft2.load_state_dict(checkpoint['state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer'])



        return model_ft2, val_acc_history, train_acc_history, valid_losses, train_losses, LRs


    def draw(self, train_losses, valid_losses):
        # 画折线图
        plt.plot(train_losses, label='train loss')
        plt.plot(valid_losses, label='valid loss')
        plt.legend()

if __name__ == '__main__':
    #train_on_gpu, model_ft, dataloaders, num_classes, filename
    # T = Train(train_on_gpu, model_ft, dataloaders, num_classes, filename, device)
    #
    # # 第一次训练
    # scheduler, criterion, optimizer_ft, params_to_update, model_ft = T.setOptimizer(1e-2)
    #
    # model, val_acc_history, train_acc_history, valid_losses, train_losses, LRs = T.train_model(20, scheduler, criterion, optimizer_ft, model_ft)
    # T.draw(train_losses, valid_losses)
    pass


    # #第二次训练
    # scheduler, criterion, optimizer, params_to_update, *_ = T.setOptimizer(1e-4)
    #
    # model, val_acc_history, train_acc_history, valid_losses2, train_losses2, LRs = T.train_model_again(model, 10, scheduler, criterion, optimizer)
    # T.draw(train_losses2, valid_losses2)
