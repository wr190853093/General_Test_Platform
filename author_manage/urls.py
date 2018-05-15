#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^getuserlist/', 'author_manage.views.user_list'),
]
