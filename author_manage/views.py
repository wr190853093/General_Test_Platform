"""
    error_code = '10001'  message = '请先删除子节点组织机构再删除父节点组织机构。'
    error_code = '10002'  message = '同节点组织机构名称重复。'
    error_code = '10003'  message = '不存在父节点组织机构。'
    error_code = '10004'  message = '所选组织机构不存在。
    error_code = '10005'  message = '员工角色错误。'
    error_code = '10006'  message = '用户名已经存在。'
    error_code = '10007'  message = '所选员工不存在。'
    error_code = '10008'  message = '所选员工已为在职状态。'
    error_code = '10009'  message = '所选员工已为离职状态。'
    error_code = '99999   message = '数据操作异常。'
    error_code = '90001'  message = '存在必填项为空.'
"""
from django.http import JsonResponse
from author_manage.models import *
from rest_framework.decorators import api_view
from common.util import *


# 新增组织机构
@api_view(['POST'])
def create_org(request):
    """
    POST请求，创建组织机构
    :param request: name,parentid
    :return: resp = {'error_code': error_code, 'message': message, 'org_id': data}
             error_code = '0'
             error_code = '10002'
             error_code = '10003'
             error_code = '90001'
    """

    name = request.POST.get('name', None)
    parent_id = request.POST.get('parentid', None)
    is_del = '1'
    data = ''
    if name:
        if parent_id:
            try:
                parent = Organization.objects.filter(id=parent_id, is_del=1)
                if parent.exists():
                    if not Organization.objects.filter(parent=parent.first(), name=name, is_del=1).exists():
                        org = Organization(name=name, is_del=is_del, parent=parent.first())
                        org.save()
                        error_code = '0'
                        message = '新增组织机构成功。'
                        data = org.id
                    else:
                        error_code = '10002'
                        message = '同节点组织机构名称重复。'
                else:
                    error_code = '10003'
                    message = '不存在父节点组织机构。'
            except Exception as e:
                print(e)
                error_code = '99999'
                message = '数据操作异常。'
        else:
            try:
                if not Organization.objects.filter(parent__isnull=True, name=name, is_del=1).exists():
                    org = Organization(name=name, is_del=is_del)
                    org.save()
                    error_code = '0'
                    message = '新增组织机构成功。'
                    data = org.id
                else:
                    error_code = '10002'
                    message = '同节点组织机构名称重复。'
            except Exception as e:
                print(e)
                error_code = '99999'
                message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'org_id': data}
    return JsonResponse(resp)
    # js = json.dumps(resp, ensure_ascii=False)
    # return HttpResponse(js)


@api_view(['POST'])
def delete_org(request):
    """
    POST请求，删除组织机构
    :param request: orgid
    :return: resp = {'error_code': error_code, 'message': message}
             error_code = '0'
             error_code = '10001'
             error_code = '10004'
             error_code = '90001'
    """

    org_id = request.POST.get('orgid', None)
    # error_code = ''
    # message = ''
    if org_id:
        try:
            org = Organization.objects.filter(id=org_id)
            if org.exists() and org.first().is_del == 1:
                if not Organization.objects.filter(parent=org_id, is_del=1).exists():
                    org.update(is_del='0')
                    error_code = '0'
                    message = '删除组织机构成功。'
                else:
                    error_code = '10001'
                    message = '请先删除子节点组织机构再删除父节点组织机构。'
            else:
                error_code = '10004'
                message = '所选组织机构不存在。'
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
def edit_org(request):
    """
    POST请求，编辑组织机构
    :param request: orgid，name
    :return: resp = {'error_code': error_code, 'message': message}
             error_code = '0'
             error_code = '10002'
             error_code = '10004'
             error_code = '99999'
             error_code = '90001'
    """

    org_id = request.POST.get('orgid', None)
    name = request.POST.get('name', None)
    # is_del = '1'
    # data = ''
    if name and org_id:
        try:
            org = Organization.objects.filter(id=org_id, is_del=1)
            if org.exists():
                parent_org = org.first().parent
                if not Organization.objects.exclude(id=org_id).filter(name=name, parent=parent_org, is_del=1).exists():
                    org.update(name=name)
                    error_code = '0'
                    message = '编辑组织机构成功。'
                else:
                    error_code = '10002'
                    message = '同节点组织机构名称重复。'
            else:
                error_code = '10004'
                message = '所选组织机构不存在。'
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
def org_tree(request):
    """
    GET请求，获取组织机构
    :param request:
    :return: resp = {'error_code': error_code, 'message': message, 'data': data}
             error_code = '0'
             error_code = '99999'
    """

    data = []
    try:
        root = Organization.objects.filter(parent__isnull=True, is_del=1)
        for r in root:
            org = get_child(r, result={}, data={}, node=[])
            data.append(org)
        error_code = '0'
        message = '获取组织机构树成功。'
    except Exception as e:
        print(e)
        error_code = '99999'
        message = '数据操作异常。'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['GET'])
