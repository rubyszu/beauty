# -*- coding: utf-8 -*-

import os,sys
import random
current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../')))

class Generate(object):
	def generate_string(self):
		seed = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
		salt = []
		for i in range(8):
			salt.append(random.choice(seed))
		return ''.join(salt)

	def random_arg(self,arr):
		return random.choice(arr)

	def random_priority(self):
		priority = ["PRIOPThh","PRIOPThi","PRIOPTno","PRIOPTlo","PRIOPTll"]
		return random.choice(priority)

	def random_num(self,a,b):
		return random.randint(a,b)


# class Generate(object):

#   def generate_string(self):
#     seed = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
#     return self.generate_array(seed)

#   def generate_array(self, l):
#     for i in range(8):
#       salt.append(random.choice(l))
#     return ''.join(salt)



    