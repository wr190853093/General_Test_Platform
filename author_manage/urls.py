# coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^creatorg/', 'author_manage.views.creat_org'),  # 新增组织
    url(r'^deleteorg/', 'author_manage.views.delete_org'),  # 删除组织
    url(r'^editorg/', 'author_manage.views.edit_org'),  # 编辑组织
    url(r'^getorgtree/', 'author_manage.views.org_tree'),  # 获取组织机构树
    # url(r'^getorginfo/', 'author_manage.views.org_info'),  # 获取组织机构信息
    url(r'^creatuser/', 'author_manage.views.creat_user'),  # 新增员工
    url(r'^deleteuser/', 'author_manage.views.delete_user'),  # 删除员工
    url(r'^edituser/', 'author_manage.views.edit_user'),  # 编辑员工
    url(r'^enableuser/', 'author_manage.views.enable_user'),  # 启用员工
    url(r'^unenableuser/', 'author_manage.views.unenable_user'),  # 禁用员工
    url(r'^getuserlist/', 'author_manage.views.user_list'),  # 获取员工列表
    url(r'^getuserinfo/', 'author_manage.views.user_info'),  # 获取员工信息
    url(r'^editpwd/', 'author_manage.views.edit_password'),  # 修改密码
]
