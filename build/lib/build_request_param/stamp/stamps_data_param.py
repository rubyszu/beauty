# -*- coding: utf-8 -*-
from common import *
from build_spec_param import authLogin,Context,compose

class StampsDataParam():
	def __init__(self, context = {}):
		dependent_api = [authLogin]
		spect_param_runner = compose(dependent_api)
		self.spec_param = spect_param_runner(context)
		
	def stampsData200Param(self):
		param = {
			"headers":{
				"Ones-User-Id": self.spec_param["Ones-User-Id"],
				"Ones-Auth-Token": self.spec_param["Ones-Auth-Token"]
			},
			"path_params":{
				"teamUUID": self.spec_param["teamUUID"]
			},
			"json":{
				"all_project": 0,
				"dashboard": 0,
				"department": 0,
				"evaluated_permission": 0,
				"field": 0,
				"field_config": 0,
				"group": 0,
				"issue_type": 0,
				"issue_type_config": 0,
				"permission_rule": 0,
				"project": 0,
				"role": 0,
				"role_config": 0,
				"sprint": 0,
				"task_stats": 0,
				"task_status": 0,
				"task_status_config": 0,
				"team": 0,
				"team_member": 0,
				"transition": 0
			}

		}
		return param

if __name__ == '__main__':
	a = StampsDataParam()
	print a.stampsData200Param()
