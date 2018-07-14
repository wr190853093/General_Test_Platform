# coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # 项目管理模块接口
    url(r'^creatproject/', 'project_manage.views.creat_project'),  # 新建项目
    url(r'^editproject/', 'project_manage.views.edit_project'),  # 编辑项目
    url(r'^fileproject/', 'project_manage.views.file_project'),  # 归档项目
    url(r'^getprojectlist/', 'project_manage.views.project_list'),  # 获取项目列表
    url(r'^addmember/', 'project_manage.views.add_member'),  # 增加成员   #  批量增加
    url(r'^deletemember/', 'project_manage.views.delete_member'),  # 删除成员 # 批量删除
    # 模块管理
    url(r'^creatmodule/', 'project_manage.views.creat_module'),  # 添加模块
    url(r'^editmodule/', 'project_manage.views.edit_module'),  # 编辑模块
    url(r'^deletemodule/', 'project_manage.views.delete_module'),  # 删除模块
    url(r'^getmoduletree/', 'project_manage.views.module_tree'),  # 获取模块树
    # 环境管理
    url(r'^createnvironment/', 'project_manage.views.creat_environment'),  # 新增环境
    url(r'^deleteenvironment/', 'project_manage.views.delete_environment'),  # 删除环境
    url(r'^editenvironment/', 'project_manage.views.edit_environment'),  # 编辑环境
    url(r'^enableevironment/', 'project_manage.views.enable_evironment'),  # 启用环境
    url(r'^unenableevironment/', 'project_manage.views.unenable_evironment'),  # 禁用环境
    url(r'^getevironmentlist/', 'project_manage.views.evironment_list'),  # 获取环境列表
    # 接口管理

]
