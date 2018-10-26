# -*- coding: utf-8 -*-
from common import *
from build_spec_param import authLogin,issueTypeAdd,Context,compose

class ProjectAddParam():
	def __init__(self, context = {}):
		dependent_api = [authLogin, issueTypeAdd]
		spect_param_runner = compose(dependent_api)
		self.spec_param = spect_param_runner(context)

	def projectAdd200Param(self):
		param = {
			"headers":{
				"Ones-User-Id": self.spec_param["Ones-User-Id"],
				"Ones-Auth-Token": self.spec_param["Ones-Auth-Token"]
			},
			"path_params":{
				"teamUUID": self.spec_param["teamUUID"]
			},
			"json":{
				"project":{
					"name": ""
				},
				"issue_types":[self.spec_param["issue_type_uuid"]]
			}
		}
		return param
