#-*- coding:utf-8 -*-

import unittest
import ones
from tomorrow import threads
from common import getCmdlineArgs

class RunTestCase():
	def __init__(self):
		self.case_path = getCmdlineArgs("case_path")
		self.rule = getCmdlineArgs("pattern")

	def addCase(self):
		self.cases = unittest.defaultTestLoader.discover(self.case_path,pattern=self.rule,top_level_dir=None)
		return self.cases

	@threads(3)
	def runCase(self,case):
		runner = ones.OnesTestRunner()
		runner.run(case)


if __name__ == '__main__':
	run_cases = RunTestCase()
	cases = run_cases.addCase()
	for key, value in zip(cases, range(len(list(cases)))):
		run_cases.runCase(key)

