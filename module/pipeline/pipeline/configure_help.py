# -*- coding: utf-8 -*-
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../../')))
from config import GlobalVariable, branch
from jsonschema import validate
import time,requests,json,unittest
reload(sys)
sys.setdefaultencoding('utf-8')
args = branch.get_args()
branch = args[0]

def request(variable):
	api_url = "%s/team/%s/pipeline/%s/configure_help" %(variable["url"],variable["team_uuid"],variable["pipeline_uuid"])
	headers = {
		"Ones-Auth-Token": "%s" %(variable["owner_token"]),
		"Ones-User-Id": "%s" %(variable["owner_uuid"])
	}
	r = requests.get(api_url,headers = headers)
	return r

class TestConfigureHelp(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.request = request(self.global_variable.json)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):
		
		#validate status code and response body
		api_schema = GlobalVariable("./api_schema/pipeline/pipeline/configure_help_200.json").json
		response_schema = {
			"status_code": self.status_code,
			"response_json": self.response_json
		}
		validate(response_schema, api_schema)
		

	def tearDown(self):
		# write to json file
		with open('response.json','w') as f:
			f.write(self.request.text)
		

def main():
	unittest.main(argv=args[1])
	
if __name__ == '__main__':
	main()