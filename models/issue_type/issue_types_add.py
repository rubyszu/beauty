# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models.model import Model
import json
from jinja2 import Environment

class IssueTypeAdd(Model):
	def __init__(self):
		super(IssueTypeAdd,self).__init__("issue_type","issue_type_add","post")
    	
if __name__ == '__main__':
	issue_type_add = IssueTypeAdd()
	issue_type_add.getRequestParam("200")