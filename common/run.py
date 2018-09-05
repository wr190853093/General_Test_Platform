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
    # case_list = sys.argv[3].split(',')
    # task_id = sys.argv[1]
    case_list = ['1', '2']
    task_id = '11'
    for case_id in case_list:
        case = Case.objects.filter(id=case_id).first()
        FUNC_TEMPLATE = '''def {test_id}(self):
                           '{desc}'
                           ITest.execute_case({data},{task_id})
                        '''
        exec(FUNC_TEMPLATE.format(test_id='test_' + case.name, desc=case.desc, data=case_id, task_id=task_id))

    @classmethod
    def execute_case(cls, case_id, task_id):
        print(case_id,task_id)
        VALUES = {}  # 用户全局变量
        case = Case.objects.filter(id=case_id).first()
        # todo 按照用例-步骤-api顺序执行测试
        steps = Step.objects.filter(case=case, is_del=1).order_by('order')
        print(steps)
        for step in steps:
            print(step.id)
            api = step.api
            environment = TaskEnvironment.objects.filter(task_id=task_id, step=step, case=case).first().environment
            url = 'https://' + environment.host + '/' + api.path
            method = api.method
            headers_str = step.headers
            body_str = step.body
            check_str = step.check
            if headers_str:
                headers = json.loads(headers_str)
            else:
                headers = {}

            if body_str:
                if headers.get('content-type', None) == 'application/x-www-form-urlencoded' \
                        or headers.get('content-type', None) == 'multipart/form-data':
                    data = json.loads(body_str)
                else:
                    data = body_str
            client = myhttp.client(url=url, method=method, headers=headers, data=data)
            client.send()
            if check_str:
                check_dict = json.loads(check_str)
                for method_name, paras in check_dict.items():
                    try:
                        CHECK_FUNC = "client.{method_name}(paras)"
                        if method_name == 'transfer':
                            VALUES[paras.get('name', None)] = client.transfer(paras.get('path', None))
                        else:
                            eval(CHECK_FUNC.format(method_name=method_name, paras=paras))
                    except Exception as e:
                        assert False, '检查点函数%s执行异常：%s' % (method_name, str(e))
                    continue
            continue



if __name__ == '__main__':
    # task_id = sys.argv[1]
    # task_time = sys.argv[2]
    task_id = 11
    task_time = 1534948993.567155
    suite = unittest.defaultTestLoader.discover('./common/', pattern='run.py')
    time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    fp = open('./static/reports/' + time_str + '.html', 'wb')
    HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='接口自动化测试报告').run(suite)
    Report.objects.create(time=task_time, file_name='/static/reports/' + time_str + '.html', status=1, task_id=task_id)
    # unittest.TextTestRunner().run(suite)
