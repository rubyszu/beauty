# -*- coding: utf-8 -*-
import itertools

#迭代器
'''
	special_params = {
		"issue_type_name": {
			"minLength": 1,
			"type": "string", 
			"maxLength": 14
		},
		"field018": {
			"minimum": 1,
			"type": "int", 
			"maximum": 100
		}
	}
'''
def iterator(special_params):
	keys,values = special_params.keys(),special_params.values()
	sets_params = list(itertools.product(*values))

	sets_data_params = []
	for i in range(len(sets_params)):
		value = sets_params[i]
		sets_data = {}
		for j in range(len(value)):
			sets_data[keys[j]] = value[j]

		sets_data_params.append(sets_data)

	return sets_data_params

if __name__ == '__main__':
	special_params = {
		"issue_type_name": {
			"type": "string", 
			"minLength": 1,
			"maxLength": 14
		},
		"field018": {
			"type": "int", 
			"minimum": 1,
			"maximum": 100
		}
	}
	print iterator(special_params)
