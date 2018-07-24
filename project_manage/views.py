# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from project_manage.models import *
from rest_framework.decorators import api_view
import json
from django.db.models import Q


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
            print(e.message)
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
                    project.update(name=name)
                    error_code = '0'
                    message = u'项目编辑成功。'
                else:
                    error_code = '20002'
                    message = u'项目名称重复。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print(e.message)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, }
    return JsonResponse(resp)


@api_view(['POST'])
def file_project(request):
    proj_id = request.POST.get('projectid', None)
    if proj_id:
        try:
            project = Project.objects.filter(id=proj_id)
            if project.exists():
                if project.first().status != 0:
                    project.update(status=0)
                    error_code = '0'
                    message = u'项目归档成功。'
                else:
                    error_code = '20003'
                    message = u'项目已为归档状态。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print(e.message)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, }
    return JsonResponse(resp)


@api_view(['GET'])
def project_list(request):
    name = request.GET.get('name', None)
    status = request.GET.get('status', None)
    error_code = ''
    message = ''
    data = []
    try:
        if name or status:
            projects = Project.objects.filter(Q(name__contains=name) | Q(status=status)).order_by('id')
        else:
            projects = Project.objects.all().order_by('id')
        for pro in projects:
            project = {}
            project['id'] = pro.id
            project['name'] = pro.name
            project['status'] = pro.get_status_display()
            data.append(project)
        error_code = '0'
        message = u'获取项目列表成功。'
    except Exception as e:
        print(e.message)
        error_code = '99999'
        message = u'数据操作异常。'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def add_member(request):
    members = request.POST.get('members', None)
    proj_id = request.POST.get('projectid', None)
    if proj_id:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            if project.exists():
                project = project.first()
                if members.endswith(','):
                    members = members[:-1].split(',')
                else:
                    members = members.split(',')

                users = Users.objects.filter(id__in=members, is_del=1, status=1)
                if users.exists():
                    for user in users:
                        project.team.add(user)
                    error_code = '0'
                    message = u'添加成员成功。'
                else:
                    error_code = '20004'
                    message = u'所选员工不存在。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print(e.message) 
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, }
    return JsonResponse(resp)



@api_view(['POST'])
def delete_member(request):
    # project.team.remove(users)
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
