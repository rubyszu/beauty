# -*- coding: utf-8 -*-
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
	project_uuid = "9CD1ULg7CDKR7N38"
	sprint_status = "8QAiCpcb"
	owner_uuid = variable["owner_uuid"]
	owner_token = variable["owner_token"]

	api_url = "%s/team/%s/project/%s/sprint_status/%s/update" %(url,team_uuid,project_uuid,sprint_status)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid)
	}
	body = {
  		"status": {
  			"name": "概要设计评审",
  			"next_uuid": "CT3AycPg"
  		}	
	}
	print(headers)
	r = requests.post(api_url,headers = headers,data = json.dumps(body))
	return r

class TestGroupSort(unittest.TestCase):
	def setUp(self):
		self.setting = GlobalVariable("./config/setting.json").json
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):
		#status code
		# self.assertEqual(200,self.status_code)
		# if(self.status_code != 200):
		# 	return self.status_code

		# write to json file
		self.global_variable.write()
		with open('response1.json','w') as f:
			f.write(self.request.text)

	def teardown(self):
		pass
		

def main():
	unittest.main(verbosity = 2)
	
if __name__ == '__main__':
	main()