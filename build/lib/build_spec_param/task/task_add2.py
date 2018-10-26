# -*- coding: utf-8 -*-
from common import *
# from build_request_param import TaskAdd2Param

def taskAdd2(context):
	from build_request_param import *
	
	task_add2_operation = ApiOperation("task","/team/{teamUUID}/task/add2","post")
	task_add2_param = TaskAdd2Param(context).taskAdd2Param()
	data = task_add2_operation.sendRequest(task_add2_param).json()
	#project uuid
	spec_param = {
		"task_uuid": data["tasks"][0]["uuid"]
	}
	
	context.update(spec_param)
	return context
