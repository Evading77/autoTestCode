import time
import unittest
from urllib import parse

import requests

from frameworkutils.browserbase import BrowerBase
from pageobjects.functions.approval import Approval
from pageobjects.functions.desk import Desk
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
        loginpage.type_pwd()
        loginpage.click_login_button()
        if loginpage.is_exist_element(loginpage.close_news):
            loginpage.click_close_news()
        self.assertIsNotNone(loginpage.login_success_ico)
        time.sleep(2)

    # 进入审批页面
    def test_2approval(self):
        deskpage=Desk(self.driver)
        self.driver.find_element_by_xpath("//div[@id='top-bar-menus']/a/span[text()='审批']").click()
        # deskpage.click_approval_menu()
        time.sleep(3)
        self.assertIsNotNone(deskpage.new_approval_button)

    # 从审批页面进入员工端
    def test_3approval_yuangong(self):
        deskpage=Desk(self.driver)
        approvalpage=Approval(self.driver)
        # approvalpage.click_new_approval_button()
        approvalpage.click_faqishenpi()
        approvalpage.click_yuangongduan()
        # cookiesList = self.driver.get_cookies()
        handle=self.driver.current_window_handle
        handlers=self.driver.window_handles
        for h in handlers:
            if h!=handle:
                self.driver.switch_to.window(h)
                break
        self.assertIsNotNone(approvalpage.weixinsaoma)

        cookies = self.driver.get_cookies()
        print(cookies)

        #使用固定的uid和key来模拟二维码扫描登录员工端
        #{"key":"dcfd4bc3acf246faa05d4b8c581c9ddc","uid":"89d64e71342e4e809a7b95da6631c0e9"}
        url="https://i.2haohr.com/api/person_ucenter_auth/wechat_login/login/"
        data={"key":"dcfd4bc3acf246faa05d4b8c581c9ddc","uid":"89d64e71342e4e809a7b95da6631c0e9"}
        r=requests.post(url,data)
        accesstoken=r.json()["data"]["accesstoken"]
        print(accesstoken)

        value = parse.urlencode({"token": accesstoken, "status": 0})

        coo=[{'domain': '.2haohr.com', 'expiry': 1593852935, 'httpOnly': False, 'name': 'Hm_lvt_c19600636d25be064923faec4309a09e', 'path': '/', 'secure': False, 'value': '1562316928'},
{'domain': '.2haohr.com', 'expiry': 1563267330, 'httpOnly': False, 'name': 'accesstoken-pd', 'path': '/', 'secure': False, 'value': '%7B%22token%22%3A%22sx044i8ac3o5xhiiu66j1x28gh7bvi1e%22%2C%22account%22%3A%22%22%2C%22status%22%3A0%7D'},
             {'domain': '.2haohr.com', 'httpOnly': False, 'name': 'Hm_lpvt_c19600636d25be064923faec4309a09e', 'path': '/', 'secure': False, 'value': '1562316936'}]

        coo1={'domain': '.2haohr.com', 'expiry': 1563267330, 'httpOnly': False, 'name': 'employee-accesstoken-pd', 'path': '/', 'secure': False, 'value': value}
        time.sleep(2)
        self.driver.add_cookie(coo1)

        cookies = self.driver.get_cookies()
        print(cookies)
        time.sleep(2)
        self.driver.refresh()

        cookies = self.driver.get_cookies()
        print(cookies)

        # self.driver.add_cookie({"name": "sessionid", "value": accesstoken})
        #
        # self.driver.refresh()  # 刷新
        # cookies = self.driver.get_cookies()
        # print(cookies)

        # url2="https://i.2haohr.com/approval/home"
        # req=urllib.request.Request(url2)
        # req.add_header('accesstoken', accesstoken)
        # response = urllib.request.urlopen(req)
        # the_page = response.read()
        # print(the_page.decode("utf8"))
        # self.driver.refresh()
        # self.driver.get(url2)
        # self.driver.refresh()
        # time.sleep(2)
        # self.driver.add_cookie(parse.urlencode({"token":accesstoken,"status":0}))
        # self.driver.refresh()



# if __name__ == "__main__":
#     #构造测试集
#     suit = unittest.TestSuite()
#     suit.addTest(TestAprroval())#把这个类中需要执行的测试用例加进去，有多条再加即可
#     runner = unittest.TextTestRunner()
#     runner.run(suit)#运行测试用例
