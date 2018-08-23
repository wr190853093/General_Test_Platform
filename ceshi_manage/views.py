"""
error_code = '30001'  message = '所选项目不存在。'
error_code = '30002'  message = '用例名称已存在。'
error_code = '30003'  message = '所选用例不存在。'
error_code = '30004'  message = '所选用例已为启用状态。'
error_code = '30005'  message = '所选用例已为跳过状态。'
error_code = '30006'  message = '所选API不存在。'
error_code = '30007'  message = '所选步骤不存在。'
error_code = '30008'  message = '请先删除最后一个步骤。'
error_code = '30009'  message = '任务名称重复。'
error_code = '30010'  message = '所选环境不存在。'
error_code = '30011'  message = '所选任务不存在。'
error_code = '30012'  message = '无可执行的测试用例。'
error_code = '30013'  message = '超时无法获取报告地址。'
error_code = '30014'  message = '。'
error_code = '30015'  message = '。'
error_code = '30016'  message = '。'
error_code = '30017'  message = '。'
error_code = '30018'  message = '。'
error_code = '30020'  message = '。'
error_code = '30019'  message = '。'
"""
from django.http import JsonResponse
from ceshi_manage.models import *
from rest_framework.decorators import api_view
from common.util import *
import jsonpath, json
import time
import os

"""
'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20180717T065026Z.3fb8acc8e9b79ba1.83a3cf4f9d897b60eb47eb2da3f13dfb3aed5f29&lang=en&text=hello

"""


@api_view(['POST'])
def create_case(request):
    """
        POST请求，新增用例
        :param request: name，desc，proj_id
        :return: resp = {'error_code': error_code, 'message': message, 'case_id': data}
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
                    message = '新增用例成功。'
                    data = case.id
                else:
                    error_code = '30002'
                    message = '用例名称已存在。'
            else:
                error_code = '30001'
                message = '所选项目不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'case_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_case(request):
    """
        POST请求，编辑用例
        :param request: case_id，name，desc，proj_id
        :return: resp = {'error_code': error_code, 'message': message, 'case_id': data}
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
                        message = '新增用例成功。'
                        data = case.id
                    else:
                        error_code = '30002'
                        message = '用例名称已存在。'
                else:
                    error_code = '30001'
                    message = '所选项目不存在。'
            else:
                error_code = '30003'
                message = '所选用例不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'case_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def enable_case(request):
    """
        POST请求，启用用例
        :param request: case_id，
        :return: resp = {'error_code': error_code, 'message': message}
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
                    message = '修改用例状态成功。'
                else:
                    error_code = '30004'
                    message = '所选用例已为启用状态。'
            else:
                error_code = '30003'
                message = '所选用例不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def unenable_case(request):
    """
        POST请求，禁用用例
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message}
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
                    message = '修改用例状态成功。'
                else:
                    error_code = '30005'
                    message = '所选用例已为跳过状态。'
            else:
                error_code = '30003'
                message = '所选用例不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def case_list(request):
    """
        GET请求，获取用例列表
        :param request:
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
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
        message = '获取用例列表成功。'
    except Exception as e:
        print(e)
        error_code = '99999'
        message = '数据操作异常。'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['GET'])
def case_info(request):
    """
        POST请求，获取用例详情
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
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
                message = '获取用例列表成功。'
            else:
                error_code = '30003'
                message = '所选用例不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def add_step(request):
    """
        POST请求，增加步骤
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message}
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
    api_id = request.POST.get('apiid', None)
    para = request.POST.get('para', None)
    # para格式 '{"headers":[{"para_id": 123, "key": "abc", "value": "21asd"},{}], "body":[{}], "check":[{}]}'
    if name and order and case_id and api_id and para and desc:
        try:
            api = Api.objects.filter(id=api_id)
            if api.exists():
                case = Case.objects.filter(id=case_id)
                if case.exists():
                    para = json.loads(para)
                    headers = jsonpath.jsonpath(para, expr='$.headers')
                    body = jsonpath.jsonpath(para, expr='$.body')
                    check = jsonpath.jsonpath(para, expr='$.check')

                    step = Step(name=name, order=order, check=check, case=case.first(), api=api.first(),
                                headers=headers, body=body)
                    step.save()
                    error_code = '0'
                    message = '新增步骤成功。'
                else:
                    error_code = '30003'
                    message = '所选用例不存在。'
            else:
                error_code = '30006'
                message = '所选API不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def step_list(request):
    """
        GET请求，获取步骤列表
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
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
                message = '获取步骤列表成功。'
            else:
                error_code = '30003'
                message = '所选用例不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_step(request):
    """
        POST请求，删除步骤
        :param request: stepid，
        :return: resp = {'error_code': error_code, 'message': message}
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
                    message = '删除步骤成功。'
                else:
                    error_code = '30008'
                    message = '请先删除最后一个步骤。'
            else:
                error_code = '30007'
                message = '所选步骤不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def create_task(request):
    """
        POST请求，新建任务
        :param request: name，desc，cases，environment
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '30003'
                 error_code = '30009'
                 error_code = '30010'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.POST.get('name', None)
    desc = request.POST.get('desc', None)
    cases = request.POST.get('cases', None)
    environment_id = request.POST.get('environmentid', None)
    if name and cases and environment_id:
        if not Task.objects.filter(name=name).exists():
            environment = Environment.objects.filter(id=environment_id, is_del=1)
            if environment.exists():
                task = Task(name=name, desc=desc, environment=environment.first())
                task.save()

                cases_list = cases.split(',')
                for c_id in cases_list:
                    c = Case.objects.filter(id=c_id)
                    if c.exists():
                        task.case.add(c.first())
                    else:
                        error_code = '30003'
                        message = '所选用例不存在。'
                        break
                else:
                    error_code = '0'
                    message = '新建任务成功.'
            else:
                error_code = '30010'
                message = '所选环境不存在。'
        else:
            error_code = '30009'
            message = '任务名称重复.'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def edit_task(request):
    """
        POST请求，编辑任务
        :param request: taskid，name，desc，cases，environment
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '30011'
                 error_code = '30003'
                 error_code = '30009'
                 error_code = '30010'
                 error_code = '99999'
                 error_code = '90001'
    """
    task_id = request.POST.get('taskid', None)
    name = request.POST.get('name', None)
    desc = request.POST.get('desc', None)
    cases = request.POST.get('cases', None)
    environment_id = request.POST.get('environmentid', None)
    if task_id and name and cases and environment_id:
        task = Task.objects.filter(id=task_id)
        if task.exists():
            if not Task.objects.filter(name=name).exclude(id=task_id).exists():
                environment = Environment.objects.filter(id=environment_id, is_del=1)
                if environment.exists():
                    task.update(name=name, desc=desc, environment=environment.first())

                    cases_list = cases.split(',')
                    for c_id in cases_list:
                        c = Case.objects.filter(id=c_id)
                        if c.exists():
                            task.case.add(c.first())
                        else:
                            error_code = '30003'
                            message = '所选用例不存在。'
                            break
                    else:
                        error_code = '0'
                        message = '编辑任务成功.'
                else:
                    error_code = '30010'
                    message = '所选环境不存在。'
            else:
                error_code = '30009'
                message = '任务名称重复.'
        else:
            error_code = '30011'
            message = '所选任务不存在.'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
