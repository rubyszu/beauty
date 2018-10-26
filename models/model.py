# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
import time,itertools,json
from datetime import datetime
from jinja2 import Environment

class Model():

	def __init__(self,module,path,method,product="project"):
		self.apiOperation = ApiOperation(module,path,method,product)
		self.dependent_models = []

	def str2Class(self):
		new_arr = []
		if not len(self.dependent_models):
			return []
		for i in range(len(self.dependent_models)):
			new_arr.append(getattr(sys.modules[__name__], self.dependent_models[i]))
		return new_arr

	def get_dependent_models(self):
		self.dependent_models = self.str2Class()
		if not len(self.dependent_models):
			return []

		all_dependent_models = [];

		for i in range(len(self.dependent_models)):
			dependent_model = self.dependent_models[i]()
			all_dependent_models.extend(dependent_model.get_dependent_models())

		all_dependent_models.extend(self.dependent_models)
		
		return all_dependent_models

	def sendRequest(self,param):
		self.apiOperation.sendRequest(param)

	def getTemplate(self,code,errcode=""):
		pass

	def buildParam(self,code,errcode="",context):
		#自定义jinja2 filter
		env = Environment()
		env.filters['randomString'] = randomString
		env.filters['randomNum'] = randomNum
		#获取构造请求参数模板
		template = env.from_string(self.getTemplate(code,errcode))
		#构造有边界值的参数
		special_params = self.ApiOperation.getSpecialParam()
		sets_of_special_params = randomSetsOfSpecialParams(special_params)

		params = []
		for sets_param in sets_of_special_params:
			templates.append(template.render(context=context, special_params=sets_param))

		return params

	def getRequestParam(self,code,errcode="",context={}):
		if not context:
			dependent_api_list = [AuthLogin().sendSuccessRequestByRandomParam]
			runner = compose(dependent_api_list)
			context = runner({})

		params = self.buildParam(code,errcode,context)
		return params
    	

    def sendSuccessRequestByRandomParam(self,context):
    	params = self.getRequestParam(200,context);
    	ramdom_request_param = Generate().randomArray(params)
    	response = self.sendRequest(ramdom_request_param).json()
    	context.update(response)
    	
    	return context

    def sendRequestAndValidate(self,param,status_code,errcode):
    	self.apiOperation.sendRequestAndValidate(param,status_code,errcode)
    	