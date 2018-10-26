# -*- coding: utf-8 -*-

import os,sys
import random

class Generate(object):
	def randomString(self,num=8):
		seed = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
		salt = []
		for i in range(num):
			salt.append(random.choice(seed))
		return ''.join(salt)

	def randomArray(self,arr):
		return random.choice(arr)

	def randomNum(self,a,b):
		return random.randint(a,b)

	



    