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
    print ''.join(salt)
    return ''.join(salt)
    