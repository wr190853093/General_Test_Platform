import json


# 判断字符串是否为有效ip（可以传带端口的字符串）
def validate_ip(ip_str):
    if ip_str.find(':'):
        ip_str = ip_str.split(':')[0]
    sep = ip_str.split('.')
    if len(sep) != 4:
        return False
    for i, x in enumerate(sep):
        try:
            int_x = int(x)
            if int_x < 0 or int_x > 255:
                return False
        except ValueError:
            return False
    return True


# 获取子节点数据
def get_child(parent, result={}, data={}, node=[]):
    child = parent.get_children().filter(is_del=1, tree_id=parent.tree_id)
    for c in child:
        ch = dict()
        ch['child_name'] = c.name
        ch['id'] = c.id
        ch['parent_id'] = c.parent_id
        node.append(ch)
        if c.get_children().filter(is_del=1).exists():
            get_child(c, node=node)
    data['parent_id'] = parent.id
    data['parent_name'] = parent.name
    result['parent'] = data
    result['node'] = node
    return result


# 获取动态过滤条件

def getkwargs(data={}):
    kwargs = {}

    for (k, v) in data.items():

        if v is not None and v != u'':
            kwargs[k] = v

    return kwargs


# 将字符串中{{}}参数处理后，返回字典
def replacetodic(str, dic):
    start_index = str.find('{{')
    end_index = str.find('}}')
    while start_index != -1:
        str = str.replace(str[start_index:end_index + 2], dic.get(str[start_index + 2:end_index]))
        start_index = str.find('{{')
        end_index = str.find('}}')
    result = json.loads(str)
    return result

if __name__ == '__main__':
    print(validate_ip('192.13.13.1232'))
