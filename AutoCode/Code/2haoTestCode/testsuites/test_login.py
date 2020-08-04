import time
import unittest

from frameworkutils.browserbase import BrowerBase
from pageobjects.functions.loginPage import Login


class TestAprroval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowerBase(cls)
        cls.driver = browser.open_browser(cls)
        # browser.login_success()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        print("结束")

    #手机登录系统
    def test_1login_success(self):
        loginpage = Login(self.driver)
        loginpage.click_cell_login()
        loginpage.type_cellphone()
        loginpage.click_next()
        loginpage.click_login_verify_code()
        time.sleep(2)
        self.driver.add_cookie({'name':'accesstoken-pd','value':'%7B%22token%22%3A%22ljebf8h0clyp6mflh8bni55nxx5dcw4u%22%2C%22account%22%3A%22%22%2C%22status%22%3A0%7D'})



        self.driver.refresh()
        time.sleep(2)

