# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))
from config import GlobalVariable
import time
import requests
import json
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')

def request(variable):
	url = variable["url"]
	team_uuid = variable["team_uuid"]
	owner_token = variable["owner_token"]
	owner_uuid = variable["owner_uuid"]

	api_url = "%s/team/%s/stamps/data" %(url, team_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid),
		"Content-Type": "application/json"
	}
	body = {
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
		"testcase_library": 0,
		"transition": 0
}
	print(headers)
	print(body)
	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestResponse(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("../../config/variable_F1059.json")
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result(self):

		with open('response.json','w') as f:
			f.write(self.request.text)
		print(self.status_code)
		print(self.request.text)
		
	def tearDown(self):
		pass

def main():
	unittest.main(verbosity = 2)
	
if __name__ == '__main__':
	main()