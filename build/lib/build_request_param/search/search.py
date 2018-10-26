# -*- coding: utf-8 -*-
from common import *
from build_spec_param import authLogin,Context,compose

class SearchParam():
	def __init__(self, context = {}):
		dependent_api = [authLogin]
		spect_param_runner = compose(dependent_api)
		self.spec_param = spect_param_runner(context)

	def search200Param(self,search_type):
		param = {
			"path_params": {
				"teamUUID": "%s" %(self.spec_param["teamUUID"])
			},
			"headers": {
				"Ones-User-Id": self.spec_param["Ones-User-Id"],
				"Ones-Auth-Token": self.spec_param["Ones-Auth-Token"]
			},
			"params": {
				"q": "1",
				"types": "%s" %(search_type),
				"limit": 50,
				"start": 0
			}
		}
		return param

if __name__ == '__main__':
	a = SearchParam()
	print a.search200Param("task")