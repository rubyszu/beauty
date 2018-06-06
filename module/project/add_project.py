# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
from jsonschema import validate
from datetime import datetime
from common import *
import time,requests,json,unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]

def request(variable):
	owner_uuid = variable["owner_uuid"]
	issue_types = variable["issue_types"]
	random_uuid = owner_uuid + Generate().generate_string()

	api_url = "%s/team/%s/projects/add" %(variable["url"],variable["team_uuid"])
	headers = {
		"Ones-Auth-Token": "%s" %(variable["owner_token"]),
		"Ones-User-Id": "%s" %(owner_uuid)
	}
	body = {
		"copy_from":{},
		"issue_types": issue_types,
		"members":variable["members"],
		"project":{
			"members":[],
			"name":"项目名称" + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
			"owner":"%s" %(owner_uuid),
			"status":1,
			"uuid":"%s" %(random_uuid) 
			}
		}

	r = requests.post(api_url,headers = headers,data=json.dumps(body))
	return r

class TestAddProject(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.request = request(self.global_variable.json)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):
		# status code and response body
		api_schema = GlobalVariable("./api_schema/project/add_project_200.json").json
		response_schema = {
			"status_code": self.status_code,
			"response_json": self.response_json
		}
		validate(response_schema, api_schema)	

	def tearDown(self):
		#write to json file
		with open('response.json','w') as f:
			f.write(self.request.text)
		

def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()