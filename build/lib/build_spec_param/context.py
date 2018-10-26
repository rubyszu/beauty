# -*- coding: utf-8 -*-
from common import *
# from config import *

class Context():
	def __init__(self):
		self.context = {}
	
	def update(self,data):
		self.context.update(data)
		return self.context
		