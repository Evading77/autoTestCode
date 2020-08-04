# coding=utf-8

import unittest
import os
import time
from frameworkutils import HTMLTestRunner_cn


def all_case():
    """所有用例"""
    # 待执行用例的目录
    # case_dir=r"F:/download/
    case_dir = os.path.join(os.getcwd(), "testsuites")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test_third_pages_check.py", top_level_dir=None)

    testcase.addTests(discover)
    print(testcase)
    return testcase


if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # 获取当前时间
    now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    # 保存报告路径
    # report_path = "F:\\Code\\trunk\\Code\\2haoTestCode\\test_report\\report_" + now + ".html"
    os.path.dirname(os.path.abspath('.')) + '/config/employee.xlsx'
    report_path = os.path.dirname(os.path.abspath('.'))+'\\2haoTestCode\\test_report\\report_' + now + ".html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              title="这是我的自动化测试报告",
                                              description="用例执行情况",
                                              verbosity=2)
    # run 所有用例
    runner.run(all_case())
    # 关闭文件
    fp.close()