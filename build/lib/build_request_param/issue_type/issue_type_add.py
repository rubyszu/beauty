# -*- coding: utf-8 -*-
from common import *
from build_spec_param import authLogin,Context,compose
import time
from datetime import datetime


class IssueTypeAddParam():
	def __init__(self, context = {}):
		dependent_api = [authLogin]
		spect_param_runner = compose(dependent_api)
		self.spec_param = spect_param_runner(context)
		print(self.spec_param)
	def buildParam(self,specialParams):
		#buildParam(self.template,specialParams);
		pass	
	def issueTypeAdd200Param(self):
		param = {
			"headers":{
				"Ones-User-Id": self.spec_param["Ones-User-Id"],
				"Ones-Auth-Token": self.spec_param["Ones-Auth-Token"]
			},
			"path_params":{
				"teamUUID": self.spec_param["teamUUID"]
			},
			"json":{
				"issue_type":{
					"name":"任务类型名称%s" %(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
					"icon": 1
				},
				"copy_from":None
			}
		}
		return param

if __name__ == '__main__':
	a = IssueTypeAddParam()
	print a.issueTypeAdd200Param()
