#coding:utf-8
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir='./testsuites'
report_dir='./test_report'

#执行指定的测试类用例
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_third_pages_check.py',top_level_dir=None)

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'test_report.html'

with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title='2hao Test Report')
    runner.run(discover)
