
from django.urls import path
from ceshi_manage.views import *

urlpatterns = [

    # 用例管理模块接口
    path(r'createcase/', create_case),  # 新建用例
    path(r'editcase/', edit_case),  # 编辑用例
    path(r'enablecase/', enable_case),  # 启用用例
    path(r'unenablecase/', unenable_case),  # 禁用用例
    path(r'getcaselist/', case_list),  # 获取用例列表
    path(r'addstep/', add_step),  # 增加步骤
    path(r'getsteplist/', step_list),  # 获取步骤列表
    path(r'deletestep/', delete_step),  # 删除步骤
    path(r'confheaders/', conf_headers),  # 配置Header参数
    path(r'confbody/', conf_body),  # 配置body参数
    path(r'addchecks/', add_checks),  # 新增检查点
    path(r'editchecks/', edit_checks),  # 新增检查点
    path(r'deletechecks/', delete_checks),  # 删除检查点

    # 任务管理模块接口
    path(r'createtask/', create_task),  # 新建任务
    path(r'edittask/', edit_task),  # 编辑任务
    path(r'runtask/', run_task),  # 运行任务
    path(r'gettasklist/', task_list),  # 获取任务列表
    path(r'gettaskcase/', task_case),  # 获取任务用例列表
]
