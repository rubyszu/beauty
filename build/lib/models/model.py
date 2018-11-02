# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models import *
from models.compose import compose
from models.context import Context
import sys
import time,itertools,json
from datetime import datetime
from jinja2 import Environment

class Model(object):
	def __init__(self,module,operation,method,product="project"):
		self.api_operation = ApiOperation(module,operation,method,product)
		self.templates = loadFile("./template/%s/%s.yaml" %(module,operation))
		self.dependent_models = self.getDependentModels()

	'''
		string to Class
		eg. ["Login","IssueTypeAdd"] -> [<class 'models.auth.login.Login'>,<class 'models.issue_type.issue_type_add.IssueTypeAdd'>]
	'''
	def str2Class(self):
		dependent_models = self.templates["dependent_model"]
		new_arr = []
		if not len(dependent_models):
			return []
		for i in range(len(dependent_models)):
			new_arr.append(getattr(sys.modules[__name__], dependent_models[i]))
		return new_arr

	'''
		递归查询API依赖的所有接口列表，按API执行顺序返回
	'''
	def getDependentModels(self):
		dependent_models = self.str2Class()
		if not dependent_models:
			return []

		all_dependent_models = [];

		for i in range(len(dependent_models)):
			dependent_model = dependent_models[i]()
			all_dependent_models.extend(dependent_model.getDependentModels())

		all_dependent_models.extend(dependent_models)
		
		return all_dependent_models

	'''
		返回API依赖的接口列表所需要的compose函数
	'''
	def getDenpendentApiList(self):
		if not self.dependent_models:
			return []

		dependent_api_list = []
		for i in self.dependent_models:
			dependent_api_list.append(i().sendSuccessRequestByRandomParam)
		return dependent_api_list

	#获取errcode对应的接口模板
	def getTemplate(self,code,errcode = ""):
		template = self.templates[code+errcode]
		return template

	#构造有边界值的请求参数
	def buildSpecialParam(self,code,errcode = ""):
		#构造有边界值的参数
		special_params = self.api_operation.getSpecialParam()
		# sets_of_special_params = iterator(special_params)

		# params = []

		# return params

	def saveToContext(self, response):
		# 业务 model 需要自己判断要存哪些数据 后续可写在模板里面
		return response;

	#API需要判断是否使用全局变量文件的数据
	def isInContext(self, context):
		#默认使用全局变量文件的数据
		return True;

	#构造请求参数
	def buildParam(self,code,errcode = "",context = {}):
		#special_param
		special_params = self.buildSpecialParam(code,errcode)
		env = Environment()
		template = env.from_string(json.dumps(self.getTemplate(code,errcode)))
		params = json.loads(str(template.render(context = context.data,special_params = special_params)))
		return params

	#获取请求需要的参数
	def getRequestParam(self,code,errcode = "",context = Context()):
		if not self.isInContext(context):
			print("~~~~ not use context")
			runner = compose(self.getDenpendentApiList())
			runner(context)
		
		params = self.buildParam(code,errcode,context)
		context.write()
		return params

	#发送成功的请求，保存有效数据到context和全局变量文件，给其他接口使用
	def sendSuccessRequestByRandomParam(self,context = {}):
		params = self.getRequestParam("200")
		ramdom_request_param = randomItem(params)
		response = self.sendRequest(ramdom_request_param).json()
		context.update(self.saveToContext(response))
		return context

	#发送请求
	def sendRequest(self,param):
		return self.api_operation.sendRequest(param)

	#验证response的数据结构
	def validateResponse(self,response,status_code,errcode = ""):
		return self.api_operation.validateResponse(response,status_code,errcode)

if __name__ == '__main__':
	# login = Model("auth","login","post")
	token_info = Model("auth","token_info","get")
	print token_info.str2Class()
	# token_info.getDenpendentApiList()
	token_info.getRequestParam("200")

    	