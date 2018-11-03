# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models.model import Model
import time,itertools,json
from datetime import datetime
from jinja2 import Template

class ProjectAdd(Model):
	def __init__(self):
		super(ProjectAdd,self).__init__("project","projects_add","post")
		
	#构造请求参数
	def getRequestParam(self,code,errcode="",context={}):
		if not context:
			api_list = self.get_dependent_models()
			runner = compose(api_list)
			context = runner({})

		params = self.buildParam(code,errcode,context)
		return params
    	