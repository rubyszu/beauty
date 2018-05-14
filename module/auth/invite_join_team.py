# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable
from jsonschema import validate
import time
import requests
import json
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]


def request(variable):
	url = variable["url"]
	owner_email = variable["owner_email"]
	owner_password = variable["owner_password"]

	api_url = "%s/auth/invite_join_team" %(url)
	headers = {
		"Content-Type": "application/json"
	}
	body = {
	  "email":"linhong+1062s1@ones.ai",
	  "name":"1062 first",
	  "password":"%s" %(owner_password),
	  "invite_code":"fkpdhS39Mz5bCquyNsjFXAxTOZnoIizQ"
	}

	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestGroupSort(unittest.TestCase):
	def setUp(self):
		# self.setting = GlobalVariable("./config/setting.json").json
		# self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):
		
		'''test login 200'''
		#status code
		self.assertEqual(200,self.status_code)
		if(self.status_code != 200):
			return self.status_code
		#response body
		api_schema = GlobalVariable("./api_schema/auth/invite_join_team_200.json").json
		validate(self.response_json, api_schema)

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