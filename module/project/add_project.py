# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
from jsonschema import validate
from datetime import datetime
from common import *
import time
import requests
import json
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]
random = Generate().generate_string()

def request(variable):
	url = variable["url"]
	team_uuid = variable["team_uuid"]
	owner_uuid = variable["owner_uuid"]
	owner_token = variable["owner_token"]
	issue_types = variable["issue_types"]
	members = variable["members"]
	project_uuid = owner_uuid + random


	api_url = "%s/team/%s/projects/add" %(url,team_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid)
	}
	body = {
		"copy_from":{},
		"issue_types": issue_types,
		"members":members,
		"project":{
			"members":[],
			"name":"项目名称" + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
			"owner":"%s" %(owner_uuid),
			"status":1,
			"uuid":"%s" %(project_uuid) 
			}
		}

	print body
	r = requests.post(api_url,headers = headers,data=json.dumps(body))
	return r

class TestAddProject(unittest.TestCase):
	def setUp(self):
		# self.setting = GlobalVariable("./config/setting.json").json
		# self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):
		#status code
		# self.assertEqual(200,self.status_code)
		# if(self.status_code != 200):
		# 	return self.status_code

		#response body
		# api_schema = GlobalVariable("./api_schema/project/add_project_200.json").json
		# validate(self.response_json, api_schema)

		# write to json file
		self.global_variable.write()
		with open('response.json','w') as f:
			f.write(self.request.text)

	def teardown(self):
		pass
		

def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()