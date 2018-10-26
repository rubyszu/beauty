# -*- coding: utf-8 -*-
from common import *
# from build_request_param import IssueTypeAddParam

def issueTypeAdd(context):
	from build_request_param import *

	issue_type_add_operation = ApiOperation("issue_type","/team/{teamUUID}/issue_type/add","post")
	issue_type_add_param = IssueTypeAddParam(context).issueTypeAdd200Param()
	data = issue_type_add_operation.sendRequest(issue_type_add_param).json()

	spec_param = {
		"issue_type_uuid": data["uuid"]
	}

	context.update(spec_param)
	return context