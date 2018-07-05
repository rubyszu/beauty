# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
from common import *
from jsonschema import validate
from datetime import datetime
import time,requests,json,unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]

def request(variable):
	owner_uuid = variable["owner_uuid"]

	api_url = "%s/team/%s/tasks/update2" %(variable["url"], variable["team_uuid"])
	headers = {
		"Ones-Auth-Token": "%s" %(variable["owner_token"]),
		"Ones-User-Id": "%s" %(owner_uuid),
		"Content-Type": "application/json"
	}
	body = {
		"tasks": [{
			"uuid": "GUGgMPPrpRI8owFO",
			"field_values": [{
				"field_uuid": "GTJBGYSC",
				"type": 16,
				"value": None
			}]
		}]
	}

	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestAddOneTask(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.request = request(self.global_variable.json)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result(self):
		#status code and response body
		# api_schema = GlobalVariable("./api_schema/task/task_add_one_task_200.json").json
		# response_schema = {
		# 	"status_code": self.status_code,
		# 	"response_json": self.response_json
		# }
		# validate(response_schema, api_schema)	
		pass

	def tearDown(self):
		# print self.response_json
		# write to json file
		with open('response.json','w') as f:
			f.write(self.request.text)


def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()