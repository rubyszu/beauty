# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
import time,itertools,json
from datetime import datetime
from jinja2 import Template

class Model():

	def __init__(self,module,path,method,product="project"):
		self.apiOperation = ApiOperation(module,path,method,product)
		self.has_send_request = False

	def sendRequest(self,param):
		self.apiOperation.sendRequest(param)

	def getTemplate(self,code,errcode=""):
		pass

	def buildParam(self,code,errcode="",context):
		template = Template(self.getTemplate(code,errcode))
		# special_params = self.buildSetsOfSpecialParams()

		keys,values = special_params.keys(),special_params.values()
		sets_params = list(itertools.product(*values))

		sets_data_params = []
		for i in range(len(sets_params)):
			value = sets_params[i]
			sets_data = {}
			for j in range(len(value)):
				sets_data[keys[j]] = value[j]
			sets_data_params.append(sets_data)

		# templates = [template.render(context=context, special_params=special_param) for sets_param in sets_data_params]
		params = []
		for sets_param in sets_data_params:
			templates.append(template.render(context=context, special_params=special_param))

		return patams

	def getRequestParam(self,code,errcode="",context={}):
		if not context and self.has_send_request:
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
    	self.has_send_request = True
    	return context

    def sendRequestAndValidate(self,param,status_code,errcode):
    	self.apiOperation.sendRequestAndValidate(param,status_code,errcode)
    	