# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
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

		#response body
		api_schema = GlobalVariable("./api_schema/stamps/data_200.json").json
		validate(self.response_json, api_schema)

		with open('response.json','w') as f:
			f.write(self.request.text)

		#spinrt uuids
		sprints = self.response_json.get("sprint").get("sprints")
		sprint_uuids = []
		for i in range(len(sprints)):
			sprint_uuids.append(sprints[i].get("uuid"))

		#issue types
		issue_types = self.response_json.get("issue_type").get("issue_types")
		issue_type = []
		for i in range(len(issue_types)):
			issue_type.append(issue_types[i].get("uuid"))

		#team members
		members = self.response_json.get("team_member").get("members")
		team_members = []
		for i in range(len(members)):
			if members[i].get("status") == 1:
				team_members.append(members[i].get("uuid"))

		#store data
		if(self.variable.__contains__("sprints")):
			sprints = self.variable["sprints"]
			sprints = sprint_uuids
		else:
			sprints = sprint_uuids
		self.global_variable.store("sprints",sprint_uuids)

		if(self.variable.__contains__("issue_types")):
			issue_types = self.variable["issue_types"]
			issue_types = issue_type
		else:
			issue_types = issue_type
		self.global_variable.store("issue_types",issue_type)

		if(self.variable.__contains__("members")):
			members = self.variable["members"]
			members = team_members
		else:
			members = team_members
		self.global_variable.store("members",team_members)

		self.global_variable.write()
		
	def tearDown(self):
		pass

def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()