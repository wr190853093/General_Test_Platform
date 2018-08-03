# coding:utf-8

from django.conf.urls import include, url
from author_manage.views import *


urlpatterns = [
    url(r'^createorg/', create_org),  # 新增组织
    url(r'^deleteorg/', delete_org),  # 删除组织
    url(r'^getorgtree/', org_tree),  # 获取组织机构树
    # url(r'^getorginfo/', org_info),  # 获取组织机构信息
    url(r'^createuser/', create_user),  # 新增员工
    url(r'^deleteuser/', delete_user),  # 删除员工
    url(r'^edituser/', edit_user),  # 编辑员工
    url(r'^enableuser/', enable_user),  # 启用员工
    url(r'^unenableuser/', unenable_user),  # 禁用员工
    url(r'^getuserlist/', user_list),  # 获取员工列表
    url(r'^getuserinfo/', user_info),  # 获取员工信息
    url(r'^editpwd/', edit_password),  # 修改密码
]
