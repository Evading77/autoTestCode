import unittest

from frameworkutils.base_page import BasePage
from frameworkutils.browserbase import BrowerBase
from frameworkutils.login import Login
from frameworkutils.thirdpagecheck import ThirdPageCheck


class TestEmployee(unittest.TestCase,BasePage,Login,ThirdPageCheck):
    @classmethod
    def setUpClass(cls):
        browser = BrowerBase(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # print("结束")

    #手机登录系统
    def test_1login_success(self):
        self.login_by_cellphone()

    #人事模块三级页面检查
    def test_2employee(self):
        self.third_pages_check()


