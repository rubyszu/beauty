# -*- coding: utf-8 -*-
import os, sys
from common import *
from models.auth.login import Login
from ddt import ddt,data
import unittest	

token_info = TokenInfo()

@ddt
class TestTokenInfo(unittest.TestCase):
	def setUp(self):
		pass

	@data(*token_info.getRequestParam("200"))
	def test_token_info_200(self,param):
		response = token_info.sendRequest(param)
		# validate status code && response
		self.assertEqual(200,response.status_code)
		token_info.validateResponse(response,"200")

	@data(*token_info.getRequestParam("400","AuthFailure.MissingToken"))
	def test_token_info_400_MissingParameter_User_Email(self,param):
		response = token_info.sendRequest(param)
		# validate status code && response
		self.assertEqual(400,response.status_code)
		token_info.validateResponse(response,"400","AuthFailure.MissingToken")

	@data(*token_info.getRequestParam("401AuthFailure.InvalidToken"))	
	def test_token_info_401(self,param):
		response = token_info.sendRequest(param)
		# validate status code && response
		self.assertEqual(401,response.status_code)
		token_info.validateResponse(response,"401","AuthFailure.InvalidToken")

	def tearDown(self):
		pass