# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
import time,itertools,json
from datetime import datetime
from jinja2 import Template

class TaskAdd2(Model):
	def __init__(self):
		super(Model,self).__init__("task","/team/{teamUUID}/task/add2","post")
		self.dependent_models = self.model_config["task"]["TaskAdd2"]

	def getTemplate(self,code,errcode=""):
		templates = loadFile("template/task/task_add2.json")
		node = code + errcode
		template = findNode(templates,node)
		return json.dumps(template)

	#构造请求参数
	def getRequestParam(self,code,errcode="",context={}):
		if not context:
			api_list = self.get_dependent_models()
			runner = compose(api_list)
			context = runner({})

		params = self.buildParam(code,errcode,context)
		return params
    	