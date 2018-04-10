# -*- coding: utf-8 -*-

import unittest
import ones

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(4, 1 + 2)
        self.assertNotEqual(5, 2 + 2)

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(3, 3 - 2)

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(5, 2 * 3)

    # @unittest.skip("demonstrating skipping")
    # def test_skipped(self):
    #     self.fail("shouldn't happen")

    @unittest.expectedFailure
    def testExpectedFail(self):
        raise TypeError

    # @unittest.expectedFailure
    # def testUnexpectedSuccess(self):
    #     pass

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(13, 6 / 3)
        self.assertEqual(43, 5 / 2)

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"),TestMathFunc("test_minus"),TestMathFunc("test_multi"),TestMathFunc("test_divide")]
    suite.addTests(tests)
    
    runner = ones.OnesTestRunner()
    runner.run(suite)