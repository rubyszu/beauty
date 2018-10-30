# -*- coding: utf-8 -*-
import os, sys
from common import *
from models.auth.stamps_data import stamps_data
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

	def tearDown(self):
		pass
		
