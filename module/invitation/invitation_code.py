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

def request():

	api_url = "https://api.ones.ai/project/v1/invitation/VUaLgrsq1ANJLwwFF5xijTEAkLAFGswE"
	headers = {
		"Content-Type": "application/json"
	}
	r = requests.get(api_url, headers=headers)
	return r

for i in range(1000):
	r = request()
	print r.text

