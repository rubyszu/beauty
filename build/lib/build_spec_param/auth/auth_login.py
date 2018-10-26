# -*- coding: utf-8 -*-
from common import *
# from common.http_base import httpBase
# import requests
# from build_request_param import AuthLoginParam

def authLogin(context):
	from build_request_param import *
	# path = "/auth/login"
	# api_url = "%s/%s/%s%s" %(httpBase()["host"],"project",httpBase()["branch"], path)
	# method = "post"
	auth_login_operation = ApiOperation("auth","/auth/login","post")
	auth_login_param = AuthLoginParam().authLoginParam("200")
	data = auth_login_operation.sendRequest(auth_login_param).json()
	# data = requests.request(method,api_url,auth_login_param)

	teams = []
	for i in range (len(data["teams"])):
		teams.append(data["teams"][i]["uuid"])

	spec_param = {
		"Ones-User-Id": data["user"]["uuid"],
		"Ones-Auth-Token": data["user"]["token"],
		"teamUUID": Generate().randomArray(teams)
	}

	context.update(spec_param)
	return context
