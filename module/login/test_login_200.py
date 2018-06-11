# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
from jsonschema import validate
from common import *
import time,requests,json,unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]

def request(variable):

	api_url = "%s/auth/login" %(variable["url"])
	headers = {
		"Content-Type": "application/json"
	}
	body = {
	  "email":"%s" %(variable["owner_email"]),
	  "password":"%s" %(variable["owner_password"])
	}

	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestLogin(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.request = request(self.global_variable.json)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):

		#validate status code and response body
		# api_schema = GlobalVariable("./api_schema/login/login_200.json").json
		# api_schema = GlobalVariable("./api_schema/login.json").json

		api_schema = load_json_schema("./api_schema/login/login_user.json")

		print api_schema

		response_schema = {
			"status_code": self.status_code,
			"response_json": self.response_json
		}
		validate(response_schema, api_schema)

	def tearDown(self):
		#get response data
		user = self.response_json.get("user")
		useruuid = user.get("uuid")
		token = user.get("token")
		teamuuid = self.response_json.get("teams")[0].get("uuid")

		#store data
		self.global_variable.store("owner_uuid",useruuid)
		self.global_variable.store("owner_token",token)
		self.global_variable.store("team_uuid",teamuuid)
		# write to json file
		self.global_variable.write()

		with open('response.json','w') as f:
			f.write(self.request.text)


def main():
	unittest.main(argv=args[1])

if __name__ == '__main__':
	main()
