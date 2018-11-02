# -*- coding: utf-8 -*-
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
		elif type(_value) in [dict, jsonref.JsonRef]:
			for _k, _v in _value.items():
				queue.append((_k, _v))

	return None

def findNodeByList(data,arr):
	for i in range(len(arr)):
		data = findNode(data,arr[i])
		if data == None:
			break
	return data

if __name__ == '__main__':
	d = {
		"config": {
			"name": "ruby11",
			"age":18
		},
		"name": "ruby",
	}
	print findNode(d,"name")


