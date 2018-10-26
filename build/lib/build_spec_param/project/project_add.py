# -*- coding: utf-8 -*-
from common import *
# from build_request_param import ProjectAddParam

def projectAdd(context):
	from build_request_param import *
	
	project_add_operation = ApiOperation("project","/team/{teamUUID}/project/add","post")
	projecr_add_param = ProjectAddParam(context).projectAdd200Param()
	data = project_add_operation.sendRequest(projecr_add_param).json()
	#project uuid
	spec_param = {
		"project_uuid": data["project"]["uuid"]
	}
	
	context.update(spec_param)
	return context
