# -*- coding: utf-8 -*-
import json
import os
from common.http_base import httpBase
from common import loadFile

# 1. 读内存
# 2. 永久化 - 读写文件

## @todo 判断有没有数据存在 从 template 识别
'''
	1.构造参数时，如果需要从文件读数据，先读文件；不用读数据，直接构造参数
		1.1如果文件包含所有字段，直接取
		1.2如果文件不包含所有字段，先执行dependent model
			2.1存context，写入文件
			2.2用context的数据构造参数

'''
class Context(object):
	def __init__(self):
		self.data = self.read()

	def read(self):
		#文件路径
		branch = httpBase()["branch"]
		self.file = "./test_data/%s/global_variable.json" %(branch)
		#当文件不存在时，创建相同路径的文件名
		if not os.path.exists(self.file):
			open(self.file,"w").close()
			return {}
		#加载文件
		else:
			#文件为空
			if not os.path.getsize(self.file):
				return {}
			#文件有内容
			else:
				data = loadFile(self.file)
				return data

	def write(self):
		data = json.dumps(self.data, indent=2)
		with open(self.file, 'w') as f:
			f.write(data)

	def update(self, data):
		self.data.update(data)
		# for key,value in data.items():
		# 	#当key不在self.data中
		# 	if key not in self.data.keys():
		# 		self.data.update({key:value})
		# 	#当key在self.data中
		# 	else:
		# 		self.data[key].update(value)

if __name__ == '__main__':
	context = Context()
	context.update({"name":"sam"})
	context.write()
	print context.data


