# -*- coding: utf-8 -*-
import os, sys
from common import *
from models.auth.login import Login
from ddt import ddt,data
import unittest	

login = Login()

@ddt
class TestLogin(unittest.TestCase):
	def setUp(self):
		pass

	@data(*login.getRequestParam("200"))
	def test_login_200(self,param):
		response = login.sendRequest(param)
		# validate status code && response
		self.assertEqual(200,response.status_code)
		login.validateResponse(response,"200")

	@data(*login.getRequestParam("400","MissingParameter.User.Email"))
	def test_login_400_MissingParameter_User_Email(self,param):
		response = login.sendRequest(param)
		# validate status code && response
		self.assertEqual(400,response.status_code)
		login.validateResponse(response,"400","MissingParameter.User.Email")

	@data(*login.getRequestParam("401AuthFailure.InvalidPassword"))	
	def test_login_401(self,param):
		response = login.sendRequest(param)
		# validate status code && response
		self.assertEqual(401,response.status_code)
		login.validateResponse(response,"401","AuthFailure.InvalidPassword")

	@data(*login.getRequestParam("630NotFound.User"))	
	def test_login_630(self,param):
		response = login.sendRequest(param)
		# validate status code && response
		self.assertEqual(630,response.status_code)
		login.validateResponse(response,"630","NotFound.User")

	def tearDown(self):
		pass
		
