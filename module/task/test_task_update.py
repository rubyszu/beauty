# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../')))
from config import GlobalVariable, branch
import time
import requests
import json
import unittest
import random
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]

def randomItem(data):
	random_item = random.choice(data)
	return random_item


def request(variable):
	url = variable["url"]
	owner_token = variable["owner_token"]
	owner_uuid = variable["owner_uuid"]
	team_uuid = variable["team_uuid"]
	priority = randomItem(variable["prioritys"])
	tasks = variable["tasks"]

	api_url = "%s/team/%s/tasks/update2" %(url, team_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid),
		"Content-Type": "application/json"
	}
	tasks_config = []
	for i in range(len(tasks)):
		if i < 2000:
			config = {
				"uuid": tasks[i],
				"priority": priority
			}
			tasks_config.append(config)
		else:
			break



	body = {
		"tasks": tasks_config
	}

	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestTaskUpdate(unittest.TestCase):
	def setUp(self):
		# self.setting = GlobalVariable("./config/setting.json").json
		# self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_task_update(self):
		
		'''test add_task_status(to_do) 200'''
		#status code
		self.assertEqual(200,self.status_code)
		

	def tearDown(self):
		with open('response.json','w') as f:
			f.write(self.request.text)



def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()