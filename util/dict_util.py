# -*- coding: utf-8 -*-
from core.extension import get_wrapped_create_function
import jsonref
import collections

def mergeDict(target, expected):
    '''Given two dict, recursively access the dicionary, merge to one dict
    Args:
        target(dict): the target dict
        expected(dict): a dict wants to merge into target

    '''
    for key, value in expected.iteritems():
        if isinstance(value, collections.Mapping):
            replace_value = mergeDict(target.get(key, {}), value)
            target[key] = replace_value
        else:
            target[key] = expected[key]
    return target

# 给定一个字典类型的数据，深度优先查询是否有某个字段
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
                    ext = assign_value(joined_key["$ext"], **to_check)
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

if __name__ == '__main__':
    d = {
      "project": {
        "issue_types": {
          "$ext": {
            "function": "util.save_value:saveSetsOfList",
            "extra_kwargs": {
              "check_list": "response.issue_type_configs",
              "save_key": "issue_type_uuid",
              "project_uuid": "context.project.uuid"
            }
          }
        }
      }
    }
    response = {
        "issue_type_configs": [
            {
                "project_uuid": "8yhRWBazBu4cW8ee",
                "issue_type_uuid": "52hNsC6o"
            },
            {
                "project_uuid": "8yhRWBazrwtHHTFO",
                "issue_type_uuid": "PVRsTwjE"
            },
            {
                "project_uuid": "8yhRWBazBu4cW8ee",
                "issue_type_uuid": "PkLcqK56"
            },
            {
                "project_uuid": "8yhRWBazrwtHHTFO",
                "issue_type_uuid": "Cc3AK2XL"
            }
        ]
    }
    context = {
        "project": {
            "status": 1, 
            "announcement": "", 
            "uuid": "8yhRWBazrwtHHTFO", 
            "status_category": "to_do", 
            "is_open_email_notify": False, 
            "status_uuid": "to_do", 
            "deadline": 0, 
            "is_pin": False, 
            "task_update_time": 0, 
            "assign": "8yhRWBaz", 
            "name": "8H3pXXnxjL3IfrLx0nN6uAH6aBxSS3i1"
        }
    }

    a = assign_value(d, response = response, context = context)
    print a









