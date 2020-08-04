# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver

from frameworkutils.HTMLTestRunner_cn import HTMLTestRunner


class Test1(unittest.TestCase):
    u'''博客园测试'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        u"""定位失败截图案例"""
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('xxxxx').send_keys(u'百度一下')
        self.driver.find_element_by_id('su').click()
        self.assertTrue(True)

    def test_02(self):
        u'''失败用例'''
        self.driver.get("http://www.cnblogs.com/yoyoketang/")
        t = self.driver.title
        self.assertIn(u"失败用例",t)

    def test_03(self):
        u'''通过用例'''
        self.driver.get("http://www.cnblogs.com/yoyoketang/")
        self.assertIn(u"上海",self.driver.title)

if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test1)
    suites =  unittest.TestSuite()
    suites.addTests([suite1])
    runer = HTMLTestRunner(title="带截图的测试报告", description="小试牛刀", stream=open("sample_test_report.html", "wb"), verbosity=2, retry=2, save_last_try=True)
    runer.run(suite1)
