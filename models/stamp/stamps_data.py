# -*- coding: utf-8 -*-
from common.http_base import httpBase
from common import *
from models.model import Model
from jinja2 import Environment
import json

class StampsData(Model):
	def __init__(self):
		super(StampsData,self).__init__("stamp","stamps_data","post")

if __name__ == '__main__':
	stamps_data = StampsData()
	print stamps_data.getRequestParam('200')