# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models.model import Model
from jinja2 import Environment
import json

class Login(Model):
	def __init__(self):
		super(Login,self).__init__("auth","login","post")
	
	#构造请求参数
	def getRequestParam(self,code,errcode=""):
		#从test_data文件中读取login数据
		branch = httpBase()["branch"]
		test_data = loadFile("test_data/%s/project/auth/login.yaml" %(branch))
		sets_of_params = findNode(test_data,code + errcode)
		print sets_of_params
		#获取请求参数模板
		env = Environment()
		template = env.from_string(json.dumps(self.getTemplate(code,errcode)))
		#构造请求参数
		params = []
		for i in sets_of_params:
			params.append(json.loads(str(template.render(context = i))))
		return params

	#请求成功后保存有效数据到context
	# def sendSuccessRequestByRandomParam(self,context):
	# 	params = self.getRequestParam(200)
	# 	ramdom_request_param = Generate().randomArray(params)
	# 	response = self.sendRequest(ramdom_request_param).json()
	# 	context.update(response)
	# 	return context

if __name__ == '__main__':
	login = Login()
	print login.getRequestParam('200')
    	