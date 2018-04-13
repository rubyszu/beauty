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

def request(variable):
	url =variable["url"]
	team_uuid = variable["team_uuid"]
	owner_token = variable["owner_token"]
	owner_uuid = variable["owner_uuid"]
	project_uuid = variable["project_uuid"]
	sprint_uuid = variable["sprint_uuid"]

	api_url = "%s/team/%s/project/%s/filters/peek" %(url, team_uuid,project_uuid)
	headers = {
		"Ones-Auth-Token": "%s" %(owner_token),
		"Ones-User-Id": "%s" %(owner_uuid),
		"Content-Type": "application/json"
	}
	body = {
	  "query":{
	    "must":[
	        {"equal":{"field_values.field006":"%s" %(project_uuid)}},
	        {"equal":{"field_values.field011":"%s" %(sprint_uuid)}}
	    ]
	  },
	  "sort":[
	    {
	      "create_time": {
	                "order": "desc"
	            }
	    }
	  ],
	  "group_by":"status_category",
	  "include_subtasks":True
	}
	print(headers)
	print(body)
	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestGroupSort(unittest.TestCase):
	def setUp(self):
		self.setting = GlobalVariable("./config/setting.json").json
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(self.setting["branch"]))
		self.variable = self.global_variable.json
		self.request = request(self.variable)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result(self):
		
		'''test group_sort'''
		#status code
		print(self.status_code)
		self.assertEqual(200,self.status_code)
		if(self.status_code != 200):
			return self.statue_code

		# with open('response.json','w') as f:
		# 	f.write(self.request.text)
		# with open('response1.json','w') as f:
		# 	f.write(self.request.text)
		print(self.status_code)
		print(self.request.text)

	def tearDown(self):

		try:
			milestone_groups_length = len(self.response_json.groups)
			print(milestone_groups_length)
			milestone_groups = list()
			milestone_sections = list()
			for x in range(0,milestone_groups_length):
				if(self.response_json.groups[x].key == ""):
					milestone_groups.append("key" + x)
				else:
					milestone_groups.append(self.response_json.groups[x].key)
				uuids = list()
				for y in range(0,len(self.response_json.groups[x].entries)):
					uuids.append(self.response_json.groups[x].entries[y].uuid)
				milestone_sections.append(uuids)

			# if(self.variable.__contains__("milestone_groups_length")):
			# 	self.variable["milestone_groups_length"] = milestone_groups_length

			self.global_variable.store("milestone_groups_length",milestone_groups_length)

			self.global_variable.store("milestone_groups",milestone_groups)

			self.global_variable.store("milestone_sections",milestone_sections)
			# write to json file
			self.global_variable.write()
		except Exception:
			pass
		

def main():
	unittest.main(verbosity = 2)
	
if __name__ == '__main__':
	main()