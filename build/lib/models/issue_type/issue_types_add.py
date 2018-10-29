# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
import json
from jinja2 import Environment

class IssueTypeAdd(Model):
	def __init__(self):
		super(Model,self).__init__("issue_type","/team/{teamUUID}/issue_types/add","post")
		self.dependent_models = self.model_config["issue_type"]["IssueTypeAdd"]

	def getTemplate(self,code,errcode=""):
		templates = loadFile("template/issue_type/issue_types_add.json")
		template = findNode(templates,code + errcode)
		
		return json.dumps(template)

	#构造请求参数
	def getRequestParam(self,code,errcode="",context={}):
		if not context:
			dependent_api_list = self.get_dependent_models()
			runner = compose(dependent_api_list)
			context = runner({})

		params = self.buildParam(code,errcode,context)
		return params
    	