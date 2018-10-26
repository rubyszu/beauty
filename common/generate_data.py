# -*- coding: utf-8 -*-
import os,sys
import random

def randomString(num=8):
	seed = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
	salt = []
	for i in range(num):
		salt.append(random.choice(seed))
	random_string = ''.join(salt)
	return random_string

def randomItem(Array):
	random_item = random.choice(arr)
	return random_item

def randomNum(Min,Max):
	random_num = random.randint(Min,Max)
	return random_num

def randomTimestamp(Min = '1970-01-01 00:00:00',Max = '2030-01-01 00:00:00'):
	
	random_timestamp = random.randint(Min,Max)
	return random_timestamp

def randomSetsOfNum(Min,Max,is_inside = True):
	if Min == Max:
		if is_inside:
			return [randomNum(Min)]
		return 
	return [Min-1,Max+1]

def randomSetsOfString(Min,Max,is_inside = True):
	if is_inside:
		sets = [randomString(Min), randomString(randomNum(Min+1, Max-1)), randomString(Max)]
	else:
		if Min == 0:
			sets = [randomString(Max+1)]
		else:
			sets = [randomString(Min-1),randomString(Max+1)]
	return sets


#对有边界值的参数构造多组数据
	'''
		{
			{	
				'issue_type_name':
					 ['T', 'W8', 'OtcfY8ok1s292b']
			},
			{	
				'field018': ['1', '2', '10']}
			}
	'''
def randomSetsOfSpecialParams(special_params,errcode = 200):
	if not special_params:
		return None
	keys,values = special_params.keys(),special_params.values()
	sets_of_special_params = {}
	for i in range(len(values)):
		spec_item = values[i]
		value = []
		if spec_item["type"] == "string":
			value.extend(randomSetsOfString(spec_item["minLength"],spec_item["maxLength"]))
		elif spec_item["type"]  == "int":
			value.extend(randomSetsOfNum(spec_item["minimum"], spec_item["maximum"]))
		sets_of_special_params.update({keys[i]:value})
	return sets_of_special_params



if __name__ == '__main__':
	spec_params = {
		'issue_type_name': {
			"type": "string",
			'maxLength': 14, 
			'minLength': 1
		}, 
		'field018': {
			"type": "int",
			'maximum': 100, 
			'minimum': 1
		}	
	}

	special_params = randomSetsOfSpecialParams(spec_params)
	print spec_params
	print iterator(special_params)





    