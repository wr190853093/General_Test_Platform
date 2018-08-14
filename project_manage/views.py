"""
error_code = '20001'  message = u'所选项目不存在。'
error_code = '20002'  message = u'项目名称重复。'
error_code = '20003'  message = u'项目已为归档状态。'
error_code = '20004'  message = u'所选员工不存在。'
error_code = '20005'  message = u'所选项目没有成员。'
error_code = '20006'  message = u'所选员工不存在或不在此项目中。'
error_code = '20007'  message = u'请先删除子节点模块再删除父节点模块。'
error_code = '20008'  message = u'所选模块不存在。'
error_code = '20009'  message = u'同节点模块名称重复。'
error_code = '20010'  message = u'不存在父节点模块。'
error_code = '20011'  message = u'所选环境已为禁用状态。'
error_code = '20012'  message = u'所选环境不存在。'
error_code = '20013'  message = u'所选环境已为启用状态。'
error_code = '20014'  message = u'路径格式错误。'
error_code = '20015'  message = u'API方法错误。'
error_code = '20016'  message = u'API已经存在。'
error_code = '20017'  message = u'所选接口不存在。'
error_code = '20018'  message = u'所选response parameter不存在。'
error_code = '20020'  message = u'所选response parameter不存在。'
error_code = '20019'  message = u'所选body parameter不存在。'
"""
from django.http import JsonResponse
from project_manage.models import *
from rest_framework.decorators import api_view
# from django.db.models import Q
from common.util import *


@api_view(['POST'])
def create_project(request):
    """
        POST请求，新增项目
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """
    name = request.POST.get('name', None)
    data = ''
    if name:
        try:
            if not Project.objects.filter(name=name).exists():
                project = Project(name=name)
                project.save()
                error_code = '0'
                message = u'新增项目成功。'
                data = project.id
            else:
                error_code = '20002'
                message = u'项目名称重复。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'project_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_project(request):
    """
        POST请求，编辑项目
        :param request: projectid，name，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20001'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """
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
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, }
    return JsonResponse(resp)


@api_view(['POST'])
def file_project(request):
    """
        POST请求，归档项目
        :param request: projectid，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20001'
                 error_code = '20003'
                 error_code = '99999'
                 error_code = '90001'
    """
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
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, }
    return JsonResponse(resp)


@api_view(['GET'])
def project_list(request):
    """
        GET请求，获取项目列表
        :param request: name，status
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
                 error_code = '0'
                 error_code = '99999'
                 error_code = '90001'
    """
    name = request.GET.get('name', None)
    status = request.GET.get('status', None)
    # error_code = ''
    # message = ''
    data = []
    try:
        searchcondition = {'name__contains': name, 'status': status}
        kwargs = getkwargs(searchcondition)
        projects = Project.objects.filter(**kwargs).order_by('id')
        for pro in projects:
            project = dict()
            project['id'] = pro.id
            project['name'] = pro.name
            project['status'] = pro.get_status_display()
            data.append(project)
        error_code = '0'
        message = u'获取项目列表成功。'
    except Exception as e:
        print(e)
        error_code = '99999'
        message = u'数据操作异常。'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def add_member(request):
    """
        POST请求，新增成员
        :param request: members，projectid
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20001'
                 error_code = '20004'
                 error_code = '99999'
                 error_code = '90001'
    """
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
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, }
    return JsonResponse(resp)


