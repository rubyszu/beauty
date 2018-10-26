# -*- coding: utf-8 -*-
from common import *
from build_spec_param import authLogin,issueTypeAdd,projectAdd,Context,compose
import time
from datetime import datetime

class TaskAdd2Param():
	def __init__(self, context = {}):
		dependent_api = [authLogin, issueTypeAdd, projectAdd]
		spect_param_runner = compose(dependent_api)
		self.spec_param = spect_param_runner(context)

	def taskAdd2200Param(self):
		param = {
			"headers":{
				"Ones-User-Id": self.spec_param["Ones-User-Id"],
				"Ones-Auth-Token": self.spec_param["Ones-Auth-Token"]
			},
			"path_params":{
				"teamUUID": 
				self.spec_param["teamUUID"]
			},
			"json":{
				"tasks": [
				{
					"uuid":"%s" %(self.spec_param["Ones-User-Id"] + Generate().randomString(8)),
					"summary": "任务标题%s" %(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
	    			"project_uuid":"%s" %(self.spec_param["project_uuid"]),
			    	"issue_type_uuid":"%s" %(self.spec_param["issue_type_uuid"]),
			    	"owner":"%s" %(Generate().randomArray(self.spec_param["team_members"])),
			    	"assign":"%s" %(self.spec_param["Ones-User-Id"]),
			    	"desc_rich":"",
			    	"parent_uuid":"",
			    	"priority":"%s" %(Generate().randomArray(self.spec_param["priority"])),
			    	"field_values":[
			    		{"field_uuid":"field018","type":4,"value":Generate().randomNum(100000,1000000)}
			    	]
				}]
			}
		}
		return param
