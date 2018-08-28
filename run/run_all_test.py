#-*- coding:utf-8 -*-

import unittest
import ones
from tomorrow import threads

case_path = "./module/task/"
rule = "add111*.py"

def add_case(case_path,rule):
	discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
	return discover

def run_case(all_case):
	runner = ones.OnesTestRunner()
	runner.run(all_case)


if __name__ == '__main__':

	cases = add_case(case_path,rule)
	run_case(cases)
