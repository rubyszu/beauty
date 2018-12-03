# -*- coding: utf-8 -*-
import json
import os
# from util.http_base import httpBase
from util.loader import loadSchema

# 1. 读内存
# 2. 永久化

class Context(object):
	def __init__(self, cli_args):
		self.cli_args = cli_args
		self.branch = self.cli_args["branch"]
		self.data = self.read()

	#获取文件内容
	def read(self):
		data = {}

		#文件路径
		self.file = "./test_data/{}/global_variable.json".format(self.branch)
		
		#当文件不存在时，创建相同路径的文件名
		if not os.path.exists(self.file):
			open(self.file,"w").close()

		#当文件存在且内容不为空时，加载文件
		elif os.path.getsize(self.file):
			file_data = loadSchema(self.file)
			data.update(file_data)
		
		#加载test_data的数据
		test_data = loadSchema("test_data/{}/project/auth/login.yaml".format(self.branch))
		data.update(test_data)

		#加载cli_args
		data.update({ "cli_args": self.cli_args })
		return data

	#将更新后的内容写入文件
	def sync(self):
		if "cli_args" in self.data:
			del self.data["cli_args"]
		data = json.dumps(self.data, indent=2)
		with open(self.file, 'w') as f:
			f.write(data)



