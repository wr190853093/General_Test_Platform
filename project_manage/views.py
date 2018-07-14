# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from project_manage.models import *
from rest_framework.decorators import api_view
import json


# Create your views here.

@api_view(['POST'])
def creat_project(request):
    name = request.POST.get('name', None)
    data = ''
    if name:
        try:
            if not Project.objects.filter(name=name).exists():
                project = Project(name=name)
                project.save()
                error_code = '0'
                message = u'新增组织机构成功。'
                data = project.id
            else:
                error_code = '20002'
                message = u'项目名称重复。'
        except Exception as e:
            print e.message
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'project_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_project(request):
    proj_id = request.POST.get('projectid', None)
    name = request.POST.get('name', None)
    if name and proj_id:
        try:
            project = Project.objects.filter(id=proj_id)
            if project.exists():
                if not Project.objects.exclude(id=proj_id).filter(name=name).exists():
                    project.name = name
                    project.save()
                    error_code = '0'
                    message = u'新增组织机构成功。'
                else:
                    error_code = '20002'
                    message = u'项目名称重复。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print e.message
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message,}
    return JsonResponse(resp)


@api_view(['POST'])
def file_project(request):
    proj_id = request.POST.get('projectid', None)
    if proj_id:
        try:
            project = Project.objects.filter(id=proj_id)
            if project.exists():
                if project.first().status != '0':
                    project.update(status='0')
                    error_code = '0'
                    message = u'项目归档成功。'
                else:
                    error_code = '20003'
                    message = u'项目已为归档状态。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print e.message
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, }
    return JsonResponse(resp)


@api_view(['GET'])
def project_list(request):
    pass


@api_view(['POST'])
def add_member(request):
    pass


@api_view(['POST'])
def delete_member(request):
    pass


@api_view(['POST'])
def creat_module(request):
    pass


@api_view(['POST'])
def edit_module(request):
    pass


@api_view(['POST'])
def delete_module(request):
    pass


@api_view(['GET'])
def module_tree(request):
    pass


@api_view(['POST'])
def creat_environment(request):
    pass


@api_view(['POST'])
def delete_environment(request):
    pass


@api_view(['POST'])
def edit_environment(request):
    pass


@api_view(['POST'])
def enable_evironment(request):
    pass


@api_view(['POST'])
def unenable_evironment(request):
    pass


@api_view(['GET'])
def evironment_list(request):
    pass
