#-*- coding:utf-8 -*-

import unittest
import ones

def all_cases():
	#cases
	case_dir = "./module/"
	testcase = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(case_dir,pattern='get*.py',top_level_dir=None)

	for test_suit in discover:
		for test_case in test_suit:
			testcase.addTest(test_case)
	print testcase
	return testcase

if __name__ == '__main__':
	runner = ones.OnesTestRunner()
	runner.run(all_cases())