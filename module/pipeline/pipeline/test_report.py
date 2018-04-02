# -*- coding: utf-8 -*-
import os, sys

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../../')))
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
	owner_uuid = variable["owner_uuid"]
	owner_token = variable["owner_token"]
	project_uuid = "T2a2bqpZc3bjwxU4"
	sprint_uuid = "F2ogSA8S"

	api_url = "%s/team/%s/project/%s/sprint/%s/test_report" %(url,team_uuid,project_uuid,sprint_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid)
	}
	
	print(headers)
	r = requests.get(api_url,headers = headers)
	return r

class TestGroupSort(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("../../../config/variable_F5001.json")
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):
		#status code
		print("----------status_code----------")
		print(self.status_code)
		self.assertEqual(200,self.status_code)
		if(self.status_code != 200):
			return self.status_code
		#response body
		print("------------response--------------")
		print(self.request.text)
		
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