# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models.model import Model
from jinja2 import Environment
from box import Box
import json

class TokenInfo(Model):
	def __init__(self):
		super(TokenInfo,self).__init__("auth","token_info","get")
	
if __name__ == '__main__':
	token_info = TokenInfo()
	print token_info.getRequestParam("200")
    	