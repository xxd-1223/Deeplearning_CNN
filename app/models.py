from django.db import models

# Create your models here.

class Flower(models.Model):
    f_num = models.AutoField(primary_key=True) #id
    f_name = models.CharField(max_length=16, unique=True) #名称
    f_branch = models.CharField(max_length=10, default=None) #所属科
    f_nickname = models.CharField(max_length=20, default=None) #别名
    f_latin_name = models.CharField(max_length=40, default=None) #拉丁学名
    f_description = models.CharField(max_length=1000, default=None) #描述
    f_feature = models.CharField(max_length=1000, default=None) #形态特征
    f_area = models.CharField(max_length=1000, default=None) #分布范围
    f_sire = models.CharField(max_length=1000, default=None) #繁殖方法


class Userupimage(models.Model):

    u_icon = models.ImageField(upload_to= 'valid/img/')
    #u_icon = models.ImageField(upload_to= '%Y/%m/%d/icons')
    class Meta:
        db_table = 'Userupimage'