# 暂时不要该接口
def org_info(request):
    # return HttpResponse('1')
    pass


@api_view(['POST'])
def create_user(request):
    """
    POST请求，新增员工
    :param request: name，username，email，org，role，password
    :return: resp = {'error_code': error_code, 'message': message, 'user_id': data}
             error_code = '0'
             error_code = '10004'
             error_code = '10005'
             error_code = '10006'
             error_code = '99999'
             error_code = '90001'
    """

    name = request.POST.get('name', None)
    username = request.POST.get('username', None)
    email = request.POST.get('email', None)  # 前台进行邮箱格式校验，后台不做校验了
    org = request.POST.get('org', None)
    role = request.POST.get('role', None)
    password = request.POST.get('password', None)  # 前台进行加密后传给后台，后台不做加密处理，避免通过抓包获取密码
    is_del = '1'
    status = '1'
    data = ''
    if name and username and org and password and role:
        try:
            role = int(role)
            if role in [0, 1, 2, 3]:
                try:
                    organize = Organization.objects.filter(id=org, is_del=1)
                    if organize.exists():
                        if not Users.objects.filter(username=username).exists():
                            user = Users(name=name, username=username, email=email, org=organize.first(),
                                         role=role, password=password, is_del=is_del, status=status)
                            user.save()
                            error_code = '0'
                            message = '新增员工成功。'
                            data = user.id
                        else:
                            error_code = '10006'
                            message = '用户名已经存在。'
                    else:
                        error_code = '10004'
                        message = '所选组织机构不存在。'
                except Exception as e:
                    print(e)
                    error_code = '99999'
                    message = '数据操作异常。'
            else:
                error_code = '10005'
                message = '员工角色错误。'
        except Exception as e:
            print(e)
            error_code = '10005'
            message = '员工角色错误。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message, 'user_id': data}
    return JsonResponse(resp)


@api_view(['POST'])
def delete_user(request):
    """
        POST请求，删除员工
        :param request: userid，
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '10007'
                 error_code = '99999'
                 error_code = '90001'
    """

    user_id = request.POST.get('userid', None)
    if user_id:
        try:
            user = Users.objects.filter(id=user_id)
            if user.exists() and user.first().is_del == 1:
                user.update(is_del='0')
                error_code = '0'
                message = '删除员工成功。'
            else:
                error_code = '10007'
                message = '所选员工不存在。'
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
# 编辑name、username、email、role、org
def edit_user(request):
    """
        POST请求，编辑员工
        :param request: userid，name，username，email，org，role，password
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '10004'
                 error_code = '10006'
                 error_code = '10004'
                 error_code = '10007'
                 error_code = '99999'
                 error_code = '90001'
    """

    user_id = request.POST.get('userid', None)
    name = request.POST.get('name', None)
    username = request.POST.get('username', None)
    email = request.POST.get('email', None)  # 前台进行邮箱格式校验，后台不做校验了
    org = request.POST.get('org', None)
    role = request.POST.get('role', None)

    if name and username and org and user_id and role:
        try:
            role = int(role)
            if role in [0, 1, 2, 3]:
                try:
                    organize = Organization.objects.filter(id=org, is_del=1)
                    if organize.exists():
                        user = Users.objects.filter(id=user_id, is_del=1)
                        if user.exists():
                            if not Users.objects.exclude(id=user.id).filter(username=username).exists():
                                user.update(name=name, username=username, email=email, org=organize.first(),
                                            role=role)
                                error_code = '0'
                                message = '编辑员工信息成功。'
                            else:
                                error_code = '10006'
                                message = '用户名已经存在。'
                        else:
                            error_code = '10007'
                            message = '所选员工不存在。'
                    else:
                        error_code = '10004'
                        message = '所选组织机构不存在。'
                except Exception as e:
                    print(e)
                    error_code = '99999'
                    message = '数据操作异常。'
            else:
                error_code = '10005'
                message = '员工角色错误。'
        except Exception as e:
            print(e)
            error_code = '10005'
            message = '员工角色错误。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'

    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)


