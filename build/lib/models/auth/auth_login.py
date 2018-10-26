# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *

class AuthLogin(Model):
	def __init__(self):
		super(Model,self).__init__("auth","/auth/login","post")

	def getTemplate(self,code,errcode=""):
		pass

	#构造请求参数
	def getRequestParam(self,code,errcode=""):
		branch = httpBase()["branch"]
		variable = loadFile("test_data/%s/project/auth/auth_login.json" %(branch))
		data = findNode(variable,code + errcode)
		params = []
		for i in range(len(data)):
			params.append({"json":data[i]})
		return params
    	