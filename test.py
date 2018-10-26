# -*- coding: utf-8 -*-
from jinja2 import Environment
import os,sys,json
import random
import requests

jsonData = {
 "uuid": '{{randomString()}}',
 "name": '{{1|randomSetsOfString(128)}}',
 # "name": '{{name}}',
 "number": '{{1|randomNum(5)}}'
}

# print json.dumps(jsonData)
def randomString(num=8):
  seed = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
  salt = []
  for i in range(num):
    salt.append(random.choice(seed))
  random_string = ''.join(salt)
  return random_string

def randomNum(Min,Max):
  random_num = random.randint(Min,Max)
  return random_num

def randomSetsOfString(Min,Max,is_inside = True):
	if is_inside:
		sets = [randomString(Min), randomString(randomNum(Min+1, Max-1)), randomString(Max)]
	else:
		if Min == 0:
			sets = [randomString(Max+1)]
		else:
			sets = [randomString(Min-1),randomString(Max+1)]
	return sets

def sendRequest():
		api_url = "https://api.ones.team/project/F1115"
		path = "/team/LmUgBPWU/project/7AmuvvhR83vsBWFm/components"
		method = "get"
		params = {
			"headers":{
				"Ones-User-Id": "7AmuvvhR",
				"Ones-Auth-Token": "cCXp3S0V48DYscVpUm9KPVU9zmhgNkvku5lqJDma4ZY33GtGoXLRw4wtfDVADayU"
			}
		}
		
	
		response = requests.request(method,api_url+path,**params)
		return response

env = Environment()
env.globals['randomString'] = randomString
env.filters['randomNum'] = randomNum
env.filters['randomSetsOfString'] = randomSetsOfString
template = env.from_string(json.dumps(jsonData))
# template = json.dumps(jsonData)

# print(template.render(name='variables'))
print(template.render())
print sendRequest()

