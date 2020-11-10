"""Graduation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path, include


#总路由


#声明views的处理函数
#view处理函数必须要求声明一个request参数，表示客户端的请求对象
#请求对象包含这些信息：请求头headers(method, path, path_info, get_full_path()



urlpatterns = [
    path('admin/', admin.site.urls),

    #配置子路由， include()导入app模块下urls.py中声明的所有子路由
    path('app/', include('app.urls')),
]
'''
Django请求流程
1.到urls分发器(总路由到子路由)
2.urls分发器根据路由规则（正则）分发到views
3.views去调用Model，交互数据
4.views将数据渲染到模板中
5.模板呈现给用户
'''