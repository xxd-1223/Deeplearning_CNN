from django.conf.urls import url
from django.urls import path

from app import views
#
#
app_name = 'app'
urlpatterns = [

    url(r'^index/', views.index, name='index'),
    url(r'^imagefield/', views.image_field, name='image_field'),

]
'''
Django请求流程
1.到urls分发器(总路由到子路由)
2.urls分发器根据路由规则（正则）分发到views
3.views去调用Model，交互数据
4.views将数据渲染到模板中
5.模板呈现给用户
'''