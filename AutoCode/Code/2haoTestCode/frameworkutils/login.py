import time

from pageobjects.functions.loginPage import LoginPage


class Login(object):
    # 手机登录方法
    def login_by_cellphone(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_cell_login()
        loginpage.type_cellphone()
        loginpage.click_next()
        loginpage.type_pwd()
        loginpage.click_login_button()
        if self.is_exist_element(loginpage.close_news):
            loginpage.click_close_news()
        self.assert_ele_is_exist(loginpage.login_success_ico)

        time.sleep(2)
