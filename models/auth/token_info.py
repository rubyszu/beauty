# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models.model import Model
from jinja2 import Environment
import json

class TokenInfo(Model):
	def __init__(self):
		super(Login,self).__init__("auth","token_info","get")
	
	#构造请求参数
	def getRequestParam(self,code,errcode=""):
		return self.getRequestParam(code,errcode)

if __name__ == '__main__':
	token_info = TokenInfo()
	print token_info.getRequestParam('200')
    	