import sys
import unittest
import HTMLTestRunnerCN
import time
import django
import os
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "General_Test_Platform.settings")
django.setup()

from ceshi_manage.models import *
from common import myhttp


class ITest(unittest.TestCase):
    case_list = sys.argv[3].split(',')
    env_id = sys.argv[4]
    # case_list = '1'
    # env_id = '1'
    for case_id in case_list:
        case = Case.objects.filter(id=case_id).first()
        FUNC_TEMPLATE = '''def {test_id}(self):
                           '{desc}'
                           ITest.execute_case({data},{env_id})
                        '''
        exec(FUNC_TEMPLATE.format(test_id='test_' + case.name, desc=case.desc, data=case_id, env_id=env_id))

    @classmethod
    def execute_case(cls, case_id, env_id):
        VALUES = {}  # 用户全局变量
        case = Case.objects.filter(id=case_id).first()
        # todo 按照用例-步骤-api顺序执行测试
        steps = Step.objects.filter(case=case, is_del=1).order_by('order')
        environment = Environment.objects.filter(id=env_id).first()
        for step in steps:
            api = step.api
            url = 'http://' + environment.host + '/' + api.path + '/'
            method = api.method
            headers_str = step.headers
            body_str = step.body
            check_str = step.check
            headers = json.loads(headers_str)
            # headers = {}
            # if headers_str:
            #     list = headers_str.split('&')
            #     for l in list:
            #         headers[l.split('=')[0]] = l.split('=')[1]
            if body_str:
                if headers.get('content-type', None) == 'application/x-www-form-urlencoded' \
                        or headers.get('content-type', None) == 'multipart/form-data':
                    data = json.loads(body_str)
                    # data = {}
                    # list = body_str.split('&')
                    # for l in list:
                    #     data[l.split('=')[0]] = l.split('=')[1]
                else:
                    data = body_str
            client = myhttp.client(url=url, method=method, headers=headers, data=data)
            if check_str:
                check_list = check_str.split('&')
                for l in check_list:
                    # if l.split('=')[0] == "response_code":
                    #     client.check_status_code(l.split('=')[1])
                    # elif l.split('=')[0] == "response_time":
                    try:
                        method_name = l.keys()[0]
                        paras = l[method_name]
                        CHECK_FUNC = "client.{method_name}(paras)"
                        if method_name == 'transfer':
                            VALUES[paras.get('name', None)] = client.transfer(paras.get('path', None))
                        else:
                            eval(CHECK_FUNC.format(method_name=method_name, paras=paras))
                    except Exception as e:
                        assert False, '检查点函数%s执行异常：%s' % (method_name, str(e.message))


if __name__ == '__main__':
    task_id = sys.argv[1]
    task_time = sys.argv[2]
    # task_id = 1
    # task_time = 1534948993.567155
    suite = unittest.defaultTestLoader.discover('./common/', pattern='run.py')
    time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    fp = open('./static/reports/' + time_str + '.html', 'wb')
    HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='接口自动化测试报告').run(suite)
    Report.objects.create(time=task_time, file_name='/static/reports/' + time_str + '.html', status=1, task_id=task_id)
    # unittest.TextTestRunner().run(suite)
