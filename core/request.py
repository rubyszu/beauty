# -*- coding: utf-8 -*-
from box import Box
import requests
from util.http_base import httpBase
from util.dict_util import assign_value
from util.replace_str import replaceString
from resolve_stage import getStage
from context.compose import compose
from response import saveParamsToContext

class Request(object):
	def __init__(self, stage):
		self.stage = stage
		self.dependent_stage_list = self.getDependentStageList()

	def getDependentStageList(self):
		'''
			return: 依赖的stage列表
		'''
		dependent_api_list = self.resolveDependentApiList()
		dependent_api_list.reverse()

		api_list_dict = {}
		stage_list = []
		for i in dependent_api_list:
			if i not in api_list_dict:
				api_list_dict.update({i: i})
				stage_list.append(getStage(i))
		
		return stage_list

	def resolveDependentApiList(self): 
		dependent_api = self.stage.variables.request.dependent_api
		if not dependent_api:
			return []

		dependent_api_list = dependent_api
		for i in dependent_api:
			dependent_stage = Request(getStage(i))
			dependent_api_list.extend(dependent_stage.getDependentStageList())
		
		return dependent_api_list

	def getApiUrl(self, context):
		'''
		Args:
			stage(dict): stage
			context(dict): context
		'''
		http_base = Box(httpBase(context["cli_args"]))
		host = http_base.host
		branch = http_base.branch

		request = self.stage.variables.request
		product = request.product
		path = request.path
		api_url = "{}/{}/{}{}".format(host, product, branch, path)
		
		request_schema = self.stage.stage.request
		#处理api URL中包含path parameters的情况
		if "path_params" in request_schema:
			api_url = replaceString(api_url, context)
			del request_schema.path_params

		return api_url

	def buildRequestParam(self, context):
		'''
		Args:
			stage(dict): stage
			context(dict): local+presist
		'''
		request = self.stage.stage.request

		if self.stage.variables.request.method == "post": 
			headers = {"Content-Type": "application/json"}
			if "headers" in request:
				request.headers.update(headers)
			else:
				request.update({"headers": headers})
		
		request_params = assign_value(request, context = context)

		return request_params

	def getRequestParam(self, context):
		'''
		Args:
		context(dict): context
		'''
		dependent_stage_list = self.getDependentStageList()
		dependent_stage_send_request_list = [Request(i).sendSuccessRequest for i in dependent_stage_list]
		runner = compose(dependent_stage_send_request_list)
		runner(context)

		params = self.buildRequestParam(context)

		return params

	def sendRequest(self, context):
		'''
		Args:
			request_params 
		'''
		request_params = self.getRequestParam(context)
		method = self.stage.variables.request.method
		api_url = self.getApiUrl(context)

		response = requests.request(method,api_url,**request_params)
		#request
		request = self.stage.stage.request
		response_json = response.json()

		self.stage = assign_value(self.stage, request = request, response = response.json())
		return self.stage, response

	# 判断API需要的请求参数是否在context
	def isParamsInContext(self, context):
		save = self.stage.save
		flag = True
		if "save" not in self.stage:
			return flag

		key_list = []
		for key in save.keys():
			if key not in context:
				flag = False
				break

		return flag

	#发送成功的请求并保存数据到context，给其他接口使用
	def sendSuccessRequest(self, context):
		if self.isParamsInContext(context):
			return context

		request_params = self.getRequestParam(context)
		stage, response = self.sendRequest(context)
		saveParamsToContext(self.stage, context)

		return context




