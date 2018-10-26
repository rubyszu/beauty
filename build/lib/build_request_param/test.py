# -*- coding: utf-8 -*-
from common import *

spec_param = [
	"issue_type_name":{
		"max":14,
		"min":1
	},
	"task_summary":{
		"max":100,
		"min":1
	}
]

for i in range(len(spec_param)):
	for j in range(len(spec_param[i])):
		print i,j

template = {
	"tasks":[
		{
			"uuid":Generate().randomString(8),
		}
	]
}