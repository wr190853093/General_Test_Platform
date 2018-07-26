# coding:utf-8

from django.conf.urls import url
from project_manage.views import *

urlpatterns = [
    # 项目管理模块接口
    url(r'^creatproject/', creat_project),  # 新建项目
    url(r'^editproject/', edit_project),  # 编辑项目
    url(r'^fileproject/', file_project),  # 归档项目
    url(r'^getprojectlist/', project_list),  # 获取项目列表
    url(r'^addmember/', add_member),  # 增加成员   #  批量增加
    url(r'^getmemberlist/', member_list),  # 获取成员列表
    url(r'^deletemember/', delete_member),  # 删除成员 # 批量删除
    # 模块管理
    url(r'^creatmodule/', creat_module),  # 添加模块
    url(r'^editmodule/', edit_module),  # 编辑模块
    url(r'^deletemodule/', delete_module),  # 删除模块
    url(r'^getmoduletree/', module_tree),  # 获取模块树
    # 环境管理
    url(r'^createnvironment/', creat_environment),  # 新增环境
    url(r'^deleteenvironment/', delete_environment),  # 删除环境
    url(r'^editenvironment/', edit_environment),  # 编辑环境
    url(r'^enableevironment/', enable_evironment),  # 启用环境
    url(r'^unenableevironment/', unenable_evironment),  # 禁用环境
    url(r'^getevironmentlist/', evironment_list),  # 获取环境列表
    # 接口管理

]
