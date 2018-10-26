# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
import time,itertools,json
from datetime import datetime
from jinja2 import Template

class ProjectAdd(Model):
	def __init__(self):
		super(Model,self).__init__("issue_type","/team/{teamUUID}/issue_types/add","post")

	def getTemplate(self,code,errcode=""):
		templates = loadFile("template/issue_type/issue_types_add.json")
		node = code + errcode
		template = findNode(templates,node)
		return json.dumps(template)

	#构造请求参数
	def getRequestParam(self,code,errcode="",context={}):
		if not context:
			dependent_api_list = [AuthLogin().sendSuccessRequestByRandomParam]
			runner = compose(dependent_api_list)
			context = runner({})

		params = self.buildParam(code,errcode,context)
		return params
    	