def run_task(request):
    """
        POST请求，运行任务
        :param request: task_id，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30011'
                 error_code = '30012'
                 error_code = '30013'
                 error_code = '99999'
                 error_code = '90001'
    """

    task_id = request.POST.get('taskid', None)
    if task_id:
        task = Task.objects.filter(id=task_id)
        if task.exists():
            task = task.first()
            # 获取到所有测试用例，判断是否存在，是否可运行
            cases = task.case.all()
            case = []
            case_list_str = ''
            env_id = task.environment.id
            for ca in cases:
                if ca.status == 1:
                    case.append(str(ca.id))
                    case_list_str = ','.join(case)
            if len(case) > 0:
                time_temp = time.time()
                print("python ./common/run.py %s %f %s %s" % (task_id, time_temp, case_list_str, env_id))
                status = os.system("python ./common/run.py %s %f %s %s" % (task_id, time_temp, case_list_str, env_id))
                if status == 0:
                    # 轮询任务历史表中知否存在报告信息
                    flag = 0
                    while flag < 30:
                        rep = Report.objects.filter(time=time_temp)
                        if rep.exists():
                            error_code = '0'
                            message = '任务执行成功。'

                            resp = {'error_code': error_code, 'message': message}
                            return JsonResponse(resp)
                        else:
                            flag += 1
                            time.sleep(1)
                    error_code = '30013'
                    message = '超时无法获取报告地址。'
                else:
                    error_code = '30013'
                    message = '超时无法获取报告地址。'
            # 没有可运行的用例
            else:
                error_code = '30012'
                message = '无可执行的测试用例'
        else:
            error_code = '30011'
            message = '所选任务不存在.'
    else:
        error_code = '90001'
        message = '存在必填项为空.'
    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['GET'])
def task_list(request):
    """
        POST请求，获取任务列表
        :param request: name，proj_id,envi_id
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30001'
                 error_code = '30010'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.GET.get('name', None)
    proj_id = request.GET.get('projectid', None)
    envi_id = request.GET.get('environmentid', None)

    data = []
    try:
        project = Project.objects.filter(id=proj_id)
        environment = Environment.objects.filter(id=envi_id, is_del=0)
        if project.exists():
            project = project.first()
            if environment.exists():
                environment = environment.first()
                searchcondition = {'name__contains': name, 'project': project, 'environment': environment}
                kwargs = getkwargs(searchcondition)
                tasks = Task.objects.filter(**kwargs).order_by('id')
                for ta in tasks:
                    task = dict()
                    task['id'] = ta.id
                    task['name'] = ta.name
                    task['desc'] = ta.desc
                    task['project'] = {'projectName': ta.project.name, 'projectId': ta.project.id}
                    task['environment'] = {'projectName': ta.environment.name, 'projectId': ta.environment.id}
                    data.append(task)
                error_code = '0'
                message = '获取任务列表成功。'
            else:
                error_code = '30010'
                message = '所选环境不存在。'
        else:
            error_code = '30001'
            message = '所选项目不存在。'
    except Exception as e:
        print(e)
        error_code = '99999'
        message = '数据操作异常。'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['GET'])
def task_case(request):
    """
        GET请求，获取任务用例列表
        :param request: taskid，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '30011'
                 error_code = '99999'
                 error_code = '90001'
    """

    task_id = request.POST.get('id', None)
    data = []
    if task_id:
        task = Task.objects.filter(id=task_id)
        if task.exists():
            task = task.first()
            cases = task.case.all()
            for ca in cases:
                case = dict()
                case['id'] = ca.id
                case['name'] = ca.name
                case['status'] = ca.get_status_display()
                case['desc'] = ca.desc
                case['project'] = {'projectName': ca.project.name, 'projectId': ca.project.id}
                data.append(case)
            error_code = '0'
            message = '获取用例列表成功。'
        else:
            error_code = '30011'
            message = '所选任务不存在.'
    else:
        error_code = '90001'
        message = '存在必填项为空.'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)
