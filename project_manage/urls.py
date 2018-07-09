# coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # 项目管理模块接口
    url(r'^creatproject/', 'project_manage.views.'),  # 新建项目
    url(r'^editproject/', 'project_manage.views.'),  # 编辑项目
    url(r'^fileproject/', 'project_manage.views.'),  # 归档项目
    url(r'^getprojectlist/', 'project_manage.views.'),  # 获取项目列表
    url(r'^addmember/', 'project_manage.views.'),  # 增加成员   #  批量增加
    url(r'^deletemember/', 'project_manage.views.'),  # 删除成员 # 批量删除
    # 模块管理
    url(r'^creatmodule/', 'project_manage.views.'),  # 添加模块
    url(r'^editmodule/', 'project_manage.views.'),  # 编辑模块
    url(r'^deletemodule/', 'project_manage.views.'),  # 删除模块
    url(r'^getmoduletree/', 'project_manage.views.'),  # 获取模块树
    # 环境管理
    url(r'^createnvironment/', 'project_manage.views.'),  # 新增环境
    url(r'^deleteenvironment/', 'project_manage.views.'),  # 删除环境
    url(r'^editenvironment/', 'project_manage.views.'),  # 编辑环境
    url(r'^enableevironment/', 'project_manage.views.'),  # 启用环境
    url(r'^unenableevironment/', 'project_manage.views.'),  # 禁用环境
    url(r'^getevironmentlist/', 'project_manage.views.'),  # 获取环境列表
    # 接口管理

]
