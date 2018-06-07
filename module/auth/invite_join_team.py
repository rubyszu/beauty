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
	api_url = "%s/auth/invite_join_team" %(variable["url"])
	headers = {
		"Content-Type": "application/json"
	}
	body = {
	  "email":"linhong+1062s1@ones.ai",
	  "name":"1062 first",
	  "password":"12345678",
	  "invite_code":"fkpdhS39Mz5bCquyNsjFXAxTOZnoIizQ"
	}

	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

class TestInviteJoinTeam(unittest.TestCase):
	def setUp(self):
		self.global_variable = GlobalVariable("./config/variable_%s.json" %(branch))
		self.request = request(self.global_variable.json)
		self.status_code = self.request.status_code
		self.response_json = self.request.json()

	def test_result_200(self):		
		#status code and response body
		api_schema = GlobalVariable("./api_schema/auth/invite_join_team_624.json").json
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