# -*- coding: utf-8 -*-
from common import loadFile,findNode,findNodeByList
from common.http_base import httpBase
import json,jsonref
import requests
from jsonschema import validate
import re

class ApiOperation(ParseApiYaml):
	def __init__(self,module,path,method,product="project"):
        super(ParseApiYaml, self).__init__(module,path,method,product)

	def ReplaceApiUrl(self,api_url,params):
		path_rex = re.compile(r'\{([^\}]*)\}')
  		path_params = re.findall(path_rex, self.api_url)
  		for i in range(len(path_params)):
  			path_param = path_params[i]
  			api_url = api_url.replace('{%s}'% path_param, params[path_param])
  		return api_url

  	'''
  		param:
			#如果path有参数，需要传"path_params"
			
  	'''
  	@thread(5)
	def sendRequest(self,param):
		api_url = self.getApiUrl()
		method = self.getMethod()
		#headers
		if param.has_key("headers"):
			param["headers"]["Content-Type"] = "application/json"
		else:
			param["headers"] = {"Content-Type": "application/json"}
		#path
		if self.api_config.has_key("parameters"):
			for i in range(len(self.api_config["parameters"])):
				if self.api_config["parameters"][i].has_key("in") and self.api_config["parameters"][i]["in"] == "path":
					path_params = param["path_params"]
					api_url = self.ReplaceApiUrl(api_url,path_params)
					del param["path_params"]
	
		response = requests.request(method,api_url,**param)
		return response

	def sendRequestAndValidate(self,param,status_code,errcode=None):
		reponse = self.sendRequest(param)
		response_schema = super(ParseApiYaml,self).getResponseSchema(status_code,errcode)
		validate(response.json(),response_schema)
