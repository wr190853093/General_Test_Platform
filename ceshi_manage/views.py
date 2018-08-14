"""
error_code = '30001'  message = u'所选项目不存在。'
error_code = '30002'  message = u'用例名称已存在。'
error_code = '30003'  message = u'所选用例不存在。'
error_code = '30004'  message = u'所选用例已为启用状态。'
error_code = '30005'  message = u'所选用例已为跳过状态。'
error_code = '30006'  message = u'所选API不存在。'
error_code = '30007'  message = u'所选步骤不存在。'
error_code = '30008'  message = u'请先删除最后一个步骤。'
error_code = '30009'  message = u'。'
error_code = '30010'  message = u'。'
error_code = '30011'  message = u'。'
error_code = '30012'  message = u'。'
error_code = '30013'  message = u'。'
error_code = '30014'  message = u'。'
error_code = '30015'  message = u'。'
error_code = '30016'  message = u'。'
error_code = '30017'  message = u'。'
error_code = '30018'  message = u'。'
error_code = '30020'  message = u'。'
error_code = '30019'  message = u'。'
"""
from django.http import JsonResponse
from ceshi_manage.models import *
from rest_framework.decorators import api_view
from common.util import *
import jsonpath


@api_view(['POST'])
def create_case(request):
    """
        POST请求，新增用例
        :param request: name，desc，proj_id
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30001'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.POST.get('name', None)
    desc = request.POST.get('desc', None)
    proj_id = request.POST.get('projectid', None)
    data = ''
    if name and proj_id and desc:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            if project.exists():
                project = project.first()
                if not Case.objects.filter(name=name).exists():
                    case = Case(name=name, desc=desc, project=project)
                    case.save()
                    error_code = '0'
                    message = u'新增用例成功。'
                    data = case.id
                else:
                    error_code = '30002'
                    message = u'用例名称已存在。'
            else:
                error_code = '30001'
                message = u'所选项目不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'case_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_case(request):
    """
        POST请求，编辑用例
        :param request: case_id，name，desc，proj_id
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30001'
                 error_code = '30002'
                 error_code = '30003'
                 error_code = '99999'
                 error_code = '90001'
    """

    case_id = request.POST.get('caseid', None)
    name = request.POST.get('name', None)
    desc = request.POST.get('desc', None)
    proj_id = request.POST.get('projectid', None)
    data = ''
    if case_id and name and proj_id and desc:
        try:
            project = Project.objects.filter(id=proj_id, status=1)
            case = Case.objects.filter(id=case_id)
            if case.exists():
                case = project.first()
                if project.exists():
                    if not Case.objects.filter(name=name).exclude(id=case_id).exists():
                        case.update(name=name, desc=desc, project=project)
                        error_code = '0'
                        message = u'新增用例成功。'
                        data = case.id
                    else:
                        error_code = '30002'
                        message = u'用例名称已存在。'
                else:
                    error_code = '30001'
                    message = u'所选项目不存在。'
            else:
                error_code = '30003'
                message = u'所选用例不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = u'数据操作异常。'
    else:
        error_code = '90001'
        message = u'存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'case_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def enable_case(request):
    """
        POST请求，启用用例
        :param request: case_id，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30003'
                 error_code = '30004'
                 error_code = '99999'
                 error_code = '90001'
    """

    case_id = request.POST.get('caseid', None)
    if case_id:
        try:
            case = Case.objects.filter(id=case_id)
            if case.exists():
                if case.first().status == 0:
                    case.update(status=1)
                    error_code = '0'
                    message = u'修改用例状态成功。'
                else:
                    error_code = '30004'
                    message = u'所选用例已为启用状态。'
            else:
                error_code = '30003'
                message = u'所选用例不存在。'
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
def unenable_case(request):
    """
        POST请求，禁用用例
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30003'
                 error_code = '30005'
                 error_code = '99999'
                 error_code = '90001'
    """

    case_id = request.POST.get('caseid', None)
    if case_id:
        try:
            case = Case.objects.filter(id=case_id)
            if case.exists():
                if case.first().status == 0:
                    case.update(status=1)
                    error_code = '0'
                    message = u'修改用例状态成功。'
                else:
                    error_code = '30005'
                    message = u'所选用例已为跳过状态。'
            else:
                error_code = '30003'
                message = u'所选用例不存在。'
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
def case_list(request):
    """
        GET请求，获取用例列表
        :param request:
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '99999'
    """

    name = request.GET.get('name', None)
    status = request.GET.get('status', None)
    data = []
    try:
        searchcondition = {'name__contains': name, 'status': status}
        kwargs = getkwargs(searchcondition)
        cases = Case.objects.filter(**kwargs).order_by('id')
        for ca in cases:
            case = dict()
            case['id'] = ca.id
            case['name'] = ca.name
            case['status'] = ca.get_status_display()
            case['desc'] = ca.desc
            case['project'] = {'projectName': ca.project.name, 'projectId': ca.project.id}
            data.append(case)
        error_code = '0'
        message = u'获取用例列表成功。'
    except Exception as e:
        print(e)
        error_code = '99999'
        message = u'数据操作异常。'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['GET'])
def case_info(request):
    """
        POST请求，获取用例详情
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    case_id = request.GET.get('case_id', None)

    data = []
    if case_id:
        try:
            case = Case.objects.filter(id=case_id)
            if case.exists():
                ca = case.first()
                case['id'] = ca.id
                case['name'] = ca.name
                case['status'] = ca.get_status_display()
                case['desc'] = ca.desc
                case['project'] = {'projectName': ca.project.name, 'projectId': ca.project.id}
                data.append(case)
                error_code = '0'
                message = u'获取用例列表成功。'
            else:
                error_code = '30003'
                message = u'所选用例不存在。'
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
def add_step(request):
    """
        POST请求，增加步骤
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30003'
                 error_code = '30006'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.POST.get('name', None)
    desc = request.POST.get('desc', None)
    order = request.POST.get('order', None)  # 步骤
    case_id = request.POST.get('case', None)
    api_id = request.POST.get('template', None)
    para = request.POST.get('para', None)
    # para格式 '{"headers":[{"para_id": 123, "key": "abc", "value": "21asd"},{}], "body":[{}], "check":[{}]}'
    if name and order and case_id and api_id and para and desc:
        try:
            api = Api.objects.filter(id=api_id)
            if api.exists():
                case = Case.objects.filter(id=case_id)
                if case.exists():
                    headers = jsonpath.jsonpath(para, expr='$.headers')
                    body = jsonpath.jsonpath(para, expr='$.body')
                    check = jsonpath.jsonpath(para, expr='$.check')

                    step = Step(name=name, order=order, check=check, case=case.first(), api=api.first(),
                                headers=headers, body=body)
                    step.save()
                    error_code = '0'
                    message = u'新增步骤成功。'
                else:
                    error_code = '30003'
                    message = u'所选用例不存在。'
            else:
                error_code = '30006'
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
def step_list(request):
    """
        GET请求，获取步骤列表
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    case_id = request.GET.get('case_id', None)

    data = []
    if case_id:
        try:
            case = Case.objects.filter(id=case_id)
            if case.exists():
                steps = Step.objects.filter(case=case.first(), is_del=1).order_by('order')
                for s in steps:
                    step = dict()
                    step['id'] = s.id
                    step['name'] = s.name
                    step['desc'] = s.desc
                    step['API'] = {'apiName': s.api.name, 'apiId': s.api.id}
                    step['headers'] = s.headers
                    step['body'] = s.body
                    step['check'] = s.check
                    data.append(step)

                error_code = '0'
                message = u'获取步骤列表成功。'
            else:
                error_code = '30003'
                message = u'所选用例不存在。'
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
def delete_step(request):
    """
        POST请求，删除步骤
        :param request: stepid，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    step_id = request.POST.get('stepid', None)

    if step_id:
        try:
            step = Step.objects.filter(id=step_id, is_del=1)
            if step.exists():
                step = step.first()
                order = step.order
                case = step.case
                if not Step.objects.filter(case=case, order__gt=order, is_del=1).exists():
                    step.is_del = 0
                    step.save()
                    error_code = '0'
                    message = u'删除步骤成功。'
                else:
                    error_code = '30008'
                    message = u'请先删除最后一个步骤。'
            else:
                error_code = '30007'
                message = u'所选步骤不存在。'
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
def create_task(request):
    """
        POST请求，新建任务
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def edit_task(request):
    """
        POST请求，编辑任务
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def run_task(request):
    """
        POST请求，运行任务
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['GET'])
def task_list(request):
    """
        POST请求，获取任务列表
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['GET'])
def task_case(request):
    """
        GET请求，获取任务用例列表
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass
