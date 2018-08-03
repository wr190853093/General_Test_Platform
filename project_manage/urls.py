# coding:utf-8

from django.urls import include, path
from project_manage.views import *

urlpatterns = [

    # 项目管理模块接口
    path(r'createproject/', create_project),  # 新建项目
    path(r'editproject/', edit_project),  # 编辑项目
    path(r'fileproject/', file_project),  # 归档项目
    path(r'getprojectlist/', project_list),  # 获取项目列表
    path(r'addmember/', add_member),  # 增加成员   #  批量增加
    path(r'getmemberlist/', member_list),  # 获取成员列表
    path(r'deletemember/', delete_member),  # 删除成员 # 批量删除
    # 模块管理
    path(r'createmodule/', create_module),  # 添加模块
    path(r'editmodule/', edit_module),  # 编辑模块
    path(r'deletemodule/', delete_module),  # 删除模块
    path(r'getmoduletree/', module_tree),  # 获取模块树
    # 环境管理
    path(r'createenvironment/', create_environment),  # 新增环境
    path(r'editenvironment/', edit_environment),  # 编辑环境
    path(r'deleteenvironment/', delete_environment),  # 删除环境
    path(r'enableenvironment/', enable_evnironment),  # 启用环境
    path(r'unenableenvironment/', unenable_environment),  # 禁用环境
    path(r'getenvironmentlist/', environment_list),  # 获取环境列表
    # 接口管理
    path(r'createapi/', create_api),  # 新增接口
    path(r'editapi/', edit_api),  # 编辑接口
    path(r'deleteapi/', delete_api),  # 删除接口
    path(r'getapilist/', api_list),  # 获取接口列表
    path(r'addheaderpara/', add_headerpara),  # 添加请求头参数
    path(r'deleteheaderpara/', delete_headerpara),  # 删除请求头参数
    path(r'getheaderparalist/', headerpara_list),  # 获取请求头参数列表
    path(r'addbodypara/', add_bodypara),  # 添加请求体参数
    path(r'deletebodypara/', delete_bodypara),  # 删除请求体参数
    path(r'getbodyparalist/', bodypara_list),  # 获取请求头参数列表
    path(r'addresponsepara/', add_responsepara),  # 添加响应参数
    path(r'deleteresponsepara/', delete_responsepara),  # 删除响应参数
    path(r'getresponseparalist/', responsepara_list),  # 获取请求头参数列表
]
