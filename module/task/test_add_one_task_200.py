# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
from jsonschema import validate
from datetime import datetime
import time,requests,json,unittest
import random
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]

def generate_string():
	seed = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
	salt = []
	for i in range(8):
		salt.append(random.choice(seed))
	return ''.join(salt)

def random_arg(arr):
	return random.choice(arr)

def random_num(a,b):
	return random.randint(a,b)

def request(variable):
	owner_uuid = variable["owner_uuid"]
	prioritys = variable["prioritys"]
	sprints = variable["sprints"]
	random_uuid = owner_uuid + generate_string()
	random_issue_type = random_arg(variable["issue_types"])
	random_assign = random_arg(variable["members"])
	random_priority = random_arg(prioritys)
	random_sprint = random_arg(sprints)
	random_assess_hour = random_num(100000,500000)
	# random_parent_uuid = random.random_arg(variable["task_uuids"])

	api_url = "%s/team/%s/tasks/add2" %(variable["url"], variable["team_uuid"])
	headers = {
		"Ones-Auth-Token": "%s" %(variable["owner_token"]),
		"Ones-User-Id": "%s" %(owner_uuid),
		"Content-Type": "application/json"
	}
	# tasks = []
	task = {
	  		"uuid":"%s" %(random_uuid),
	    	"summary": "任务标题" + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	    	"project_uuid":"GAy6uL3m1xR4AFr3",
	    	"issue_type_uuid":"%s" %(random_issue_type),
	    	"owner":"%s" %(owner_uuid),
	    	"assign":"%s" %(random_assign),
	    	"desc_rich":"",
	    	"parent_uuid":"",
	    	"priority":"%s" %(random_priority),
	    	"field_values":[
	    		{"field_uuid":"field018","type":4,"value":random_assess_hour},
	    		{"field_uuid":"011","type":7,"value":random_sprint}
	    	]
	}
	# for i in range(10):
	# 	tasks.append(task)
	# print tasks
	body = {
	  "tasks":[task]}

	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestAddOneTask(unittest.TestCase):
	def setUp(self):
		# self.setting = GlobalVariable("./config/setting.json").json
		# self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
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
		print self.response_json
		# write to json file
		with open('response.json','w') as f:
			f.write(self.request.text)


def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()