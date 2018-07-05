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

	api_url = "%s/team/%s/field/Kg8AWzK3/update" %(variable["url"], variable["team_uuid"])
	headers = {
		"Ones-Auth-Token": "%s" %(variable["owner_token"]),
		"Ones-User-Id": "%s" %(variable["owner_uuid"]),
		"Content-Type": "application/json"
	}
	body = {
		"field": {
			"name": "Android系统版本",
			"type": 2,
			"uuid": "Kg8AWzK3",
			"options": [{
				"uuid": "GDM55VNE",
				"value": "V5.1",
				"selected": False,
				"background_color": "#ff6a39",
				"color": "#fff",
				"desc": ""
			}, {
				"uuid": "SpdJDCrL",
				"value": "V4.2",
				"selected": False,
				"background_color": "#e0ecfb",
				"color": "#307fe2",
				"desc": ""
			}, {
				"uuid": "TMi2NkU8",
				"value": "V4.4",
				"selected": False,
				"background_color": "#aa8066",
				"color": "#fff",
				"desc": ""
			}, {
				"uuid": "RKFC31QP",
				"value": "V4.1",
				"selected": False,
				"background_color": "#d9f4ed",
				"color": "#00b388",
				"desc": ""
			}, {
				"uuid": "9ENcXoDX",
				"value": "V4.0",
				"selected": False,
				"background_color": "#fdf4d9",
				"color": "#f1b300",
				"desc": ""
			}, {
				"uuid": "LaRRpuz3",
				"value": "v6.0",
				"selected": False,
				"background_color": "#d9f4ed",
				"color": "#00b388",
				"desc": ""
			}, {
				"uuid": "3UVSZhnH",
				"value": "V5.0",
				"selected": False,
				"background_color": "#e63422",
				"color": "#fff",
				"desc": ""
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