import requests
import hashlib
import json
import jsonpath
import sys
from imp import reload

reload(sys)
# sys.setdefaultencoding('utf8')
import pymysql.cursors


class client():

    def __init__(self, url, method, headers, data):
        self.response = None
        self.method = method
        self.url = url
        self.headers = headers
        self.data = data

    def send(self):
        if self.method == 1:
            self.response = requests.request('POST', url=self.url, headers=self.headers, data=self.data)
        elif self.method == 0:
            self.response = requests.request('GET', url=self.url, headers=self.headers, params=self.data)
        else:
            print('不支持的http方法类型')

    def response2json(self):
        try:
            json_str = json.dumps(self.response.json())
        except:
            json_str = None
        return json_str

    def __format(self, message, expected, actual):
        return "[%s] 预期结果:%s，实际结果:%s" % (message, expected, actual)

    def __get_value_from_path(self, node_path):
        if self.response:
            object = jsonpath.jsonpath(self.response.json(), node_path)
            if object:
                return object
        return None

    def check_status_code(self, kargs):
        if self.response:
            result = self.response.status_code
            assert result == kargs.get('code', None), self.__format(kargs.get('message', None), kargs.get('code', None),
                                                                    result)
        else:
            assert False, '响应报文为空'

    def check_contains_str(self, kargs):
        result = self.reponse2json()
        assert kargs.get('str', None) in result, self.__format(kargs.get('message', None), kargs.get('str', None),
                                                               result)

    def check_node_exist(self, kargs):
        result = self.__get_value_from_path(kargs.get('node_path', None))
        assert result is not None, self.__format(kargs.get('message', None), kargs.get('node_path', None) + ' 存在',
                                                 result)

    def check_nodeText_equals(self, kargs):
        text = None
        node = self.__get_value_from_path(kargs.get('node_path', None))
        if node:
            text = node[0]
        assert str(text) == str(kargs.get('context', None)), self.__format(kargs.get('message', None),
                                                                           kargs.get('context', None), text)

    def check_nodeText_notequals(self, kargs):
        text = None
        node = self.__get_value_from_path(kargs.get('node_path', None))
        if node:
            text = node[0]
        assert text != kargs.get('context', None), self.__format(kargs.get('message', None), kargs.get('context', None),
                                                                 text)

    def check_nodeText_startswith(self, kargs):
        text = None
        node = self.__get_value_from_path(kargs.get('node_path', None))
        if node:
            text = node[0]
        assert text.startswith(kargs.get('context', None)) == True, self.__format(kargs.get('message', None),
                                                                                  kargs.get('context', None), text)

    def check_nodeText_contains(self, kargs):
        text = None
        node = self.__get_value_from_path(kargs.get('node_path', None))
        if node:
            text = node[0]
        assert kargs.get('context', None) in text, self.__format(kargs.get('message', None), kargs.get('context', None),
                                                                 text)

    def check_nodes_count(self, kargs):
        nodes = self.__get_value_from_path(kargs.get('node_path', None))
        if nodes:
            assert len(nodes) == kargs.get('count', None), self.__format(kargs.get('message', None),
                                                                         kargs.get('count', None), len(nodes))
        else:
            assert False, self.__format(kargs.get('message', None), kargs.get('count', None), None)

    def transfer(self, path):
        value = None
        try:
            json_object = self.response.json()
            object = jsonpath.jsonpath(json_object, path)
            if object:
                value = object[0]
        except Exception as e:
            print(e)

        return value

    @classmethod
    def exctue_sql(cls, sql):
        config = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "db": "demo",
            "charset": "utf8"
        }
        try:
            connection = pymysql.connect(**config)
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchone()[0]
        except Exception as e:
            return e

    def check_db(self, kargs):
        node = self.__get_value_from_path(kargs.get('node_path', None))
        sql = kargs.get('sql', None)
        result = self.exctue_sql(sql)
        message = kargs.get('message', None)
        if node:
            assert node[0] == result, self.__format(message, node, result)
        else:
            assert False, self.__format(kargs.get('message', None), kargs.get('count', None), None)
