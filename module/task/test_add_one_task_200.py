# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
from common import *
from jsonschema import validate
from datetime import datetime
import time
import requests
import json
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]
random = Generate().generate_string()

task_status_name = "ruby %s" %(time.time()) 

def request(variable):
	url = variable["url"]
	team_uuid = variable["team_uuid"]
	project_uuid = variable["project_uuids"][0]
	issue_type_uuid = variable["issue_types"][0]
	owner_token = variable["owner_token"]
	owner_uuid = variable["owner_uuid"]

	api_url = "%s/team/%s/tasks/add2" %(url, team_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid),
		"Content-Type": "application/json"
	}
	body = {
	  "tasks":[
	  	{
	  		"uuid":"%s" %(owner_uuid + random),
	    	"summary": "任务" + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	    	"project_uuid":"%s" %(project_uuid),
	    	"issue_type_uuid":"%s" %(issue_type_uuid),
	    	"owner":"%s" %(owner_uuid),
	    	"assign":"%s" %(),
	    	"desc_rich":"",
	    	"parent_uuid":"",
	    	"priority":"PRIOPTno",
	    	"field_values":[
	    		{"field_uuid":"field018","type":4,"value":100000}
	    	]
	  	}
	]

	# print(headers)
	# print(body)
	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestResponse(unittest.TestCase):
	def setUp(self):
		# self.setting = GlobalVariable("./config/setting.json").json
		# self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result(self):
		
		'''test add_task_status(to_do) 200'''
		#status code
		self.assertEqual(200,self.status_code)
		if(self.status_code != 200):
			return

		#response body
		api_schema = GlobalVariable("./api_schema/task/task_add_one_task_200.json").json
		validate(self.response_json, api_schema)

	def tearDown(self):
		#store task_status_to_do 
		task_status_to_do = self.response_json["uuid"]
		self.global_variable.store("task_status_to_do",task_status_to_do)
		#task_statuses_to_do length值+1
		if(self.variable.__contains__("task_statuses_to_do_length")):
			task_statuses_to_do_length = self.variable["task_statuses_to_do_length"] + 1
		else:
			task_statuses_to_do_length = 1
		self.global_variable.store("task_statuses_to_do_length",task_statuses_to_do_length)
		#task_statuses_to_do数组新增task_status_to_do元素
		if(self.variable.__contains__("task_statuses_to_do")):
			task_statuses_to_do = self.variable["task_statuses_to_do"]
			task_statuses_to_do.append(task_status_to_do)
		else:
			task_statuses_to_do = list()
			task_statuses_to_do.append(task_status_to_do)
		self.global_variable.store("task_statuses_to_do",task_statuses_to_do)
		# write to json file
		self.global_variable.write()


def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':


	for i in range(10):
		main()