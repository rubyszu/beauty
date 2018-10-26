# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *

class AuthLogin(Model):
	def __init__(self):
		super(Model,self).__init__("auth","/auth/login","post")
	#构造请求参数
	def getRequestParam(self,code,errcode=""):
		branch = httpBase()["branch"]
		sets_of_params = loadFile("test_data/%s/project/auth/auth_login.yaml" %(branch))
		params = findNode(sets_of_params,code + errcode)
		
		# request_params = []
		
		# for i in range(len(params)):
		# 	request_params.append({"json":params[i]})
		
		# return request_params
		return params
    	