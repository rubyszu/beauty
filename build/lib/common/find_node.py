# -*- coding: utf-8 -*-
import jsonref

def findNode(data, key):

	queue = [("", data)]
	while len(queue) > 0:
		_key, _value = queue[0]
		queue = queue[1:]
		if _key == key:
			return _value
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


