import unittest
import os
from testcase_check01 import TestCheck01
from testcase_check02 import TestCheck02
from HTMLTestRunner import HTMLTestRunner

def test_func_01():
    suite = unittest.TestSuite()
    suite.addTest(TestCheck01("test_md01"))
    suite.addTest(TestCheck01("test_md02"))
    suite.addTest(TestCheck02("test_md01"))
    suite.addTest(TestCheck02("test_md02")) 
    return suite

def test_func_02():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCheck01))
    suite.addTest(unittest.makeSuite(TestCheck02))
    return suite

def test_func_03():
    curpath = os.path.dirname(__file__)
    suite = unittest.defaultTestLoader.discover(curpath, pattern="testcase_check01.py")
    return suite

if __name__ == "__main__":
    suite01 = test_func_01()
    suite02 = test_func_02()
    suite03 = test_func_03()

    runner = unittest.TextTestRunner(verbosity=2)
    print('-'*30)
    runner.run(suite01)
    print('-'*30)
    runner.run(suite02)
    
    print('-'*30)
    report_file = os.sep.join([os.path.dirname(__file__), "reports", "html_report.html"])
    if not os.path.exists(os.sep.join([os.path.dirname(__file__), "reports"])):
        os.mkdir(os.sep.join([os.path.dirname(__file__), "reports"]))
    with open(report_file, 'wb') as fl:
        runner1 = HTMLTestRunner.HTMLTestRunner(title='测试标题', description='描述', stream=fl)
        runner1.run(suite03)