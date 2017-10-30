# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))
try:
	import importlib
	importlib.reload(sys)
except Exception:
	reload(sys)
from config import GlobalVariable
import time
import requests
import json
import unittest

task_status_name = "ruby %s" %(time.time()) 

def request(variable):
	url = variable["url"]
	team_uuid = variable["team_uuid"]
	owner_token = variable["owner_token"]
	owner_uuid = variable["owner_uuid"]

	api_url = "%s/team/%s/task_statuses/add" %(url, team_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid),
		"Content-Type": "application/json"
	}
	body = {
	  "task_status":{
	    "name": "%s" %(task_status_name),
	    "category":"to_do"
	  }
	}
	# print(headers)
	# print(body)
	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestResponse(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("../../data/variable.json")
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result(self):
		
		'''test add_task_status(to_do) 200'''
		#status code
		print(self.status_code)
		print(self.response_json)
		self.assertEqual(200,self.status_code)
		if(self.status_code != 200):
			return
		#task status uuid
		self.assertIn("uuid", self.response_json)
		self.assertEqual(len(self.response_json["uuid"]), 8)
		#task status name
		self.assertIn("name", self.response_json)
		self.assertIsInstance(self.response_json["name"],str)
		self.assertEqual(task_status_name,self.response_json["name"])
		#task status category
		self.assertIn("category", self.response_json)
		self.assertIsInstance(self.response_json["category"],str)
		self.assertEqual("to_do",self.response_json["category"])
		#task status built_in
		self.assertIn("built_in",self.response_json)
		self.assertIsInstance(self.response_json["built_in"],bool)
		self.assertFalse(self.response_json["built_in"])
		#create_time
		self.assertIn("create_time",self.response_json)
		self.assertEqual(type(self.response_json["create_time"]),int)
		# server_update_stamp
		self.assertIn("server_update_stamp",self.response_json)
		self.assertIsInstance(self.response_json["server_update_stamp"],int)

	def tearDown(self):
		#store task_status_to_do 
		task_status_to_do = self.response_json["uuid"]
		self.global_variable.store("task_status_to_do",task_status_to_do)
		#task_statuses_to_do length值+1
		if(self.variable.__contains__("task_statuses_to_do_length")):
			task_statuses_to_do_length = self.variable["task_statuses_to_do_length"] + 1
		else:
			task_statuses_to_do_length = 1
		self.global_variable.store("task_statuses_to_do_length",task_statuses_to_do_length)
		#task_statuses_to_do数组新增task_status_to_do元素
		if(self.variable.__contains__("task_statuses_to_do")):
			task_statuses_to_do = self.variable["task_statuses_to_do"]
			task_statuses_to_do.append(task_status_to_do)
		else:
			task_statuses_to_do = list()
			task_statuses_to_do.append(task_status_to_do)
		self.global_variable.store("task_statuses_to_do",task_statuses_to_do)
		# write to json file
		self.global_variable.write()


def main():
	unittest.main(verbosity = 2)
	
if __name__ == '__main__':
	main()