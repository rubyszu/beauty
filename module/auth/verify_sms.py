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

def request():

	api_url = "https://api.ones.ai/project/v1/auth/verify_sms"
	headers = {
		"Content-Type": "application/json"
	}
	body = {
	  		"phone":"+86%s" %(branch)
	}

	r = requests.post(api_url, headers=headers, data=json.dumps(body))
	return r

for i in range(10):
	r = request()
	print r.json()
	time.sleep(65)

