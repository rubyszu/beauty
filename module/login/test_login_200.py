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
	owner_email = variable["owner_email"]
	owner_password = variable["owner_password"]

	api_url = "%s/auth/login" %(url)
	headers = {
		"Content-Type": "application/json"
	}
	body = {
	  "email":"%s" %(owner_email),
	  "password":"%s" %(owner_password)
	}

	print("------------headers------------")
	print(headers)
	print("------------body--------------")
	print(body)

	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestGroupSort(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("../../config/variable_F5001.json")
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):
		
		'''test login 200'''
		#status code
		print("----------status_code----------")
		print(self.status_code)
		self.assertEqual(200,self.status_code)
		if(self.status_code != 200):
			return self.status_code
		#response body
		print("------------response--------------")
		print(self.request.text)

		self.assertIn("user", self.response_json)
		self.assertIn("teams",self.response_json)

		user = self.response_json.get("user")
		print("-----------type(user)------------")
		print(type(user))
		print("-------------user-----------")
		print(user)
		useruuid = user.get("uuid")
		token = user.get("token")
		print("-----------token-----------")
		print(token)
		teams = self.response_json.get("teams")
		teamuuid = teams[0].get("uuid")
		print("-----------teamuuid-----------")
		print(teamuuid)

		if(self.variable.__contains__("owner_uuid")):
			owner_uuid = self.variable["owner_uuid"]
			owner_uuid = useruuid
		else:
			owner_uuid = useruuid
		self.global_variable.store("owner_uuid",useruuid)

		if(self.variable.__contains__("owner_token")):
			owner_token = self.variable["owner_token"]
			owner_token = token
		else:
			owner_token = token
		self.global_variable.store("owner_token",token)

		if(self.variable.__contains__("team_uuid")):
			team_uuid = self.variable["team_uuid"]
			team_uuid = teamuuid
		else:
			team_uuid = teamuuid
		self.global_variable.store("team_uuid",teamuuid)
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