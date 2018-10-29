# -*- coding: utf-8 -*-
# from common import ParseApiYaml
from common.parse_api_yaml import ParseApiYaml
from common.http_base import httpBase
import json,jsonref
import requests
from jsonschema import validate
import re

class ApiOperation:
	def __init__(self,module,operation,method,product="project"):
		self.ApiYaml = ParseApiYaml(module,operation,method,product)
        # super(ParseApiYaml, self).__init__(module,path,method,product)

    #当api url包含path参数，需要传入参数替换成新的api url
	def ReplaceApiUrl(self,api_url,params):
		path_rex = re.compile(r'\{([^\}]*)\}')
  		path_params = re.findall(path_rex, self.api_url)
  		for i in range(len(path_params)):
  			path_param = path_params[i]
  			api_url = api_url.replace('{%s}'% path_param, params[path_param])
  		return api_url

  	'''
  		param:
 			#请求接口需要的参数
			#如果path有参数，需要传"param.path_params"
			
  	'''
	def sendRequest(self,param):

		# api_url = self.getApiUrl()
		api_url = self.ApiYaml.getApiUrl()
		# method = self.getMethod()
		method = self.ApiYaml.getMethod()
		#api_config
		api_config = self.ApiYaml.api_config

		#headers
		if param.has_key("headers"):
			param["headers"]["Content-Type"] = "application/json"
		else:
			param["headers"] = {"Content-Type": "application/json"}
		#path
		if api_config.has_key("parameters"):
			for i in range(len(api_config["parameters"])):
				if api_config["parameters"][i].has_key("in") and api_config["parameters"][i]["in"] == "path":
					path_params = param["path_params"]
					api_url = self.ReplaceApiUrl(api_url,path_params)
					del param["path_params"]
	
		response = requests.request(method,api_url,**param)
		# print response.status_code
		# print response.json()
		return response

	def validateResponse(self,response,status_code,errcode = ""):
		print response
		print response.json()
		# response_schema = super(ParseApiYaml,self).getResponseSchema(status_code,errcode)
		response_schema = self.ApiYaml.getResponseSchema(status_code,errcode)
		validate(response.json(),response_schema)

if __name__ == '__main__':
	auth_login = ApiOperation("auth","login","post")