@api_view(['POST'])
# 根据userid修改状态
def enable_user(request):
    """
        POST请求，启用员工
        :param request: userid
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '10007'
                 error_code = '10008'
                 error_code = '99999'
                 error_code = '90001'
    """

    user_id = request.POST.get('userid', None)
    if user_id:
        try:
            user = Users.objects.filter(id=user_id, is_del=1)
            if user.exists():
                if user.first().status == 0:
                    user.update(status=1)
                    error_code = '0'
                    message = '修改员工状态成功。'
                else:
                    error_code = '10008'
                    message = '所选员工已为在职状态。'
            else:
                error_code = '10007'
                message = '所选员工不存在。'
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
# 根据userid修改状态
def unenable_user(request):
    """
        POST请求，禁用员工
        :param request: userid
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '10007'
                 error_code = '10009'
                 error_code = '99999'
                 error_code = '90001'
    """

    user_id = request.POST.get('userid', None)
    if user_id:
        try:
            user = Users.objects.filter(id=user_id, is_del=1)
            if user.exists():
                if user.first().status == 1:
                    user.update(status=0)
                    error_code = '0'
                    message = '修改员工状态成功。'
                else:
                    error_code = '10009'
                    message = '所选员工已为离职状态。'
            else:
                error_code = '10007'
                message = '所选员工不存在。'
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
def user_list(request):
    """
        GET请求，获取员工列表
        :param request: name，username，orgid
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
                 error_code = '0'
                 error_code = '10004'
                 error_code = '99999'
                 error_code = '90001'
    """

    name = request.GET.get('name', '')
    username = request.GET.get('username', '')
    org = request.GET.get('orgid', None)
    data = []
    try:
        if org:

            organize = Organization.objects.filter(id=org, is_del=1)
            if organize.exists():
                users = Users.objects.filter(org=organize.first(), is_del=1)
            else:
                error_code = '10004'
                message = '所选组织机构不存在。'
                resp = {'error_code': error_code, 'message': message, 'data': data}
                return JsonResponse(resp)
        else:
            users = Users.objects.filter(name__contains=name, username__contains=username, is_del=1).order_by('id')
        for u in users:
            user = dict()
            user['id'] = u.id
            user['name'] = u.name
            user['username'] = u.username
            user['email'] = u.email
            user['org'] = u.org.name
            user['role'] = u.get_role_display()
            user['status'] = u.get_status_display()
            data.append(user)
        error_code = '0'
        message = '获取员工列表成功。'
    except Exception as e:
        print(e)
        error_code = '99999'
        message = '数据操作异常。'
    resp = {'error_code': error_code, 'message': message, 'data': data}
    return JsonResponse(resp)


@api_view(['GET'])
def user_info(request):
    """
        GET请求，获取员工信息
        :param request: userid，
        :return: resp = {'error_code': error_code, 'message': message, 'data': data}
                 error_code = '0'
                 error_code = '10007'
                 error_code = '99999'
                 error_code = '90001'
    """

    user_id = request.GET.get('userid', None)
    data = []
    if user_id:
        try:
            users = Users.objects.filter(is_del=1, id=user_id)
            if users.exists():
                u = users.first()
                user = dict()
                user['id'] = u.id
                user['name'] = u.name
                user['username'] = u.username
                user['email'] = u.email
                user['org'] = u.org.name
                user['role'] = u.get_role_display()
                data.append(user)
                error_code = '0'
                message = '获取员工信息成功。'
            else:
                error_code = '10007'
                message = '所选员工不存在。'
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
def edit_password(request):
    """
        POST请求，获取员工信息
        :param request: userid，password
        :return: resp = {'error_code': error_code, 'message': message}
                 error_code = '0'
                 error_code = '10007'
                 error_code = '99999'
                 error_code = '90001'
    """

    user_id = request.POST.get('userid', None)
    pwd = request.POST.get('password', None)
    if user_id and pwd:
        try:
            users = Users.objects.filter(is_del=1, id=user_id)
            if users.exists():
                users.update(password=pwd)
                error_code = '0'
                message = '重置密码成功。'
            else:
                error_code = '10007'
                message = '所选员工不存在。'
        except Exception as e:
            print(e)
            error_code = '99999'
            message = '数据操作异常。'
    else:
        error_code = '90001'
        message = '存在必填项为空.'
    resp = {'error_code': error_code, 'message': message}
    return JsonResponse(resp)
