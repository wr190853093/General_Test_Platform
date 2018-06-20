# coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^creatorg/', 'author_manage.views.creat_org'),
    url(r'^deleteorg/', 'author_manage.views.delete_org'),
    url(r'^editorg/', 'author_manage.views.edit_org'),
    url(r'^getorgtree/', 'author_manage.views.org_tree'),
    # url(r'^getorginfo/', 'author_manage.views.org_info'),
    url(r'^creatuser/', 'author_manage.views.creat_user'),
    url(r'^deleteuser/', 'author_manage.views.delete_user'),
    url(r'^edituser/', 'author_manage.views.edit_user'),
    url(r'^getuserlist/', 'author_manage.views.user_list'),
    url(r'^getuserinfo/', 'author_manage.views.user_info'),
    url(r'^editpwd/', 'author_manage.views.edit_password'),
]
