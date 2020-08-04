# coding=utf-8
from selenium.webdriver.common.by import By

from frameworkutils.base_page import BasePage


class Login(BasePage):

    cell_login="xpath=>//*/div/span[text()='手机号登录']"
    # cell_login = (By.XPATH, "//*/div/span[text()='手机号登录']")

    #手机号输入框
    cellphone_input="xpath=>//*/input[@placeholder='请输入手机号']"

    #下一步
    next_step="xpath=>//*/button[@size='large']"

    #请输入密码
    pwd_input="xpath=>//*/input[@placeholder='请输入密码']"

    #马上登录
    login_button="xpath=>//*/span[text()='马上登录']"

    #关闭消息弹窗
    close_news = "xpath=>//div[@class='popupWrap_egN7r']/../../div[1]/*"
    # is_exist_close_news=is_exist_element(close_news)

    #登录成功后的用户图标
    login_success_ico="xpath=>//img[contains(@src,'brand')]"

    login_verify_code="xpath=>//a[text()='切换验证码登录']"




    # # 判断消息弹窗是否存在
    # def is_exist_element(self, selector):
    #
    #     s = str(self.find_element(selector))
    #
    #     if len(s) == 0:
    #         print("不存在%s元素" % selector)
    #         return False
    #     if len(s) == 1:
    #         return True
    #     else:
    #         print("存在%s个元素分别是%s" % (len(s), selector))
    #         return False

    def click_login_verify_code(self):
        self.click(self.login_verify_code)


    def click_cell_login(self):
        self.click(self.cell_login)

    def type_cellphone(self):
        self.type(self.cellphone_input,"13076998012")

    def click_next(self):
        self.click(self.next_step)

    def type_pwd(self):
        self.type(self.pwd_input,"dfy123")

    def click_login_button(self):
        self.click(self.login_button)

    def click_close_news(self):
        self.click(self.close_news)


