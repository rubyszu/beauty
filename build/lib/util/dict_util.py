# -*- coding: utf-8 -*-
from core.extension import get_wrapped_create_function
import jsonref

#给定一个字典类型的数据，深度优先查询是否有某个字段
def findNode(data, key):
    queue = [("", data)]
    while len(queue) > 0:
        _key, _value = queue[0]
        queue = queue[1:]
        if _key == key:
            return _value
        #jsonref解析带有$ref的json后变成jsonref.JsonRef类型，所以加入这个类型的判断
        # type(_value) in [dict, jsonref.JsonRef]
        elif isinstance(_value,(dict,jsonref.JsonRef)):
            for _k, _v in _value.items():
                queue.append((_k, _v))

    return None

def findNodeByList(data,arr):
    for i in range(len(arr)):
        data = findNode(data,arr[i])
        if data == None:
            break
    return data

def recurse_access_key(current_val, keys):
    """ Given a list of keys and a dictionary, recursively access the dicionary
    using the keys until we find the key its looking for

    If a key is an integer, it will convert it and use it as a list index

    Example:

        >>> recurse_access_key({'a': 'b'}, ['a'])
        'b'
        >>> recurse_access_key({'a': {'b': ['c', 'd']}}, ['a', 'b', '0'])
        'c'

    Args:
        current_val (dict): current dictionary we have recursed into
        keys (list): list of str/int of subkeys

    Returns:
        str or dict: value of subkey in dict
    """
    if not keys:
        return current_val
    else:
        current_key = keys.pop(0)

        try:
            current_key = int(current_key)
        except ValueError:
            pass

        return recurse_access_key(current_val[current_key], keys)

def isfotmat(string, **to_check):

    flag = False

    split_list = string.split(".")
    if "." in string and split_list[0] in to_check:
        flag = True

    return flag

def assign_value(expected, **to_check):
    """Save a value in the response for use in future tests

    Args:
        expected (dict or list): expected saved dict
        to_check (dict): An element of the response from which the given key
            is extracted
        

    Returns:
        dict: dictionary of save_name: value, where save_name is the key we
            wanted to save this value as
    """
    if not to_check:
        return None;

    expected_type = type(expected)

    #dict
    if isinstance(expected, dict):
        saved = {}
        for save_as, joined_key in expected.items():
            #处理赋值的情况
            if isinstance(joined_key, str) and isfotmat(joined_key, **to_check):
                split_key = joined_key.split(".")
                saved[save_as] = recurse_access_key(to_check, split_key)
            #dict
            elif isinstance(joined_key, dict):
                saved[save_as] = assign_value(joined_key, **to_check)

                #处理注入函数的情况
                if joined_key.has_key("$ext"):
                    ext = joined_key["$ext"]
                    saved[save_as] = get_wrapped_create_function(ext)

            #list in dict
            elif isinstance(joined_key, list):
                saved[save_as] = assign_value(joined_key, **to_check)

            expected.update(saved) 
            
    #list
    if isinstance(expected, list):
        for i in range(len(expected)):
            if isinstance(expected[i], str) and isfotmat(expected[i], **to_check):
                split_key = expected[i].split(".")
                expected[i] = recurse_access_key(to_check, split_key)

            elif isinstance(expected[i], dict):
                expected[i] = assign_value(expected[i],**to_check)

        return expected

    return expected