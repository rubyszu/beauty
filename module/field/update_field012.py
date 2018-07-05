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

	api_url = "%s/team/%s/field/field012/update" %(variable["url"], variable["team_uuid"])
	headers = {
		"Ones-Auth-Token": "%s" %(variable["owner_token"]),
		"Ones-User-Id": "%s" %(variable["owner_uuid"]),
		"Content-Type": "application/json"
	}
	body = {
		"field": {
		"uuid": "field012",
		"name": "优先级",
		"name_pinyin": "you1xian1ji2",
		"desc": "",
		"type": 1,
		"default_value": "X9czPcVb",
		"renderer": 0,
		"filter_option": 0,
		"search_option": 0,
		"create_time": 1529929057,
		"built_in": true,
		"fixed": false,
		"options": [{
			"uuid": "KuGkbsRb",
			"value": "较高",
			"selected": false,
			"background_color": "#ffe9e2",
			"color": "#ff6a39",
			"desc": "可能会阻碍进程的严重问题。"
		}]
	}
}
	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestGroupSort(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.request = request(self.global_variable.json)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result(self):
		#status code and response body
		# api_schema = GlobalVariable("./api_schema/filter_peek/test_group_sort_200.json").json
		# response_schema = {
		# 	"status_code": self.status_code,
		# 	"response_json": self.response_json
		# }
		# validate(response_schema, api_schema)
		pass


	def tearDown(self):
		# entries = self.response_json.get("groups")[0].get("entries")
		# task_uuids = []
		# for i in range(len(entries)):
		# 	task_uuids.append(entries[i].get("uuid"))
		# self.global_variable.store("task_uuids",task_uuids)
		# self.global_variable.write()
		# write to json file
		with open('response.json','w') as f:
			f.write(self.request.text)

def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()