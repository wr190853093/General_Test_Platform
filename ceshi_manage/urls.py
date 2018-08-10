
from django.urls import path
from ceshi_manage.views import *

urlpatterns = [

    # 用例管理模块接口
    path(r'createcase/', create_case),  # 新建项目
    path(r'editcase/', edit_case),  # 编辑项目
    path(r'enablecase/', enable_case),  # 启用环境
    path(r'unenablecase/', unenable_case),  # 禁用环境
    path(r'getcaselist/', case_list),  # 获取项目列表
    path(r'addstep/', add_step),  # 增加成员   #  批量增加
    path(r'getsteplist/', step_list),  # 获取成员列表
    path(r'deletestep/', delete_step),  # 删除成员
    path(r'confheaders/', conf_headers),  # 配置Header参数
    path(r'confbody/', conf_body),  # 配置body参数
    path(r'addchecks/', add_checks),  # 新增检查点
    path(r'editchecks/', edit_checks),  # 新增检查点
    path(r'deletechecks/', delete_checks),  # 删除检查点

]
