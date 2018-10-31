# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
import time,itertools,json
from datetime import datetime
from jinja2 import Environment

class Model(object):
	def __init__(self,module,operation,method,product="project"):
		self.api_operation = ApiOperation(module,operation,method,product)
		self.templates = loadFile("./template/%s/%s.yaml" %(module,operation))
		self.dependent_models = self.templates["dependent_model"]

	def str2Class(self):
		new_arr = []
		if not len(self.dependent_models):
			return []
		for i in range(len(self.dependent_models)):
			new_arr.append(getattr(sys.modules[__name__], self.dependent_models[i]))
		return new_arr

	def getDependentModels(self):
		self.dependent_models = self.str2Class()
		if not len(self.dependent_models):
			return []

		all_dependent_models = [];

		for i in range(len(self.dependent_models)):
			dependent_model = self.dependent_models[i]()
			all_dependent_models.extend(dependent_model.get_dependent_models())

		all_dependent_models.extend(self.dependent_models)
		
		return all_dependent_models

	#获取errcode对应的接口模板
	def getTemplate(self,code,errcode = ""):
		template = self.templates[code+errcode]
		print type(template)
		return template

	#构造请求参数
	def buildSpecialParam(self,code,errcode = "",context = {}):
		#构造有边界值的参数
		valid_values = self.api_operation.getSpecialParam()
		# sets_of_special_params = randomSetsOfSpecialParams(valid_values)

		# params = []
		# for sets_param in sets_of_special_params:
		# 	templates.append(template.render(context = context, special_params = sets_param))
		# params = template.render(context = context)

		# return params

	#获取请求需要的参数
	def getRequestParam(self,code,errcode="",context={}):
		if not context:
			dependent_api_list = [AuthLogin().sendSuccessRequestByRandomParam]
			runner = compose(dependent_api_list)
			context = runner({})

		params = self.buildParam(code,errcode,context)
		return params

	def sendSuccessRequestByRandomParam(self,context):
		params = self.getRequestParam(200,context)
		ramdom_request_param = Generate().randomArray(params)
		response = self.sendRequest(ramdom_request_param).json()
		context.update(response)
		return context

	#发送请求
	def sendRequest(self,param):
		return self.apiOperation.sendRequest(param)

	#验证response的数据结构
	def validateResponse(self,response,status_code,errcode = ""):
		return self.apiOperation.validateResponse(response,status_code,errcode)

if __name__ == '__main__':
	# login = Model("auth","login","post")
	login = Model("auth","query_test","get")
	login.buildParam(200)

    	