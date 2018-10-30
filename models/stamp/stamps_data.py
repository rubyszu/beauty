# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models.model import Model
from jinja2 import Environment
import json

class StampsData(Model):
	def __init__(self):
		super(StampsData,self).__init__("stamp","stamps_data","post")

	#构造请求参数
	def getRequestParam(self,code,errcode=""):
		test_data = loadFile("test_data/%s/project/auth/login.yaml" %(branch))
		sets_of_params = findNode(test_data,code + errcode)
		#获取请求参数模板
		env = Environment()
		template = env.from_string(json.dumps(self.getTemplate(code,errcode)))
		#构造请求参数
		params = []
		for i in sets_of_params:
			params.append(json.loads(str(template.render(context = i))))
		return params

if __name__ == '__main__':
	login = Login()
	print login.getRequestParam('200')