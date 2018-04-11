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
	sprint_uuid = "57Kka6UW"
	owner_uuid = variable["owner_uuid"]
	owner_token = variable["owner_token"]

	api_url = "%s/team/%s/project/%s/sprint/%s/sprint_statuses/update" %(url,team_uuid,project_uuid,sprint_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid)
	}
	body = {
		"sprint_statuses":[{
			"status_uuid": "8iFzXs9k",
			"plan_start_time": 1523376000,
			"plan_end_time": 1522540800,
			"actual_start_time": 1514764800,
			"actual_end_time": 1485907200,
			"is_current_status": False
		}, {
			"status_uuid": "HbQMsBuH",
			"plan_start_time": 1485993600,
			"plan_end_time": 1523376000,
			"actual_start_time": 1486166400,
			"actual_end_time": 1483488000,
			"is_current_status": True

		}]
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
		with open('response.json','w') as f:
			f.write(self.request.text)

	def teardown(self):
		pass
		

def main():
	unittest.main(verbosity = 2)
	
if __name__ == '__main__':
	main()