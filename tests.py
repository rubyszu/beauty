import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# class SimpleTest(unittest.TestCase):
#     @unittest.skip("demonstrating skipping")
#     def test_skipped(self):
#         self.fail("shouldn't happen")

#     def test_pass(self):
#         self.assertEqual(10, 7 + 3)

#     def test_fail(self):
#         self.assertEqual(11, 7 + 3)

@unittest.skip("classing skipping")
class CompletelySkippedTest(unittest.TestCase):

    def test_not_run_at_all(self):
        self.fail("shouldn't happen")

def main():
	unittest.main(verbosity = 2)
	
if __name__ == '__main__':
	# main()
	suite = unittest.TestSuite()

    test = CompletelySkippedTest("test_not_run_at_all")
    suite.addTests(tests)
    
    url = "https://api.ones.team/project/F5001/team/VnfMZEQS/pipeline/VtzqKwq6/callback?token=9QSZPPJ2TfNgE46QkyBGWg"
    runner = ones.OnesTestRunner(url)
    runner.run(suite)