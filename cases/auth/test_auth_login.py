# -*- coding: utf-8 -*-
import os, sys
from build_request_param import *
from common import *
from ddt import ddt,data
import unittest	

auth_login = AuthLogin()

@ddt
class TestLogin(unittest.TestCase):
	def setUp(self):
		pass

	@data(*auth_login.getRequestParam("200"))
	def test_auth_login_200(self,param):
		response = auth_login.sendRequest(param)
		# validate status code && response
		self.assertEqual(200,response.status_code)
		self.auth_login_operation.validateReponse(param,"200")

	@data(*auth_login.getRequestParam("400","MissingParameter.User.Email"))
	def test_auth_login_400_MissingParameter_User_Email(self,param):
		response = auth_login.sendRequest(param)
		# validate status code && response
		self.assertEqual(400,response.status_code)
		self.auth_login_operation.validateReponse(param,"200","MissingParameter.User.Email")

	@data(*auth_login.getRequestParam("401"))	
	def test_auth_login_401(self,param):
		response = auth_login.sendRequest(param)
		# validate status code && response
		self.assertEqual(401,response.status_code)
		self.auth_login_operation.validateReponse(param,"401")

	@data(*auth_login.getRequestParam("630"))	
	def test_auth_login_630(self,param):
		response = auth_login.sendRequest(param)
		# validate status code && response
		self.assertEqual(630,response.status_code)
		self.auth_login_operation.validateReponse(param,"630")

	def tearDown(self):
		pass
		

