# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models.model import Model
import json
from jinja2 import Environment

class IssueTypeAdd(Model):
	def __init__(self):
		super(IssueTypeAdd,self).__init__("issue_type","issue_type_add","post")

	#构造请求参数
	def getRequestParam(self,code,errcode="",context={}):
		if not context:
			dependent_api_list = self.get_dependent_models()
			runner = compose(dependent_api_list)
			context = runner({})

		params = self.buildParam(code,errcode,context)
		return params
    	