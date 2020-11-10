import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Deeplearning.preprocess_predata import Preprocess_preddata
from app.models import Flower, Userupimage



def index(request):
    return render(request, 'index.html')





def image_field(request):
    if request.method == "GET":
        return render(request, 'image_field.html')
    elif request.method == "POST":
        icon = request.FILES.get("icon")
        if icon is not None:
            user = Userupimage()
            user.u_icon = icon
            deletepath = "'../../static/upload/valid/img/" + user.u_icon.url
            user.save()
            # 参数的意思分别是分类数，权重文件路径，上传了几张图片（最大为8），使用的模型
            # try:
            P = Preprocess_preddata(10, "F:/PycharmProjects/Graduation/Deeplearning/checkpoint.pth", 1, 3)
            preds, best_acc, _ = P.predictone(".\\static\\upload")
            # except:
            #     return HttpResponse("无法预测")
            # else:
            #
            preds -= 1
            if preds ==0:
                preds = 1
            flower = Flower.objects.get(f_num=preds)
            print("-----------preds = ", preds)
                #参数的意思分别是分类数，权重文件路径，上传了几张图片（最大为8），使用的模型
                # try:
            os.remove(deletepath)
                # except:
                #     print("无法删除")

            return render(request,"info.html",{'name': flower.f_name, 'branch': flower.f_branch, 'nickname': flower.f_nickname,
                                           'latin_name':flower.f_latin_name, 'description':flower.f_description,
                                           'feature': flower.f_feature, 'area': flower.f_area, 'sire': flower.f_sire})
        else:
            return HttpResponse("没有图片")
    else:
        return HttpResponse("上传失败")
