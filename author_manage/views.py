# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from author_manage.models import *
from rest_framework.decorators import api_view
import json


# 新增组织机构
@api_view(['POST'])
def creat_org(request):
    name = request.POST.get('name', None)
    parent_id = request.POST.get('parentid', None)
    is_del = '1'
    data = ''
    if name:
        if parent_id:
            try:
                parent = Organization.objects.filter(id=parent_id, is_del='1')
                if parent.exists():
                    if not Organization.objects.filter(parent=parent, name=name, is_del='1').exists():
                        org = Organization(name=name, is_del=is_del, parent=parent_id)
                        org.save()
                        error_code = '0'
                        message = u'新增组织机构成功。'
                        data = org.id
                    else:
                        error_code = '10002'
                        message = u'同节点组织机构名称重复。'
                else:
                    error_code = '10003'
                    message = u'不存在父节点组织机构。'
            except Exception as e:
                print e.message
                error_code = '10099'
                message = u'数据操作异常。'
        else:
            try:
                if not Organization.objects.filter(parent__isnull=True, name=name, is_del='1').exists():
                    org = Organization(name=name, is_del=is_del)
                    org.save()
                    error_code = '0'
                    message = u'新增组织机构成功。'
                    data = org.id
                else:
                    error_code = '10002'
                    message = u'同节点组织机构名称重复。'
            except Exception as e:
                print e.message
                error_code = '10099'
                message = u'数据操作异常。'
    else:
        error_code = '10001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['GET', 'POST'])
def delete_org(request):
    org_id = request.REQUEST.get('orgid', None)
    # error_code = ''
    # message = ''
    if org_id:
        try:
            org = Organization.objects.filter(id=org_id)
            if org.exists() and org.first().is_del == 1:
                if not Organization.objects.filter(parent=org_id, is_del='1').exists():
                    org.update(is_del='0')
                    error_code = '0'
                    message = u'删除组织机构成功。'
                else:
                    error_code = '10001'
                    message = u'请先删除子节点组织机构再删除父节点组织机构。'
            else:
                error_code = '10004'
                message = u'所选组织组织机构不存在。'
        except Exception as e:
            print e.message
            error_code = '10099'
            message = u'数据操作异常。'
    else:
        error_code = '10001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_org(request):
    org_id = request.POST.get('orgid', None)
    name = request.POST.get('name', None)
    is_del = '1'
    data = ''
    if name and org_id:
        try:
            org = Organization.objects.filter(id=org_id, is_del='1')
            if org.exists():
                parent_org = org.first().parent
                if not Organization.objects.filter(name=name, parent=parent_org, is_del='1').exists():
                    org.update(name=name)
                    error_code = '0'
                    message = u'编辑组织机构成功。'
                else:
                    error_code = '10002'
                    message = u'同节点组织机构名称重复。'
            else:
                error_code = '10004'
                message = u'所选组织组织机构不存在。'
        except Exception as e:
            print e.message
            error_code = '10099'
            message = u'数据操作异常。'
    else:
        error_code = '10001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


def get_childtree(parent):
    child = Organization.objects.filter(parent=parent.id)
    for c in child:
        get_childtree(c)
    pass



@api_view(['GET', 'POST'])
def org_tree(request):
    error_code = ''
    message = ''
    data = []
    root = Organization.objects.filter(parent__isnull=True)

    # for p in root:
    #     child = Organization.objects.filter(parent=p.id)
    #     for c in child:
    #         pass
    # data = [{'parent_name': parent.name, 'parent_id': parent.id,
    #           'nodes':[{'child1_name': child1.name, 'child1_id': child1.id},
    #                  {'child2_name': child2.name, 'child2_id': child2.id, 'nodes':[...]}
    #           ]}]
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


# @api_view(['GET', 'POST'])
# def org_info(request):
#     pass


@api_view(['POST'])
def creat_user(request):
    pass


@api_view(['GET', 'POST'])
def delete_user(request):
    pass


@api_view(['POST'])
def edit_user(request):
    pass


@api_view(['GET', 'POST'])
def user_list(request):
    pass


@api_view(['GET', 'POST'])
def user_info(request):
    pass


