# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
import time
import requests
import json
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]
# print(branch)

def request(variable):
	url = variable["url"]
	team_uuid = variable["team_uuid"]
	owner_token = variable["owner_token"]
	owner_uuid = variable["owner_uuid"]

	api_url = "%s/team/%s/stamps/data" %(url, team_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid),
		"Content-Type": "application/json"
	}
	body = {
		"all_project": 0,
		"dashboard": 0,
		"department": 0,
		"evaluated_permission": 0,
		"field": 0,
		"field_config": 0,
		"group": 0,
		"issue_type": 0,
		"issue_type_config": 0,
		"permission_rule": 0,
		"project": 0,
		"role": 0,
		"role_config": 0,
		"sprint": 0,
		"task_stats": 0,
		"task_status": 0,
		"task_status_config": 0,
		"team": 0,
		"team_member": 0,
		"transition": 0
}
	print(headers)
	print(body)
	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestResponse(unittest.TestCase):
	def setUp(self):
		# self.setting = GlobalVariable("./config/setting.json").json
		# self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result(self):

		#field:priority
		fields = self.response_json.get("field").get("fields")
		prioritys = []
		
		for i in range(len(fields)):
			if fields[i].get("uuid") == "field012":
				options = fields[i].get("options")
				for y in range(len(options)):
					prioritys.append(options[y].get("uuid"))



		#store data
		self.global_variable.store("prioritys",prioritys)

		self.global_variable.write()

		
	def tearDown(self):
		with open('response.json','w') as f:
			f.write(self.request.text)

def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()