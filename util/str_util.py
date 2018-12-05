#  -*- coding: utf-8 -*-
import re

# 传入参数，替换{args}
def replaceString(string, params):
	'''
	Args:
		string(str): 需要替换的字符串
		params(dict): 参数
	'''
	path_rex = re.compile(r'\{([^\}]*)\}')
	path_params = re.findall(path_rex, string)

	for i in path_params:
		string = string.replace('{%s}' %i, params[i])

	return string

# combine string
def spliceString(*string_list):
	'''
	Args:
		string_list(list): a list of string
	'''
	string = "/".join(string_list)
	return string
