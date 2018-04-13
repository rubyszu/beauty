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

	api_url = "%s/team/%s/members" %(url, team_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid)
	}
	r = requests.get(api_url, headers=headers)
	return r

class TestResponse(unittest.TestCase):
	def setUp(self):
		self.setting = GlobalVariable("./config/setting.json").json
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
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