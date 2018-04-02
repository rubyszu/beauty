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

	api_url = "%s/team/%s/pipelines" %(url,team_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid)
	}
	print(headers)
	r = requests.get(api_url,headers = headers)
	return r

class TestGroupSort(unittest.TestCase):
	def setUp(self):
		self.setting = GlobalVariable("../../../config/setting.json").json
		self.global_variable = GlobalVariable("../../../config/variable_%s.json" %(self.setting["branch"]))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):
		#status code
		print("----------status_code----------")
		print(self.status_code)
		# self.assertEqual(200,self.status_code)
		# if(self.status_code != 200):
		# 	return self.status_code
		#response body
		print("------------response--------------")
		print(self.request.text)

		pipelines = self.response_json.get("pipelines")
		uuids = []
		print(len(pipelines))
		print(pipelines[0].get("uuid"))
		for i in range(len(pipelines)):
			uuids.append(pipelines[i].get("uuid"))
		print(uuids)


		if(self.variable.__contains__("pipeline_uuids")):
			pipeline_uuids = self.variable["owner_uuid"]
			pipeline_uuids = uuids
		else:
			pipeline_uuids = uuids
		self.global_variable.store("pipeline_uuids",uuids)

		
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