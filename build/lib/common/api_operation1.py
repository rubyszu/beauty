# -*- coding: utf-8 -*-
from common import loadFile,findNode,findNodeByList
from common.http_base import httpBase
import json,jsonref
import requests
from jsonschema import validate
import re

class ApiOperation:
	def __init__(self,module,path,method,product="project"):
		schema = loadFile("./api_schema/api/%s/%s.yaml" %(product,module))
		self.product = product
		self.path = path
		self.method = method
		node = ["paths",self.path,self.method]
		self.api_operation = findNodeByList(schema,node)

	def getApiUrl(self):
		http_base = httpBase()
		self.api_url = "%s/%s/%s%s" %(http_base["host"],self.product,http_base["branch"],self.path)
		return(self.api_url)

	#从yaml取有边界值的参数
	'''
		spec_params = {
			'issue_type_name': {
				"type": "string",
				'maxLength': 14, 
				'minLength': 1
			}, 
			'field018': {
				"type": "int",
				'maximum': 100, 
				'minimum': 1
			}	
		}	
	'''
	def getSpecialParam(self):
		#query
		special_params = {}
		if self.api_operation.has_key("parameters"):
			parameters = self.api_operation["parameters"]
			special_params.update(self.getSpecialParamConfig("query",parameters))

		#request body
		request_params = []
		node = ["requestBody","schema"]
		request_body = findNodeByList(self.api_operation,node)
		if request_body != None:
			if response_schema.has_key("oneOf"):
				break
			else:
				request_params = request_body["properties"]
				special_params.update(self.getSpecialParamConfig("body",request_params))
				
		return special_params

	def getSpecialParamConfig(self,param_type,parameters):
		special_params = {}
		for i in range(len(parameters)):
			parameter = parameters[i]

			if param_type == "query" and (not parameter.has_key("in") or (parameter["in"] and parameter["in"] != "query")):
				continue

			param = parameter["name"]
			param_schema = parameter["schema"]

			if not param_schema.has_key("type") or ( param_schema["type"] and param_schema["type"] not in ("int","string")):
				continue

			if param_schema["maxLength"] > param_schema["minLength"] or param_schema["maximum"] > param_schema["minimum"]:
				value = {key:value for key,value in param_schema.items() if key in ("type","maximum","minimum","maxLength","minLength")}
				spec_params.update({param: value})

		return special_params

	#对有边界值的参数构造多组数据
	#{{'issue_type_name': ['T', 'W8', 'OtcfY8ok1s292b'],'field018': ['1', '2', '10']}
	def buildSetsOfSpecialParams(self,special_params):
		special_params = self.getSpecialParam()
		if not special_params:
			return None
		keys,values = special_params.keys(),special_params.values()
		sets_of_special_params = {}
		for i in range(len(valuges)):
			spec_item = values[i]
			value = []
			if spec_item["type"] == "string":
				value.extend(randomStringArr(spec_item["minLength"],spec_item["maxLength"]))
			elif spec_item["type"]  == "int":
				value.extend(randomNumArr(spec_item["minimum"], spec_item["maximum"]))
			sets_of_special_params.update({keys[i]:value})
		return sets_of_special_params

	def ReplaceApiUrl(self,params):
		path_rex = re.compile(r'\{([^\}]*)\}')
  		path_params = re.findall(path_rex, self.api_url)
  		for i in range(len(path_params)):
  			path_param = path_params[i]
  			self.api_url = self.api_url.replace('{%s}'% path_param, params[path_param])
  		return self.api_url

	def getResponseSchema(self,status_code,errCode=None):
		node = ["responses",status_code,"schema"]
		response_schema = findNodeByList(self.api_operation,node)
		if response_schema.has_key("oneOf"):
			for i in range(len(response_schema["oneOf"])):
				err = findNode(response_schema["oneOf"][i],"errcode")
				if err != None and err.get("enum")[0] == errcode:
					response_schema = response_schema["oneOf"][i]
					break
		return response_schema

	def sendRequest(self,param):
		self.api_url = self.getApiUrl()
		#headers
		if param.has_key("headers"):
			param["headers"]["Content-Type"] = "application/json"
		else:
			param["headers"] = {"Content-Type": "application/json"}
		#path
		if self.api_operation.has_key("parameters"):
			for i in range(len(self.api_operation["parameters"])):
				if self.api_operation["parameters"][i].has_key("in") and self.api_operation["parameters"][i]["in"] == "path":
					path_params = param["path_params"]
					self.api_url = self.ReplaceApiUrl(path_params)
					del param["path_params"]
	
		response = requests.request(self.method,self.api_url,**param)
		return response

	def sendRequestAndValidate(self,param,status_code,errcode=None):
		response = self.sendRequest(param)
		response_schema = getResponseSchema(status_code,errcode=None)
		validate(response.json(),response_schema)
