# -*- coding: utf-8 -*-
import unittest
import os, sys

current_file_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(current_file_path, '../../../')))
reload(sys)
sys.setdefaultencoding('utf-8')


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        self.assertEqual(3, 3+1)

    def test_minus(self):
        self.assertEqual(1, 1-0)

    def test_multi(self):
        self.assertEqual(6, 6*1)

    def test_divide(self):
        self.assertEqual(2, 2/2)


def main():
	unittest.main()
	
if __name__ == '__main__':
	main()