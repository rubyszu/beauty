import unittest

class MyTest(unittest.TestCase):

    currentResult = None # holds last result object passed to run method

    def setUp(self):
        pass

    def tearDown(self):
        ok = self.currentResult.wasSuccessful()
        errors = self.currentResult.errors
        failures = self.currentResult.failures
        print ' All tests passed so far!' if ok else \
                ' %d errors and %d failures so far' % \
                (len(errors), len(failures))

    def run(self, result=None):
        self.currentResult = result # remember result for use in tearDown
        unittest.TestCase.run(self, result) # call superclass run method

    def test_onePlusOneEqualsTwo(self):
        self.assertTrue(1 + 1 == 2) # succeeds

    def test_onePlusOneEqualsThree(self):
        self.assertTrue(1 + 1 == 3) # fails

    def test_onePlusNoneIsNone(self):
        self.assertTrue(1 + None is None) # raises TypeError

if __name__ == '__main__':
    unittest.main()