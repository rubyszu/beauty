import unittest
import ddt
from ddt import ddt,data
 
 
@ddt
class MyTestCase(unittest.TestCase):
 
    def setUp(self):
        '''
        testcase init ...
        :return:
        '''
        print('setup')
 
    @data(['t1' ,'r1'] ,
              ['t2' , 'r2'])
    # @unpack
    def test_sth(self , testdata , expectresult):
        '''
        must use test_***
        :return:
        '''
        print('test something')
        print(colored('%s - %s'%(testdata , expectresult), 'blue'))
 
    def tearDown(self):
        '''
        testcase release ...
        :return:
        '''
        print('teardown')
        print()
 
if __name__ == '__main__':
    unittest.main()