# -*- coding: utf-8 -*-
import os, sys
from common import *
from models.auth.login import Login
from ddt import ddt,data
import unittest	

stamps_data = StampsData()

@ddt
class TestStampsData(unittest.TestCase):
	def setUp(self):
		pass

	@data(*stamps_data.getRequestParam("200"))
	def test_stamps_data_200(self,param):
		response = stamps_data.sendRequest(param)
		# validate status code && response
		self.assertEqual(200,response.status_code)
		stamps_data.validateResponse(response,"200")

	@data(*stamps_data.getRequestParam("400","AuthFailure.MissingToken"))
	def test_stamps_data_400_MissingParameter_User_Email(self,param):
		response = stamps_data.sendRequest(param)
		# validate status code && response
		self.assertEqual(400,response.status_code)
		stamps_data.validateResponse(response,"400","AuthFailure.MissingToken")

	@data(*stamps_data.getRequestParam("401AuthFailure.InvalidToken"))	
	def test_stamps_data_401(self,param):
		response = stamps_data.sendRequest(param)
		# validate status code && response
		self.assertEqual(401,response.status_code)
		stamps_data.validateResponse(response,"401","AuthFailure.InvalidToken")

	def tearDown(self):
		pass

