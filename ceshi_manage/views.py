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
error_code = '20011'  message = u'所选环境已为启用状态。'
error_code = '20012'  message = u'所选环境不存在。'
error_code = '20013'  message = u'所选环境已为禁用状态。'
error_code = '20014'  message = u'路径格式错误。'
error_code = '20015'  message = u'API方法错误。'
error_code = '20016'  message = u'API已经存在。'
error_code = '20017'  message = u'所选接口不存在。'
error_code = '20018'  message = u'所选response parameter不存在。'
error_code = '20020'  message = u'所选response parameter不存在。'
error_code = '20019'  message = u'所选body parameter不存在。'
"""
from django.http import JsonResponse
from ceshi_manage.models import *
from rest_framework.decorators import api_view
from common.util import *


@api_view(['POST'])
def create_case(request):
    """
        POST请求，新增用例
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def edit_case(request):
    """
        POST请求，编辑用例
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def enable_case(request):
    """
        POST请求，启用用例
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def unenable_case(request):
    """
        POST请求，禁用用例
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['GET'])
def case_list(request):
    """
        GET请求，获取用例列表
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def add_step(request):
    """
        POST请求，增加步骤
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['GET'])
def step_list(request):
    """
        GET请求，获取步骤列表
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def delete_step(request):
    """
        POST请求，删除步骤
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def conf_headers(request):
    """
        POST请求，配置headers
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def conf_body(request):
    """
        POST请求，配置body
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def add_checks(request):
    """
        POST请求，新增检查点
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def edit_checks(request):
    """
        POST请求，编辑检查点
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def delete_checks(request):
    """
        POST请求，删除检查点
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass


@api_view(['POST'])
def create_task(request):
    """
        POST请求，新建任务
        :param request: name，
        :return: resp = {'error_code': error_code, 'message': message, 'project_id': data}
                 error_code = '0'
                 error_code = '20002'
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
                 error_code = '20002'
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
                 error_code = '20002'
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
                 error_code = '20002'
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
                 error_code = '20002'
                 error_code = '99999'
                 error_code = '90001'
    """

    pass
