# -*- coding: utf-8 -*-
from common import *
from build_spec_param import authLogin,issueTypeAdd,projectAdd,Context,compose

class SpecApiParam():
	def __init__(self):
		self.context = {}
	
	def authLogin(self):
		auth_login_operation = ApiOperation("auth","/auth/login","post")
		auth_login_param = AuthLoginParam().authLoginParam("200")
		data = auth_login_operation.sendRequest(self.auth_login_param).json()

		spec_param = self.context
		#userUUID
		spec_param["Ones-User-Id"] = data["user"]["uuid"]
		#userToken
		spec_param["Ones-Auth-Token"] = data["user"]["token"]
		#teamUUID
		teams = []
		for i in range (len(data["teams"])):
			teams.append(data["teams"][i]["uuid"])
		spec_param["teamUUID"] = Generate().randomArg(teams)
		
		self.context = spec_param
		return spec_param

	def issueTypeAdd(self):
		issue_type_add_operation = ApiOperation("issue_type","/team/{teamUUID}/issue_type/add","post")
		issue_type_add_param = IssueTypeAddParam(self).issueTypeAdd200Param()
		data = auth_login_operation.sendRequest(issue_type_add_param).json()

		spec_param = self.context
		#issue type uuid
		spec_param[issue_type_uuid] = data["uuid"]
		
		self.context = spec_param
		return spec_param

	def stampsData(self):
		stamps_data_operation = ApiOperation("stamp","/team/{teamUUID}/stamps/data","post")
		stamps_data_param = StampsDataParam(self).stampsData200PAram()
		data = stamps_data_operation.sendRequest(stamps_data_param).json()

		spec_param = self.context
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

		self.context = spec_param
		return spec_param

	def projectAdd(self, *args):
		project_add_operation = ApiOperation("project","/team/{teamUUID}/project/add","post")
		projecr_add_param = ProjectAddParam(self).projectAdd200Param()
		data = project_add_operation.sendRequest(projecr_add_param).json()

		spec_param = self.context
		#project uuid
		spec_param["project_uuid"] = data["project"]["uuid"]
		
		self.context = spec_param
		return spec_param
		
	def taskAdd2(self,args):
		task_add2_operation = ApiOperation("task","/team/{teamUUID}/task/add2","post")
		task_add2_param = TaskAdd2Param(self).taskAdd2Param()
		data = task_add2_operation.sendRequest(task_add2_param).json()

		spec_param = self.context
		#task uuid
		spec_param["task_uuid"] = data["tasks"][0]["uuid"]

		self.context = spec_param
		return spec_param
