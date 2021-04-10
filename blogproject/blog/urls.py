#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2021/4/8 14:07
# @Author    :Willbur

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'   #视图函数命名空间，告诉django这个urls.py是属于哪个应用的
urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<int:pk>/',views.detail,name='detail'),
    path('archives/<int:year>/<int:month>/',views.archive,name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]