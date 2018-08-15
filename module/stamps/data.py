# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
from jsonschema import validate
import time,requests,json,unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]

def request(variable):
	api_url = "%s/team/%s/stamps/data" %(variable["url"], variable["team_uuid"])
	headers = {
		"Ones-Auth-Token": "%s" %(variable["owner_token"]),
		"Ones-User-Id": "%s" %(variable["owner_uuid"]),
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
	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestResponse(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.request = request(self.global_variable.json)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result(self):

		#validate status code and response body
		# api_schema = GlobalVariable("./api_schema/stamps/data_200.json").json
		# response_schema = {
		# 	"status_code": self.status_code,
		# 	"response_json": self.response_json
		# }
		# validate(response_schema, api_schema)
		pass
		
	def tearDown(self):
		#write to json file
		with open('response.json','w') as f:
			f.write(self.request.text)

		#field:priority
		fields = self.response_json.get("field").get("fields")
		prioritys = []
		
		for i in range(len(fields)):
			if fields[i].get("uuid") == "field012":
				options = fields[i].get("options")
				for y in range(len(options)):
					prioritys.append(options[y].get("uuid"))

		#project uuids
		projects = self.response_json.get("project").get("projects")
		project_uuids = []
		for i in range(len(projects)):
			project_uuids.append(projects[i].get("uuid"))

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
		self.global_variable.store("prioritys",prioritys)
		self.global_variable.store("projects",project_uuids)
		self.global_variable.store("project_uuid",project_uuids[0])
		self.global_variable.store("sprints",sprint_uuids)
		self.global_variable.store("issue_types",issue_type)
		self.global_variable.store("members",team_members)

		self.global_variable.write()

def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()