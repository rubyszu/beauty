# -*- coding: utf-8 -*-
import json
import os
from common.http_base import httpBase
from common import loadFile

# 1. 读内存
# 2. 永久化 - 读写文件

class Context(object):
	def __init__(self):
		self.data = self.read()

	#获取文件内容
	def read(self):
		#文件路径
		branch = httpBase()["branch"]
		self.file = "./test_data/%s/global_variable.json" %(branch)
		#当文件不存在时，创建相同路径的文件名
		if not os.path.exists(self.file):
			open(self.file,"w").close()
			return {}
		#当文件存在时，加载文件
		else:
			#如果文件为空，返回
			if not os.path.getsize(self.file):
				return {}
			#如果文件有内容，转换成dictionary后返回
			else:
				data = loadFile(self.file)
				return data

	#将更新后的内容写入文件
	def write(self):
		data = json.dumps(self.data, indent=2)
		with open(self.file, 'w') as f:
			f.write(data)

	#更新文件内容
	def update(self, data):
		self.data.update(data)
		self.write()

if __name__ == '__main__':
	context = Context()
	context.update({"name":"sam"})
	context.write()
	print context.data


