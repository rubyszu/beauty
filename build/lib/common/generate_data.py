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

def randomSetsOfNum(Min,Max):
	sets = [Min, randomNum(Min+1, Max-1), Max]
	return sets

def randomSetsOfString(Min,Max):
	sets = [randomString(Min), randomString(randomNum(Min+1, Max-1)), randomString(Max)]
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
def randomSetsOfSpecialParams(special_params):
	if not special_params:
		return None
	keys,values = special_params.keys(),special_params.values()
	sets_of_special_params = {}
	for i in range(len(valuges)):
		spec_item = values[i]
		value = []
		if spec_item["type"] == "string":
			value.extend(randomStringArr(spec_item["minLength"],spec_item["maxLength"]))
		elif spec_item["type"]  == "int":
			value.extend(randomNumArr(spec_item["minimum"], spec_item["maximum"]))
		sets_of_special_params.update({keys[i]:value})
	return sets_of_special_params






    