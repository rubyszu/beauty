# -*- coding: utf-8 -*-
from common import loadFile,findNode,findNodeByList
from common.http_base import httpBase
import os

#解析swagger文档
class ParseApiYaml:
	def __init__(self,module,operation,method,product="project"):
		schema = loadFile("./api_schema/api/%s/%s/%s.yaml" %(product,module,operation))
		self.path = findNode(schema,"paths").keys()[0]
		self.product = product
		self.method = method
		node = ["paths",self.path,self.method]
		self.api_config = findNodeByList(schema,node)

	#获取请求方法
	def getMethod(self):
		return self.method

	#获取请求接口
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
			path 和 header的参数，暂不需要处理
		'''
		special_params = {}

		if self.api_config.has_key("parameters"):
			parameters = self.api_config["parameters"]
		
			for i in parameters:
				# 获取query中有边界值的参数
				if i["in"] == "query":
					special_params.update({i["name"]:i["schema"]})

		#获取request body中有边界值的参数
		request_params = []
		node = ["requestBody","schema"]
		request_body = findNodeByList(self.api_config,node)
		if request_body != None:
			#oneOf情况，延后处理
			if request_body.has_key("oneOf"):
				return
			else:
				special_params.update(request_body["properties"])

		#处理special_params为空的情况
		if not special_params:
			return parameters
			
		special_params = self.getSpecialParamConfig(special_params)
		return special_params

	'''
		获取有边界值的参数的配置
		param_type：["path","header","query","body"]
	'''
	def getSpecialParamConfig(self,parameters):
		
		special_params = {}
		for key,value in parameters.items():

			#目前只处理param_type in ("string","int")的参数
			if not value.has_key("type") or (value["type"] not in ("int","string")):
				continue

			if ("maxLength" in value and "minLength" in value) or ("maximum" in value and "minimum" in value):
				value = {k:v for k,v in value.items() if k in ("type","maximum","minimum","maxLength","minLength")}
				special_params.update({key: value})
		return special_params

	'''
		eg. status_code:"400",errcode:"MissingParameter.User.Email"
	'''
	def getResponseSchema(self,status_code,errcode=""):
		node = ["responses",status_code,"schema"]
		response_schema = findNodeByList(self.api_config,node)
		if response_schema.has_key("oneOf"):
			for i in range(len(response_schema["oneOf"])):
				err = findNode(response_schema["oneOf"][i],"errcode")
				if not err and err.get("enum")[0] == errcode:
					response_schema = response_schema["oneOf"][i]
					break
		return response_schema

if __name__ == '__main__':
	# auth_login = ParseApiYaml("auth","login","post")
	# issue_type_add = ParseApiYaml("issue_type","issue_type_add","post")
	project_add = ParseApiYaml("project","projects_add","post")
	# auth_login.getSpecialParam()
