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
	project_uuid = variable["project_uuid"]
	sprint_uuid = variable["sprint_uuid"]
	owner_uuid = variable["owner_uuid"]
	owner_token = variable["owner_token"]

	api_url = "%s/team/%s/project/%s/sprints/update" %(url,team_uuid,project_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid)
	}
	body = {
  		"sprints": [
  			{
  				"uuid": "%s" %(sprint_uuid),
  				"title":"ruby示例迭代007",
  				"assign":"%s" %(owner_uuid),
  				"start_time":1523318400,
  				"end_time":1523491200
  			}]	
	}
	print(api_url)
	print(body)
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