@api_view(['GET'])
def member_list(request):
    """
        GET请求，获取成员列表
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
                 error_code = '0'
                 error_code = '20001'
                 error_code = '20005'
                 error_code = '99999'
                 error_code = '90001'
    """
    proj_id = request.GET.get('projectid', None)
    data = []
    if proj_id:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            if project.exists():
                project = project.first()
                users = project.team
                if users.exists():

                    for user in users.all():
                        member = {}
                        member_id = user.id
                        name = user.name
                        role = user.get_role_display()
                        member['name'] = name
                        member['role'] = role
                        member['id'] = member_id
                        data.append(member)
                    error_code = '0'
                    message = u'获取成员成功。'
                else:
                    error_code = '20005'
                    message = u'所选项目没有成员。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_member(request):
    """
        GET请求，删除成员
        :param request: membersid，projectid
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20006'
                 error_code = '99999'
                 error_code = '90001'
    """
    members_id = request.POST.get('membersid', None)
    proj_id = request.POST.get('projectid', None)

    if members_id and proj_id:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            if project.exists():
                project = project.first()

                if members_id.endswith(','):
                    members_id = members_id[:-1].split(',')
                else:
                    members_id = members_id.split(',')

                members = Users.objects.filter(id__in=members_id, is_del=1, status=1)

                if members.exists() and set(members).issubset(set(project.team.all())):
                    for member in members:
                        project.team.remove(member)
                    else:
                        error_code = '0'
                        message = u'删除员工成功。'
                else:
                    error_code = '20006'
                    message = u'所选员工不存在或不在此项目中。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def create_module(request):
    """
        POST请求，新增模块
        :param request: name，parentid，projectid
        :return: resp = {'error_code': error_code, 'message': message, 'module_id': data}
                 error_code = '0'
                 error_code = '20009'
                 error_code = '20010'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.POST.get('name', None)
    parent_id = request.POST.get('parentid', None)
    proj_id = request.POST.get('projectid', None)
    data = ''

    if name and proj_id:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            if project.exists():
                if parent_id:
                    try:
                        parent = Module.objects.filter(id=parent_id)

                        if parent.exists():
                            if not Module.objects.filter(parent=parent.first(), name=name).exists():
                                module = Module(name=name, parent=parent.first(), project=project.first())
                                module.save()
                                error_code = '0'
                                message = u'新增模块成功。'
                                data = module.id
                            else:
                                error_code = '20009'
                                message = u'同节点模块名称重复。'
                        else:
                            error_code = '20010'
                            message = u'不存在父节点模块。'
                    except Exception as e:
                        print(e)
                        error_code = '99999'
                        message = u'数据操作异常。'
                else:
                    try:
                        if not Module.objects.filter(parent__isnull=True, name=name, is_del=1).exists():
                            module = Module(name=name, project=project.first())
                            module.save()
                            error_code = '0'
                            message = u'新增模块成功。'
                            data = module.id
                        else:
                            error_code = '20009'
                            message = u'同节点模块名称重复。'
                    except Exception as e:
                        print(e)
                        error_code = '99999'
                        message = u'数据操作异常。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'module_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_module(request):
    """
        POST请求，编辑模块
        :param request: moduleid，name，
        :return: resp = {'error_code': error_code, 'message': message,}
                 error_code = '0'
                 error_code = '20009'
                 error_code = '20008'
                 error_code = '99999'
                 error_code = '90001'
    """

    module_id = request.POST.get('moduleid', None)
    name = request.POST.get('name', None)
    # is_del = '1'
    # data = ''
    if name and module_id:
        try:
            module = Module.objects.filter(id=module_id, is_del=1)
            if module.exists():
                parent_module = module.first().parent
                if not Module.objects.exclude(id=module_id).filter(name=name, parent=parent_module, is_del=1).exists():
                    module.update(name=name)
                    error_code = '0'
                    message = u'编辑模块成功。'
                else:
                    error_code = '20009'
                    message = u'同节点模块名称重复。'
            else:
                error_code = '20008'
                message = u'所选模块不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_module(request):
    """
        POST请求，删除模块
        :param request: moduleid，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20007'
                 error_code = '20008'
                 error_code = '99999'
                 error_code = '90001'
    """

    module_id = request.POST.get('moduleid', None)
    # error_code = ''
    # message = ''
    if module_id:
        try:
            module = Module.objects.filter(id=module_id)
            if module.exists() and module.first().is_del == 1:
                if not Module.objects.filter(parent=module_id, is_del=1).exists():
                    module.update(is_del='0')
                    error_code = '0'
                    message = u'删除模块成功。'
                else:
                    error_code = '20007'
                    message = u'请先删除子节点模块再删除父节点模块。'
            else:
                error_code = '20008'
                message = u'所选模块不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def module_tree(request):
    """
        GET请求，获取模块树
        :param request:
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
                 error_code = '0'
                 error_code = '99999'
                 error_code = '90001'
    """

    proj_id = request.GET.get('projectid', None)
    data = []
    error_code = ''
    message = ''
    if proj_id:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            if project.exists():
                root = Module.objects.filter(parent__isnull=True, is_del=1, project=project.first())
            else:
                root = Module.objects.filter(parent__isnull=True, is_del=1)
            for r in root:
                module = get_child(r, result={}, data={}, node=[])
                data.append(module)
            error_code = '0'
            message = u'获取模块树成功。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def create_environment(request):
    """
        POST请求，新增环境
        :param request: name，host，projectid，type
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
                 error_code = '0'
                 error_code = '20001'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.POST.get('name', None)
    host = request.POST.get('host', None)
    proj_id = request.POST.get('projectid', None)
    env_type = request.POST.get('type', None)
    data = ''
    if name and host and proj_id and env_type:
        try:
            if validate_ip(host) and int(env_type) in (0, 1, 2, 3):
                project = Project.objects.filter(id=proj_id, status=1)
                if project.exists():
                    environment = Environment(name=name, host=host, type=env_type, project=project.first())
                    environment.save()
                    error_code = '0'
                    message = u'新增环境成功。'
                    data = environment.id

                else:
                    error_code = '20001'
                    message = u'所选项目不存在。'
            else:
                error_code = '99999'
                message = u'数据操作异常。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_environment(request):
    """
        POST请求，编辑环境
        :param request: environmentid，name，host，projectid，type
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20001'
                 error_code = '20012'
                 error_code = '99999'
                 error_code = '90001'
    """

    envi_id = request.POST.get('environmentid', None)
    name = request.POST.get('name', None)
    host = request.POST.get('host', None)
    proj_id = request.POST.get('projectid', None)
    env_type = request.POST.get('type', None)
    if envi_id and name and host and proj_id and env_type:
        try:
            environment = Environment.objects.filter(id=envi_id, is_del=1)
            if environment.exists():
                if validate_ip(host) and int(env_type) in (0, 1, 2, 3):
                    project = Project.objects.filter(id=proj_id, status=1)
                    if project.exists():
                        environment.update(name=name, host=host, type=env_type, project=project.first())
                        error_code = '0'
                        message = u'编辑环境成功。'
                    else:
                        error_code = '20001'
                        message = u'所选项目不存在。'
                else:
                    error_code = '99999'
                    message = u'数据操作异常。'
            else:
                error_code = '20012'
                message = u'所选环境不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_environment(request):
    """
        POST请求，删除环境
        :param request: environmentid，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20012'
                 error_code = '99999'
                 error_code = '90001'
    """

    envi_id = request.POST.get('environmentid', None)
    if envi_id:
        try:
            environment = Environment.objects.filter(id=envi_id, is_del=1)
            if environment.exists():
                environment.update(is_del='0')
                error_code = '0'
                message = u'删除环境成功。'
            else:
                error_code = '20012'
                message = u'所选环境不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def enable_evnironment(request):
    """
        POST请求，启用环境
        :param request: environmentid，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20012'
                 error_code = '20013'
                 error_code = '99999'
                 error_code = '90001'
    """

    envi_id = request.POST.get('environmentid', None)
    if envi_id:
        try:
            environment = Environment.objects.filter(id=envi_id, is_del=1)
            if environment.exists():
                if environment.first().status == 0:
                    environment.update(status=1)
                    error_code = '0'
                    message = u'修改环境状态成功。'
                else:
                    error_code = '20013'
                    message = u'所选环境已为启用状态。'
            else:
                error_code = '20012'
                message = u'所选环境不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def unenable_environment(request):
    """
        POST请求，禁用环境
        :param request: environmentid，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20012'
                 error_code = '20011'
                 error_code = '99999'
                 error_code = '90001'
    """

    envi_id = request.POST.get('environmentid', None)
    if envi_id:
        try:
            environment = Environment.objects.filter(id=envi_id, is_del=1)
            if environment.exists():
                if environment.first().status == 1:
                    environment.update(status=0)
                    error_code = '0'
                    message = u'修改环境状态成功。'
                else:
                    error_code = '20011'
                    message = u'所选环境已为禁用状态。'
            else:
                error_code = '20012'
                message = u'所选环境不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def environment_list(request):
    """
        GET请求，获取环境列表
        :param request: name，host，projectid，type，status
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
                 error_code = '0'
                 error_code = '20001'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.GET.get('name', None)
    host = request.GET.get('host', None)
    proj_id = request.GET.get('projectid', None)
    env_type = request.GET.get('type', None)
    status = request.GET.get('status', None)

    data = []
    if proj_id:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            if project.exists():
                project = project.first()

                searchcondition = {'name__contains': name, 'host__contains': host,
                                   'project': project, 'type': env_type,
                                   'status': status}
                kwargs = getkwargs(searchcondition)
                evironments = Environment.objects.filter(**kwargs).order_by('id')
                for env in evironments:
                    evironments = dict()
                    evironments['id'] = env.id
                    evironments['name'] = env.name
                    evironments['host'] = env.host
                    evironments['project'] = {'projectName': env.project.name, 'projectId': env.project.id}
                    evironments['status'] = env.get_status_display()
                    evironments['env_type'] = env.get_type_display()

                    data.append(evironments)
                error_code = '0'
                message = u'获取环境列表成功。'

            else:
                error_code = '20001'
                message = u'所选项目不存在。'

        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def create_api(request):
    """
        POST请求，新增API
        :param request: name，desc，path，method，projectid，moduleid
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20008'
                 error_code = '20008'
                 error_code = '20014'
                 error_code = '20015'
                 error_code = '20016'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.POST.get('name', None)
    desc = request.POST.get('desc', None)
    path = request.POST.get('path', None)
    method = request.POST.get('method', None)
    proj_id = request.POST.get('projectid', None)
    module_id = request.POST.get('moduleid', None)
    data = ''

    if name and proj_id and path and method and module_id:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            if project.exists():
                module = Module.objects.filter(id=module_id, is_del=1)
                if module.exists():
                    if path.endswith('/') and path.startswith('/'):
                        if method in ('GET', 'POST'):
                            if method == 'GET':
                                method = 0
                            else:
                                method = 1
                            if not Api.objects.filter(project=project.first(), is_del=1, path=path).exists():
                                api = Api(name=name, desc=desc, project=project.first(), module=module.first(),
                                          path=path, method=method)
                                api.save()
                                error_code = '0'
                                message = u'新增API成功。'
                                data = api.id
                            else:
                                error_code = '20016'
                                message = u'API已经存在。'
                        else:
                            error_code = '20015'
                            message = u'API方法错误。'
                    else:
                        error_code = '20014'
                        message = u'路径格式错误。'

                else:
                    error_code = '20008'
                    message = u'所选模块不存在。'
            else:
                error_code = '20001'
                message = u'所选项目不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'api_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_api(request):
    """
        POST请求，编辑API
        :param request: apiid,name，desc，path，method，projectid，moduleid，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20008'
                 error_code = '20014'
                 error_code = '20015'
                 error_code = '20016'
                 error_code = '20017'
                 error_code = '99999'
                 error_code = '90001'
    """

    api_id = request.POST.get('apiid', None)
    name = request.POST.get('name', None)
    desc = request.POST.get('desc', None)
    path = request.POST.get('path', None)
    method = request.POST.get('method', None)
    proj_id = request.POST.get('projectid', None)
    module_id = request.POST.get('moduleid', None)

    if api_id and name and proj_id and path and method and module_id:
        try:
            api = Api.objects.filter(id=api_id, is_del=1)
            if api.exists():
                project = Project.objects.filter(id=proj_id, status=1)
                if project.exists():
                    module = Module.objects.filter(id=module_id, is_del=1)
                    if module.exists():
                        if path.endswith('/') and path.startswith('/'):
                            if method in ('GET', 'POST'):
                                if method == 'GET':
                                    method = 0
                                else:
                                    method = 1
                                if not Api.objects.filter(project=project.first(), is_del=1, path=path).exclude(
                                        id=api_id).exists():
                                    api.update(name=name, desc=desc, project=project.first(), module=module.first(),
                                               path=path, method=method)
                                    error_code = '0'
                                    message = u'编辑API成功。'
                                else:
                                    error_code = '20016'
                                    message = u'API已经存在。'
                            else:
                                error_code = '20015'
                                message = u'API方法错误。'
                        else:
                            error_code = '20014'
                            message = u'路径格式错误。'
                    else:
                        error_code = '20008'
                        message = u'所选模块不存在。'
                else:
                    error_code = '20001'
                    message = u'所选项目不存在。'
            else:
                error_code = '20017'
                message = u'所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_api(request):
    """
        POST请求，删除API
        :param request: apiid，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '20017'
                 error_code = '99999'
                 error_code = '90001'
    """

    api_id = request.POST.get('apiid', None)
    if api_id:
        try:
            api = Api.objects.filter(id=api_id, is_del=1)
            if api.exists():
                api.update(is_del='0')
                error_code = '0'
                message = u'删除API成功。'
            else:
                error_code = '20017'
                message = u'所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def api_list(request):
    """
        GET请求，获取API列表
        :param request: name，moduleid,projectid
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '99999'
    """

    name = request.GET.get('name', None)
    module_id = request.GET.get('moduleid', None)
    proj_id = request.GET.get('projectid', None)
    data = []

    try:
        project = module = None
        if proj_id:
            project = Project.objects.filter(id=proj_id, status=1)
        if module_id:
            module = Module.objects.filter(id=module_id, is_del=1)

        searchcondition = {'name__contains': name, 'module__in': module, 'project__in': project}
        kwargs = getkwargs(searchcondition)
        apis = Api.objects.filter(**kwargs).order_by('id')
        for i in apis:
            api = dict()
            api['id'] = i.id
            api['name'] = i.name
            api['path'] = i.path
            api['project'] = {'projectName': i.project.name, 'projectId': i.project.id}
            api['method'] = i.method
            api['desc'] = i.desc
            api['module'] = {'moduleName': i.module.name, 'moduleId': i.module.id}

            data.append(api)
        error_code = '0'
        message = u'获取环境列表成功。'

    except Exception as e:
        print(e)
        error_code = '99999'
        message = u'数据操作异常。'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def add_headerpara(request):
    """
        POST请求，新增head parameter
        :param request: apiid，key，desc，isnull，datatype
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20017'
                 error_code = '99999'
                 error_code = '90001'
    """
    api_id = request.POST.get('apiid', None)
    key = request.POST.get('key', None)
    desc = request.POST.get('desc', None)
    is_null = request.POST.get('isnull', None)
    data_type = request.POST.get('datatype', None)

    if api_id and key and desc and is_null and data_type:
        try:
            api = Api.objects.filter(id=api_id, is_del=1)
            if api.exists():
                api = api.first()
                if int(data_type) in (0, 1, 2, 3, 4) and int(is_null) in (0, 1):
                    para = Parameter(key=key, desc=desc, is_null=is_null, data_type=data_type)
                    para.save()
                    headpara = HeaderPara(api=api, para=para)
                    headpara.save()
                    error_code = '0'
                    message = u'添加head parameter成功。'
                else:
                    error_code = '99999'
                    message = u'数据操作异常。'
            else:
                error_code = '20017'
                message = u'所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_headerpara(request):
    """
        POST请求，删除head parameter
        :param request: headid，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20018'
                 error_code = '99999'
                 error_code = '90001'
    """

    head_id = request.POST.get('headid', None)

    if head_id:
        try:
            headpara = HeaderPara.objects.filter(id=head_id, is_del=1)
            if headpara.exists():
                headpara = headpara.first()
                para = headpara.para
                headpara.is_del = 0
                headpara.save()
                para.is_del = 0
                para.save()
                error_code = '0'
                message = u'删除head parameter成功。'
            else:
                error_code = '20018'
                message = u'所选head parameter不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def headerpara_list(request):
    """
        GET请求，获取head parameter列表
        :param request: apiid，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    api_id = request.GET.get('apiid', None)
    data = []

    if api_id:
        try:
            api = Api.objects.filter(id=api_id, is_del=1)
            if api.exists():
                api = api.first()
                headers = HeaderPara.objects.filter(api=api, is_del=1)
                for head in headers:
                    para = dict()
                    para['headid'] = head.id
                    para['key'] = head.para.key
                    para['isnull'] = head.para.get_is_null_display()
                    para['desc'] = head.para.desc
                    para['datatype'] = head.para.get_data_type_display()
                    data.append(para)

                error_code = '0'
                message = u'获取headers列表成功。'
            else:
                error_code = '20017'
                message = u'所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def add_bodypara(request):
    """
        POST请求，新增body parameter
        :param request: apiid，key，desc，isnull，datatype
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20017'
                 error_code = '99999'
                 error_code = '90001'
    """
    api_id = request.POST.get('apiid', None)
    key = request.POST.get('key', None)
    desc = request.POST.get('desc', None)
    is_null = request.POST.get('isnull', None)
    data_type = request.POST.get('datatype', None)

    if api_id and key and desc and is_null and data_type:
        try:
            api = Api.objects.filter(id=api_id, is_del=1)
            if api.exists():
                api = api.first()
                if int(data_type) in (0, 1, 2, 3, 4) and int(is_null) in (0, 1):
                    para = Parameter(key=key, desc=desc, is_null=is_null, data_type=data_type)
                    para.save()
                    bodypara = BodyPara(api=api, para=para)
                    bodypara.save()
                    error_code = '0'
                    message = u'添加body parameter成功。'
                else:
                    error_code = '99999'
                    message = u'数据操作异常。'
            else:
                error_code = '20017'
                message = u'所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_bodypara(request):
    """
        POST请求，删除body parameter
        :param request: bodyid，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20019'
                 error_code = '99999'
                 error_code = '90001'
    """

    body_id = request.POST.get('bodyid', None)

    if body_id:
        try:
            bodypara = BodyPara.objects.filter(id=body_id, is_del=1)
            if bodypara.exists():
                bodypara = bodypara.first()
                para = bodypara.para
                bodypara.is_del = 0
                bodypara.save()
                para.is_del = 0
                para.save()
                error_code = '0'
                message = u'删除body parameter成功。'
            else:
                error_code = '20019'
                message = u'所选body parameter不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def bodypara_list(request):
    """
        GET请求，获取body parameter列表
        :param request: apiid，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20017'
                 error_code = '99999'
                 error_code = '90001'
    """

    api_id = request.GET.get('apiid', None)
    data = []

    if api_id:
        try:
            api = Api.objects.filter(id=api_id, is_del=1)
            if api.exists():
                api = api.first()
                bodyers = BodyPara.objects.filter(api=api, is_del=1)
                for body in bodyers:
                    para = dict()
                    para['bodyid'] = body.id
                    para['key'] = body.para.key
                    para['isnull'] = body.para.get_is_null_display()
                    para['desc'] = body.para.desc
                    para['datatype'] = body.para.get_data_type_display()
                    data.append(para)

                error_code = '0'
                message = u'获取Bodys列表成功。'
            else:
                error_code = '20017'
                message = u'所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def add_responsepara(request):
    """
        POST请求，新增response parameter
        :param request: apiid，key，desc，isnull，datatype
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20017'
                 error_code = '99999'
                 error_code = '90001'
    """
    api_id = request.POST.get('apiid', None)
    key = request.POST.get('key', None)
    desc = request.POST.get('desc', None)
    is_null = request.POST.get('isnull', None)
    data_type = request.POST.get('datatype', None)

    if api_id and key and desc and is_null and data_type:
        try:
            api = Api.objects.filter(id=api_id, is_del=1)
            if api.exists():
                api = api.first()
                if int(data_type) in (0, 1, 2, 3, 4) and int(is_null) in (0, 1):
                    para = Parameter(key=key, desc=desc, is_null=is_null, data_type=data_type)
                    para.save()
                    responsepara = ResponsePara(api=api, para=para)
                    responsepara.save()
                    error_code = '0'
                    message = u'添加response parameter成功。'
                else:
                    error_code = '99999'
                    message = u'数据操作异常。'
            else:
                error_code = '20017'
                message = u'所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_responsepara(request):
    """
        POST请求，删除response parameter
        :param request: responseid，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20020'
                 error_code = '99999'
                 error_code = '90001'
    """

    response_id = request.POST.get('responseid', None)

    if response_id:
        try:
            responsepara = ResponsePara.objects.filter(id=response_id, is_del=1)
            if responsepara.exists():
                responsepara = responsepara.first()
                para = responsepara.para
                responsepara.is_del = 0
                responsepara.save()
                para.is_del = 0
                para.save()
                error_code = '0'
                message = u'删除response parameter成功。'
            else:
                error_code = '20020'
                message = u'所选response parameter不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def responsepara_list(request):
    """
        GET请求，获取response parameter列表
        :param request: apiid，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20017'
                 error_code = '99999'
                 error_code = '90001'
    """

    api_id = request.GET.get('apiid', None)
    data = []

    if api_id:
        try:
            api = Api.objects.filter(id=api_id, is_del=1)
            if api.exists():
                api = api.first()
                responseers = ResponsePara.objects.filter(api=api, is_del=1)
                for response in responseers:
                    para = dict()
                    para['responseid'] = response.id
                    para['key'] = response.para.key
                    para['isnull'] = response.para.get_is_null_display()
                    para['desc'] = response.para.desc
                    para['datatype'] = response.para.get_data_type_display()
                    data.append(para)

                error_code = '0'
                message = u'获取responses列表成功。'
            else:
                error_code = '20017'
                message = u'所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)
