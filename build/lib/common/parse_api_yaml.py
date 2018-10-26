# -*- coding: utf-8 -*-
from common import loadFile,findNode,findNodeByList
from common.http_base import httpBase
import json,jsonref
import requests
from jsonschema import validate
import re

class ParseApiYaml:
	def __init__(self,module,path,method,product="project"):
		schema = loadFile("./api_schema/api/%s/%s.yaml" %(product,module))
		self.product = product
		self.path = path
		self.method = method
		node = ["paths",self.path,self.method]
		self.api_config = findNodeByList(schema,node)

	def getMethod(self):
		return self.method

	def getApiUrl(self):
		http_base = httpBase()
		api_url = "%s/%s/%s%s" %(http_base["host"],self.product,http_base["branch"],self.path)
		return(api_url)

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
		'''
			path 和 header，目前暂不需要
		'''
		#query
		special_params = {}
		if self.api_config.has_key("parameters"):
			parameters = self.api_config["parameters"]
			special_params.update(self.getSpecialParamConfig("query",parameters))

		#request body
		request_params = []
		node = ["requestBody","schema"]
		request_body = findNodeByList(self.api_config,node)
		if request_body != None:
			#oneOf情况，延后处理
			if response_schema.has_key("oneOf"):
				break
			else:
				request_params = request_body["properties"]
				special_params.update(self.getSpecialParamConfig("body",request_params))
				
		return special_params

	'''
		param_type：["path","header","query","body"]
	'''
	def getSpecialParamConfig(self,param_type,parameters):
		special_params = {}
		for i in range(len(parameters)):
			parameter = parameters[i]

			if param_type == "query" and (not parameter.has_key("in") or (parameter["in"] and parameter["in"] != "query")):
				continue

			param = parameter["name"]
			param_schema = parameter["schema"]

			#目前只处理param_type in ("string","int")的参数
			if not param_schema.has_key("type") or ( param_schema["type"] and param_schema["type"] not in ("int","string")):
				continue

			if param_schema["maxLength"] > param_schema["minLength"] or param_schema["maximum"] > param_schema["minimum"]:
				value = {key:value for key,value in param_schema.items() if key in ("type","maximum","minimum","maxLength","minLength")}
				spec_params.update({param: value})

		return special_params

	'''
		eg. status_code:"400",errcode:"MissingParameter.User.Email"
	'''
	def getResponseSchema(self,status_code,errcode=None):
		node = ["responses",status_code,"schema"]
		response_schema = findNodeByList(self.api_config,node)
		if response_schema.has_key("oneOf"):
			for i in range(len(response_schema["oneOf"])):
				err = findNode(response_schema["oneOf"][i],"errcode")
				if err != None and err.get("enum")[0] == errcode:
					response_schema = response_schema["oneOf"][i]
					break
		return response_schema
