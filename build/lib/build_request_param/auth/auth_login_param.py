# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
import json

class AuthLoginParam():
	def __init__(self):
		branch = httpBase()["branch"]
		self.variable = loadFile("test_data/%s/project/auth/auth_login.json" %(branch))

	def authLogin200Param(self,key):
		data = findNode(self.variable,key)
		if key == "200":
			param = {}
			param["json"] = data
			return param
		else:
			param = []
			for i in range(len(data)):
				param.append({"json":data[i]})
			return param

	def authLogin400()

if __name__ == '__main__':
	a = AuthLoginParam()
	print a.authLoginParam("200")
