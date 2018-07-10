import HTMLTestRunner
import os,time,sys
import unittest
from time import strftime
from public import send_mail

# class testadd(unittest.TestCase):
#     def setUp(self):
#         pass
#     def test_add1(self):
#         self.assertEqual(2+3+5,10)
#     def test_add2(self):
#         self.assertEqual(0+8+7,15)
#     def tearDown(self):
#         pass
#
# def suite():
#     suiteTest=unittest.TestSuite()
#     suiteTest.addTest(testadd("test_add1"))
#     suiteTest.addTest(testadd("test_add2"))
#     return suiteTest


def interface():
    newtime = time.strftime('%Y-%m-%d-%H%M%S',time.localtime())# 获取当前时间
    report_dir=(os.path.dirname(os.path.dirname(__file__))) # 获取当前项目目录路径
    file_dir=report_dir+r'/test_report/'  #定义测试报告生成目录
    filepath= file_dir+ newtime + u'接口测试报告.html'  #定义生成文件名
    fp=open(filepath,'wb')

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'接口自动化测试报告',
                                         description=u'm某某项目接口测试执行')

    base_dir=os.path.dirname(os.path.dirname(__file__))
    file=os.path.join(base_dir,'testcase')
    suite=unittest.defaultTestLoader.discover(file,pattern="*.py")
    runner.run(suite)
    fp.close()

    send_mail.send_email(filepath)


if __name__=="__main__" :
    interface()

#
# if __name__=="__main__":
#     filepath='D:\\pyresult.html'
#     fp=open(filepath,'wb')
#     runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"测试描述")
#     runner.run(suite())
#     fp.close()