# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
import time,itertools,json
from datetime import datetime
from jinja2 import Template

class TaskAdd2(Model):
	def __init__(self):
		super(TaskAdd2,self).__init__("task","/team/{teamUUID}/task/add2","post")

	#构造请求参数
	def getRequestParam(self,code,errcode="",context={}):
		if not context:
			api_list = self.get_dependent_models()
			runner = compose(api_list)
			context = runner({})

		params = self.buildParam(code,errcode,context)
		return params
    	