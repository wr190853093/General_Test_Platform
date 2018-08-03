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
        ch = {}
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


if __name__ == '__main__':
    print(validate_ip('192.13.13.1232'))