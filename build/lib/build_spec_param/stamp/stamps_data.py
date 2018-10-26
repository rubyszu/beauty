# -*- coding: utf-8 -*-
from common import *
# from build_request_param import StampsDataParam

def StampsDataAdd(context):
	from build_request_param import *
	
	stamps_data_operation = ApiOperation("issue_type","/team/{teamUUID}/issue_type/add","post")
	stamps_data_param = StampsDataParam(context).stampsData200PAram()
	data = stamps_data_operation.sendRequest(stamps_data_param).json()

	#field:priority
	fields = data["field"]["fields"]
	prioritys = []
	for i in range(len(fields)):
		if fields[i]["uuid"] == "field012":
			options = fields[i]["options"]
			for y in range(len(options)):
				prioritys.append(options[y]["uuid"])

	#team members
	members = data["team_member"]["members"]
	team_members = []
	for i in range(len(members)):
		if members[i]["status"] == 1 and members[i]["team_member_status"] == 1:
			team_members.append(members[i]["uuid"])

	spec_param = {
		"prioritys": prioritys,
		"team_members": team_members
	}

	context.update(spec_param)
	return context