import HTMLTestRunner
import os,time,sys
import unittest

class testadd(unittest.TestCase):
    def setUp(self):
        pass
    def test_add1(self):
        self.assertEqual(2+3+5,10)
    def test_add2(self):
        self.assertEqual(0+8+7,15)
    def tearDown(self):
        pass

def suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(testadd("test_add1"))
    suiteTest.addTest(testadd("test_add2"))
    return suiteTest

if __name__=="__main__":
    filepath='D:\\pyresult.html'
    fp=open(filepath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"测试描述")
    runner.run(suite())
    fp.close()